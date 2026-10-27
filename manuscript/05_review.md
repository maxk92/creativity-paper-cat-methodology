# 05_review.md: Peer review, THIRD ROUND (reviewer-critic, Phase 7)

Manuscript reviewed: `manuscript/manuscript.qmd` (working-tree revision after commit 73d8d44; 327 lines).
Checked against:
- `03_findings.md` (re-run after 62f7d8e), including its "Changes" section and Flag 13;
- `02_artifacts.md` (42 labels, 37 embedded);
- the round-2 review (previous version of this file);
- `R/07_reliability_projection.R`, line 39, read only to see how raters are drawn in the projection;
- `phd_library.bib` and `web_references.bib`, to check that citation keys resolve.

Venue: Creativity Research Journal (profile imrad-apa). Line numbers refer to the current `manuscript.qmd`.

I respected these author positions and do not criticise them here:
- the empirical focus, with the projection kept as a side note;
- no requests for further projection, simulation or model-test analyses (they are listed once, in Section 6);
- the sparse design is not foregrounded;
- the Methods FILL INs on allocation, raters, stimuli, ethics, software versions and data availability;
- the author-supplied cause of the "not recognised" ratings.

APA formatting (no leading zero for values bounded by 1, *p* < .001, thousands separators) is intended and is not counted as a mismatch.

---

## 1. Summary and recommendation

This revision does what the author set out to do. The paper now reports the experiment and what was observed, and the problems that came with the round-2 projection are gone because that material was removed rather than patched.

**Fixed since round 2:**
- **Projection rater sets (N-C1).** The "most/least informative" sets are removed. The projection is a single random-rater side note in the supplement, cited once in the Discussion (line 201) with its "treated as known" caveat. The ".754" headline and "who rates matters as much as how many" are gone.
- **Pooled raw-mean statistics (N-M1).** These are gone. The abstract and the Discussion (lines 9, 195, 215) now quote the within-n τb and reversal shares.
- **The 1-rating spread (N-M5).** It is now described as reflecting "severity and discrimination" (line 211), with the mean range reported.
- **Pipeline residue (N-M3, N-M4, N-m9).** It is removed: no "analysis notebook", no "output", no "will be refreshed".
- **The round-2 minor points.** All 12 are resolved.
- **Numbers.** Every number I checked matches `03_findings.md`, and no removed value is quoted (Section 4).

**What still separates the draft from acceptance:**
1. **The normative scoring recommendation** (abstract, box item 5, Conclusion) goes beyond the evidence. The paper says so itself at line 217: it did not show that GRM scores are more accurate. Since the author does not want a predictive check, the recommendation should be **re-grounded or softened**, not backed by a new analysis (round-1 M1, still partially resolved).
2. **The text equates "the MFRM" with a shared category structure** (lines 51, 61, 213). M2 is itself a partial-credit many-facet model. The only constraint that the Rasch/MFRM family necessarily imposes is equal discrimination, and the evidence on that is mixed (BIC disagrees). A Rasch-literate CRJ reviewer will flag this. It is a wording fix (new major issue N3-M1).
3. **Two citation keys are defined differently in the two .bib files** (kaufman2008/kaufman2008a are swapped, and wind2019a refers to different papers). This happened after round 2, apparently when the web references were merged into `phd_library.bib`. The reference list will be wrong unless this is fixed (new major issue N3-M2).
4. **The Methods FILL INs.** They are the author's task, but the manuscript cannot be submitted until they are done.

**Recommendation: minor revision.** The remaining issues are wording and bibliography fixes that need no new analysis. This is conditional on completing the Methods FILL INs, which are a precondition for submission rather than a review issue.

One risk the author should know about, which I am not asking to be addressed: an external psychometric reviewer may still ask for the analyses the paper chose not to run. Listing them in the Limitations (line 245) is the right mitigation. Wording such as "were beyond the scope of this descriptive study" may read better to reviewers than "were deliberately not carried out".

