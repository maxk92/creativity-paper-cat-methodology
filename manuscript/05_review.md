# 05_review.md: Peer review, FIFTH ROUND (reviewer-critic, Phase 7)

Manuscript reviewed: `manuscript/manuscript.qmd` (working tree after commit 04aefc5, final wording pass; 342 lines).
Checked against:
- `03_findings.md` (re-run after commit 04aefc5), including Changes item 8 (never-quote list) and Flags 5, 7, 13–15;
- `02_artifacts.md` (43 labels);
- the round-4 review (previous version of this file);
- `/home/max/drive/phd_library.bib` (the only bibliography in the YAML, line 26).

Venue: Creativity Research Journal (profile imrad-apa). Line numbers refer to the current `manuscript.qmd`.

I respected these author positions and do not criticise them here:
- the empirical focus, with the projection kept as a side note;
- no requests for projection, simulation or further model-test analyses (listed once, in Section 6, not counted);
- the sparse design is not foregrounded;
- the Methods FILL INs are the author's;
- the author-supplied cause of the "not recognised" ratings (line 96).

APA formatting (no leading zero for values bounded by 1, *p* < .001, thousands separators) is intended and is not counted as a mismatch.

---

## 1. Summary and recommendation

The final wording pass applied all eleven round-4 minor points. Ten are fully resolved. One (m-4, model labels) is resolved in the table cells, but the old labels remain in three captions and in the row labels of one main-text table. These are already on the FI-18 display list.

**Fixed since round 4:**
- **Abstract.** It has 249 words and no rendered markers. The calibration-set phrase is conditional ("because some rater parameters were imprecise, consider …"). The claims behind the removed markers are tracked in the hidden comment block (lines 32–36).
- **Traceability.** `tbl-overview-rater-response-styles` is embedded in the supplement (line 279) and cited at lines 132, 166 and 216. Every response-style value quoted in the text, including the abstract's .579 to .016, can now be found in an embedded object.
- **Methods completeness.** The Q3 "computable" definition is now stated (line 118) and matches the notebook note (F1.9). A one-sentence pointer to the projection is in place (line 128). M1 is described as estimated by marginal maximum likelihood with a normal product distribution (line 108).
- **Wording.** The following are fixed:
  - "first and third quartiles" (162);
  - one cseh2019 paraphrase, used at 52, 60 and 212;
  - R18's threshold standard errors (218);
  - mean percentile shifts next to the quintile shares (194, 228);
  - the "which" referent (234);
  - hove2024 now sits on a sentence about incomplete designs (126), which fits the source;
  - kaufman2008a's "mask" claim and the cseh2019 paraphrase are on FI-17 (line 52; comment line 38).
- **Format.** `number-sections: false` for both docx and pdf (lines 13, 16).
- **Numbers.** Every number checked matches `03_findings.md`, and no value from the never-quote list appears (Section 4).

**What remains:**
1. **The author's items:** the Methods FILL INs, the FI-17 source checks and the ATC confirmations. These are preconditions for submission, not review issues.
2. **FI-18 display fixes** in the notebook. The most visible is the main-text `tbl-reliability-overview`, which still prints "M1 (RSM)", "M2 (PCM)" and "Q1 0.596, Q3 0.769".
3. **Seven new minor points** (Section 3), all wording or format. None needs an analysis. The one with the most substance is m5-1: the Methods say θ is standard normal in all models, but M1 and M2 estimated the latent variance.

**Recommendation: minor revision. From the reviewer's side, the paper is ready for submission once the author items and the FI-18 display fixes are done.** The seven new minor points are recommended, but none would block submission. A psychometric reviewer may still ask for the analyses the paper did not run. Lines 256–258 present these as beyond the scope of this descriptive study, which is the appropriate response.

**Counts:**
- Response check (27 points): **12 resolved, 2 partially resolved, 0 not resolved, 8 deferred to author, 5 declined (author priority or project rule).**
- New issues: **0 critical, 0 major, 7 minor.** One minor issue was introduced by this revision (m5-4); six are pre-existing and raised for the first time now.

---

## 2. Response check

