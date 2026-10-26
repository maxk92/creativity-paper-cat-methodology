# 05_review.md: Peer review (reviewer-critic, Phase 7)

Manuscript reviewed: `manuscript/manuscript.qmd` (GRM/JRT version, after commit a97e51d).
Checked against: `03_findings.md` (authoritative numbers), `02_artifacts.md` (objects, display problems), the R source in `data-analysis/creativity-ratings-psychometrics/R/` (only to check how two statistics were computed), and the rendered figures `grm_raw_mean_vs_theta.png` and `grm_rel_post_by_theta.png`.
Venue: Creativity Research Journal (profile imrad-apa).
Line numbers refer to `manuscript.qmd`.

---

## Summary of the paper

The paper analyses 7820 creativity ratings of 3668 football actions ("products") given by 19 student raters on a 7-point scale, in a sparse, connected, incomplete design (mean 2.132 ratings per product, matrix fill 0.112). It is framed as exploratory, with three RQs:
- RQ1: reliability as a function of the number of ratings;
- RQ2: how raters differ;
- RQ3: whether rater differences need to be modelled.

**Models.** A GRM is fitted by MML in mirt, together with an adjacent-category ladder: M1 RSM/MFRM in sirt, M2 PCM and M3 GPCM in mirt. The GRM wins on AIC, BIC and SABIC.

**Reliability.**
- The empirical marginal reliability of the obtained scores is 0.672 [0.649, 0.687], against a hypothetical full-panel value of 0.960.
- Mean product-level rel_post rises from 0.520 (one rating) to 0.919 (ten ratings).
- Conventional indices are reported as reference values: pairwise α .928, crossed-block α .658, Krippendorff α .392.

**Rater differences.**
- Raters differ in thresholds, spacing, discrimination (0.631 to 3.709) and information. Intervals are wide for raters with about 50 ratings.
- LR tests reject a shared category structure and equal discrimination. BIC disagrees on discrimination.

**Score consequences.**
- Raw mean ratings move 0.350 of products to a different quintile relative to the GRM. The constrained models move at most 0.202.
- Excluding three raters with fewer than 15 ratings barely affects the results.

**Conclusion.** Studies should plan the number of ratings, use a calibration set, and score with JRT instead of averaging.

**Does it deliver the author's three aims?**
- **Aim 1 (number of ratings and reliability):** only partly. The by-n table is observational and confounded (see C3), so it describes these data rather than giving a planning tool. The planning claim in the abstract, the Discussion and the callout box goes further than the evidence.
- **Aim 2 (rater differences):** largely delivered, with good attention to uncertainty. Some headline values rest on raters with very few ratings and on parameters that are hard to interpret (see M4, M5).
- **Aim 3 (rater differences must be modelled):** the weakest link.
  - The raw-mean comparison, which is the central evidence, has a computational artefact (C1).
  - The argument mixes up severity with discrimination and category structure (M2).
  - The GRM is used as the reference standard without validity or fit evidence that would justify it (M1).

## Overall recommendation

**Major revision.**

The topic suits CRJ, and it is timely: there is no JRT work on sport creativity ratings yet. The transparency about the limits of the design is unusually good: no cut-offs are applied, the non-computable C2 is reported, the BIC disagreement is reported, and the observational by-n caveat is stated. Every number checks out against `03_findings.md`.

Three things stand between the draft and a publishable paper:
- The share-changing-quintile statistic for the raw mean is partly an artefact of ties.
- The methods are not yet reproducible: allocation, raters, stimuli and ethics are all [FILL IN].
- The applied recommendations, which are the paper's selling point for a sport audience, rest on evidence that cannot yet carry them: observational by-n means, and no criterion showing that GRM scores are better than raw means.

None of these is fatal, and most can be fixed with the existing data.

Issue counts: **3 critical, 12 major, 22 minor.**

---

## Critical issues

### C1. The raw-mean vs GRM quintile and percentile statistics are partly an artefact of ties (lines 9, 201, 207, 237, 251, 259; tbl-raw-mean-vs-grm)