**Counts:**
- Response check (42 points): **23 resolved, 6 partially resolved, 1 not resolved, 8 deferred to author, 4 declined under author priority.**
- New issues: **0 critical, 2 major, 12 minor.**

---

## 2. Response check

Status codes:
- **R** = resolved;
- **P** = partially resolved;
- **N** = not resolved;
- **D** = deferred to author (legitimately a FILL IN or author decision);
- **X** = declined under author priority.

### 2a. Round-2 points

| # | Status | Justification | Location |
|---|---|---|---|
| N-C1 Projection rater sets chosen by noisy point estimates | **R** | The informativeness-based sets are removed from the notebook and the text. The projection is random raters only, labelled as a side note, with "treated as known" stated. | 201; supplement 298–304 |
| N-M1 Pooled raw-mean statistics | **R** | The pooled row is gone. The abstract and the Discussion quote τb .832 / .815 and reversals .042 / .067 within n. | 9, 177, 195, 215 |
| N-M2 Projection gives no concrete planning answer | **X** | The workload-weighted scheme and k-for-target are declined. The corresponding claim was softened: box item 2 now says "plan … with the precision of individual scores in mind". The disclosure of uniform draws is still missing (new minor n6). | 201, 225, 245 |
| N-M3 "Analysis notebook" cited as an authority | **R** | Both sentences are gone. Residual: line 149 now asserts the rater-composition confound without support (new minor n2). | 149, 211 |
| N-M4 "Will be refreshed when more ratings are collected" | **R** | Moved to the hidden comment FI-19 as an internal note. | comment line 33 |
| N-M5 1.436 spread framed as severity | **R** | Line 211 says "in both severity and discrimination" and reports the mean range with the maximum. The abstract quotes only the mean ranges. Residual: a range is set by the most extreme raters (new minor n4). | 9, 177, 211 |
| N-m1 Selective central rate | **R** | R13, R18 and R12 are all named. | 157 |
| N-m2 APA thousands separators | **R** | Applied in the text (7,820; 3,668; −11,733.227; 23,767.020 …). The tables are under FI-18. | throughout |
| N-m3 τ-equivalence sentence | **R** | Rewritten: alpha requires essential τ-equivalence, which allows intercepts, but the raw mean does not adjust for them. The paragraph is split. | 49, 51 |
| N-m4 primi2019 / forthmann2023 unverified | **R** | Claim reworded to product-level precision and added to FI-17. | 45 |
| N-m5 Novelty claims in the abstract | **R** | "Little is known" plus an ATC-2 marker. | 9 |
| N-m6 "Non-trivial share" unmarked | **R** | τb quoted and ATC-22 added. | 195 |
| N-m7 New number (.892) in the Discussion | **R** | Removed. The analogous placement of the projection values is minor n6. | 201 |
| N-m8 Post hoc "≥ 400 ratings" grouping | **R** | The grouping and the "0.86 to 2.81" range are gone. Examples are given instead. | 9, 165, 167 |
| N-m9 "Not listed in the output" | **R** | Removed. | — |
| N-m10 Selective by-n values | **R** | n = 1, 2 and 3 are quoted. | 149 |
| N-m11 .237 next to .202 | **R** | The tie-resolved share is removed. The raw-mean and model-choice paragraphs are separate. | 215, 217 |
| N-m12 Box duplicates the implications | **R** | The implications text is reduced to two qualifications plus the box. Whether CRJ accepts boxes is FI-16. | 221–231 |

### 2b. First-round points still open in round 2

