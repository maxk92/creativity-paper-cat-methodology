# 05_review.md: Peer review, FOURTH ROUND (reviewer-critic, Phase 7)

Manuscript reviewed: `manuscript/manuscript.qmd` (working-tree revision after commit b769767; 332 lines).
Checked against:
- `03_findings.md` (re-run after commit 0411801), including Changes item 12 (removed values) and Flags 13–15;
- `02_artifacts.md` (42 labels, 37 embedded);
- the round-3 review (previous version of this file);
- `/home/max/drive/phd_library.bib`, now the only bibliography in the YAML (line 25).

Venue: Creativity Research Journal (profile imrad-apa). Line numbers refer to the current `manuscript.qmd`.

I respected these author positions and do not criticise them here:
- the empirical focus, with the projection kept as a side note;
- no requests for analyses that add design choices only to project or extrapolate (listed once, in Section 6);
- the sparse design is not foregrounded;
- the Methods FILL INs (allocation, raters, stimuli, ethics, software versions, data availability, and the Q3 "computable" definition);
- the author-supplied cause of the "not recognised" ratings (line 90).

APA formatting (no leading zero for values bounded by 1, *p* < .001, thousands separators) is intended and is not counted as a mismatch.

---

## 1. Summary and recommendation

This revision closes every substantive point from round 3. No critical or major issues remain.

**Fixed since round 3:**
- **MFRM framing (N3-M1).** A shared category structure is now attributed only to the rating-scale MFRM (M1). M2 is identified as the partial-credit MFRM (lines 52, 102). Equal discrimination is named as the one constraint common to all Rasch-family models, and the BIC disagreement is stated each time this result is used: abstract, Discussion 198 and 216, Limitations 248, Conclusion 254. The argument is now correct and fair to the Rasch tradition.
- **Bibliography (N3-M2).** There is one bibliography file. kaufman2008 is the *Essentials* book and is cited for the "five to ten" rule (line 46). kaufman2008a is Kaufman, Baer, Cole and Sexton (2008, CRJ). wind2019 is Wind and Jones (2019, incomplete designs), cited for linking (lines 210, 226). wind2019a is Wind and Sebok-Syer (2019, DRF), cited for differential rater functioning (line 248). All cited keys resolve, and none is defined twice.
- **"Model rather than average" (round-1 M1 / C-M1).** The recommendation now reads "consider", is grounded in the observed rater differences, and states in the abstract, box item 5 and the Conclusion that greater accuracy was not shown. This was the main gap between claims and evidence, and it is closed.
- **Round-3 minor points.** n1–n5 and n7–n12 are resolved. Only n6 is partly open: the projection still has no pointer in Methods.
- **Numbers.** Every number checked matches `03_findings.md`, and no removed value is quoted (Section 4).

**What remains:**
1. The **Methods FILL INs and the FI-17 source checks**. These are the author's task and a precondition for submission, not review issues.
2. A short list of **minor wording, traceability and format points** (Section 3). None needs a new analysis. The most visible are:
   - the abstract (length, an unqualified calibration-set recommendation, and markers in the rendered text);
   - the per-rater response-style values, which are quoted but not shown in any embedded object;
   - the table labels "M1 (RSM/MFRM)", which now conflict with the corrected text, where M2 is also an MFRM.

**Recommendation: minor revision, close to acceptance.** I would consider the manuscript ready for submission once:
- the author has completed the FILL INs and FI-17 verifications;
- the minor points below have been applied or consciously declined.

A psychometric reviewer may still ask for the analyses the paper did not run. Lines 248–250 now present them as "beyond the scope of this descriptive study", which is the right mitigation.

**Counts:**
- Response check (33 points): **17 resolved, 3 partially resolved, 0 not resolved, 8 deferred to author, 5 declined (under author priority or project rule).**
- New issues: **0 critical, 0 major, 11 minor.** Five of the minor issues were introduced or exposed by this revision; six are pre-existing points first raised now.

---

## 2. Response check