**Problem.**
- `R/jrt_functions.R` computes `pct_rank <- (rank(x) - 0.5)/length(x)`, which gives ties their mean rank. It then computes `quintile <- floor(pct_rank*5)+1`.
- The raw mean takes very few distinct values: 7 for one rating, 13 for two ratings. About 53% of all ratings are 1 or 2.
- As a result, whole tie blocks of the raw mean are assigned to a single quintile at their mid-rank. With ~26% of single ratings equal to 1 and ~27% equal to 2, the "2" block has a mid-rank near 0.40 and goes wholesale into quintile 3. No 1-rating product can then be in raw-mean quintile 2.
- The raw-mean "quintiles" are therefore not quintiles. Some are nearly empty and others oversized. The GRM scores, which are continuous, fill true quintiles.
- Much of the 0.350 "share changing quintile", and the 0.385 / 0.319 / 0.266 gradient by n, can arise from ties alone, even if the GRM merely broke ties without reordering anything. The gradient across n is also expected because more ratings mean fewer ties.
- The same applies to the percentile shift (0.080).
- The model-vs-GRM comparisons (0.202, 0.150, 0.075) involve continuous EAPs on both sides. So the headline contrast "raw mean 0.350 vs at most 0.202" (abstract, line 207, line 237, callout item 4) compares a tie-inflated statistic with a tie-free one.

**Why it matters.** This is the main quantitative evidence for aim 3 and appears in the abstract. A psychometrically literate reviewer will spot it from the figure alone: the raw-mean axis is visibly discrete.

**Fix.**
1. Recompute with a tie-aware definition. One option is to count a quintile change only when the GRM quintile falls outside the range of quintiles that the product's raw-mean tie block spans. Another is to report the share of discordant pairs, i.e., pairs strictly ordered by the raw mean and reversed by the GRM. That is Kendall-type and handles ties directly.
2. Alternatively, drop the quintile statistic for the raw mean and keep the Spearman correlation (which is tie-corrected) and the within-tie spread.
3. The cleanest evidence that is already in hand is the 1-rating facet of `fig-raw-mean-vs-theta`. The same single rating maps to very different GRM scores depending on the rater, and the orderings can reverse: a single 7 from one rater sits below a single 4 from another. The 1-rating row's max θ̂ range among equal raw means (1.436) is also pure rater effect, with no confounding by n. Build the argument on that.
4. Also see minor issue m14 on the "all" row's pooling across n.

### C2. Methods are not reproducible in their current state (lines 7, 69, 73, 77, 81, 85, 139, 145)

**Problem.** The following are all [FILL IN]:
- ethics approval and consent;
- preregistration status;
- rater recruitment and characteristics;
- the stimulus material (competitions, clip selection, clip length);
- the rating software, the instruction, the anchors and the "not recognised" wording;
- randomisation and the data-collection period;
- **the allocation of products to raters (FI-4)**;
- the definitions of the raw-mean groups (FI-20);
- software versions;
- data availability.

**Why it matters.**
- "Sample, design and procedures fully reproducible" is a stated venue criterion.
- The allocation procedure is not a cosmetic gap. Three things depend on it:
  - the MAR assumption (line 85);
  - the interpretation of the by-n table (C3);
  - whether the products with many ratings are a selected subset. The counts of exactly 125 products with 4 ratings and 125 with 5 suggest a design artefact or a benchmark block.

**Fix.**
- Complete FI-1 to FI-4, FI-6, FI-15 and FI-20 before anything else.
- In particular, state how products came to have 1 vs 2 vs 3+ ratings. Was it random, due to rater dropout, a benchmark set, or thesis-specific subsets?
- Then say explicitly whether the 4+ rating products differ systematically, for example in match, action type or rater composition.

### C3. The by-n reliability table cannot serve as the planning tool it is presented as (lines 9, 161, 225, 247, 256, 277)

**Problem.**
- RQ1 and aim 1 are answered with mean rel_post among products that happened to receive n ratings. The manuscript itself notes (lines 173, 225, 265) that this is observational. Products are not randomly assigned to n, the 9- and 10-rating cells have 3 products each, and precision also depends on *which* raters rated a product.
- Despite this, the text says:
  - "the number of ratings per action can be planned for a target score reliability" (line 247);
  - "Plan the number of ratings per action from the reliability you need ... (see @tbl-grm-reliability-by-n)" (callout item 1);
  - "We have shown ... that the reliability of the scores depends on the number of ratings per action" (line 277; causal wording).
- "Product-level precision depended mainly on the number of ratings" (line 225) is not quantified. No variance decomposition is reported.
- rel_post = 1 − PSD² is also defined relative to the N(0,1) prior. With 1–2 ratings it partly reflects the prior (see M6).