| # | Status | Justification | Location |
|---|---|---|---|
| C2 Methods not reproducible | **D** | Still FILL IN (FI-1–4, 6, 15, 21, 22). Author's task by constraint, and a precondition for submission. | 69–89, 131 |
| C3 By-n table used as a planning tool | **R** | The by-n table is described as observational (235). The projection is a side note. Planning wording is softened (box item 2). | 149, 201, 225, 235 |
| M1 GRM as reference standard | **P** | Line 217 now says correctly that it was not shown that GRM scores are more accurate, and the held-out check is declined (**X**). However, the abstract, box item 5 and the Conclusion still recommend modelling over averaging as if the data had shown it. The fix is softening or re-grounding (Section 3, carried-over item C-M1). | 9, 217, 228, 249 |
| M2 Severity vs category structure vs discrimination | **R** | The three are kept apart. The 1-rating spread is attributed to severity *and* discrimination. The fact that severity was not tested on its own is disclosed (107, 211). The M0 vs M1 test is **X**. A residual RQ2 wording point is minor n8. | 51, 107, 211 |
| M3 Cross-package M1–M2 LR test | **X** | Disclosed as approximate (107, 243) and listed as future work (245). | 107, 243, 245 |
| M4 b1 extremes read as severity | **R** | Line 99 no longer equates higher thresholds with a stricter rater. b1 is reported as "first thresholds" with SEs. "Stricter rater" is an open author option (ATC-6, comment line 34). | 99, 161 |
| M5 Truncated parameter draws | **X** | Disclosed as conditional and approximate (115, 239). Diagnostics declined. | 115, 239 |
| M6 Dependence on the normal prior | **X** | The prior dependence of rel~post~ and the normal latent assumption are disclosed (117, 201, 239). The sensitivity refit is declined as a model test of that kind. | 117, 201, 239 |
| M7 "Not recognised" missingness | **D** | MAR caveat present (235). The rate by rater is FI-22. The cause is author-supplied. | 89, 235 |
| M8 Student raters and CAT "appropriate judges" | **D** | Scope caveats are present (9, 221, 241). The pool description is FI-21. | 73, 221, 241 |
| M11 Results as a number list | **P** | Descriptive and much tighter. Line 175 still packs the LR tests, the AIC/BIC contrast, the M3 range, unordered steps and M1 fit into one paragraph. Consider splitting it into "ladder tests" and "ladder rater fit". | 139–191, esp. 175 |
| M12 Render and display problems | **P** | Headers, tolerance and the projection and raw-mean captions are fixed in the notebook. Still open under FI-18: code names in cells and captions, "(info_weighted_area)" in a caption, M3 "0.000545256" in `tbl-score-agreement`, "bootstrap, 1000 replications" vs 361 failed. | comment line 32 |
| m3 Over-precise values | **P** | Five-decimal values remain (191, 241). Three decimals would do in the text; the table can keep five. | 191, 241 |
| m4 "Did not change the scores" | **N** | Still "did not change the scores" in the same sentence as a maximum change of 0.16246. ATC-26 offers the fix; it only needs to be applied. | 91 |
| m6 Q3 "computable" pairs | **P** | Still undefined (111, 139), and not printed in the notebook. 17 pairs share no products, but 171 − 137 = 34 are not computable. Either define it from the code or write "the 137 pairs for which Q3 could be computed". | 111, 139 |
| m10 Cause of "not recognised" | **D** | Author-supplied (89). | 89 |
| m13 R01 information maximum | **R** | "Neither of whom used category 7". | 171 |
| m14 Pooling in the "all" row | **R** | Resolved by removal of the row. | — |
| m16 "Products" vs "actions" | **R** | Defined once (77) and used consistently since then. | 77 |
| m18 Supplement S-numbering | **D** | FI-16 (render configuration). | comment line 31 |
| m19 `tbl-marginal-reliability-models` unused | **D** | Now an open author option (comment line 34). Recommended: it is an existing result (empirical reliability M1 .626 → GRM .672) and directly informs RQ3b without new design choices. | — |
| m20 Drift and collection timespan | **D** | FI-3. | 81 |
| m21 Abstract density | **P** | Shorter (about 230 words) but still number-dense. Check the CRJ limit (FI-16). | 9 |
| m22 Figure captions and legends | **D** | FI-18. | — |

