# 05_review.md: Peer review (Phase 7, reviewer-critic)

Target venue: *Creativity Research Journal* (profile `imrad-apa`, APA 7th).
Manuscript reviewed: `manuscript/manuscript.qmd` (line numbers refer to this file).
Checked against: `manuscript/03_findings.md`, `manuscript/02_artifacts.md`, `results/tables/rater_descriptive_statistics.csv` (for one disputed value), both bibliographies.

Severity scale: **Critical** = must be fixed before submission (factual error or a central claim the evidence does not support); **Major** = a reviewer would very likely require it; **Minor** = polish, clarity, formatting.

---

## Summary assessment

**Recommendation as it stands: major revision.** (Not submittable yet: about 30 `FILL IN` placeholders carry most of the Methods.)

The paper applies a Bayesian graded-response JRT model (rater-specific slope and location, shared thresholds) to a large, sparse but connected set of creativity ratings of football actions. It then compares that model with an equal-discrimination variant by PSIS-LOO and runs an IRT D-study. The analysis is competent and transparently reported. Convergence, PPC scope, plug-in information and missing uncertainty are all stated openly, and the Results are largely descriptive. Almost every number matches `03_findings.md`.

A skeptical CRJ reviewer would raise five main objections:

1. One reported count is wrong (ceiling rates).
2. The Abstract, Discussion and Conclusion draw conclusions about scoring approaches (means, MFRM fair averages) that were not compared. The scope statement itself excludes them.
3. The key RQ1 inference, "judges differ in discrimination, and equal discrimination is untenable", rests on a PSIS-LOO comparison with clear warning signs. In a shared-threshold model, that inference also cannot be separated from rater differences in scale use.
4. The reliability and D-study values have no uncertainty. This conflicts with the venue's CI criterion and is cheap to fix.
5. Until the placeholders are filled, nobody can judge whether this is a CAT at all (rater expertise, instructions, imposed definition, three dimensions rated together). The novelty and "design reference" framing is stronger than one rater pool of unknown expertise supports.

Once these are addressed, the paper would be a useful domain contribution of the kind Cseh and Jeffries (2019) call for. Its methodological novelty is modest, because it applies an existing model to a new domain, and it should be framed that way.

---

## Major issues (ranked)

### 1. [Critical] Wrong count of raters with zero ceiling rate
- **Location:** Results, "Descriptive rater response styles", line 169 ("five raters had a ceiling rate of zero").
- **Problem:** `rater_descriptive_statistics.csv`, and the F0.8 table inside `03_findings.md` itself, show `ceiling_rate = 0.0` for **eight** raters: R01, R03, R06, R17, R18, R20, R21 and R22. Ceiling rate is the share of category 7 (01 notebook: `(vals == 7).mean()`). These are exactly the eight raters with `n_categories_used` < 7. The "five" comes from the direction/comparison line of F0.8, which contradicts its own table.
- **Why it matters:** This is a text-vs-data error. It also shows that `03_findings.md` contains at least one wrong derived statement, so it should not be treated as infallible.
- **Fix:** Send it back to the results-interpreter to correct F0.8. Then either report the corrected count or drop the clause. Do not hand-edit the number before the findings file is corrected.

### 2. [Critical] Claims about mean and Rasch-family scoring go beyond the evidence
- **Location:**
  - Abstract, line 9: "fair scores should model judges rather than average them".
  - Discussion, "Consequences for mean and Rasch-family scoring", line 231.
  - Recommendation 2, line 250.
  - Conclusion, line 275: "CAT studies in sport should therefore model judges rather than average them".
- **Problem:**
  - Line 56 and Limitations (line 257) state that comparisons of scoring approaches are out of scope.
  - The only evidence offered is the PSIS-LOO comparison of two JRT variants. The equal-discrimination comparison model is a *cumulative-logit graded-response model with a common slope*. It is not an MFRM (adjacent-category Rasch family with rater-specific or shared step structure), and it is not a mean score. So rejecting it does not test the MFRM or mean scoring, even though they share an equal-weighting assumption.
  - Line 231 concedes that "the practical size of the resulting differences in action scores remains to be established". This makes the normative recommendations in the Abstract and Conclusion unsupported. If JRT scores and mean or leniency-adjusted scores were almost perfectly correlated in these data, the recommendation would have no practical consequence.