Status codes:
- **R** = resolved;
- **P** = partially resolved;
- **N** = not resolved;
- **D** = deferred to author (a FILL IN or an author decision);
- **X** = declined under author priority or under the project rule that numbers are quoted as printed.

### 2a. Round-4 minor points (m-1 to m-11)

| # | Status | Justification | Location |
|---|---|---|---|
| m-1 Abstract: length, calibration phrase, markers, "student raters" | **R** | 249 words (comment line 36; the CRJ limit is still FI-16). The calibration phrase is grounded and conditional: "because some rater parameters were imprecise, consider linking …". No markers render. ATC-2, FI-1, ATC-5, ATC-14 and ATC-15 are tracked in the comment block. | 9; comment 32–36 |
| m-2 kaufman2008a "mask" not on FI-17 | **R** | Added to the FI-17 marker at line 52 and to comment line 38, with the instruction to change the source if needed. | 52, 210; comment 38 |
| m-3 "Q3" as quartile vs Yen's Q3 | **R** | The text reads "first and third quartiles .596 and .769". Residual (display only): the main-text `tbl-reliability-overview` note still prints "Q1 0.596, Q3 0.769". Add it to FI-18. | 162 |
| m-4 Model labels vs MFRM framing | **P** | The cells now print "M1 (rating-scale MFRM)" and "M2 (partial-credit MFRM)" (03_findings, Changes item 3). Still old: the `tbl-reliability-overview` row labels ("M1 (RSM)", "M2 (PCM)"; main text); the captions of `tbl-model-fit` ("M1 rating scale model / MFRM, M2 partial credit model"), `tbl-rater-fit-m1` and `tbl-threshold-order` ("M2 (PCM)"). All are listed under FI-18. | 156; supplement 333–339; comment 39 |
| m-5 Projection pointer in Methods | **R** | "As a side note, the reliability expected for 1 to 10 ratings per product was projected from the fitted GRM …" | 128 |
| m-6 Response-style values not shown | **R** | `tbl-overview-rater-response-styles` is embedded and cross-referenced. The manuscript does not quote R09's mean, so the 3.642/3.643 display difference (Flag 5) does not arise. | 132, 166, 216, 279 |
| m-7 cseh2019 paraphrase | **R** | One wording, "the number of raters needed for adequate reliability has to be established for each domain", is used at 52, 60 and 212, and is on FI-17. | 52, 60, 212 |
| m-8 R18 standard errors | **R** | "(R18 for its thresholds, R19 and R16 for their discriminations)". | 218 |
| m-9 Quintile changes without size | **R** | Mean percentile shifts are given in Results (.042/.033/.017) and Discussion (.042/.017), with the boundary caveat. | 194, 228 |
| m-10 "which" referent; hove2024 | **R** | "…distinct from rater training; training, unlike a calibration set, conflicts with …". hove2024 now supports "Conventional reliability indices assume a complete design or must be adapted to an incomplete one", which matches the source (ICC guidelines for incomplete designs). | 126, 234 |
| m-11 Heading numbering; M1 equivalence wording | **R** | `number-sections: false` (docx and pdf). M1 "corresponds to a two-facet rating-scale MFRM …, here estimated by marginal maximum likelihood with a normal product distribution". See new m5-4 for a remaining redundancy. | 13, 16, 108 |

### 2b. Earlier points still open after round 4