Status codes:
- **R** = resolved;
- **P** = partially resolved;
- **N** = not resolved;
- **D** = deferred to author (a FILL IN or an author decision);
- **X** = declined under author priority or under the project rule that numbers are quoted as printed.

### 2a. Round-3 points

| # | Status | Justification | Location |
|---|---|---|---|
| N3-M1 MFRM equated with a shared category structure | **R** | The rating-scale vs partial-credit MFRM distinction is introduced with eckes2015, which carries an FI-17 marker. RQ3a is reworded. M2 is identified as the partial-credit MFRM. The Discussion says that the Rasch family as a whole is questioned only by the discrimination result, on which BIC disagreed. Residual: the table labels "M1 (RSM/MFRM)" (new minor m-4). | 52, 62, 102, 108, 198, 216, 248, 254 |
| N3-M2 Conflicting bib keys | **R** | `web_references.bib` is removed from the YAML. Key-by-claim check: kaufman2008 (book) for "five to ten"; kaufman2008a (CRJ 2008) for alpha > .70 and "mask"; wind2019 (Wind & Jones) for linking; wind2019a (DRF) for DRF. Residual: the "mask" claim is newly attributed and not yet on FI-17 (new minor m-2). | 25, 44, 46, 202, 210, 226, 248 |
| C-M1 / round-1 M1 "Model rather than average" | **R** | Abstract: "consider scoring with a model that adjusts for rater differences and report how far it departs from raw means". Box item 5 ends "This study does not show that model-based scores are more accurate." Conclusion: "whether such scores are more accurate remains to be examined". These agree with line 222. | 9, 222, 233, 254 |
| n1 R18 information interval | **R** | Now "R19 and R16 also had the widest information intervals" (R19 [0.41, 11.02], R16 [0.73, 6.49]). Residual SE wording: new minor m-8. | 210 |
| n2 Unsupported rater-composition claim | **R** | Replaced by "products did not receive their number of ratings through a design manipulation (see Rating design)" plus an FI-4 marker. | 150 |
| n3 n = 2 reversals not purely rater effects | **R** | Rating-pattern clause added. The .042 value is identified as the one that reflects rater differences alone, as modelled. | 218 |
| n4 Range set by extreme raters | **R** | "As a range, it is set by the most extreme raters …, some of whose parameters are imprecise (R18, R19)." | 214 |
| n5 Abstract qualifiers | **R** | "shared rating-scale structure", "although BIC favoured equal discrimination" and "raw share of lowest-category ratings". | 9 |
| n6 Projection disclosure and placement | **P** | "(each rater equally likely)" is added in the Discussion and the supplement, matching the notebook caption. Still missing: a one-sentence pointer in Methods (Scores and reliability). The values still appear first in the Discussion, which is acceptable for a side note if the author prefers. | 116–118, 204, 305 |
| n7 Misplaced response-style sentence | **R** | Moved to the end of the response-style paragraph. | 158 |
| n8 RQ2 "severity" | **R** | RQ2 now reads "threshold location, scale use, discrimination and information". | 61 |
| n9 Unverified attributions | **R** | FI-17 markers added for looney2004/anderlucci2021/heiniger2021 (48), myszkowski2021/primi2019 (208), and wind2018/wind2019/reise1990 (210). | 48, 208, 210 |
| n10 Box item 3 overstated | **R** | "more strongly linked and their parameters more precisely estimated". | 231 |
| n11 Ambiguous model-fit sentence | **R** | "the GRM is lower by 46.566 on AIC, BIC and SABIC alike". | 140 |
| n12 Misplaced agreement sentence | **R** | Moved to the raw-mean paragraph. | 218 |

### 2b. Earlier points still open in round 3