- **Fix:**
  - Delete the prescriptive clause from the Abstract and Conclusion, or recast it as a hypothesis.
  - In line 231, state that the result bears only on the equal-*slope* constraint within a cumulative-logit model.
  - Recommendation 2 should say "a model that includes rater leniency (e.g., MFRM or JRT)" and cite Primi et al. (2019) for the leniency part only.
  - Alternatively, bring the scoring comparison into scope. The excluded notebooks exist, but that would be a different paper.

### 3. [Major] The PSIS-LOO comparison is under-qualified where it matters most
- **Location:**
  - Methods line 127, Results lines 187–191, Discussion lines 223 and 243 ("worsens out-of-sample prediction").
  - Abstract line 9, Conclusion line 275, Limitations line 267.
- **Problems:**
  - **Asymmetric Pareto-k warnings.** The share of observations with k > 0.7 is 2.80% for the rater-specific model and 0.14% for the equal model (F2.6). High-k observations tend to make PSIS-LOO over-optimistic, and here the problem falls mostly on the favoured model. The difference could therefore be biased in that model's favour. Count, maximum k and share above 1 are not available. No moment matching, `reloo` or K-fold check was run.
  - **Very large p_loo.** p_loo is about 2,574 and 2,376 for N = 7,844 ratings. Vehtari et al. (2017) flag p_loo that is large relative to N, and an approximately 200-unit difference in p_loo for 23 added parameters (22 `z_j` plus σ_log a), as signs that the PSIS approximation is strained. Readers will notice this.
  - **Unit of leave-out.** The observation unit (a single rating) is not stated. With 898 actions rated once, leaving out that rating leaves θ_i informed only by the prior. These cases are likely where the high-k values sit. Whether "out-of-sample" means new ratings of seen actions, new actions or new raters is not specified.
  - **No decision rule.** There is a placeholder for this, but as written the Results quote the notebook's ratio of 8.3 without saying how it is to be judged.
  - **Caveats missing where the claim is made.** The Abstract, Discussion "Contribution" section and Conclusion all state the result without the caveat, which appears only in Limitations.
- **Fix:**
  - Re-estimate the comparison with exact K-fold CV, ideally grouped by action (e.g., 10-fold). Alternatively, use PSIS with moment matching or refits for the k > 0.7 observations. Report k diagnostics in full (count, maximum, share > 1).
  - State the leave-out unit and the predictive target in Methods.
  - Pre-specify or justify the decision criterion.
  - Until a robust check exists, phrase the Abstract and Conclusion as "PSIS-LOO favoured … although Pareto-k diagnostics indicated that the approximation was unreliable for 2.8% of observations".

### 4. [Major] "Discrimination" under shared thresholds is confounded with rater scale use
- **Location:** Methods line 109; Results line 165 ("individual differences in scale use enter the model only through leniency"); Discussion line 227 ("how sharply their ratings separated more from less creative actions").
- **Problems:**
  - With η = a_jθ + λ_j and shared τ, a rater with a small a_j concentrates ratings in the few categories near their location, regardless of θ. That is the signature of central tendency or range restriction. Scale-use differences therefore enter through **both** λ_j and a_j. Line 165 is technically incorrect.
  - Reviewer observation, not yet a finding: it should go through the results-interpreter before any use. The raters with the lowest posterior-mean a_j (R18, R13, R12, R10) are among the most lenient, and in `rater_descriptive_statistics.csv` they have the highest `central_category_rate` values (R13, R18, R12 are the top three). The rater-response-style figure (panel D) shows this to readers without any comment from the text.
  - The PSIS-LOO preference for rater-specific slopes may therefore partly reflect rater-specific category use, which a rater-specific-threshold model would absorb. It would not then reflect "discernment".
  - The PPC cannot detect this. Pooled category shares are fitted almost by construction by the shared cutpoints, and rater means by λ_j. Per-rater category distributions, the check that would bear on this, were not examined (line 155).
- **Fix:**
  - Correct line 165.
  - Reframe a_j as the slope under a common category structure.
  - Add a per-rater category-share PPC.
  - Ideally, fit rater-specific thresholds (or a rater-specific threshold scale) for at least the high-volume raters, as the paper itself proposes in Limitations (line 259), and see whether slope heterogeneity survives.
  - At minimum, list this confound explicitly in the Discussion and Limitations.