**Tally:**

| Status | Round-2 points (18) | Round-1 points still open (24) | Total (42) |
|---|---|---|---|
| Resolved | 17 | 6 | **23** |
| Partially resolved | 0 | 6 | **6** |
| Not resolved | 0 | 1 | **1** |
| Deferred to author | 0 | 8 | **8** |
| Declined under author priority | 1 | 3 | **4** |

---

## 3. New issues

### Critical

None.

### Major

#### N3-M1. "The MFRM" is equated with a shared category structure (lines 51, 61, 101, 213; also 249)

**Problem.**
- Line 51 says: "The MFRM therefore still assumes a shared category structure and equal discrimination".
- RQ3a (line 61) pairs "category structure (RSM/MFRM)".
- Line 213 says: "Category structure and discrimination remain constrained in the MFRM after severity has been modelled, and both constraints were rejected".
- Only the *rating-scale* form of the MFRM shares one category structure. The partial-credit many-facet model, with rater-specific category thresholds, is standard in Facets (Linacre; Eckes 2015, rater-related scale structure). The paper's own M2 is essentially that model: a Rasch model with raters as items and rater-specific thresholds.
- The only constraint the Rasch/MFRM family necessarily imposes is therefore **equal discrimination**. That is the constraint with mixed evidence: the LR test and AIC reject it, BIC does not (line 175).

**Why it matters.**
- The paper's argument for JRT over the MFRM (lines 51, 213, the Conclusion and box item 5) currently rests on two rejected constraints.
- Correctly stated, the case against the MFRM *family* rests on one constraint, with disagreement among criteria. The shared-category-structure result argues against the rating-scale MFRM, not against Rasch modelling.
- A Rasch-literate CRJ reviewer will raise this at once.

**Fix (wording only).**
- Write "the rating-scale form of the MFRM (M1)" wherever a shared category structure is meant.
- State once that a partial-credit MFRM relaxes this (cite eckes2015), and that M2 corresponds to it.
- In lines 213 and 249, say that the rejection of a shared category structure concerns the rating-scale MFRM. Say also that the Rasch family as a whole is questioned only by the discrimination result, which BIC did not support.

#### N3-M2. Conflicting citation-key definitions across the two bibliography files (YAML lines 23–25)

**Problem.** Round 2 found no duplicate keys. Since then, about 48 keys from `web_references.bib` also appear in `phd_library.bib`. Most copies are identical (spot-checked: hennessey2011, pellegrino2025, zahno2023). Three are not:
- **`kaufman2008` / `kaufman2008a` are swapped.**
  - `phd_library.bib` (lines 23655, 23819): kaufman2008 = *Essentials of Creativity Assessment* (book), and kaufman2008a = Kaufman, Baer, Cole & Sexton (2008, CRJ).
  - `web_references.bib` (lines 9, 489): the reverse.
  - The manuscript uses the web assignment: line 45 cites @kaufman2008a for the "five to ten raters" rule, which the bib note attributes to the book.
- **`wind2019a` refers to different papers.**
  - `phd_library.bib` (line 24046): Wind & Sebok-Syer, differential rater functioning.
  - `web_references.bib` (line 626): Wind & Jones, incomplete rating designs.
  - Lines 207 and 221 need Wind & Jones. Under the library definition, the DRF paper would be cited for linking-set claims, and @wind2019b (line 243, DRF, web only) would duplicate it.
  - `phd_library.bib` has the Wind & Jones paper under `wind2019` (line 24020).

**Why it matters.** Which entry renders depends on how pandoc/citeproc resolves duplicate keys across files. Either way, two in-text citations will point to the wrong source. An editor or reviewer who checks the references will notice.

**Fix (bibliography only, no hand-editing of citation formatting).**
- Use one bibliography file:
  - either remove the merged duplicates from one file;
  - or drop `web_references.bib` from the YAML, after adding the web-only keys (deayala2022, forthmann2023, barth2020, dejoode2023, tenhove2024, wind2019b, and any others) to the library.