| # | Status | Justification | Location |
|---|---|---|---|
| n6 (round 3) Projection disclosure and placement | **R** | Closed by the Methods pointer (m-5). The disclosure "each rater equally likely", with parameters treated as known, is in the Discussion and the supplement. | 128, 212, 315 |
| M12 Render and display problems | **P** | "Ratings (n)" is replaced by context-specific headers, and the model labels in the cells are fixed. The remaining items are on FI-18 (comment line 39): code-name Quantity labels; old model names in captions and overview rows; empty "Overlap" column; diagonal "1" and integer "3"/"0" cells; scientific-notation *p*; missing separators in notes; three figure legends. Add the "Q1/Q3" note (m-3 residual). | comment 39 |
| m21 Abstract density | **R** | 249 words. Still number-dense, but each number supports a stated result. | 9 |
| N-M2 (round 2) Projection gives no planning answer | **X** | Declined under author priority. No k-for-target figure appears anywhere. | 212, 238 |
| C2 Methods not reproducible | **D** | FI-1–4, 6, 9, 15, 21–23. A precondition for submission. | 76–98, 126, 140 |
| M3 Cross-package M1–M2 LR test | **X** | Disclosed as approximate and listed as beyond scope. | 114, 256, 258 |
| M5 Truncated parameter draws | **X** | Disclosed as conditional and approximate (87 rejected). | 122, 252 |
| M6 Dependence on the normal prior | **X** | Disclosed: prior dependence of rel~post~, and a normal latent distribution despite the low-end concentration. | 124, 212, 252 |
| M7 "Not recognised" missingness | **D** | The cause is author-supplied. The MAR caveat is present. The rate by rater is FI-22. | 96, 248 |
| M8 Student raters and "appropriate judges" | **D** | Scope caveats are present. The pool description is FI-21. | 80, 234, 254 |
| m3 Over-precise values | **X** | Withdrawn in round 4. The five-decimal values are printed that way in `tbl-sensitivity-rater-exclusion`. | 98, 202, 254 |
| m10 Cause of "not recognised" | **D** | The author-supplied text is in place. | 96 |
| m18 Supplement S-numbering | **D** | FI-16 (crossref prefix setting). | comment 37 |
| m19 `tbl-marginal-reliability-models` unused | **D** | Still an open author option (comment line 41). I still recommend embedding it in the supplement. It would also back up the fix in m5-1 (latent variances 0.962 and 1.087). | — |
| m20 Drift and collection timespan | **D** | FI-3 (data-collection period). | 88 |
| m22 Figure captions and legends | **D** | FI-18. | comment 39 |

**No regressions.** I re-checked every point marked resolved in rounds 3 and 4: N3-M1, N3-M2, C-M1, n1–n5, n7–n12, M11, m4 and m6. All are still resolved. The Q3 definition (round-4 m6, FI-30) is now stated in the text rather than deferred.

**Tally:**

| Status | Round-4 minors (11) | Earlier open points (16) | Total (27) |
|---|---|---|---|
| Resolved | 10 | 2 | **12** |
| Partially resolved | 1 | 1 | **2** |
| Not resolved | 0 | 0 | **0** |
| Deferred to author | 0 | 8 | **8** |
| Declined (author priority / project rule) | 0 | 5 | **5** |

---

## 3. New issues

### Critical

None.

### Major

None.

### Minor

**(rev.)** marks issues introduced by this revision. **(pre.)** marks pre-existing issues raised for the first time now.

- **m5-1 (pre.) "Standard normal" is stated for all models, but M1 and M2 estimated the latent variance (line 106; also 108).**
  - **Problem.** Line 106: "All models share the JRT frame …: product creativity is a single latent dimension θ with a standard normal distribution." In Rasch-family models, discrimination is fixed, so the latent variance must be free. `tbl-marginal-reliability-models` prints latent variances of 0.962 (M1) and 1.087 (M2), and 1 for M3 and the GRM (F1.6). Line 108 correctly says "a normal product distribution" for M1.
  - **Why it matters.** A Rasch-oriented reviewer will notice this.
  - **Fix.** For example: "…with a normal distribution (mean 0; variance fixed at 1 in M3 and the GRM and estimated in M1 and M2, whose discriminations are fixed)". This is wording only. If the author wants to quote the two variances, embedding `tbl-marginal-reliability-models` (m19) makes them traceable.
- **m5-2 (pre.) The abstract's opening sentence claims more than the Introduction supports (line 9).**
  - **Problem.** "The CAT is the standard procedure for rating creative products and is also used for actions in sport."
  - **Why it matters.** The Introduction calls the CAT "the established method" (50). It describes the sport studies as trained-expert ratings on a scale from tactical-creativity research (60), and the Methods call the present procedure "CAT-style" and a departure from the CAT rules (76, 88). The sport studies are therefore not shown to be CAT.
  - **Fix.** Soften to, for example, "…is the established method for rating creative products, and similar expert ratings are used for actions in sport". This keeps the word count.