| # | Status | Justification | Location |
|---|---|---|---|
| N-M2 (round 2) Projection gives no planning answer | **X** | Declined under author priority. Box item 2 is worded without a k-for-target figure. | 230 |
| C2 Methods not reproducible | **D** | FI-1–4, 6, 15, 21–23. A precondition for submission. | 70–92, 132 |
| M3 Cross-package M1–M2 LR test | **X** | Disclosed as approximate and listed as beyond scope. | 108, 248, 250 |
| M5 Truncated parameter draws | **X** | Disclosed as conditional and approximate. | 116, 244 |
| M6 Dependence on the normal prior | **X** | Disclosed (prior dependence of rel~post~, normal latent distribution despite low-end concentration). | 118, 204, 244 |
| M7 "Not recognised" missingness | **D** | The cause is author-supplied (90). The MAR caveat is present (240). The rate by rater is FI-22. | 90, 240 |
| M8 Student raters and CAT "appropriate judges" | **D** | Scope caveats present. Pool description is FI-21. | 74, 226, 246 |
| M11 Results as a number list | **R** | The ladder paragraph is split into "LR tests and criteria" (176) and "M3 range, step order, M1 fit" (178). | 176, 178 |
| M12 Render and display problems | **P** | Fixed in the notebook: tolerance "10⁻⁴", M3 "0.001", "info_weighted_area" removed, replication captions corrected. Remaining items are on the FI-18 list (code-name Quantity labels, "M1 (RSM)" vs "M1 (RSM/MFRM)", empty "Overlap" column, diagonal "1", scientific-notation *p*, separators in notes). Add the ambiguous "Ratings (n)" in `tbl-grm-reliability-by-n` and `tbl-raw-mean-vs-grm` (02_artifacts, display item 5) to FI-18. | comment line 32 |
| m3 Over-precise values | **X** | Withdrawn. The five-decimal values (92, 194, 246) are printed that way in `tbl-sensitivity-rater-exclusion`, and the project rule forbids rounding. The five decimals are also needed to show the .67199/.67186 difference. | 92, 194, 246 |
| m4 "Did not change the scores" | **R** | "changed the product scores only slightly [ATC-26], with a largest change … of 0.16246". | 92 |
| m6 Q3 "computable" pairs | **R** | Rephrased as "the pairs for which Q3 could be computed (137 of 171)". The definition is deferred to FI-30, which is correct because it is not in the notebook (03_findings F1.9). | 112, 140 |
| m10 Cause of "not recognised" | **D** | Author-supplied text now in place (90). | 90 |
| m18 Supplement S-numbering | **D** | FI-16. | comment line 31 |
| m19 `tbl-marginal-reliability-models` unused | **D** | Open author option (comment line 35). Still recommended: it is an existing result and supports RQ3b without new design choices. | — |
| m20 Drift and collection timespan | **D** | FI-3 (data-collection period). | 82 |
| m21 Abstract density | **P** | Now about 250 words and still number-dense (see new minor m-1). | 9 |
| m22 Figure captions and legends | **D** | FI-18. | comment line 32 |

**Tally:**

| Status | Round-3 points (15) | Earlier points still open (18) | Total (33) |
|---|---|---|---|
| Resolved | 14 | 3 | **17** |
| Partially resolved | 1 | 2 | **3** |
| Not resolved | 0 | 0 | **0** |
| Deferred to author | 0 | 8 | **8** |
| Declined (author priority / project rule) | 0 | 5 | **5** |

Which points are in each column:
- **Round-3 points (15):** N3-M1, N3-M2 and C-M1/round-1 M1 (counted once), plus n1–n12.
- **Earlier points (18):** N-M2, C2, M3, M5–M8, M11, M12, m3, m4, m6, m10 and m18–m22.

---

## 3. New issues

### Critical

None.

### Major

None.

### Minor

Items marked **(rev.)** were introduced or exposed by this revision. Items marked **(pre.)** are pre-existing and first raised now.

- **m-1 (rev.) Abstract: length, an unqualified calibration recommendation, markers (line 9).**
  - The abstract is now about 250 words. Check the CRJ limit (FI-16). If it must be shortened, the clauses "We fitted, by marginal maximum likelihood, …" and the per-n reliabilities are the easiest to compress.
  - "link raters through a common calibration set" is stated without the qualification the Discussion gives (line 226: only if raters with few ratings rate it and it is large enough), and the study did not use such a set. Ground it in the data ("because parameters of raters with few ratings were imprecise, …") or soften it to "consider".
  - Two [AUTHOR TO CONFIRM] markers sit inside the rendered abstract. They must be removed before submission.
  - "19 student raters" depends on FI-1 ("confirm") but carries no marker of its own.
