# Approaches to rater-based creativity scores

## The problem

Each football action is rated for creativity on a 1–7 scale by a varying
number of raters, between 1 and 12 per action. Different actions are rated by
different, partly overlapping subsets of raters. This **unbalanced,
incompletely crossed design** raises three questions:

1. **How much do raters agree?** (agreement and reliability)
2. **How do raters differ?** (severity, scale use, discrimination, consistency)
3. **Which action score should be used downstream?** And how much does that
   choice change the ranking of actions?

Four approaches answer these questions with increasingly explicit models of
rater behaviour. Each has its own notebook, and every notebook runs on its own
after the shared preprocessing (`00`) and overview (`01`) notebooks.

| | Approach | Notebook | Rater model | Action score | Reliability concept |
|---|---|---|---|---|---|
| A | Classical consensus (CAT / CTT) | [`02a_classical_consensus.ipynb`](notebooks/02a_classical_consensus.ipynb) | none (raters exchangeable) | mean of ratings | Krippendorff's α, Spearman–Brown |
| B | Linear mixed model / G-theory | [`02b_linear_mixed_model.ipynb`](notebooks/02b_linear_mixed_model.ipynb) | additive severity (random intercept) | BLUP fair score (1–7) | variance components, ICC(A,1)/Φ, ICC(C,1)/Eρ², D-study |
| C | Ordinal many-facet model (MFRM) | [`02c_ordinal_facet_model.ipynb`](notebooks/02c_ordinal_facet_model.ipynb) | severity on the logit scale, shared thresholds | latent θ (logits) | separation reliability, infit/outfit |
| D | Judge Response Theory (JRT) | [`02d_judge_response_theory.ipynb`](notebooks/02d_judge_response_theory.ipynb) | severity + rater-specific discrimination | latent θ (N(0,1)) | information, marginal reliability |
| — | Comparison and final scores | [`03_approach_comparison.ipynb`](notebooks/03_approach_comparison.ipynb) | — | all of the above | side-by-side summary |

The R notebook [`02_creativity_ratings_R.qmd`](notebooks/02_creativity_ratings_R.qmd)
covers the same ground with R packages: `lme4` (B), `sirt::rm.facets` and
`brms` (C), and `mirt`/`jrt` with judge-specific thresholds (D).

### How the approaches relate

```
A  classical:  y_ij = T_i + e_ij                    raters interchangeable, severity is error
      │  + rater main effect
B  LMM:        y_ij = mu + u_i + v_j + e_ij         interval scale, additive severity
      │  ordinal link instead of normal errors
C  MFRM:       logit P(y_ij <= k) = tau_k - (theta_i + lambda_j)
      │  + rater-specific discrimination a_j
D  JRT:        logit P(y_ij <= k) = tau_k - (a_j * theta_i + lambda_j)
```

Each step relaxes an assumption of the previous one. C is nested in D (all
$a_j$ equal), so the two can be compared formally with LOO-CV. A and B differ
in whether rater severity is treated as error or estimated and removed. That
choice matters most in an incomplete design, where different actions see
different raters.

---

## A — Classical consensus scoring (CAT / classical test theory)

**Question.** Do independent judges agree, and how reliable is the average of
their ratings?

**Method.** The Consensual Assessment Technique (Amabile, 1982) scores a
product by the mean of independent expert judgements. Score quality is
established through inter-rater reliability; judges are treated as parallel
measurements (Kaufman et al., 2008; Silvia et al., 2008).
- **Krippendorff's α** (Hayes & Krippendorff, 2007; Krippendorff, 2018)
  handles missing ratings, varying numbers of raters per unit, and ordinal
  data, so it is the natural agreement coefficient for this design.
- Pairwise statistics separate **absolute agreement** (exact/adjacent
  agreement, MAE, Bland–Altman limits; Bland & Altman, 1986) from **relative
  consistency** (correlations; weighted κ, Cohen, 1968).
- The **Spearman–Brown** formula (Spearman, 1910; Brown, 1910) projects
  single-rating reliability to the reliability of a k-rating mean.
- Leave-one-rater-out consistency is the judge-level analogue of a corrected
  item–total correlation.

**Strengths.** Transparent, assumption-light, standard in creativity research,
and directly comparable to the CAT literature.

**Limits.** No model of rater differences. In an incomplete design, a raw
mean mixes action creativity with the severity of whichever raters rated it.
Single-rating actions get no uncertainty estimate. Rater-mean centring is only
a naive fix: it confounds severity with the quality of the actions a rater
happened to see.

**Use when** a field-standard, easily communicated score is needed, or as the
baseline against which rater corrections are judged.

## B — Linear crossed random-effects model / generalizability theory

**Question.** How much rating variance is due to actions, raters and noise,
and how reliable are scores for a given number of ratings?

**Method.**
- Ratings are modelled as $y_{ij}=\mu+u_i+v_j+\varepsilon_{ij}$, with
  crossed random effects for actions and raters (Baayen et al., 2008;
  Bates et al., 2015).
