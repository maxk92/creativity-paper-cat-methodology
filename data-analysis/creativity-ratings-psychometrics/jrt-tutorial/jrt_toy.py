"""
Judge Response Theory on a toy dataset: graded response model fitted by
marginal maximum likelihood (EM with fixed quadrature), EAP scoring,
reliability and information. Pure numpy/scipy so every step is visible.
"""
import sys
import numpy as np
from scipy.optimize import minimize
from scipy.special import expit

# ----------------------------------------------------------------------------
# 1. Simulate the toy data
# ----------------------------------------------------------------------------
N_PRODUCTS, K = 24, 5          # 24 products, ratings 1..5
JUDGES = ["A", "B", "C", "D"]
TRUE_A = np.array([1.6, 1.6, 0.8, 2.6])        # discrimination
TRUE_B = np.array([
    [-1.5, -0.5, 0.5, 1.5],    # A: reference judge
    [-0.7,  0.3, 1.2, 2.2],    # B: severe (all thresholds shifted up)
    [-1.5, -0.5, 0.5, 1.5],    # C: same thresholds as A, but noisy
    [-2.2, -0.8, 0.8, 2.2],    # D: sharp, avoids the extreme categories
])


def cat_probs(theta, a, b):
    """GRM category probabilities. theta: (Q,), b: (K-1,) -> (Q, K)."""
    theta = np.atleast_1d(theta)
    pstar = expit(a * (theta[:, None] - b[None, :]))  # P(X>=k)
    cum = np.hstack([np.ones((len(theta), 1)), pstar, np.zeros((len(theta), 1))])
    return cum[:, :-1] - cum[:, 1:]


def simulate(seed):
    rng = np.random.default_rng(seed)
    theta = rng.normal(size=N_PRODUCTS)
    theta = (theta - theta.mean()) / theta.std()
    X = np.zeros((N_PRODUCTS, len(JUDGES)), dtype=int)
    for j in range(len(JUDGES)):
        P = cat_probs(theta, TRUE_A[j], TRUE_B[j])
        for i in range(N_PRODUCTS):
            X[i, j] = rng.choice(K, p=P[i])       # 0..K-1 internally
    return theta, X


# ----------------------------------------------------------------------------
# 2. Marginal likelihood machinery
# ----------------------------------------------------------------------------
NODES = np.linspace(-6, 6, 61)
PRIOR = np.exp(-0.5 * NODES**2)
PRIOR /= PRIOR.sum()


def pattern_lik(X, a, b, nodes=NODES):
    """L[i, q] = prod_j P(X_ij | theta_q). Missing ratings (-1) are skipped."""
    L = np.ones((X.shape[0], len(nodes)))
    for j in range(X.shape[1]):
        P = cat_probs(nodes, a[j], b[j])          # (Q, K)
        obs = X[:, j] >= 0
        L[obs] *= P[:, X[obs, j]].T
    return L


def marginal_loglik(X, a, b):
    return np.log(pattern_lik(X, a, b) @ PRIOR).sum()


def unpack(par):
    """Unconstrained -> (a, ordered b). a = exp(.), b = cumulative sums."""
    a = np.exp(par[0])
    b = np.concatenate([[par[1]], par[1] + np.cumsum(np.exp(par[2:]))])
    return a, b


def pack(a, b):
    return np.concatenate([[np.log(a), b[0]], np.log(np.diff(b))])


def em(X, max_iter=2000, tol=1e-8, verbose=False):
    J = X.shape[1]
    a = np.ones(J)
    b = np.tile(np.array([-1.5, -0.5, 0.5, 1.5]), (J, 1))
    trace = [marginal_loglik(X, a, b)]
    first = {}
    for it in range(max_iter):
        # E-step: posterior weight of each node for each product
        L = pattern_lik(X, a, b)
        W = L * PRIOR
        W /= W.sum(axis=1, keepdims=True)          # (N, Q)
        # expected counts r[j][q, k]: how many products "at node q" got rating k
        for j in range(J):
            R = np.zeros((len(NODES), K))
            for k in range(K):
                R[:, k] = W[X[:, j] == k].sum(axis=0)
            if it == 0:
                first[j] = (W.copy(), R.copy())

            def negq(par, R=R):
                aj, bj = unpack(par)
                P = np.clip(cat_probs(NODES, aj, bj), 1e-300, None)
                return -(R * np.log(P)).sum()
            res = minimize(negq, pack(a[j], b[j]), method="BFGS")
            a[j], b[j] = unpack(res.x)
        trace.append(marginal_loglik(X, a, b))
        if verbose and it < 5:
            print(f"iter {it+1}: logLik = {trace[-1]:.4f}  a = {np.round(a, 3)}")
        if abs(trace[-1] - trace[-2]) < tol:
            break
    return a, b, np.array(trace), first