- **m-2 (rev.) The kaufman2008a "mask" claim is not on the FI-17 list (lines 46, 202).** After the key realignment, Kaufman, Baer, Cole and Sexton (2008, CRJ; expert vs nonexpert raters) is cited for "a high alpha from a large panel can mask low agreement among individual raters" (46) and again for the Krippendorff-vs-Cronbach contrast (202). The FI-17 marker at line 46 covers only "five to ten" (kaufman2008) and primi2019/forthmann2025. Add the "mask" attribution to FI-17. If the CRJ article does not make the point, cite the source that does (for example the *Essentials* book, if that is where it is made).
- **m-3 (rev.) "Q3" used for both a quartile and Yen's statistic (line 154).** "interquartile range of .173 (Q1 .596, Q3 .769)" appears 14 lines after the Q3 local-dependence results (140). Write "first and third quartiles .596 and .769". The overview table note prints "Q1 0.596, Q3 0.769"; changing the wording in the text does not change any number.
- **m-4 (rev.) Table labels contradict the corrected MFRM framing (tables `tbl-model-fit`, `tbl-score-agreement`, `tbl-theta-correlations`, `tbl-rater-fit-m1`, `tbl-marginal-reliability-models`; captions of `tbl-model-fit` and `tbl-rater-fit-m1`).** The text now says that M2 is also an MFRM (partial-credit form), but the tables label only M1 as "RSM/MFRM", and the captions say "rating scale model / MFRM". A reader who compares text and tables will see an inconsistency. FI-18 already proposes "M1 (rating-scale MFRM)". With the text change this is no longer cosmetic, so apply it in the notebook labels and captions. "M2 (PCM)" could become "M2 (PCM; partial-credit MFRM)". This is display only.
- **m-5 (rev.) Projection has no pointer in Methods (residual of n6).** The projection is described only in the supplement (305). One sentence at the end of Scores and reliability (around line 118) would complete the Methods, for example: "As a side note, reliability for 1–10 ratings per product was projected from the fitted GRM (Supplement)". This is a description, not a new analysis.
- **m-6 (pre.) Response-style values are quoted but not shown (lines 9, 158, 208).** Rater SDs, floor, ceiling and central rates (for example .579/.016, .799/.764/.735/.192, .080) come from the unlabelled N1 cell `fb6df84b` (03_findings F0.8). The embedded figure `fig-overview-rater-response-styles` shows means, SDs, categories used, and extreme vs middle shares, but not the floor, ceiling or central rates. The abstract's only rater-difference number (.579 to .016) is therefore not traceable to any object in the paper. Label that cell's table and embed it in the supplement. This is display only: the values already exist.
- **m-7 (pre.) Inconsistent paraphrase of cseh2019 (lines 46 vs 204).** Line 46: "the *number of raters* must be established for each domain". Line 204: "who argue that *reliability* must be established for each domain". Use one wording that matches the source.
- **m-8 (pre.) "Largest standard errors" is imprecise for R18 (line 210).** R18's discrimination SE (0.26) is not large; its *threshold* SEs are the largest (b1 *SE* 3.05). R19 and R16 have the largest discrimination SEs (2.22, 1.36). Write, for example, "which also had the largest standard errors (R18 for its thresholds, R19 and R16 for their discriminations)".
- **m-9 (pre.) Quintile changes read without the size of the shifts (line 220).** "The choice among the models also shifted rankings: … .202 of products changed quintile under M1 and .075 under M3". A quintile change also counts small moves across a boundary. Mean percentile shifts are already reported in Results (.042 for M1, .017 for M3; line 186). Quote them in the same sentence so that the reader does not over-read the quintile shares.
- **m-10 (pre.) Ambiguous referent and citation placement (lines 226, 120).**
  - Line 226: "a calibration set … is distinct from rater training, which conflicts with the CAT rule …". "which" can be read as referring to the calibration set. Write "…distinct from rater training; training, unlike a calibration set, conflicts with …".
  - Line 120: "[see also @hove2024]" follows Krippendorff's alpha. ten Hove et al. (2024) is about choosing ICCs for incomplete designs. Move the citation to a sentence about reliability indices in incomplete designs, or drop it. A reviewer may otherwise ask why no ICC was reported (an analysis the paper need not add).