**Why it matters.** Aim 1 is the paper's first stated contribution and its main applied deliverable for sport scientists. As it stands, a reviewer will say the paper does not answer "how many ratings are needed".

**Fix (feasible with the current fit, no new data).**
1. Add a model-based projection, i.e., a D-study analogue. For n = 1…10, draw n raters at random from the fitted pool (or weighted by their workload), draw θ ~ N(0,1), simulate ratings from the GRM, and compute the expected rel_post or empirical reliability. Propagate parameter uncertainty with the existing draws.
2. This gives a design-based curve with intervals that is not confounded with allocation. It directly answers the question raised by @cseh2019.
3. Keep the observed by-n table as a check. Base the "plan the number of ratings" recommendation on the projection.
4. Optionally, add a simple regression of rel_post on n plus rater-set mean discrimination to support or drop "mainly".

---

## Major issues

### M1. The GRM is treated as the reference standard, but neither fit nor validity evidence supports that role (lines 201–211, 237, 243, 251, 259, 277)

**Problem.**
- All ranking shifts are computed "relative to the GRM". "Changes the ranking" is then read as "raw means are wrong" (line 251: "direct evidence that this choice changes which actions rank high"; callout item 4; Conclusion). But a difference in rankings shows only that the scores differ, not which ones are more accurate.
- The absolute-fit evidence for the GRM is close to nil, as the paper itself admits (line 267):
  - C2 could not be computed;
  - S-X² is computed on data that are ~90% imputed *from the fitted model*;
  - infit and outfit are below 1 by construction;
  - Q3 is heavily biased with ~2 raters per product.
- GRM superiority is relative only: 46.6 AIC points over M3 at equal npar.

**Why it matters.** Aim 3 ("rater differences must be acknowledged and modelled") is the paper's normative message. Without a criterion, a reviewer can argue that the GRM merely reshuffles noise. That reading is plausible here, because a single rating from R18 (a = 0.631) or R19 (a SE 2.220) is reweighted heavily.

**Fix.**
1. Add a predictive check that needs no new data. Among products with 3+ ratings, hold out one rating. Predict it once from the raw mean of the remaining ratings and once from the GRM, using the GRM-predicted category for the held-out rater. Compare by log score or by ordinal agreement.
2. Do the same with the M1 vs GRM pair. This turns "the ranking changes" into "the GRM predicts unseen ratings better or worse".
3. If the check is not done, soften the claims: say that the scores *differ* and that the GRM *adjusts for* modelled rater differences, and drop "direct evidence".

### M2. The argument for aim 3 mixes up two kinds of rater differences, and severity is never tested (lines 49–51, 197, 235, 239)

**Problem.**
- The raw-mean critique, following @primi2019, is about **severity** confounding in incomplete designs. The MFRM (M1) already corrects for it.
- The LR tests address something else: **category structure** (M1 vs M2) and **discrimination** (M2 vs M3).
- Line 235 links them: "The LR tests rejected even the weaker constraints of the Rasch family ... Averaging therefore treats raters as interchangeable". The rejection of equal discrimination does not bear on raw-mean averaging. And the M1 constraints are not "weaker" than essential τ-equivalence: essential τ-equivalence allows rater-specific intercepts, which is roughly what M1's severity facet does.
- The most basic rater effect, severity differences, is never tested formally. There is no M0 (no rater facet, or common thresholds) vs M1 comparison, and no M1 severities with SEs. Rater means in line 177 are unadjusted for which products each rater saw.

**Fix.**
1. Add M0, a rating scale model with a common severity across raters, and test M0 vs M1 by LR. Alternatively, report the M1 severity estimates with SEs and a separation index.
2. Then restructure the logic into three steps:
   - (i) severity differs, so raw means are confounded (evidence: M0 vs M1, and the 1-rating facet);
   - (ii) beyond severity, scale use and discrimination differ (M1 vs M2 vs M3);
   - (iii) GRM vs constrained models.
3. Rewrite line 235 accordingly and fix the "even the weaker constraints" sentence.

### M3. Validity of the M1 vs M2 LR test (lines 103, 111, 197, 271)

**Problem.**
- The test compares a sirt log-likelihood with a mirt log-likelihood. The two packages may differ in quadrature, in how the latent variance is handled (tbl-marginal-reliability-models: M1 0.962, M2 1.087) and in constants.
- It is also unclear how M1's *shared* category structure was specified for raters who never used category 7 (R01, R03, R06, R18) or categories 6–7 (R17). In a strict RSM their likelihood contains categories they never used.
- The df shortfall (84 vs 90) is explained, but nesting itself is not shown.