- The variance components are the inputs of **generalizability theory**
  (Cronbach et al., 1972; Shavelson & Webb, 1991; Brennan, 2001).
  - Φ counts rater severity as error. For one rating it equals ICC(A,1) in
    McGraw & Wong's (1996) terms.
  - Eρ² does not, and equals ICC(C,1) for one rating.
  - A **D-study** projects both to k ratings.
- Classical ICC formulas (Shrout & Fleiss, 1979) assume fully crossed designs.
  For ill-structured designs like this one, variance components from a mixed
  model are the recommended route (Putka et al., 2008).
- The action effects (BLUPs) are **severity-adjusted, shrunken fair scores**.
  Actions with few ratings are pulled toward the mean in proportion to their
  uncertainty.
- Estimation is Bayesian (PyMC) because `statsmodels` does not scale to
  thousands of crossed levels. A REML check runs on a subsample.

**Strengths.** Separates signal from rater bias. Gives interpretable variance
shares and an actionable D-study. Its fair scores account for unequal numbers
of ratings and for which raters an action received. The model is easy to
extend: the notebook adds `match` as a facet.

**Limits.** Treats the 1–7 scale as interval-scaled with normal errors.
Raters may differ only in severity, not in scale use or discrimination.

**Use when** the goal is a reliability analysis with variance components, or
a severity-adjusted score on the original rating scale.

## C — Ordinal many-facet model (Bayesian MFRM, rating-scale type)

**Question.** Where do actions and raters lie on a common latent scale once
the ordinal nature of the ratings is respected? Which raters fit the model?

**Method.**
- Many-facet Rasch measurement (Linacre, 1989; Eckes, 2015) models ordered
  categories through thresholds $\tau_k$ shared by all raters, the
  rating-scale structure of Andrich (1978). Actions (θ) and raters (λ) are
  additive facets on the logit scale.
- Primi et al. (2019) introduced MFRM to creativity assessment.
- The notebook uses the cumulative-logit link, as in Bayesian ordinal
  regression (Bürkner & Vuorre, 2019). Classical MFRM software uses the
  adjacent-category (Rasch) link with the same facet structure; the R
  notebook includes `sirt::rm.facets` for comparison.
- **Infit/outfit** mean squares flag erratic and overly predictable raters
  (Wright & Masters, 1982).
- **Separation reliability** describes how reliably actions, and raters, are
  distinguished. For raters, a high value means severity differences are real
  and need correcting.

**Strengths.** Respects the ordinal, bounded scale. Gives the established
rater-fit statistics of the Rasch tradition. Its scores are on an interval
logit scale, under the model.

**Limits.** All raters share thresholds and discrimination: they may differ
only by a shift. Fit statistics depend on the model being approximately right.

**Use when** the 1–7 scale should be treated as ordinal, or when Rasch-style
rater-fit diagnostics are needed (common in rater-mediated assessment).

## D — Judge Response Theory (JRT)

**Question.** Do judges differ in how *well* they discriminate creativity,
not just in severity? How much information does each judge add?

**Method.**
- Myszkowski & Storme (2019) proposed treating judges like **items in
  polytomous IRT**, for example Samejima's (1969) graded response model. Each
  judge gets a discrimination $a_j$ (and, in the full model, own thresholds).
- The `jrt` R package (Myszkowski, 2021) implements the full family.
- The Python notebook fits a constrained version: rater-specific
  discrimination and severity with shared thresholds, because the sparse
  rater overlap cannot support judge-specific thresholds.
- Judge **information functions** show where on the creativity continuum a
  judge is informative.
- **Marginal reliability** (Green et al., 1984) as a function of the number
  of judges gives an IRT D-study.
- **LOO-CV** (Vehtari et al., 2017) tests whether rater-specific
  discrimination improves out-of-sample prediction over model C.

**Strengths.** The most realistic model of judge behaviour. More
discriminating judges count more in the latent score, and the model shows
which judges add information.

**Limits.** Needs more data per rater. Identification requires fixing the
scale of θ. A more flexible model is not automatically better: when the
LOO difference is within about two standard errors, the simpler model C is
preferred.

**Use when** judges are suspected to differ in quality (expertise, attention),
or when the aim is to evaluate judges, for example to select or train them.

---

## Comparison notebook

[`03_approach_comparison.ipynb`](notebooks/03_approach_comparison.ipynb)
reads the standardized outputs of A–D (`scores_<key>.csv`, `raters_<key>.csv`,
`model_diagnostics_<key>.csv`, with keys `classical`, `lmm`, `mfrm`, `jrt`).
It compares:
- action scores and ranks (correlations, rank shift, top/bottom overlap),
- rater severity and rater-quality indicators,
- reliability across approaches.

It then builds exploratory rater flags and writes the final
`data/processed/action_scores.csv` and `rater_diagnostics.csv`, followed by an
automated cautious interpretation and a QC checklist.

