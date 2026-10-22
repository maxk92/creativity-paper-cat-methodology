# Models

## The problem

Each football action (product) is rated for creativity on a 1–7 scale by a varying
number of raters, between 1 and 12 per action. Different actions are rated by
different, partly overlapping subsets of raters. Every product therefore has its own
rater set R_n, and the precision of its score depends on who rated it.

## Central model: JRT as a graded response model

Judge Response Theory (Myszkowski & Storme, 2019) treats judges as the items of a
polytomous IRT model and products as persons. "JRT" names this framing; it is not a
model of its own. Any polytomous IRT model fitted with raters as items is a JRT model.
The paper uses Samejima's (1969) graded response model:

  P(X_nj ≥ k | θ_n) = 1 / (1 + exp(−a_j (θ_n − b_jk))),  θ ~ N(0, 1)

with a rater-specific discrimination a_j and rater-specific ordered thresholds b_jk.
It is fitted with `mirt::mirt(wide, 1, itemtype = "graded")` by marginal maximum
likelihood (EM algorithm, fixed quadrature) on the products × raters matrix, with
`NA` for ratings that do not exist (`R/02_grm.R`). The `jrt` R package (Myszkowski,
2021) fits the same models through `mirt` and adds plots. It is not used here,
because `mirt` gives direct control over estimation, missing data and fit statistics.

**Information and reliability** (`R/03_grm_information.R`). Rater information
I_j(θ) adds up over raters under local independence. The posterior-based
conditional reliability is rel(θ) = I(θ)/(I(θ) + 1), with SE(θ) = 1/√(I(θ) + 1).
This convention is used throughout.
- **Full panel** (hypothetical, every rater rates the product): the information and
  reliability curves, plus the model-based marginal reliability.
- **Actual scores:** EAP estimates with posterior SD. The product-level reliability
  is rel_post = 1 − PSD². rel_info uses the information of the product's own raters
  at θ̂. The **empirical marginal reliability**, Var(θ̂)/(Var(θ̂) + mean PSD²), is
  the primary reliability figure.

## Comparison models

**Adjacent-category ladder** (`R/04_model_comparison.R`). All three models are fitted
by MML on the same data:

| Model | Thresholds | Discrimination | Software | Corresponds to |
|---|---|---|---|---|
| M1 RSM | shared, shifted by rater severity | equal | `sirt::rm.facets` | many-facet Rasch model (Linacre, 1989; Eckes, 2015; Primi et al., 2019) |
| M2 PCM | rater-specific | equal | `mirt`, `"Rasch"` | MFRM with rater-specific thresholds |
| M3 GPCM | rater-specific | rater-specific | `mirt`, `"gpcm"` | JRT in the adjacent-category form |

- **LR tests:** M1 vs M2 asks whether rater-specific thresholds are needed; M2 vs M3
  asks whether rater-specific discriminations are needed.
- **Information criteria:** AIC, BIC and SABIC for M1–M3 and the GRM. The GRM comes
  from the cumulative family, so it is compared by information criteria only.
- **Why M1 uses `sirt`:** `mirt` recodes each rater's observed categories, and its
  RSM refuses raters with different numbers of categories. `rm.facets` keeps every
  rater on the full 0–6 category set. The script checks that the two packages agree
  where both apply.

**Naive indices** (`R/05_naive_indices.R`) are reference values for common practice.
They are not used downstream.
- **Cronbach's α** measures the consistency of the unweighted rater mean. It assumes
  τ-equivalent raters.
- **Krippendorff's α (ordinal)** measures the agreement of single ratings, with
  raters treated as interchangeable (Hayes & Krippendorff, 2007).

## References

- Eckes, T. (2015). *Introduction to many-facet Rasch measurement* (2nd ed.). Peter Lang.
- Hayes, A. F., & Krippendorff, K. (2007). Answering the call for a standard reliability measure for coding data. *Communication Methods and Measures, 1*(1), 77–89.
- Linacre, J. M. (1989). *Many-facet Rasch measurement*. MESA Press.
- Myszkowski, N. (2021). Development of the R library "jrt": Automated item response theory procedures for judgment data and their application with the consensual assessment technique. *Psychology of Aesthetics, Creativity, and the Arts, 15*(3), 426–438. *(verify page range)*
- Myszkowski, N., & Storme, M. (2019). Judge response theory? A call to upgrade our psychometrical account of creativity judgments. *Psychology of Aesthetics, Creativity, and the Arts, 13*(2), 167–175. https://doi.org/10.1037/aca0000225
- Primi, R., Silvia, P. J., Jauk, E., & Benedek, M. (2019). Applying many-facet Rasch modeling in the assessment of creativity. *Psychology of Aesthetics, Creativity, and the Arts, 13*(2), 176–186.
- Samejima, F. (1969). Estimation of latent ability using a response pattern of graded scores. *Psychometrika Monograph Supplement, No. 17*.