- Then align the keys:
  - kaufman2008 → the source the text intends at lines 43/45/199;
  - kaufman2008a → the "five to ten" source;
  - wind2019a → Wind & Jones 2019.
- Re-run a render and check the reference list for these three entries.

#### Carried over, not new: C-M1 (round-1 M1, still partially resolved). The recommendation to model rather than average is not supported by the reported analyses (abstract line 9; box item 5, line 228; Conclusion line 249)

This is counted under M1 in Section 2, not as a new issue. It is the main claims-versus-evidence gap.
- Line 217 says correctly that the paper does not show GRM scores to be more accurate.
- The abstract ("model rater differences rather than average them"), box item 5 ("Score actions with a model … rather than with the raw mean") and the Conclusion still recommend it as if the data had shown it.

Under the author priority, the fix is to re-ground the recommendation or soften it. Do not add a predictive check. Two options:
- **Re-ground** it on what *is* shown plus established theory: "raters differed in thresholds and discrimination in these data, and in incomplete designs raw means do not adjust for such differences [@primi2019]; model-based scores do, under the model's assumptions."
- **Soften** it: "consider scoring with a model that adjusts for rater differences, and report how much the ordering differs from raw means".

Either keeps ATC-15 meaningful.

### Minor

- **n1. R18 does not have a wide information interval (line 207).** "R18, R19 and R16 … had the largest standard errors and the widest information intervals." R18's interval is [0.01, 0.35]. In absolute width it is among the narrowest, and wider ones belong to R14, R15 and R12. Write: "the largest standard errors and, for R19 and R16, the widest information intervals".
- **n2. Unsupported rater-composition claim in the Results (line 149).** "Products with different numbers of ratings were also rated by different raters (see Rating design)." The notebook no longer prints or states this (03_findings F1.14), and the Rating design section is a FILL IN. Either let FI-4 supply the fact, or replace the sentence with "The by-n values are observational; products did not receive their number of ratings by design (see Rating design)" plus a [FILL IN: FI-4] marker. Otherwise delete it, because line 235 already says that the by-n values are observational.
- **n3. Reversals at n = 2 are not purely rater effects (line 215).** "These differences have consequences …" attributes the .067 reversals for two ratings to rater differences. With two or more ratings, the GRM score also depends on the *pattern* of ratings, not only their mean, so some reversals would occur even with identical raters. Line 211 already makes this point for the ranges. Add the same clause here. The n = 1 value (.042) is the clean rater-effect figure.
- **n4. The range statistic is driven by the most extreme raters (abstract; lines 177, 211).** A range of GRM scores at equal raw mean is set by the two most extreme raters for that rating. These include the imprecisely estimated R18 and R19. Add a short qualifier in line 211, for example "as a range, it is set by the most extreme raters, some of whose parameters are imprecise". No new analysis is needed.
- **n5. Abstract qualifiers (line 9).**
  - "Likelihood-ratio tests rejected a shared category structure and equal discrimination" leaves out that BIC favoured equal discrimination and that the M1–M2 test is cross-package. Add "(BIC favoured equal discrimination)".
  - Write "a shared rating-scale structure" (see N3-M1).
  - The floor-rate range (.579 to .016) is unadjusted for which actions each rater saw. Either say "raw share" or let the GRM threshold result carry the claim.
- **n6. Projection disclosure and placement (lines 201, 300).**
  - Raters are drawn uniformly (`sample.int(J, k)`, `R/07_reliability_projection.R` line 39). Each of the five raters with 50–73 ratings, whose parameters are least precise, is as likely to be drawn as R01. Add "(each rater equally likely)" to the supplement text and the Discussion sentence. This is a disclosure, not a new analysis.
  - The projection is described only in the supplement. One sentence in Methods, under Scores and reliability, pointing to it would make the Methods complete.
  - Its values (.508, .688, .925) appear first in the Discussion. As a side note this is defensible, but APA convention puts results in Results. Either move the one sentence to the end of the by-n Results paragraph, or keep it and accept the convention break.