- **m5-3 (pre.) Box item 3 drops the condition stated in the Discussion (line 239 vs 234).**
  - **Problem.** The Discussion says that a calibration set stabilises the parameters of raters with few ratings "only if these raters rate it and it is large enough". Box item 3 says that rating a common set makes raters "more strongly linked and their parameters more precisely estimated", without the size condition.
  - **Why it matters.** The study used no calibration set, so the recommendation is not tested here.
  - **Fix.** Add "a sufficiently large common calibration set", or end the item with "(not tested in this study)". This is covered by ATC-14.
- **m5-4 (rev.) The new model names make the Methods definitions circular (line 108).**
  - **Problem.** "M1, the rating-scale MFRM, was the rating scale model … it corresponds to a two-facet rating-scale MFRM". "M2, the partial-credit MFRM, was the partial credit model … corresponds to a partial-credit MFRM".
  - **Fix.** Define each model once. For example: "M1 was the rating scale model with raters as items, which corresponds to a two-facet rating-scale MFRM (hereafter rating-scale MFRM) …". Do the same for M2. This is wording only.
- **m5-5 (pre.) The gap statements in the Introduction are categorical (line 60).**
  - **Problem.** "a Rasch analysis exists only for a coach-completed questionnaire" and "there is no evidence on how raters differ".
  - **Why it matters.** ATC-2 notes that the literature search was not systematic, so absolute absence claims are not supported.
  - **Fix.** Write "we found a Rasch analysis only for …" and "we found no evidence on …". The third gap already reads "to our knowledge".
- **m5-6 (pre.) A coefficient does not "describe the mean" (lines 52, 210).**
  - **Problem.** "A panel coefficient describes the mean over all raters of a panel" (52) and "The conventional figures describe the mean over a large or complete panel" (210).
  - **Fix.** Write "refers to the reliability of the mean over all raters of a panel". This makes the contrast with the precision of a single product's score precise.
- **m5-7 (pre.) Format and render checks (YAML lines 11–27; line 118; bibliography).**
  - **Manuscript format.** The PDF uses a plain `article` class, and `shorttitle` (line 3) is not used by it. If CRJ requires APA manuscript format (double spacing, running head, title page) at submission, switch the format or template rather than editing text (FI-16).
  - **Bibliography notes.** Several bib entries carry `note` fields such as "Found via web search for paper" and, for forthmann2025, "Citekey year 2023 = online-first …". Check in the rendered reference list that the CSL does not print them. If it does, change the CSL or the bib, not the rendered text.
  - **APA numerals.** "at least 3 jointly rated products" (118) would be "three" in APA 7 prose.

---

## 4. Number and citation check against 03_findings.md and phd_library.bib

### Numeric mismatches

**None found.** Every number in the abstract, Methods, Results, Discussion, Conclusion and supplement text was checked against `03_findings.md`:
- **Cleaning and design:** 9,148 / 1,290 / 0.0 (R04) / 12 pairs, 13 rows / 7,844 / 22; R20 13, R21 9, R22 2 (24); one product; 7,820 / 3,668 / 19; 50–1,174; 2.132, median 2, 1–10, 1.726; .112; 17 of 171; median overlap 13; unused categories (R01, R03, R06, R18: 7; R17: 6 and 7); 4/5/6 thresholds.
- **Estimation:** 61 points, 10⁻⁴, 165 iterations; 200 draws, 87 rejected.
- **Fit:**
  - −11,733.227 / −11,756.510 / 46.566 / 127; S-X² *p* .294–.671;
  - infit 0.334–0.971, outfit 0.322–0.961 (R19, R18);
  - Q3: −.238, 137 of 171, 20 flagged, ten shown, nine negative, R10–R11 positive; definition (≥ 3 shared products, residual variance) matches note `ef6ed18f`; ≥ 30 shared products, 0.2;
  - C2: 17 of 171; about 90% imputed.
- **Reliability:**
  - .672 [.649, .687]; .960 [.953, .968], grid .960;
  - .928 [.891, .943] (14, 1,900; 639 of 1,000; 361); .658 [.526, .756] (3, 139); .392 [.362, .417] (19, 2,771);
  - by n: .520 (897), .698 (2,080), .757 (357), .919 (3), "higher with each further rating" verified row by row; PSD 0.686 → 0.285;
  - rel~post~: median .698, IQR .173 (.596, .769), .057–.929; *r* = .935; 320.