**Run order:** `00` → `01` → `02a`, `02b`, `02c` → `02d` (self-contained; fits its own
equal-discrimination model for LOO) → `03`.

---

## References

- Amabile, T. M. (1982). Social psychology of creativity: A consensual assessment technique. *Journal of Personality and Social Psychology, 43*(5), 997–1013.
- Andrich, D. (1978). A rating formulation for ordered response categories. *Psychometrika, 43*(4), 561–573.
- Baayen, R. H., Davidson, D. J., & Bates, D. M. (2008). Mixed-effects modeling with crossed random effects for subjects and items. *Journal of Memory and Language, 59*(4), 390–412.
- Bates, D., Mächler, M., Bolker, B., & Walker, S. (2015). Fitting linear mixed-effects models using lme4. *Journal of Statistical Software, 67*(1), 1–48.
- Bland, J. M., & Altman, D. G. (1986). Statistical methods for assessing agreement between two methods of clinical measurement. *The Lancet, 327*(8476), 307–310.
- Brennan, R. L. (2001). *Generalizability theory*. Springer.
- Brown, W. (1910). Some experimental results in the correlation of mental abilities. *British Journal of Psychology, 3*(3), 296–322.
- Bürkner, P.-C., & Vuorre, M. (2019). Ordinal regression models in psychology: A tutorial. *Advances in Methods and Practices in Psychological Science, 2*(1), 77–101.
- Cohen, J. (1968). Weighted kappa: Nominal scale agreement with provision for scaled disagreement or partial credit. *Psychological Bulletin, 70*(4), 213–220.
- Cronbach, L. J., Gleser, G. C., Nanda, H., & Rajaratnam, N. (1972). *The dependability of behavioral measurements: Theory of generalizability for scores and profiles*. Wiley.
- Eckes, T. (2015). *Introduction to many-facet Rasch measurement* (2nd ed.). Peter Lang.
- Green, B. F., Bock, R. D., Humphreys, L. G., Linn, R. L., & Reckase, M. D. (1984). Technical guidelines for assessing computerized adaptive tests. *Journal of Educational Measurement, 21*(4), 347–360.
- Hayes, A. F., & Krippendorff, K. (2007). Answering the call for a standard reliability measure for coding data. *Communication Methods and Measures, 1*(1), 77–89.
- Kaufman, J. C., Baer, J., Cole, J. C., & Sexton, J. D. (2008). A comparison of expert and nonexpert raters using the consensual assessment technique. *Creativity Research Journal, 20*(2), 171–178.
- Krippendorff, K. (2018). *Content analysis: An introduction to its methodology* (4th ed.). Sage.
- Linacre, J. M. (1989). *Many-facet Rasch measurement*. MESA Press.
- McGraw, K. O., & Wong, S. P. (1996). Forming inferences about some intraclass correlation coefficients. *Psychological Methods, 1*(1), 30–46.
- Myszkowski, N. (2021). Development of the R library "jrt": Automated item response theory procedures for judgment data and their application with the consensual assessment technique. *Psychology of Aesthetics, Creativity, and the Arts, 15*(3), 426–438. *(verify page range)*
- Myszkowski, N., & Storme, M. (2019). Judge response theory? A call to upgrade our psychometrical account of creativity judgments. *Psychology of Aesthetics, Creativity, and the Arts, 13*(2), 167–175. https://doi.org/10.1037/aca0000225
- Primi, R., Silvia, P. J., Jauk, E., & Benedek, M. (2019). Applying many-facet Rasch modeling in the assessment of creativity. *Psychology of Aesthetics, Creativity, and the Arts, 13*(2), 176–186.
- Putka, D. J., Le, H., McCloy, R. A., & Diaz, T. (2008). Ill-structured measurement designs in organizational research: Implications for estimating interrater reliability. *Journal of Applied Psychology, 93*(5), 959–981.
- Samejima, F. (1969). Estimation of latent ability using a response pattern of graded scores. *Psychometrika Monograph Supplement, No. 17*.
- Shavelson, R. J., & Webb, N. M. (1991). *Generalizability theory: A primer*. Sage.
- Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses in assessing rater reliability. *Psychological Bulletin, 86*(2), 420–428.
- Silvia, P. J., Winterstein, B. P., Willse, J. T., Barona, C. M., Cram, J. T., Hess, K. I., Martinez, J. L., & Richard, C. A. (2008). Assessing creativity with divergent thinking tasks: Exploring the reliability and validity of new subjective scoring methods. *Psychology of Aesthetics, Creativity, and the Arts, 2*(2), 68–85.
- Spearman, C. (1910). Correlation calculated from faulty data. *British Journal of Psychology, 3*(3), 271–295.
- Vehtari, A., Gelman, A., & Gabry, J. (2017). Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC. *Statistics and Computing, 27*(5), 1413–1432.
- Wright, B. D., & Masters, G. N. (1982). *Rating scale analysis*. MESA Press.