- **n7. Misplaced sentence (line 171).** "The response styles have no per-rater uncertainty" ends the information paragraph. It belongs after the response-style paragraph (line 157), or only in the Limitations, where it already is (line 239).
- **n8. RQ2 promises "severity" (line 60).** No severity measure or test is reported: thresholds are described as "threshold location", and severity on its own was not tested (107, 211). Reword RQ2 to "threshold location (severity), scale use, discrimination and information". Alternatively, resolve ATC-6 in favour of reading thresholds as severity, with the GRM caveat.
- **n9. Unverified attributions not on the FI-17 list.**
  - @primi2019 "left such rater-by-scale interactions to future research" (205);
  - @myszkowski2021 on "central versus extreme responding" (205);
  - the characterisation of @looney2004, @anderlucci2021 and @heiniger2021 (47);
  - @wind2018 / @wind2019a "rater estimates … depend on the linking set" (207);
  - @reise1990 on GRM parameter recovery (207).

  Add these to FI-17.
- **n10. Box item 3 overstates what a calibration set adds (line 226).** "So that raters are linked and their parameters comparable": the design was already connected, and all parameters lie on one scale (line 85). Write "more strongly linked and more precisely estimated", in line with the qualification at line 221.
- **n11. Ambiguous model-fit sentence (line 139).** "Their comparison reduces to the log-likelihood (−11,733.227 vs. −11,756.510), a difference of 46.566 on all three criteria" can be read as a log-likelihood difference of 46.566. Write "… so the GRM is lower by 46.566 on AIC, BIC and SABIC alike".
- **n12. Misplaced agreement sentence (line 217).** "These results agree with @primi2019 and @myszkowski2019 on the limits of averaging" sits in the model-choice paragraph, which is about MFRM/PCM/GPCM vs the GRM, not about averaging. Move it to the raw-mean paragraph (215).

---

## 4. Number and citation check against 03_findings.md

### Numeric mismatches

**None found.** Every number in the abstract, Methods, Results, Discussion, Conclusion and supplement text was checked against `03_findings.md`:
- **Cleaning and design:** 9,148 / 1,290 / 0.0 (R04) / 12 pairs, 13 rows / 7,844 / 22; R20 13, R21 9, R22 2 (24); one product dropped; 7,820 / 3,668 / 19; 2.132, median 2, 1–10, 1.726; .112; 17 of 171; median overlap 13; unused categories (R01, R03, R06, R18: 7; R17: 6 and 7); 50–1,174 ratings per rater.
- **Estimation:** 61 points, 0.0001, 165 iterations; 200 draws, 87 rejected.
- **Fit:** −11,733.227 / −11,756.510 / 46.566 / 127 parameters; S-X² *p* .294–.671; infit 0.334–0.971, outfit 0.322–0.961 (R19, R18); Q3 −.238, 137, 20, ten shown, 9 negative, R10–R11 positive; C2 17 of 171; "about 90%" (notebook note `3b49bdab`).
- **Reliability:** .672 [.649, .687]; .960 [.953, .968], grid .960; .928 [.891, .943] (14 raters, 1,900); .658 [.526, .756] (3, 139); .392 [.362, .417] (19, 2,771); 1,000 / 361; by n: .520 (897), .698 (2,080), .757 (357), .919 (3), monotone; PSD 0.686 → 0.285; rel~post~ median .698, IQR .173 (.596, .769), .057–.929; *r* = .935; 320.
- **Raters:**
  - Means 1.760–3.836; SD 1.022–1.953; floor .579 / .016; ceiling .080, five at .000; central .799 / .764 / .735 / .192; categories 2,029 / 2,113 / 109.
  - b1 −6.56 (*SE* 3.05) to 0.29 (0.06); −3.38 (0.49); R02 −0.71 / 2.03; R13 −3.38 / 4.43; threshold counts.
  - *a* 0.63 (0.26), 3.71 (2.22), 3.70 (1.36), 0.86 (0.15), 1.96 (0.16), 2.50 (0.33), 2.81 (0.42).
  - Information 0.12 [0.01, 0.35], 3.54 [0.41, 11.02], 3.30 [0.73, 6.49], 0.24 [0.11, 0.42], 0.98 [0.72, 1.22], 1.70 [0.90, 2.56]; shares .005 [.000, .013], .135 [.017, .331]; θ max 2.700 / 2.400 / −0.550; shares at θ = ±2 (.001, .083, .221).