- **Raters:**
  - means 1.760 (R06)–3.836 (R18); SD 1.022 (R01)–1.953 (R19); lowest-category share .579 (R06) / .016 (R13); highest-category .080 (R19), five at 0; middle .799 / .764 / .735 / .192; categories 2,029 / 2,113 / 109;
  - *b*~1~ −6.56 (3.05) to 0.29 (0.06); −3.38 (0.49) next lowest (verified against R09 −2.21, R10 −2.04, R12 −2.01); R02 −0.71 / 2.03; R13 −3.38 / 4.43;
  - *a* 0.63 (0.26), 3.71 (2.22), 3.70 (1.36), 0.86 (0.15), 1.96 (0.16), 2.50 (0.33), 2.81 (0.42); R17 1.45, R12 2.90;
  - information 0.12 [0.01, 0.35], 3.54 [0.41, 11.02], 3.30 [0.73, 6.49], 0.24 [0.11, 0.42], 0.98 [0.72, 1.22], 1.70 [0.90, 2.56]; shares .005 [.000, .013], .135 [.017, .331]; θ max 2.700 / 2.400 / −0.550; shares .001, .083, .221.
- **Ladder:** χ²(84) = 737.457, χ²(18) = 121.958, both *p* < .001; AIC 23,767.020 / 23,852.978; BIC 24,529.585 / 24,555.360; M3 *a* 0.283 (0.055) – 2.606 (1.419); nine / nine unordered; M1 fit R17 1.328 / 1.190, R18 1.009 / 1.071, R12 0.238 / 0.255.
- **Raw mean vs GRM:** all 12 cells of `tbl-raw-mean-vs-grm`; τ~b~ .815–.842.
- **Score agreement:** .975 / .978 / .042 / .202; .985 / .983 / .033 / .150; .996 / .996 / .017 / .075; ladder Pearson .980–.993 and Spearman .983–.996 (recomputed from the off-diagonal cells); 1.000; "all correlations with the GRM .975 or higher".
- **Sensitivity:** .67199 / .67186; .95986 / .96186; 7,844 / 3,669; 3,668; .99997; 0.00171; 0.16246; .00491; .99880; 0.19820.
- **Projection (side note):** .508, .688, .925; 50 replications, 2,000 products, seed 20260713; "each rater equally likely" and "treated as known" match the caption and the method note.

### Never-quote list (Changes item 8, Flag 13)

**None quoted.** A pattern search found only legitimate coincidences: "0.7" inside −0.71, 0.73 and 0.72, and "(PCM)" in the hidden comment block. In particular, none of the following appears:
- the most/least-informative projection values or comparisons;
- true_r2 or the rel~post~ quantiles of the projection;
- the pooled raw-mean row or the raw-mean subgroup correlations, shifts or quintile shares;
- 3-decimal CI bounds or parameters (11.017, 6.489, 3.709);
- the removed sentences ("brackets", "overstates");
- tolerance "0.0001", "0.000545256", AUDIT's "6 unused end categories", REPORT's 0.7–1.3;
- "Ratings (n)", or "M1 (RSM/MFRM)" in the text;
- R09's mean in either form (3.642 / 3.643).

"Confounded" (56, 222) is attributed to @primi2019, not to the notebook.

### Embedded objects

- **Coverage.** 38 of the 43 labels are embedded: 10 in the main text, 28 in the supplement. `02_artifacts.md` still says 37, because it was written before `tbl-overview-rater-response-styles` was embedded.
- **Cross-references.** Every embedded object is cross-referenced in the text, and every `@tbl-`/`@fig-` reference points to an embedded object.
- **Not embedded (5):** `tbl-cleaning-log`, `tbl-overview-ratings-per-action`, `fig-overview-rater-overlap`, `tbl-grm-global-fit` and `tbl-marginal-reliability-models`.
  - The text needs none of the first four. Their values are in embedded tables or in the Methods text.
  - `tbl-marginal-reliability-models` is recommended (m19, m5-1).

### Citations (phd_library.bib only)