- **m-11 (pre.) Format and model-equivalence wording (YAML line 15; line 102).**
  - `number-sections: true` in the PDF format numbers the headings, which APA 7 does not do (CRJ uses APA). Set it to false or check the CRJ template (FI-16).
  - Line 102: "M1 was the RSM, equivalent to a two-facet rating-scale MFRM". A Rasch reviewer may note that Facets estimates the MFRM by JMLE with fixed product parameters, whereas M1 here is estimated by MML with a normal product distribution (latent variance 0.962 in `tbl-marginal-reliability-models`). Write "corresponds to … (estimated by marginal maximum likelihood)". This is wording only.

---

## 4. Number and citation check against 03_findings.md and phd_library.bib

### Numeric mismatches

**None found.** Every number in the abstract, Methods, Results, Discussion, Conclusion and supplement text was checked against `03_findings.md`:
- **Cleaning and design:** 9,148 / 1,290 / 0.0 (R04) / 12 pairs, 13 rows / 7,844 / 22; R20 13, R21 9, R22 2 (24); one product dropped; 7,820 / 3,668 / 19; 50–1,174; 2.132, median 2, 1–10, 1.726; .112; 17 of 171; median overlap 13; unused categories (R01, R03, R06, R18: 7; R17: 6 and 7).
- **Estimation:** 61 points, 10⁻⁴, 165 iterations; 200 draws, 87 rejected.
- **Fit:** −11,733.227 / −11,756.510 / 46.566 / 127; S-X² *p* .294–.671; infit 0.334–0.971, outfit 0.322–0.961 (R19, R18); Q3 −.238, 137 of 171, 20 flagged, ten shown, nine negative, R10–R11 positive; ≥ 30 shared products, 0.2; C2 17 of 171; about 90%.
- **Reliability:** .672 [.649, .687]; .960 [.953, .968], grid .960; .928 [.891, .943] (14, 1,900; 639 of 1,000; 361); .658 [.526, .756] (3, 139); .392 [.362, .417] (19, 2,771); by n .520 (897), .698 (2,080), .757 (357), .919 (3), monotone; PSD 0.686 → 0.285; rel~post~ median .698, IQR .173 (.596, .769), .057–.929; *r* = .935; 320.
- **Raters:**
  - means 1.760 (R06)–3.836 (R18); SD 1.022 (R01)–1.953 (R19); floor .579 / .016; ceiling .080, five at .000; central .799 / .764 / .735 / .192; categories 2,029 / 2,113 / 109;
  - b1 −6.56 (3.05) to 0.29 (0.06); −3.38 (0.49); R02 −0.71 / 2.03; R13 −3.38 / 4.43; threshold counts 4 / 5 / 6;
  - *a* 0.63 (0.26), 3.71 (2.22), 3.70 (1.36), 0.86 (0.15), 1.96 (0.16), 2.50 (0.33), 2.81 (0.42); R17 1.45, R12 2.90;
  - information 0.12 [0.01, 0.35], 3.54 [0.41, 11.02], 3.30 [0.73, 6.49], 0.24 [0.11, 0.42], 0.98 [0.72, 1.22], 1.70 [0.90, 2.56]; shares .005 [.000, .013], .135 [.017, .331]; θ max 2.700 / 2.400 / −0.550; shares at θ = ±2 .001, .083, .221.