- **Ladder:** χ²(84) = 737.457, χ²(18) = 121.958; AIC 23,767.020 / 23,852.978; BIC 24,529.585 / 24,555.360; M3 *a* 0.283 (0.055) – 2.606 (1.419); nine / nine unordered; M1 fit R17 1.328 / 1.190, R18 1.009 / 1.071, R12 0.238 / 0.255.
- **Raw mean vs GRM:** all 12 cells of `tbl-raw-mean-vs-grm`.
- **Score agreement:** .975 / .978 / .042 / .202; .985 / .983 / .033 / .150; .996 / .996 / .017 / .075; ladder .980–.993, .983–.996; 1.000.
- **Sensitivity:** all values (.67199 / .67186; .95986 / .96186; .99997; .99996; 0.00171; 0.16246; .00491; .99880; 0.19820).
- **Discussion:** R17 1.45, R12 2.90; projection .508, .688, .925; 50 replications, 2,000 products, seed 20260713.

### Removed or unprinted values (Flag 13)

**None quoted.**
- The most/least-informative values (.754, .947, .108, .884, .892, .920, .701) are absent.
- So are true_r2, the pooled raw-mean values (.796, .083 pooled, .237, .350, .906, .932, .995, .814, 2.252), the subgroup correlations, percentile shifts and quintile shares (.104, .220, …), M3 "0.001", the "confounded" and "not comparable" notebook sentences, Tolerance "0.000", and the 3-decimal parameters and CI bounds.
- The ".083" at line 171 is R06's share at θ = +2 (F2.3), not the removed pooled discordant share.
- "Confounded" at lines 49 and 211 is attributed to @primi2019, not to the notebook.
- No target-k value or between-scheme comparison appears.

### Citations

- **All cited keys resolve** in at least one bibliography file.
- **Key conflicts** (kaufman2008/2008a swapped; wind2019a two different papers): see N3-M2.
- **Still awaiting PDF verification (FI-17, marked):**
  - worldeconomicforum2025;
  - the framing claims for safardilha2019, memmert2011, batey2012 and barbot2019b;
  - the ".70" claim;
  - kaufman2008a;
  - primi2019 / forthmann2023 on product-level precision;
  - pellegrino2025 "retained a GRM";
  - the kempe2018 / zahno2023 / dejoode2023 characterisation.
- **Should be added to FI-17:** see n9.

### Interpretation in the Results

The Results are descriptive and carry no ATC markers. The remaining evaluative sentences are methodological caveats and are acceptable:
- line 161: "spacing is partly the same fact as discrimination";
- line 175: "supported by the LR test and AIC, but not by BIC";
- line 187: "the scores differ, not which score is more accurate".

**One exception:** line 149, "Products with different numbers of ratings were also rated by different raters". This is an unsupported factual claim about the design, not printed in the notebook (n2).

---

## 5. Marker check

**Volume.** There are **58 visible markers: 31 [AUTHOR TO CONFIRM] and 27 [FILL IN]**, down from 76. The reduction is appropriate. The Discussion still has a marker after almost every paragraph, but each now corresponds to a distinct claim.