**Why it matters.** χ² = 737 is large, so the conclusion is probably robust. But a psychometric reviewer will ask whether the models are truly nested and whether the likelihoods are on the same scale.

**Fix.**
- Refit M1 in mirt, using `itemtype = "rsm"` or a constrained PCM with equal step deviations, on the same quadrature. Report that LR test, or at least show that the two packages give the same log-likelihood for a common model.
- State how sirt handles raters with unused categories under the shared structure.

### M4. Severity and scale use are read from GRM thresholds that are confounded with discrimination and with sparse category counts (lines 9, 181, 229)

**Problem.**
- The abstract reports "the most lenient and most severe first thresholds were −6.565 and 0.295".
- R18's b1 = −6.565 has SE 3.047. It rests on 55 ratings, of which exactly one is in category 1 (`tbl-category-usage`), and on a low discrimination (0.631).
- In the GRM, b = −d/a, so low-a raters get stretched thresholds automatically. The "wide spacing" of R18 and R13 (line 181) and the "narrow spacing" of R19 (a = 3.709) are therefore partly the same fact as their discriminations, not separate evidence of scale use.
- b1 alone is also a poor summary of severity: R18 has the *highest* raw mean (3.836) but the "most lenient" b1.

**Fix.**
- Remove the b1 extremes from the abstract.
- Summarise severity on a comparable metric, for example each rater's expected rating at θ = 0 and at θ = ±1, with intervals from the existing draws, or the intercepts d.
- Describe spacing as conditional on a, or report the spacing of the intercepts.
- Flag R18 explicitly as poorly determined.

### M5. The parameter-draw intervals come from a truncated distribution (lines 125, 133, 169, 187)

**Problem.**
- 87 draws were rejected to obtain 200 accepted ones, i.e., about 30% of all draws. This tells you the asymptotic normal approximation is poor for some raters, very likely R18, R19 and R16.
- Rejection truncates the sampling distribution. Percentile intervals from 200 draws rest on about 5 draws in each tail.
- The very wide R19 interval [0.410, 11.017] shows the problem.

**Fix.**
- Report which raters caused the rejections.
- Draw on a transformed scale, for example log a with intercepts d, which removes the a ≤ 0 rejections. Alternatively, use a parametric bootstrap that refits the GRM to simulated data.
- Increase to at least 1000 accepted draws.
- At a minimum, state in the Methods that the intervals are conditional on valid parameter sets and approximate for low-n raters.

### M6. Dependence on the normal prior and latent distribution is not examined (lines 101, 123, 127)

**Problem.**
- θ ~ N(0,1) is assumed, and EAP scores and rel_post depend on it. With one rating, rel_post = 0.520 largely reflects shrinkage toward the prior.
- The ratings are strongly floor-heavy: 53% in categories 1–2. The latent distribution may well be skewed, which affects both the EAPs (and hence the ranking comparisons) and the reliability values.

**Fix.**
- Refit the GRM with mirt's empirical-histogram or Davidian-curve option as a sensitivity check. Report the change in empirical reliability and in θ̂ rankings.
- Say explicitly that rel_post is defined relative to a unit prior variance.

### M7. Missingness: 1290 "not recognised" ratings and an unknown allocation (lines 85, 89, 265)

**Problem.**
- 14% of the raw rows were "action not recognised". The manuscript attributes them to video quality (line 89) without evidence and without a marker.
- If non-recognition depends on the action, for example on complex or fast actions, or on the rater, the MAR assumption fails. This also feeds into how many ratings each product ended up with.

**Fix.**
- Report non-recognition rates by rater, and ideally by product.
- Mark the causal sentence for author confirmation, or support it.
- Add the issue to the Limitations together with the allocation question (C2).

### M8. The rater sample and the CAT "appropriate judges" requirement (lines 73, 269)

**Problem.**
- The raters were Bachelor's and Master's students rating for their theses. Football expertise was not recorded.
- CRJ reviewers will measure this against Amabile's requirement of domain-familiar judges and against the expertise literature (Kaufman & Baer). Calling the role of expertise "outside the scope" (line 63) does not settle whether *these* raters are appropriate judges.
- The planning values and the rater heterogeneity may well be specific to a novice pool.