- **Ladder:** χ²(84) = 737.457, χ²(18) = 121.958, both *p* < .001; AIC 23,767.020 / 23,852.978; BIC 24,529.585 / 24,555.360; M3 *a* 0.283 (0.055) – 2.606 (1.419); nine / nine unordered; M1 fit R17 1.328 / 1.190, R18 1.009 / 1.071, R12 0.238 / 0.255.
- **Raw mean vs GRM:** all 12 cells of `tbl-raw-mean-vs-grm`; τb range .815–.842 (198).
- **Score agreement:** .975 / .978 / .042 / .202; .985 / .983 / .033 / .150; .996 / .996 / .017 / .075; ladder .980–.993 and .983–.996; 1.000.
- **Sensitivity:** .67199 / .67186; .95986 / .96186; 7,844 / 3,669; .99997; 0.00171; 0.16246; .00491; .99880; 0.19820.
- **Projection (side note):** .508, .688, .925; 50 replications, 2,000 products, seed 20260713; "each rater equally likely" matches the notebook caption.

### Removed or unprinted values (Changes item 12, Flag 13)

**None quoted.** A pattern search for the removed values found only legitimate coincidences:
- .334 (R19 infit); .022 (part of 1.022); .080 (R19 ceiling, F0.8, not the pooled mean shift); .959 and .004 (parts of .95986 and .00491).
- "Confounded" (lines 50, 214) is attributed to @primi2019, not to the notebook.
- No most/least-informative value, true_r2, pooled raw-mean statistic, subgroup correlation or percentile shift, tolerance "0.0001"/"0.000", "0.000545256", "6 unused end categories", 0.7–1.3 range or target-k value appears.
- The "at least 3 shared products" Q3 definition, which exists only in the R code, is correctly **not** stated (FI-30).

### Citations (phd_library.bib only)

- **Resolution.** All 74 cited keys resolve in `phd_library.bib`, each defined once. They include myford2003/2004, embretson2013, runco2012, joode2023, ayala2022, hove2024 and forthmann2025. `web_references.bib` is no longer in the YAML.
- **Keys flagged in round 3: content now matches claims.**

| Key | Entry | Cited for | Match |
|---|---|---|---|
| kaufman2008 | Kaufman, Plucker & Baer (2008), *Essentials of Creativity Assessment* (bib note: source of the "5–10 judges" rule) | "five to ten raters" (46) | Yes |
| kaufman2008a | Kaufman, Baer, Cole & Sexton (2008), CRJ 20(2), expert vs nonexpert CAT raters | alpha > .70 (44, FI-17); "high alpha can mask low agreement" (46, 202) | Plausible; "mask" not yet on FI-17 (m-2) |
| wind2019 | Wind & Jones (2019), JEM 56(1), incomplete rating designs and rater effects | linking set (210); calibration links raters (226) | Yes |
| wind2019a | Wind & Sebok-Syer (2019), JEM 56(2), differential rater functioning | DRF not tested (248) | Yes |
| wind2018 | Wind & Jones (2018), linking set size in sparse networks | linking set (210) | Yes |

- **Other spot checks, metadata vs claim:**
  - eckes2015 for the rating-scale vs partial-credit MFRM and for connectedness: plausible, FI-17 marked.
  - pellegrino2025 (IRT for divergent-thinking rater effects) "retained a GRM": FI-17 marked.
  - shin2025 (Rasch validation of a coach-rated creactability scale) matches the "rates players rather than actions" characterisation.
  - hove2024 is about ICCs in incomplete designs; placement is questionable (m-10).
  - forthmann2025 (planning missing-data designs for ratings) fits product-level precision, FI-17 marked.
- **Still awaiting PDF verification (FI-17, marked):** wef2025/oecd2024 and the sport framing claims; ".70"; kaufman2008 "five to ten"; primi2019/forthmann2025; looney2004/anderlucci2021/heiniger2021; eckes2015 PCM-MFRM; pellegrino2025; kempe2018/zahno2023/joode2023; myszkowski2021/primi2019 (208); wind2018/wind2019/reise1990 (210). **Add:** kaufman2008a "mask" (m-2).

### Interpretation in the Results