**Present and appropriate:**
- all Methods gaps;
- the FI-17 verification items;
- the novelty claims, ATC-2 in the abstract and the Introduction;
- the departure from the CAT rules (ATC-19);
- the cumulative-link rationale (ATC-8);
- "did not change" (ATC-26);
- each interpretive Discussion paragraph;
- the projection side note (ATC-5);
- the box (ATC-23).

**Over-claims without a marker, or under a marker that does not fit the claim:**

| Location | Claim | Problem |
|---|---|---|
| 9, 228, 249 | "model rater differences rather than average them" | Marked (ATC-15), but line 217 concedes that the evidence for accuracy is absent. A marker does not cure this: re-ground or soften it (C-M1). |
| 51, 61, 213 | The MFRM assumes a shared category structure | Marked only at 213 (ATC-7/9), and conceptually inaccurate (N3-M1). |
| 149 | Products with different n were rated by different raters | No marker, no support (n2). |
| 205 | Attributions to primi2019 and myszkowski2021 | No FI-17 marker (n9). |
| 207 | R18 "widest information intervals" | Factually wrong for R18; ATC-12 covers only the ranking point (n1). |
| 215 | "These differences have consequences" (n = 2 reversals) | Marked (ATC-22), but needs the rating-pattern qualifier (n3). |
| 9 | LR tests "rejected … equal discrimination" | No marker, and the BIC disagreement is omitted (n5). |
| 226 | "so that raters are linked and their parameters comparable" | Covered only by the box-wide ATC-23; overstated (n10). |

**Missing [FILL IN] items to consider:**
- the definition of a "computable" Q3 pair (m6);
- the rater composition by number of ratings, if the line-149 claim is kept (n2, FI-4).

---

## 6. Optional extensions (not counted as issues)

The author has deliberately excluded these. They are listed once for completeness, and several are already named as future work at line 245:
- a severity test (model without rater effects vs M1);
- an M1–M2 LR test within one package;
- a held-out predictive check of model-based against raw-mean scores;
- the projection over parameter draws, with workload-weighted or selected rater sets;
- k for a target reliability (.70 / .80 / .90);
- diagnostics of the rejected parameter draws;
- a sensitivity refit with a non-normal latent distribution;
- equal-raw-mean ranges without the five raters with fewer than 75 ratings;
- the rater composition of products by number of ratings.

---

## 7. Top 5 remaining points

1. **Re-ground or soften the "model rather than average" recommendation** (C-M1; abstract line 9, box item 5 line 228, Conclusion line 249). Base it on the observed rater differences plus the known confounding of raw means in incomplete designs (@primi2019), or word it as "consider". Do not imply that the GRM scores were shown to be more accurate (line 217).
2. **Correct the MFRM framing** (N3-M1; lines 51, 61, 101, 213, 249). A shared category structure is a property of the rating-scale MFRM (M1), and M2 is the partial-credit MFRM. The case against the Rasch family rests on equal discrimination, where BIC disagrees. Also add the BIC qualifier to the abstract (n5).
3. **Fix the bibliography conflicts** (N3-M2). kaufman2008/kaufman2008a are swapped, and wind2019a points to different papers in the two .bib files. Deduplicate to a single source of truth, realign the keys, re-render and check the reference list.
4. **Complete the Methods FILL INs and the FI-17 verifications** (C2, M7, M8, n9; author). Above all, cover allocation (FI-4) and the rater pool (FI-21). FI-4 also decides whether the line-149 claim (n2) stays.
5. **Apply the small accuracy fixes:**
   - R18's interval claim (n1, line 207);
   - the n = 2 reversal qualifier (n3, line 215);
   - the range qualifier (n4, line 211);
   - "each rater equally likely" in the projection note (n6);
   - resolve ATC-26 "did not change the scores" (m4, line 91);
   - define or rephrase Q3 "computable" pairs (m6, lines 111 and 139).