**Fix.**
- Report what is known: football playing or coaching experience, any training, and how many sessions each rater did.
- Add an explicit generalisability caveat to the abstract or the Conclusion, and to the applied recommendations: "for this student rater pool".

### M9. The "15 ratings is a lower limit" recommendation has no evidential basis (lines 91, 253, 258)

**Problem.**
- The 15-rating cut-off has no justification or citation; "up to seven parameters cannot be estimated reliably" is a heuristic.
- No rater in the final data has between 15 and 49 ratings: the excluded raters had 13, 9 and 2, and the minimum retained is 50. The data therefore say nothing about 15.
- The data do show that 50 ratings are *not* enough for stable discrimination: R19 has SE 2.220.

**Fix.**
- Reword callout item 3 and line 253 along these lines: "raters with about 50 ratings still had very imprecise parameters; the cut-off of 15 used here is a pragmatic minimum and is not supported as adequate".
- Add a [FILL IN] for the source or rationale of 15.

### M10. The exploratory framing is coherent, but the conclusions are worded confirmatorily and normatively (lines 57, 149, 219, 235, 277)

**Problem.**
- The exploratory RQ framing is coherent in itself, and having no hypotheses is defensible for a first JRT application in this domain.
- The paper then:
  - uses NHST language ("rejected") as the backbone of RQ3a;
  - adds two secondary questions (SQ1, SQ2), which makes five questions in total;
  - closes with "We have shown" (line 277) and "should" recommendations.
- RQ3 as worded in aim (3) ("need to be modelled") is normative. Data alone cannot answer it without a criterion (see M1).

**Fix.**
- Keep the RQs, but rephrase RQ3 descriptively, for example: "how much do scores and rankings depend on whether rater differences are modelled?"
- Fold SQ1 and SQ2 into the Methods as model-choice steps rather than research questions.
- Soften the Conclusion to "In these data ...".

### M11. The Results section is a number dump and contains interpretation (lines 149, 153, 185, 187, 211)

**Problem.**
- Interpretive statements in the Results:
  - line 149 (summary: "raters were heterogeneous in all parameters");
  - line 185 ("also differed", with no test);
  - line 187 ("Wide intervals indicate that a rater's informativeness is not yet well determined");
  - line 211, an explicit interpretive conclusion carrying ATC-10. It belongs in the Discussion.
- Line 153 lists twelve information-criterion deltas, and line 177 lists three 6-decimal shares.
- A CRJ readership of creativity and sport researchers will not get through the Results.
- Main-text objects: 8 tables (one with 17 columns) and 3 figures, plus a supplement of 24 objects.

**Fix.**
- Move line 211 and the second half of line 187 to the Discussion.
- In the Results, report key contrasts and refer readers to the tables for the rest.
- Move `tbl-grm-rater-parameters` to the supplement, and replace it in the main text with a compact severity and discrimination figure (forest plot with SEs).
- Check the CRJ word and figure limits (FI-16).

### M12. Render blockers and display problems in the main-text tables (02_artifacts.md, problems 1–5; FI-18)

**Problem.**
- `tbl-grm-rater-parameters` contains unescaped `|` characters in `category_boundaries`, which will break the table when rendered.
- Main-text tables use snake_case headers (`rel_post_mean`, `share_products_changing_quintile_by_2_or_more`), code strings (`mirt::marginal_rxx`) and "theta" instead of θ.
- `tbl-reliability-overview` says "bootstrap, 1000 replications" for an interval for which 361 replications failed.
- `tbl-grm-convergence` shows tol = 0.000.

**Why it matters.** This is not APA-compliant, and the manuscript would be returned before review.

**Fix.** Apply FI-18 in the notebook `tidy()` and captions, then re-run the embedder.

---

## Minor issues