### 5. [Major] Reliability and D-study values have no uncertainty, and the benchmark comparisons do not fit
- **Location:** Methods line 143; Results lines 203 and 213; Discussion line 235; Abstract.
- **Problems:**
  - **No intervals.** The venue criterion asks for CIs. None of ρ_emp, ρ(1.73) or ρ(1..10) has one, although computing them is trivial in a Bayesian model: evaluate both coefficients for every posterior draw, or for a thinned set. The plug-in information ignores the very large posterior SDs for R20–R22 (0.50 to 0.68).
  - **Equal weights in the D-study.** Line 143 discloses this, but its consequence is not discussed. Three raters with 2 to 13 ratings get the same weight as R01 with 1,174.
  - **Prior ignored in ρ(k).** ρ(k) uses 1/(kĪ) as the error variance, which leaves out the N(0,1) prior's contribution to posterior precision. That is fine as a definition, but it should be said, because ρ_emp (which does include the prior) is quoted next to it.
  - **What ρ_emp measures.** ρ_emp is essentially the variance of the shrunken posterior means. The reported score SD of 0.813, squared, practically equals .66. Readers should be told that, under a unit-variance prior, ρ_emp measures shrinkage.
  - **Rule-of-thumb comparison.** Discussion line 235 compares IRT marginal reliability with the classical five-to-ten-judge rule ("just below the lower end"), and that comparison is not hedged. It then compares ρ_emp with the .70 alpha benchmark and hedges it afterwards. Both comparisons mix frameworks.
- **Fix:**
  - Add posterior intervals for all reliability coefficients and as a band in Figure "fig-jrt-information-reliability" B.
  - Add a volume-weighted D-study as a sensitivity check, or one that drops raters with n < 50.
  - Recast the rule-of-thumb sentence with the same caveat as the alpha comparison, or drop it.
  - Decide on the .70/.80/.90 benchmarks (line 213), cite a source for them, or remove them.

### 6. [Major] Until the Methods placeholders are filled, the CAT status of the ratings cannot be judged
- **Location:** Title; Abstract; Methods lines 62–80.
- **Problem:** The CAT has specific requirements: judges familiar with the domain, independent judgement, no imposed definition, and relative rating (Amabile, 1982; Hennessey et al., 2011). The manuscript leaves open recruitment, expertise, whether a definition of creativity was shown, training or anchors, and assignment. It also says raters scored technical correctness and aesthetic appeal at the same time, which opens the way for halo effects. A CRJ reviewer will challenge "consensual assessment" in the title if the raters were, for example, students given a definition. Line 62 already hedges with "CAT-style". The core Methods are placeholders, so the design is not currently reproducible (venue criterion 2).
- **Fix:**
  - Fill the placeholders.
  - If the procedure departs from the CAT, say so in the Abstract and title (e.g., "expert-judgement ratings in a CAT framework") and discuss the consequences.
  - Report whether the three dimensions were rated on the same screen or in a fixed order.

### 7. [Major] Missing methods information that has no placeholder
- **Location:** Methods, as indicated below.
- **Items:**
  - (a) **Action attrition.** Line 70 says 4,104 actions were looked up and 3,669 remain, but no step accounts for the 435 lost actions. Presumably all their ratings were "not recognised". Say so and give the count, which must come from the notebook.
  - (b) **Drift order.** The drift indicator (Appendix B; Limitations line 265) needs a definition of "the order in which they rated" (timestamps? export order?). The analysis does not appear in Methods at all.
  - (c) **LOO unit.** State the leave-out unit and that the pointwise log-likelihood is per rating (see Issue 3).
  - (d) **Krippendorff's α.** Add a citation (e.g., Hayes & Krippendorff, 2007) and the software. Only the version has a placeholder.
  - (e) **Nesting of actions.** Actions come from matches, teams and players. The model assumes independent θ_i, but nothing is said about clustering or how many actions come from the same match or player.
  - (f) **"Not recognised" exclusions.** These 1,292 rows (about 14% of the raw rows; the largest exclusion) may be informative missingness. Report the rate per rater and per action type, and discuss it.
  - (g) **Rationale for action types.** Line 70 names Clearance, Interception, Dispossessed and Error events as rated "actions". Why can a dispossession or an error be a creative product? This is a content-validity question beyond the sampling placeholder.
  - (h) **Information function.** Give the graded-response Fisher information formula (line 129). At present it is only described.
  - (i) **Average-rater reference.** The sum-to-zero leniency is unweighted, so the "average rater" includes R22 (n = 2). State this.
  - (j) **Data origin.** State whether these are secondary data (e.g., pooled thesis projects) and why the design is sparse and unbalanced.