def direct_ml(X, a0, b0):
    """Check: maximise the marginal log-likelihood directly (no EM)."""
    J = X.shape[1]

    def neg(par):
        ab = [unpack(par[j * K:(j + 1) * K]) for j in range(J)]
        return -marginal_loglik(X, np.array([t[0] for t in ab]),
                                np.array([t[1] for t in ab]))
    x0 = np.concatenate([pack(a0[j], b0[j]) for j in range(J)])
    res = minimize(neg, x0, method="BFGS", options={"gtol": 1e-7})
    ab = [unpack(res.x[j * K:(j + 1) * K]) for j in range(J)]
    return np.array([t[0] for t in ab]), np.array([t[1] for t in ab]), -res.fun


# ----------------------------------------------------------------------------
# 3. Scoring, reliability, information
# ----------------------------------------------------------------------------
def eap(X, a, b):
    W = pattern_lik(X, a, b) * PRIOR
    W /= W.sum(axis=1, keepdims=True)
    m = W @ NODES
    sd = np.sqrt(W @ NODES**2 - m**2)
    return m, sd, W


def judge_info(theta, a, b):
    """GRM item information: sum_k (dP_k/dtheta)^2 / P_k."""
    theta = np.atleast_1d(theta)
    pstar = expit(a * (theta[:, None] - b[None, :]))
    d = a * pstar * (1 - pstar)
    z = np.zeros((len(theta), 1))
    dP = np.hstack([z, d]) - np.hstack([d, z])   # slope of each category curve
    P = cat_probs(theta, a, b)
    return (dP**2 / np.clip(P, 1e-300, None)).sum(axis=1)


def cronbach_alpha(X):
    X = X.astype(float)
    k = X.shape[1]
    return k / (k - 1) * (1 - X.var(axis=0, ddof=1).sum() / X.sum(axis=1).var(ddof=1))


if __name__ == "__main__":
    np.set_printoptions(linewidth=160, suppress=True)
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 62   # 62 = the tutorial dataset
    theta_true, X = simulate(seed)
    print("Ratings (rows = products, columns = judges A-D):\n", X + 1)

    # Step 3: judge parameters
    a, b, trace, first = em(X, tol=1e-10, verbose=True)
    print("\nEM iterations:", len(trace) - 1, " final logLik:", round(trace[-1], 4))
    print("discrimination a:", np.round(a, 2))
    print("thresholds b (rows = judges):\n", np.round(b, 2))

    # Step 4: fair scores
    m, sd, W = eap(X, a, b)
    fair = np.array([np.mean([(cat_probs(m[i], a[j], b[j]) @ np.arange(1, K + 1))[0]
                              for j in range(len(JUDGES))]) for i in range(N_PRODUCTS)])
    print("\nEAP:", np.round(m, 2))
    print("PSD:", np.round(sd, 2))
    print("fair rating (1-5):", np.round(fair, 2))

    # Step 5a: reliability
    v, e = m.var(ddof=1), (sd**2).mean()
    info_nodes = sum(judge_info(NODES, a[j], b[j]) for j in range(len(JUDGES)))
    print("\nempirical reliability:", round(v / (v + e), 3))
    print("expected (marginal) reliability:", round(((info_nodes / (info_nodes + 1)) * PRIOR).sum(), 3))
    print("Cronbach's alpha of the raw ratings:", round(cronbach_alpha(X + 1), 3))

    # Step 5b: information
    grid = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
    info = np.array([judge_info(grid, a[j], b[j]) for j in range(len(JUDGES))])
    print("\ninformation at theta = -2..2 (rows = judges):\n", np.round(info, 2))
    print("panel information:", np.round(info.sum(axis=0), 2))
    print("average information per judge:",
          np.round([(judge_info(NODES, a[j], b[j]) * PRIOR).sum() for j in range(len(JUDGES))], 2))

    # Missing ratings: rescore product 13 without judge D (-1 = missing)
    p = X[12].copy()
    p[3] = -1
    m13, sd13, _ = eap(p[None, :], a, b)
    print("\nproduct 13 without judge D: EAP", round(m13[0], 2), "PSD", round(sd13[0], 2))