- **m1. APA number format.** Values that cannot exceed 1 (reliabilities, correlations, proportions, p) should be written without a leading zero, e.g. .672. The manuscript uses 0.672 throughout. This is formatting, not rounding, but it must be applied consistently from the notebook outputs. It is the author's decision how to do this without violating the "no rounding" rule.
- **m2. Exact p-values (line 197).** "exact *p* = 4.22e-105" and "1.79e-17" are not APA style. Report *p* < .001 only. Scientific notation is not used in APA text.
- **m3. Over-precise values.** Six-decimal category shares (line 177: 0.259463, 0.270205, 0.013939) and five-decimal sensitivity values (line 215) are inconsistent with the rest of the paper. Ask the notebook to print these at 3 decimals instead of rounding by hand.
- **m4. "Did not change the scores" (lines 91, 269).** This overstates the result: the max |Δθ̂| was 0.16246, and 0.00491 of products changed quintile. Say "changed them negligibly".
- **m5. S-X² is described as "conservative" (line 115).** Imputing ~90% of cells from the fitted model biases the test *toward* fit, which makes it close to uninformative. Say so plainly. Consider dropping the S-X² p-values from the Results (line 155) or labelling them as uninformative.
- **m6. Q3 (lines 117, 155).** With ~2 raters per product, Q3 is close to its lower bound by construction. Explain what makes 137 of 171 pairs "computable" (this is not defined in the notebook). Also note that the 20 flags come from a criterion (mean ± 0.2) that has no reference distribution.
- **m7. Pairwise Cronbach's α CI (lines 129, 169).** The 639 successful replications are not a random subset: they are the resamples in which all pairs keep their overlap. Say that the interval may be biased, not merely "approximate".
- **m8. Line 223.** "both lie in the range that CAT studies usually report" needs a citation.
- **m9. Line 225.** "first football-specific evidence" is a novelty claim without a marker. It also depends on C3.
- **m10. Line 89.** The cause given for "not recognised" ratings is unsupported (see M7). Add an [AUTHOR TO CONFIRM] marker.
- **m11. Line 47.** "A rule of thumb of five to ten raters is often cited [@kaufman2008a]" and line 45 "usually reach coefficient alphas above .70" should be added to the FI-17 PDF verification list.
- **m12. Line 243.** "labels for automated rating" introduces an application that is not mentioned anywhere else. Either introduce it in the Introduction or drop it.
- **m13. Line 191.** The phrasing "ranged from 2.700 (R01) and 2.400 (R06) to −0.550 (R13)" is awkward. Also, R01's maximum information at θ = 2.7 comes from a rater who never used category 7. Consider explaining this.
- **m14. tbl-raw-mean-vs-grm, "all" row.** The equal-raw-mean groups in the pooled row mix products with different n. That is why the overall max range (2.252) exceeds the within-n maximum (2.196): differential shrinkage, not only rater severity. The "mean θ̂ range" is also an unweighted mean over groups of very different size. Define both in the Methods (FI-20), and quote the "all" max range with this caveat or not at all (lines 201, 237).
- **m15. Line 237 mechanism sentence (ATC-21).** The 1-rating facet would actually support it directly, because there the only difference between equal raw means is the rater. Point to that facet.
- **m16. Terminology.** "Products" is CAT jargon and reads oddly for sport-science readers. Define it once and then use "actions" consistently, or keep "products" consistently. The title, abstract and Discussion currently switch between the two.
- **m17. "Information per rating" (line 187).** This is information integrated over N(0,1). Name it "average information" and define it once, without implying it is per observed rating.
- **m18. Supplement numbering (line 36).** Main-text references to supplement tables will be numbered as if they were main tables. CRJ usually expects online supplements labelled S1, S2, ... Configure crossref prefixes.
- **m19. tbl-marginal-reliability-models is not used.** Its empirical reliability by model (M1 0.626 → GRM 0.672) speaks directly to SQ2 and to the practical cost of constrained scoring. Consider embedding it in the supplement and citing one sentence from it.
- **m20. Drift and time effects.** Timestamps exist (03_findings "Not found"), but no summary of the collection period or session structure is given. Report at least the timespan. This is relevant to the drift limitation in line 271.
- **m21. Abstract.** At ~230 words it is dense with numbers and reads like a results list. "placed a share of 0.350 of actions in a different quintile" is awkward. Check the CRJ limit (FI-16).
- **m22. Figure captions.** `fig-grm-rel-post-by-theta` (the 1–5+ colour legend) and `fig-grm-rel-consistency` (opacity levels) are not explained, and `fig-grm-panel-information` has no y-axis labels (FI-18).

---

## Number and citation checks

### Text vs data (03_findings.md)

I checked every numeric value in the abstract, the Methods, the Results, the Discussion and the Conclusion against `03_findings.md`. **No mismatches were found.** This covers:
- the cleaning counts;
- the design figures;
- all information criteria and deltas;
- the LR statistics and df;
- fit ranges and Q3;
- all by-n rows;
- the rel_post distribution;
- the reliability CIs;
- the naive indices with n_boot_failed 361;
- the response styles;
- all thresholds, discriminations and SEs quoted;
- information and shares with intervals;
- θ at maximum and the shares at θ = ±2;
- M3 discriminations;
- threshold-order counts;
- M1 fit;
- every raw-mean vs GRM cell;
- score agreement and θ correlations;
- the sensitivity values.