- **Fix:** Add one or two sentences per item. Numbers must come via the results-interpreter.

### 8. [Major] Research questions, hypotheses and the aim–analysis match
- **Location:** Introduction lines 51–56.
- **Problems:**
  - **No hypotheses.** The venue criteria ask for hypotheses, and none are stated. The prior JRT literature (Myszkowski, 2021; Barbot et al., 2023) gives a directional expectation for RQ1 (unequal discrimination).
  - **RQ1 overstates coverage.** RQ1 says it "includes the use of the rating categories", but rater-specific category use was explicitly not modelled. Only pooled category shares and shared thresholds are reported, so the RQ promises more than the analysis delivers.
  - **Design reference.** The study is called a "design reference" (line 56), but expertise, the second half of the Cseh and Jeffries (2019) call quoted at line 37, is excluded.
- **Fix:**
  - State explicitly that the study is exploratory with no confirmatory hypotheses, or state H1 for unequal discrimination.
  - Narrow RQ1's category clause to "pooled category use under a shared category structure".
  - Temper "design reference" to "reference for the number of judges in one rater pool".

### 9. [Major] The novelty and contribution claims are overstated
- **Location:** Abstract line 9 ("for actions in sport, no such evidence exists"); line 49; Discussion line 243 ("first JRT analysis"); line 247 ("reproducible template"); line 271 ("fully reproducible").
- **Problems:**
  - **No documented search.** The "first" claim rests on a search that is not documented. The line-49 placeholder already suggests SPORTDiscus/PsycINFO.
  - **"No such evidence" is too absolute.** Kempe and Memmert (2018) and Zahno and Hossner (2023) give at least agreement evidence for football ratings.
  - **Reproducibility not yet shown.** "Fully reproducible" is not true yet: the git commit is "not available", package versions for 00/01 are missing, and there is no repository.
  - **Nature of the contribution.** The methodological contribution is an application of an existing model (JRT; Myszkowski & Storme, 2019), and the parameter values come from one pool of raters of unknown expertise.
- **Fix:**
  - Document the search (databases, terms, date) in a footnote or supplement.
  - Change "no such evidence exists" to "no evidence on judge parameters or panel size exists".
  - Keep "to our knowledge".
  - Remove "fully reproducible" until code and data are archived with a commit or DOI.
  - Frame the contribution as domain-specific evidence plus a worked example.

### 10. [Major] Pseudonymisation leak in a notebook that the data-availability statement will expose
- **Location:** Methods line 147 (availability statement placeholder); `00_data_loading_preprocessing.ipynb`, cell `520638b8` (03_findings X2).
- **Problem:** The stored output of `ratings_raw.head()` shows original rater user IDs. If the notebooks are shared as promised, rater anonymity is breached, which raises an ethics issue for a human-participants study.
- **Fix:** Clear or re-run that cell without the raw display before archiving. Check the other notebooks for the same problem.

### 11. [Major] Limitations that are absent or only implied
- **Location:** Limitations, lines 255–271.
- **Problem:** The section is good on computation. It omits the following:
  - (i) the slope and scale-use confound (Issue 4);
  - (ii) possible informative missingness from the "not recognised" exclusion;
  - (iii) clustering of actions within matches and players;
  - (iv) heavy shrinkage of single-rated actions toward the prior, which matters for Recommendation 5;
  - (v) the normal latent prior for a strongly right-skewed rating distribution;
  - (vi) the equal-weight D-study;
  - (vii) unknown rater expertise as a threat to the CAT interpretation, beyond the "scope" remark.
- **Fix:** Add a sentence for each, in the existing numbered format.

---

## Minor issues

1. **Krippendorff's α framing (Methods line 98; Discussion line 235).**
   - The framing is mostly correct: it is called crude, it treats raters as interchangeable, it is not a reliability of the JRT scores, and it has no CI.
   - However, "For comparability with common CAT reporting" contradicts the later statement that it "should not be compared" with the model-based coefficients. Rephrase as "for descriptive continuity with agreement indices common in CAT reports".
   - Keep the ordinal-scale caveat (the AUTHOR TO CONFIRM at line 98 should be "yes") and consider an ordinal-level α.
   - A bootstrap CI is cheap to add.
   - Agreement statistics and the χ² sit in Methods. Either move "Realised rating design and descriptive agreement" into Results or say explicitly that it is a design description.