- **Resolution.** All 73 unique cited keys resolve in `phd_library.bib`, each defined once. (Round 4 reported 74. No cited key is missing.)
- **Claim-to-source spot checks:**
  - kaufman2008 (*Essentials*) for "five to ten": matches.
  - kaufman2008a (CRJ 20(2), expert vs nonexpert raters) for ".70" and "high alpha can mask low agreement": plausible; both are on FI-17.
  - cseh2019 ("A scattered CAT", *PACA* 13(2)) for domain-specific numbers of raters: plausible, FI-17.
  - hove2024 (ICC guidelines for incomplete designs) for "conventional indices … must be adapted to an incomplete one": matches.
  - wind2018 / wind2019 for linking: match. wind2019a for differential rater functioning: matches.
  - forthmann2025 (planning missing-data designs) for product-level precision: matches, FI-17.
  - eckes2015 for the partial-credit MFRM: FI-17.
  - pellegrino2025 "retained a GRM": FI-17.
- **Still awaiting PDF verification (FI-17, marked):**
  - the framing claims (wef2025, oecd2024, safardilha2019, santos2016, memmert2011, batey2012, barbot2019b);
  - ".70";
  - kaufman2008, kaufman2008a, cseh2019, primi2019, forthmann2025;
  - looney2004, anderlucci2021, heiniger2021;
  - eckes2015 (partial-credit MFRM), pellegrino2025;
  - kempe2018, zahno2023, joode2023;
  - myszkowski2021 and primi2019 (216);
  - wind2018, wind2019, reise1990 (218).
- **Not on FI-17, low risk:** myszkowski2019 for "alpha requires only essential τ-equivalence … differ in their intercepts" (56). This is standard psychometrics. Verify it with the other myszkowski2019 attribution if convenient.

### Interpretation in the Results

The Results are descriptive. The remaining evaluative sentences are methodological caveats and are acceptable:
- "spacing is partly the same fact as discrimination" (170);
- "supported by the LR test and AIC, but not by BIC" (184);
- "the scores differ, not which score is more accurate" (198);
- "These values are observed …" (158, with FI-4).

None of the mechanism sentences from the notebook markdown (Flag 14) is quoted in the Results.

---

## 5. Marker check

**Volume.** There are **60 inline markers: 28 [AUTHOR TO CONFIRM] and 32 [FILL IN].** A 61st, "[AUTHOR TO CONFIRM: author list and affiliations]" in the YAML (line 7), renders on the title page. Round 4 had 62. The drop comes from:
- the two markers removed from the abstract, now tracked in comment lines 32–36;
- the Q3 definition (FI-30), now stated;
- the merged FI-17 marker at line 52.

**Present and appropriate:**
- all Methods gaps (FI-1–4, 6, 9, 15, 21–23);
- the FI-17 verification items (46, 50, 52, 54, 58 ×2, 60, 216, 218);
- novelty (ATC-2, line 60, and in the comment for the abstract);
- exploratory framing (ATC-20);
- the CAT departure (ATC-19);
- the ignorability caveat for the design (ATC-18);
- the cumulative-link rationale (ATC-8);
- "only slightly" (ATC-26);
- S-X² power and the bootstrap caveat (ATC-11);
- every interpretive Discussion paragraph;
- the projection side note (ATC-5);
- the box (ATC-23);
- the Conclusion (ATC-1, 5, 14, 15).

**Claims without a marker, or under a marker that does not fully fit:**

| Location | Claim | Problem |
|---|---|---|
| 9 | "is also used for actions in sport" | Unmarked, and stronger than lines 60 and 88 support (m5-2). |
| 106 | θ standard normal in all models | Unmarked factual inaccuracy for M1 and M2 (m5-1). |
| 239 | Box item 3 without the size condition | Under ATC-14, but less conditional than line 234 (m5-3). |
| 60 | "exists only", "there is no evidence" | Under ATC-2, but worded categorically (m5-5). |

**Before submission**, all of the following must be resolved and removed:
- every inline marker and the YAML affiliation marker;
- the hidden comment block (lines 30–42);
- the `mark-highlight.lua` filter and the `soul`/`xcolor` highlight setup (YAML lines 18–24), if they serve only the markers.

---

## 6. Optional extensions (not counted as issues)