The AUDIT-only values ("6 unused end categories", "0.7–1.3") are correctly **not** quoted.

### Correct numbers, questionable use

- The 0.350 vs 0.202 contrast (abstract, lines 207, 237) is correctly transcribed but computationally inflated by ties (C1).
- The overall max θ̂ range of 2.252 (lines 201, 237) pools products across n (m14).
- R18's b1 −6.565 is reported in the abstract as "most lenient" without its SE of 3.047 (M4).

### Citations

- All 80 citation keys resolve: they are in `phd_library.bib` or `web_references.bib`, with no duplicate definitions among the keys checked.
- Claims that still need PDF verification beyond FI-17: @kaufman2008a (rule of thumb of five to ten raters), the "alphas above .70" claim (@baer2004, @kaufman2008, @hennessey2011), and the characterisation of @kempe2018, @zahno2023 and @dejoode2023 as reporting "ICCs or agreement at most" (line 53).
- Line 223 ("range CAT studies usually report") has no citation.

### Interpretive claims in Results

- Line 149: the summary paragraph ("raters were heterogeneous in all parameters", "constraints ... were rejected").
- Line 185: "also differed", with no test.
- Line 187: the second half ("Wide intervals indicate ...").
- Line 197: the last sentence (borderline, acceptable).
- Line 211: the explicit conclusion with ATC-10. Move it to the Discussion.

---

## Marker check ([AUTHOR TO CONFIRM] / [FILL IN])

**Present and appropriate.**
- Every interpretive Discussion claim carries an ATC marker: ATC-3 to ATC-16 and ATC-21 to ATC-23.
- The exploratory framing (ATC-20), the CAT departure (ATC-19), the cumulative-link rationale (ATC-8), the literature-search limitation (ATC-2) and the ATC-18 benchmark question are all marked.
- All Methods gaps carry FI markers.

**Missing markers (over-claims without a flag).**
- Lines 91 and 269: "excluding them did not change the scores" (m4).
- Line 89: the cause of "not recognised" ratings (M7, m10).
- Line 115: S-X² "conservative" (m5).
- Line 225: "first football-specific evidence" and "depended mainly on" (C3, m9).
- Abstract (line 9): "most lenient and most severe first thresholds" (M4).
- Line 149: the Results summary sentence.
- Line 235: "even the weaker constraints of the Rasch family" is a substantive psychometric claim. It currently sits under ATC-7, but the claim itself is questionable (M2).

**Missing [FILL IN].**
- The rationale or source for the 15-rating cut-off (M9).
- Non-recognition rates by rater (M7).
- A latent-distribution sensitivity check (M6).
- The tie handling in the percentile and quintile computation (C1).

**Volume.** There are about 40 markers. Resolving them is itself a sizeable task, and the manuscript cannot be submitted with any of them left in place. The callout box carries a marker on every line; decide whether the box stays at all. CRJ does not normally use such boxes.

---

## Top 5 points to address first

1. **Fix the raw-mean comparison (C1).** Recompute the percentile and quintile statistics in a tie-aware way, or replace them with a discordant-pair statistic. Rebuild the aim-3 evidence around the 1-rating facet, where the only difference is the rater. Update the abstract, lines 201, 207 and 237, and the callout.
2. **Add a model-based projection of reliability by number of ratings (C3).** Simulate from the fitted GRM with random rater subsets and parameter uncertainty. Base the "plan the number of ratings" recommendation on it rather than on the observational by-n means.
3. **Complete the Methods (C2, M7, M8).** Cover allocation (FI-4), raters, stimuli, the instruction, ethics, software versions and data availability. Report non-recognition rates, and state how products came to have 1, 2 or 3+ ratings.
4. **Tighten the logic of aim 3 (M1, M2, M3).** Test severity directly (M0 vs M1, or M1 severities with SEs). Verify the M1–M2 LR test within one package. Add a held-out-rating predictive check, or else soften "direct evidence" to "the scores differ".
5. **Stop over-reading parameters of low-n raters (M4, M5, M9).** Drop the R18 b1 extreme from the abstract. Report severity on a comparable metric. Fix or disclose the 30% draw rejection. Rephrase the 15-rating "lower limit", which the data cannot support.