2. **σ_log a prior (Methods line 111; Results line 181).** It is *not* misused, which is good. The manuscript does not argue from the ETI excluding zero, which is impossible under an Exponential prior. However:
   - the Exp(2) prior has mean 0.5 and the posterior mean is 0.39;
   - no prior-sensitivity check was run (line 123).
   Add a prior–posterior overlay, or one sensitivity refit, so readers can see that the data drive σ_log a. Make sure no later draft cites "the 89% ETI of σ_log a excludes 0" as evidence (03_findings F1.3 records that fact, so it is a temptation).

3. **The information-peak pairing is model-implied (Results line 195; Discussion line 239).** Under shared thresholds, a rater's information peak sits where (τ_k − λ_j)/a_j falls. So "lower leniency → peak at higher θ" follows from the parameterisation and is not an independent observation. Saying in the Discussion that it is "consistent with this reading" is circular. State that it follows from the model, and remove it as support.

4. **Evaluative sentences in Results.** Line 219 ("action-level precision … was limited") and the .70/.80/.90 benchmarks at line 213 are evaluative. Move them to the Discussion. Line 183 explains how to read the figure, which belongs in the figure caption. Otherwise the Results stay descriptive.

5. **Multiplicity and borderline cases (lines 175, 181).**
   - With 22 credible-interval checks, about one exclusion is expected by chance. Say that the counts are descriptive.
   - R09's lower bound (0.0012) is mentioned, but R16's leniency lower bound (−0.011, F2.3) is an equally borderline case on the other side. Treat both the same way, or neither.

6. **The χ² example uses a tiny-n rater (line 96).** The upper end of the pass share (77.8%, R21) comes from a rater with 9 ratings. Use high-volume raters for the example, or give the n.

7. **"Face validity" (line 39).** Predicting the temporal proximity of actions to goals is criterion or predictive validity, not face validity.

8. **Citations to verify against the sources (all in the Introduction or Discussion).**
   - `kaufman2008` (line 37): that a high alpha from a large panel can "mask low agreement".
   - `kaufman2008a` (line 37): give the page for the five-to-ten-judge rule (the bib note says the claim came from the vault).
   - `primi2019` (line 47): that rater × scale interactions were "left to future research". Note also that Primi et al. rated divergent-thinking responses, not products.
   - `barbot2023` (line 227): that judges differed in discrimination. It is a VR feasibility study.
   - `anderlucci2021` (lines 45 and 49): described as "MFRM" or "Rasch-family". Verify the method.
   - `zahno2024` (line 39): it may be a conceptual paper rather than a rating study.
   - `safardilha2019`, and the WEF wording (line 31): already flagged.
   - The G-theory sentence (line 37) has no citation. Add Brennan (2001) or Cronbach et al. (1972), or delete it. G-theory should stay background only, as it does now.

9. **MFRM, G-theory and mean scores as background.** In the Introduction they are background only, which is correct. In the Discussion, the section "Consequences for mean and Rasch-family scoring" goes beyond background (see Issue 2). Retitle it, for example "Implications of unequal slopes for scoring", and shorten it.

10. **Interval conventions.** Mixing 89% ETIs (thresholds and hyperparameters) with 95% intervals elsewhere invites confusion. Report 95% throughout, or justify the 89% choice in one sentence.

11. **Score precision (line 207).** Add one sentence on what a posterior SD of 0.65 means for single-rated actions relative to the prior SD of 1. Those scores are largely shrunk toward the mean.

12. **Sparse category 7 (109 ratings).** The top cutpoint, and the largest gap between it and the one below, rest on few observations. Note this in the "Category use" subsection.

13. **"Fair scores" (line 41).** The term is used before it is defined (line 45 defines MFRM fair averages). Define it on first use or rephrase.

14. **Appendix E embeds `tbl-jrt-derived-counts`.** The embedder classified it as an internal source of values. A reader-facing "derived counts" table looks odd. Consider dropping it, or merging the threshold gaps into `tbl-jrt-model-summary`.