The author has excluded these. They are listed once for completeness, and line 258 already names most of them as beyond scope:
- a severity test (a model without rater effects vs M1);
- an M1–M2 LR test within one package;
- a held-out predictive check of model-based against raw-mean scores;
- projections over parameter draws or with selected or workload-weighted rater sets;
- k for a target reliability;
- diagnostics of the rejected draws;
- a refit with a non-normal latent distribution;
- an ICC for the incomplete design.

---

## 7. What remains before submission

### A. Author FILL INs (Methods and scope)

- **FI-1:** larger project context; ethics approval and consent; confirm "Bachelor's and Master's students", recruitment and starting number of raters; confirm "19 student raters" in the abstract.
- **FI-2:** competitions and matches, action-selection rule, clip length, video source.
- **FI-3:** rating software; verbatim instruction and creativity definition (original and English); anchor wording at 1, 4 and 7; wording of the "action not recognised" option; randomisation, sessions and breaks, and the data-collection period (m20); wording and scales of the other two rated dimensions.
- **FI-4:** allocation of products to raters, and how products came to have 1, 2 or 3+ ratings (lines 92, 158, 248).
- **FI-6:** software versions.
- **FI-9:** why five raters were not usable for the pairwise alpha; optionally, which three raters form the crossed block.
- **FI-15:** preregistration status; data and code availability.
- **FI-21:** rater-pool description (lines 80, 234, 254).
- **FI-22:** rate of "not recognised" ratings by rater (lines 96, 248).
- **FI-23:** rationale for the cut-off of 15 ratings.
- **FI-16:** CRJ requirements: abstract limit (now 249 words), manuscript format (m5-7), figure and table limits, supplement policy and S-numbering, whether boxes are accepted, heading format.
- **FI-17:** PDF verification of all attributions listed in Section 4, including kaufman2008a "mask" and the cseh2019 paraphrase.
- **YAML:** the author list and affiliations.

### B. ATC confirmations

- ATC-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23 and 26, as marked inline.
- The abstract claims tracked only in the comment block: ATC-2 ("little is known"), and ATC-5/14/15 (the two implication sentences).
- Open author options (comment line 41):
  - embed `tbl-marginal-reliability-models` (recommended);
  - promote figures to the main text;
  - keep or drop the box;
  - "stricter rater" wording (ATC-6);
  - the 1.283/1.537 clause in the abstract.

### C. Remaining text issues (this review; all wording, none blocking)

1. m5-1: θ is not standard normal in M1 and M2 (line 106).
2. m5-2: soften the abstract's opening claim about the CAT in sport (line 9).
3. m5-3: add the size condition to box item 3 (line 239).
4. m5-4: remove the circular model definitions (line 108).
5. m5-5: "we found …" instead of categorical absence claims (line 60).
6. m5-6: "refers to the reliability of the mean" (lines 52, 210).
7. m5-7: APA manuscript format, a check that bib `note` fields do not render, and "three" for "3" (line 118).

### D. Remaining display issues (FI-18, notebook only, no new analyses)

- Old model names:
  - `tbl-reliability-overview` rows "M1 (RSM)" / "M2 (PCM)". This table is in the main text, so it is the priority.
  - The captions of `tbl-model-fit`, `tbl-rater-fit-m1` and `tbl-threshold-order` (m-4).
- "Q1 0.596, Q3 0.769" in the `tbl-reliability-overview` note: use "quartiles" (m-3 residual).
- Code-name Quantity labels: `tbl-design-summary`, `tbl-grm-reliability-summary`, `tbl-sensitivity-rater-exclusion`, `tbl-reliability-overview`, and the header "marginal_rxx (mirt)".
- The empty "Overlap" column in `tbl-grm-q3-flagged`.
- Integer display: diagonal "1" in `tbl-theta-correlations`; R08's "3" and the "0" shares in `tbl-overview-rater-response-styles`.
- *p* values in scientific notation.
- Missing thousands separators in notes.
- Legends of `fig-grm-panel-information`, `fig-grm-rel-consistency` and `fig-grm-rel-post-by-theta`.
- Optional: APA leading zeros in tables.
- Housekeeping: re-run the results-embedder so that `02_artifacts.md` shows 38 embedded labels.