The Results are descriptive. The remaining evaluative sentences are methodological caveats and are acceptable:
- "in the GRM, spacing is partly the same fact as discrimination" (162);
- "supported by the LR test and AIC, but not by BIC" (176);
- "the scores differ, not which score is more accurate" (190);
- "These values are observed …" (150, with FI-4).

No mechanism sentence from the notebook markdown (Flag 14) is quoted in the Results.

---

## 5. Marker check

**Volume.** There are **62 visible markers: 30 [AUTHOR TO CONFIRM] and 32 [FILL IN]** (round 3: 58). The increase is appropriate. It comes from the new FI-17 verification markers (48, 52, 208, 210), FI-30 (112) and FI-4 (150), each tied to a specific claim.

**Present and appropriate:**
- all Methods gaps (FI-1–4, 6, 9, 15, 21–23, 30);
- the FI-17 verification items;
- novelty (ATC-2, abstract and line 54);
- exploratory framing (ATC-20);
- departure from the CAT rules (ATC-19);
- the cumulative-link rationale (ATC-8);
- "only slightly" (ATC-26);
- S-X² power (ATC-11);
- each interpretive Discussion paragraph;
- the projection side note (ATC-5);
- the box (ATC-23);
- the Conclusion (ATC-1, 5, 14, 15).

**Claims without a marker, or under a marker that does not fit the claim:**

| Location | Claim | Problem |
|---|---|---|
| 46, 202 | kaufman2008a: high alpha can mask low agreement | No FI-17 entry for this attribution (m-2). |
| 9 | "19 student raters" | Depends on FI-1 ("confirm"), unmarked in the abstract (m-1). |
| 9 | "link raters through a common calibration set" | Marked (ATC-14) but lacks the qualification given at line 226 (m-1). |
| 210 | "largest standard errors" for R18, R19, R16 | Covered by ATC-12 for the ranking point only; imprecise for R18 (m-8). |

**Before submission:** every marker, including the two inside the rendered abstract, must be resolved and removed. The hidden comment block (lines 29–36) does not render and can stay until the final pass.

---

## 6. Optional extensions (not counted as issues)

The author has excluded these. They are listed once for completeness, and lines 248–250 already name most of them as beyond scope:
- a severity test (no-rater-effect model vs M1);
- an M1–M2 LR test within one package;
- a held-out predictive check of model-based against raw-mean scores;
- projections over parameter draws, or with workload-weighted or selected rater sets;
- k for a target reliability;
- diagnostics of the rejected parameter draws;
- a non-normal latent distribution refit;
- an ICC for the incomplete design.

---

## 7. Top 5 remaining points

No substantive issue remains. Once the author has completed the FILL INs and FI-17 checks, the paper is ready for submission, subject to these points:

1. **Complete the Methods FILL INs and the FI-17 verifications** (C2, M7, M8; author). Above all, cover allocation (FI-4), the rater pool (FI-21), the non-recognition rate (FI-22) and the Q3 "computable" definition (FI-30). Add kaufman2008a's "high alpha can mask low agreement" to FI-17 (m-2).
2. **Finish the abstract** (m-1, m21):
   - check the CRJ word limit (about 250 words now);
   - qualify or soften the calibration-set recommendation;
   - remove the in-abstract markers;
   - confirm "student raters".
3. **Align the table labels with the corrected MFRM framing** (m-4): "M1 (rating-scale MFRM)", and M2 marked as the partial-credit MFRM. Also complete the other FI-18 display items, including "Ratings (n)" per product vs per rater (M12).
4. **Make every quoted number traceable to an object:** label and embed the per-rater response-style table from N1 `fb6df84b` (m-6, display only). Consider embedding `tbl-marginal-reliability-models` (m19).
5. **Apply the small wording fixes:**
   - one Methods sentence pointing to the projection (m-5);
   - "first and third quartiles" instead of Q1/Q3 (m-3);
   - consistent cseh2019 paraphrase (m-7);
   - the R18 standard-error wording (m-8);
   - mean percentile shifts next to the quintile shares (m-9);
   - the "which" referent and the hove2024 placement (m-10);
   - unnumbered APA headings and the M1 "corresponds to (MML)" wording (m-11).