15. **APA 7th formatting.**
    - `number-sections: true` numbers headings, which APA does not do.
    - The abstract is about 260 words. Check it against the CRJ limit.
    - Bibliography entries:
      - `myszkowski2021`: pages "426" only, no DOI.
      - `myford2003` / `myford2004`: journal name in lower case, no DOI.
      - `linacre1989`: choose the dissertation or the MESA Press form.
    - `forthmann2023` and `barth2020` will render as 2025 and 2021. This is fine for APA, but the keys may confuse co-authors.
    - Fill the author and affiliation placeholder.

16. **Known render issues (brief).**
    - stdout ("Table saved…"), sampler progress and the Pareto-k `UserWarning` leak into the embeds; the LOO table embed will show the warning twice.
    - The embed of `fig-jrt-category-curves-information` includes the 22-row information table, which leaves the main caption empty.
    - DataFrame index columns appear in the tables.
    - Fix all of these in the notebooks (separate display cells, `#| warning: false`, `hide_index`).

---

## Consistency check (text vs. `03_findings.md`)

**Mismatch found: 1.**

| Location | Manuscript | Data | Status |
|---|---|---|---|
| Line 169 | "five raters had a ceiling rate of zero" | `rater_descriptive_statistics.csv` and the F0.8 table: ceiling_rate = 0.0 for 8 raters (R01, R03, R06, R17, R18, R20, R21, R22). The "five" in the F0.8 direction line contradicts its own table. | **Mismatch: correct via the results-interpreter** |

**Verified as matching** (rounding consistent with the CSV values):
- **Raw data and cleaning:** 9,150 rows; 23 → 22 raters; 4,104 actions looked up; 1,292 / 0 / 1 / 0 / 13 rows removed; 25 duplicate rows forming 11 pairs and 1 triple; 7,844 ratings, 3,669 actions, 22 raters.
- **Design:** 2.14 and 1.73 ratings per action; 898 (24.5%), 2,080 (56.7%), 691 (18.8%) actions; maximum 12; ratings per rater 2–1,174, median 316.5; three raters under 15 shared actions (R22, R21, R20), with 2, 9 and 13 ratings.
- **Allocation and agreement:** χ²(210) = 1260.2, V = .127, passes 46.5% to 77.8%, 49% of cells sparse; α = .42 on 2,771 actions (75.5%).
- **Convergence and PPC:** R-hat 1.0048; ESS 2,014 / 3,034; equal model 1.0038 / 1,552; PPC 7/7 and 22/22.
- **Category use:** 52.9% and 5.7%; 2,116 and 109 ratings; cutpoints −2.25 to 6.44; gaps 2.05 / 1.43 / 1.35 / 1.67 / 2.19.
- **Raw rater statistics:** means 1.76 (R06) to 3.84 (R18); floor .58.
- **Leniency:** −2.93 to 1.63; σ_λ 1.23 [0.96, 1.58]; 16 raters (8 / 8).
- **Discrimination:** 0.96 to 3.24; median 2.08; ratio 3.39; pool 1.87; μ 0.62 [0.47, 0.77]; σ 0.39 [0.28, 0.52]; 11 raters (6 / 5); R07, R08 and R14 statement; R09 0.0012; posterior SDs 0.68, 0.58, 0.50.
- **PSIS-LOO:** elpd −11,537.93 and −11,701.19; difference 163.25 (SE 19.68); ratio 8.3; p_loo 2,573.69 and 2,375.88; Pareto-k shares 2.80% and 0.14%.
- **Information:** peaks 0.29 (R18) to 3.28 (R02); pool peak 1.33 at θ = 0.74; R06 at 1.74 and R01 at 2.10.
- **Reliability and scores:** ρ_emp .66; ρ(1.73) .65; score SD 0.813, range −2.08 to 3.08; posterior SD 0.65 → 0.40; interval width 2.58 → 1.57; 0.86 vs 0.46.
- **D-study:** .51, .68, .76, .81, .90 (k = 9), .91 (k = 10).
- **Drift:** 20 raters; R01 −.300, R09 −.368, R12 .202.
- **Abstract:** all values match the above.

**Object coverage (vs. `02_artifacts.md`):** all 18 labelled objects are embedded and referenced in the text. Panel A of `fig-jrt-information-reliability` and panels B–D of `fig-overview-rater-response-styles` are not interpreted. Panel D is relevant to Issue 4.
