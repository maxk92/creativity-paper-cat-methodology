# Revision instructions for the orchestrator: new rating data

Written 2026-11-04 for a revision of `manuscript/manuscript.qmd` (commit 457c56f). Line numbers below refer to that version.

The data have changed from 7,820 ratings / 3,668 products / 19 raters to **9,046 ratings / 3,669 products / 24 raters**. This triggers FI-19 in `author_todo.md`: every analysis and every number must be regenerated. The main conclusions hold, but several statements are now false or need qualifying (section 3).

## 1. Before starting

1. **Ask the author to confirm the data freeze.** Further ratings are being considered. If more arrive, this revision has to be repeated. The values below belong to this data set only:
   `3669 products x 24 raters | 9046 ratings | md5 68037eafc9939992751c2bf646c48a9e` (`results/data/data_fingerprint.txt`).
2. **Check that the analysis changes are committed.** At the time of writing, the notebooks and results were re-run but not committed.
3. **Do not re-run notebook 00.** It downloads the sheet again and could change the data.

## 2. How to run the revision

| Phase | Action |
|---|---|
| 0–2 | Re-read config and brief. Keep `01_dossier.md`, `06_web_literature.md` and the bibliography. No new literature is needed unless a rewrite below requires it. |
| 3 | results-embedder: regenerate `02_artifacts.md` (labels unchanged: 36 in NB02, 6 in NB01). |
| 4 | results-interpreter: regenerate `03_findings.md` from `00`, `01` and `02_jrt_results`. |
| 5 | outline-architect: minimal update applying section 3. **Stop at human checkpoint 1** and put the decisions in section 7 to the author. |
| 6 | manuscript-writer: revise `manuscript.qmd`, using sections 3–5. Do not rewrite passages listed in section 4 beyond their numbers. |
| 7 | reviewer-critic: new review, also checking section 8. **Stop at human checkpoint 2.** |

Rules for this revision:

- **Numbers come only from the notebooks through the results-interpreter.** Section 5 is a checklist of where each value changes and what to expect. It is not a source. If a value differs, the notebook wins: use it and report the difference in `_status.md`.
- **The paper describes the final data only.** Do not mention an earlier data set, a data update or how estimates changed. Old values here exist only to locate text.
- **No new analyses.** The author's priority of 2026-10-27 still applies: stick to the empirical findings and keep the projection a side note.
- **New or changed interpretive claims go in `author_todo.md`**, following the convention set at the final cleanup. Regenerate its line numbers and quoted sentences, and retire FI-19 if the author confirms the freeze.
- **Do not use these as sources:** `data/archive_pre_rerun_20261103/` and `notebooks/01_data_overview_new_ratings.ipynb` (working comparison, not in `paper.config.yml`).

## 3. Statements that must change (not just numbers)

Suggested wording is a starting point. All of it needs author confirmation.

### C1. The GRM no longer has the lowest value on every criterion (lines 138, 196, 240)

M1 (rating-scale MFRM) now has the lowest BIC: M1 28,235.202 < GRM 28,239.363 (difference 4.161) < M2 28,256.560 < M3 28,288.744. The GRM still has the lowest AIC and SABIC, and it still beats M3 on all three criteria by 49.381 with the same number of parameters (158).

- Line 138 "the GRM had the lowest AIC, BIC and SABIC of the four models": now wrong.
- Line 196 "the GRM, which had the lowest values on all information criteria": now wrong.
- Line 240 "the GRM is the best-fitting of the compared models": qualify. Suggested: "the GRM had the lowest AIC and SABIC of the compared models, whereas BIC favoured M1; it is not a validated reference."
- Line 138 also says GRM and M3 differ by the same amount "on AIC, BIC and SABIC alike". That remains true, but keep it distinct from the difference to the best model, which is M1 for BIC.

Retaining the GRM is now an author decision (section 7, D1).

### C2. The shared category structure is no longer rejected by every criterion (lines 9, 174, 196, 214, 246, 252)

The LR test (χ²(105) = 840.447, *p* < .001) and AIC still reject M1 against M2, but **BIC now prefers M1 over M2** (28,235.202 vs. 28,256.560). Until now, the disagreement between criteria concerned equal discrimination only. It now covers both constraints.

- Line 9 (abstract): "although BIC favoured equal discrimination" must also cover the shared category structure. Suggested: "although BIC favoured the constrained models in both cases".
- Line 174: add the M1 versus M2 BIC comparison; currently only M2 versus M3 is given.
- Line 196 and line 252: "The shared category structure of M1 ... was rejected" becomes "was rejected by the LR test and AIC but not by BIC".
- Line 214: "there the criteria disagreed" currently implies that they agree on M1. Rewrite accordingly. The statement that M2 already allows rater-specific category structures remains true.
- Line 246: extend the BIC sentence, and keep the caveat that M1–M2 crosses software packages, so the comparison is approximate.
- A possible explanation for the author to confirm: BIC's penalty grows with the number of parameters (GRM 158, M2 135, M1 30), so it weighs heavily against rater-specific parameters as the panel grows.

### C3. Reliability no longer rises with every further rating (lines 148, 202)

Line 148 says mean rel~post~ "was higher with each further rating in the table". It no longer is: .915 at nine ratings, **.897 at ten**, .922 at eleven, .948 at twelve, .947 at thirteen. Mean PSD also rises at ten and thirteen.

- Describe the overall rise and name the exceptions. The rows from ten upward rest on 14, 4, 2 and 1 products, and the three-rating row is now small too (68 products).
- Replace "up to .919 for the three products with ten ratings" and "The rows for nine and ten ratings rest on three products each".
- "no mean reached the full-panel value" remains true (highest .948 vs. .969).
- Lines 148 and 238 ("observed", "observational") remain correct and matter more now. Do not read the table as a causal effect of adding ratings.

### C4. The crossed-block alpha no longer lies close to the empirical reliability (line 200)

"The alpha of the fully crossed block (.658, three raters) lay close to the empirical reliability" is no longer supported: the block alpha is .750 [.684, .800] and the empirical reliability .689 [.669, .703]. Delete the sentence, or say that the two refer to different quantities and leave out any claim of closeness. The block now consists of different raters (R07, R11, R23; 261 products). This also retires ATC-13.

### C5. The most extreme estimates no longer come only from raters with about 50 ratings (lines 164, 166, 208, 212, 214)

R16 now has 268 ratings, and its estimate is no longer extreme (*a* = 2.47, *SE* 0.26). **R16 must no longer be described as a rater with few ratings.**

- Highest discrimination: R26 3.19 (46 ratings, *SE* 1.72), then **R06 3.10 (520 ratings, *SE* 0.45)**, R27 3.04 (47, *SE* 0.91), R25 3.01 (138, *SE* 0.47), R24 2.89 (190, *SE* 0.37). So high discrimination is no longer confined to imprecisely estimated raters.
- Lowest discrimination: R18 0.66 (55, *SE* 0.27), then R09 0.93 (400, *SE* 0.15).
- Line 208: name R18 (thresholds, *b*~1~ *SE* 2.86), R26 and R19 (discrimination, *SE* 1.72 and 1.01). The widest information intervals are now R26 [0.11, 6.75], R19 [0.27, 5.31] and R27 [0.50, 4.12]. "The information shares are therefore not a ranking of rater quality" still holds.
- Line 212: "(R18, R19)" names raters behind the score range. Write "for example R18" unless the interpreter can show which raters set the range.
- Line 214: "Part of the spread in discrimination may also be estimation noise for raters with few ratings" can stay, but should not suggest that the spread is mainly noise, given the well-estimated raters above.
- Shares cannot be compared with earlier values as a sign of a more even spread, because a panel of 24 lowers them mechanically.

### C6. Location of maximum information (line 170)

"highest for R01 (2.700) and R06 (2.400), neither of whom used category 7": the order is now R01 2.80, **R16 2.40**, R06 2.30. R16 did use category 7, so the clause must go or apply to R01 and R06 only. Lowest: R13 −0.60. R06 contributes .001 at θ = −2 and .082 at θ = +2. The sentence on R12 needs a new value: R12 .137 at θ = −2, the highest share there, followed by R24 .120.

### C7. One rater now has an internal category gap (lines 90, 104, 160)

R27 used categories 1, 2, 3, 4 and 6, but not 5 or 7.

- Line 90 "No rater had an unused category inside their observed range": now false.
- Line 90 list: eight raters have unused categories. Category 7 was never used by R01, R03, R06, R18, R25 and R26; categories 6 and 7 by R17; categories 5 and 7 by R27.
- Line 104: add that an internal gap makes the M1–M2 nesting approximate. The degrees of freedom are 105 against the formula's 115.
- Line 160: R27's thresholds compare different category boundaries from other raters, as the `tbl-category-usage` caption and the plausibility note in `tbl-grm-rater-parameters` state. Do not compare them directly. R17 and R27 have four thresholds; R01, R03, R06, R18, R25 and R26 have five; all others have six.

### C8. Rater pseudonyms are no longer consecutive (lines 9, 70, 88, 116, 126)

Existing raters keep their IDs. New raters are R23–R28 (section 6). Final data: R01–R19 and R23–R27. Excluded: R20, R21, R22 and R28. Replace "pseudonymised as R01 to R19" and "the three excluded raters are R20 to R22". Line 70's "students who rated as part of their thesis projects" and the abstract's "student raters" must be reconfirmed for the new raters (FI-1).

### C9. The duplicate rule changed (line 86)

"the last entry was kept" becomes "the entry with the latest timestamp was kept". Use 21 pairs, one conflicting, 22 rows removed.

### C10. Examples for the M1 misfit account (lines 176, 214)

Line 176: R09 (infit 1.083, outfit 1.060), R17 (1.323, 1.167) and R18 (1.170, 1.231) now have values above 1; R12 remains lowest (0.260, 0.278).

Line 214 uses R17 as "comparatively low" discrimination (now 1.81, no longer low) and R12 as high (2.72). Better examples are **R18 (0.66) and R09 (0.93): the two lowest GRM discriminations, both above 1 under M1**. The account is better supported than before, but still illustrative.

### C11. Local dependence (line 138)

Of the 10 pairs shown, 8 now deviate negatively and 2 positively (R09–R23 and R10–R11). 28 pairs are flagged (17 negative, 11 positive).

### C12. Exclusion sensitivity (lines 88, 192, 244; ATC-26)

The largest change in a product score is now 0.35026 (previously 0.16246). The other measures remain small (*r* = .99994, mean absolute difference 0.00204, .00273 changing quintile). "changed the product scores only slightly" is defensible only with both figures in view, so the author should re-confirm it.

### C13. Rating design and data-collection facts (lines 78, 82, 148, 238; FI-3, FI-4)

The author's still-open description of how products came to have their number of ratings now has to cover the latest collection. Ratings in the sheet span 2025-10-09 to 2026-11-02. Most of the latest ratings went to products that already had three or more ratings, which is why few products now have exactly three while the number with 4–9 grew. Raise this with the author. Do not write an allocation rule the author has not confirmed.

For FI-3 (session length, breaks): timestamps of R03, R06 and R13 up to November 2025 are partly batched (identical to the millisecond), so timing data for them are unusable. No current claim relies on them; just avoid making one.

## 4. Conclusions that hold (update numbers only)

- The reliability of the obtained scores is far below the full-panel figure (.689 vs. .969).
- High alpha alongside low single-rating agreement (pairwise α .949, Krippendorff's α .391). The Spearman–Brown reading on line 200 stays.
- Product-level reliability is lower with fewer ratings, and limited at one or two ratings (.522 and .699).
- Raters differ in category use, thresholds, discrimination and information. For raters with many ratings, the differences exceed their standard errors (R09 vs. R06, line 206).
- The LR test rejects equal discrimination, while BIC favours it over M3 (M2 28,256.560 vs. M3 28,288.744). AIC favours M3.
- Raw means and GRM scores partly order products differently, and the choice of model shifts rankings.
- All "does not show greater accuracy" statements (lines 188, 220, 231, 252).
- The design recommendations in the box (lines 227–231). "About 50 ratings per rater still left them imprecise" still holds, now for R17, R18, R19, R26 and R27. Check the example tables in each item.

## 5. Number checklist by line

Old values help locate the text. Expected values come from the 2026-11-04 run; display forms may differ in the notebooks.

### Abstract (line 9), rewritten within the word limit (249 words now; FI-16)

| Quantity | Old | Expected |
|---|---|---|
| Raters / ratings / actions | 19 / 7,820 / 3,668 | 24 / 9,046 / 3,669 |
| Empirical vs. full-panel reliability | .672, .960 | .689, .969 |
| Mean reliability at 1 / 2 ratings | .520 / .698 | .522 / .699 |
| Share of lowest category | .579 to .016 | unchanged |
| Kendall's τ~b~ at 1 / 2 ratings | .832 / .815 | .833 / .818 |

Also apply C2 to the BIC clause.

### Method

| Line | Quantity | Old | Expected |
|---|---|---|---|
| 70 | Raters; ratings per rater | 19; 50–1,174 | 24; 46–1,174 |
| 86 | Raw rows | 9,148 | 10,447 |
| 86 | Not recognised | 1,290 | 1,347 |
| 86 | Out-of-range value | 1 (R04) | unchanged |
| 86 | Duplicate pairs; rows removed | 12; 13 | 21; 22 |
| 86 | After cleaning | 7,844 by 22 | 9,077 by 28 |
| 88 | Excluded raters | R20 (13), R21 (9), R22 (2); 24 ratings | also R28 (7); 31 ratings |
| 88 | Products dropped | 1 | unchanged |
| 88 | Largest score change | 0.16246 | 0.35026 |
| 90 | Final data | 7,820 / 3,668 / 19 | 9,046 / 3,669 / 24 |
| 90 | Mean; median; range; harmonic mean | 2.132; 2; 1–10; 1.726 | 2.466; 2; 1–13; 1.806 |
| 90 | Fill | .112 | .103 |
| 90, 108 | Pairs without shared products | 17 of 171 | 30 of 276 |
| 90 | Median overlap | 13 | 19 |
| 100 | GRM iterations | 165 | 436 |
| 108 | Q3 computable pairs | 137 of 171 | 222 of 276 |
| 108 | Share imputed | about 90% | 89.7%, wording stands |
| 112 | Rejected draws | 87 | 43 |
| 116 | Raters not usable for pairwise alpha (FI-9) | R19, R14, R02, R16, R12 | R26, R19, R14, R02, R12, R27 |
| 116 | Computable replications | 639; 361 | 647; 353 |
| 118, 305 | Projection range | 1–10 ratings | unchanged |
| 126 | Refit | 22 raters | 28 raters |

### Results

| Line | Quantity | Old | Expected |
|---|---|---|---|
| 138 | Parameters GRM, M3 | 127 | 158 |
| 138 | Log-likelihood GRM, M3 | −11,733.227, −11,756.510 | −13,471.275, −13,495.966 |
| 138 | GRM lower than M3 by | 46.566 | 49.381 |
| 138 | S-X² *p* | .294–.671 | .328–.665 |
| 138 | Infit | 0.334 (R19)–0.971 (R18) | 0.429 (R02)–0.980 (R18) |
| 138 | Outfit | 0.322 (R19)–0.961 (R18) | 0.402 (R02)–0.971 (R18) |
| 138 | Mean Q3; flagged | −.238; 20 | −.202; 28 |
| 144 | Empirical reliability | .672 [.649, .687] | .689 [.669, .703] |
| 144 | Full panel; grid | .960 [.953, .968]; .960 | .969 [.965, .974]; .969 |
| 144 | Pairwise α | .928 [.891, .943], 14 raters, 1,900 products, 639 | .949 [.926, .958], 18 raters, 1,946 products, 647 |
| 144 | Crossed α | .658 [.526, .756], 139 products | .750 [.684, .800], 261 products |
| 144 | Krippendorff's α | .392 [.362, .417], 19 raters, 2,771 products | .391 [.363, .417], 24 raters, 2,837 products |
| 148 | 1 rating | .520, 897 products | .522, 832 products |
| 148 | 2 ratings | .698, 2,080 products | .699, 2,107 products |
| 148 | 3 ratings | .757, 357 products | .756, 68 products |
| 148 | Mean PSD | 0.686 to 0.285 | 0.684 to 0.230, not monotonic (C3) |
| 148 | Full-panel comparison | .960 | .969 |
| 152 | Median; IQR; quartiles | .698; .173; .596, .769 | .712; .1905; .599, .789 |
| 152 | Range | .057–.929 | .068–.954 |
| 152 | rel~post~ vs. rel~info~; products differing by > .1 | .935; 320 | .947; 229 |
| 156 | Means; SDs | unchanged endpoints | 1.760 (R06)–3.836 (R18); 1.022 (R01)–1.953 (R19) |
| 156 | Floor; ceiling; central | see line | .579 (R06), .016 (R13); R19 .080; R13 .799, R18 .764, R12 .735, R06 .192 |
| 156 | Raters with no 7s | 5 | 8: R01, R03, R06, R17, R18, R25, R26, R27 |
| 156 | Category 1; 2; 7 | 2,029; 2,113; 109 | 2,179; 2,355; 128 |
| 160 | Number of raters | 19 | 24 |
| 160 | *b*~1~ range | −6.56 (R18, *SE* 3.05) to 0.29 (R06, *SE* 0.06) | −6.25 (R18, *SE* 2.86) to 0.25 (R06, *SE* 0.05) |
| 160 | Next lowest *b*~1~ | −3.38 (R13, *SE* 0.49) | −3.36 (R13, *SE* 0.47) |
| 160 | Spacing R02; R13 | −0.71 to 2.03; −3.38 to 4.43 | −0.67 to 1.99; −3.36 to 4.31 |
| 164 | Discrimination | see C5 | R01 1.82 (*SE* 0.13); R02 2.71 (*SE* 0.35); R06 3.10 (*SE* 0.45) |
| 166 | Average information, range | 0.12 (R18) to 3.54 (R19) | 0.135 [0.02, 0.39] (R18) to 2.52 [0.11, 6.75] (R26) |
| 166 | Shares, range | .005 to .135 | .004 [.000, .011] (R18) to .074 [.003, .178] (R26) |
| 166 | Examples | R09 0.24; R01 0.98; R02 1.70 | R09 0.28 [0.13, 0.48]; R01 0.86 [0.66, 1.05]; R02 1.97 [1.11, 2.97] |
| 174 | LR M1–M2 | χ²(84) = 737.457 | χ²(105) = 840.447 |
| 174 | LR M2–M3 | χ²(18) = 121.958 | χ²(23) = 156.593 |
| 174 | AIC M3, M2 | 23,767.020, 23,852.978 | 27,307.931, 27,418.524 |
| 174 | BIC M2, M3 | 24,529.585, 24,555.360 | 28,256.560, 28,288.744 |
| 176 | M3 discrimination | 0.283 (R09) to 2.606 (R16) | 0.305 (R18, *SE* 0.141) to 2.221 (R27, *SE* 0.873) |
| 176 | Unordered steps M2; M3 | 9; 9 | 9; 8 |
| 178 | 1 rating: τ~b~; reversed; mean, max range | .832; .042; 1.283, 1.436 | .833; .041; 1.229, 1.430 |
| 178 | 2 ratings | .815; .067; 1.537, 2.196 | .818; .066; 1.531, 2.170 |
| 178 | 3+ ratings (691 → 730) | .842; .070; 0.619, 1.396 | .849; .071; 0.537, 1.317 |
| 184 | M1: *r*; ρ; quintile; shift | .975; .978; .202; .042 | .977; .979; .206; .042 |
| 184 | M2 | .985; .983; .150; .033 | .985; .984; .155; .032 |
| 184 | M3 | .996; .996; .075; .017 | .996; .996; .081; .016 |
| 184 | Ladder Pearson; Spearman | .980–.993; .983–.996 | .981–.993; .984–.996 |
| 192 | All-raters fit | 22 raters, 7,844 ratings, 3,669 products | 28 raters, 9,077 ratings, 3,670 products |
| 192 | Empirical | .67199 to .67186 | .68896 to .68837 |
| 192 | Model-based | .95986 to .96186 | .96893 to .97142 |
| 192 | Scores: *r*; mean; max; quintile | .99997; 0.00171; 0.16246; .00491 | .99994; 0.00204; 0.35026; .00273 |
| 192 | Common products; raters | 3,668; 19 | 3,669; 24 |
| 192 | Discrimination: *r*; max | .99880; 0.19820 | .99802; 0.19349 |

### Discussion and conclusion

| Line | Quantity | Old | Expected |
|---|---|---|---|
| 196 | τ~b~ range | .815 to .842 | .818 to .849 |
| 200 | Full panel; pairwise α | .960; .928 | .969; .949 |
| 200 | Empirical | .672 [.649, .687] | .689 [.669, .703] |
| 200 | Krippendorff; pairwise α | .392; .928 | .391; .949 |
| 202 | 1; 2 ratings | .520; .698 | .522; .699 |
| 202 | Projection 1; 2; 10 ratings | .508; .688; .925 | .530; .705; .928 |
| 206 | R09; R06 | 0.86 (*SE* 0.15); 2.81 (*SE* 0.42) | 0.93 (*SE* 0.15); 3.10 (*SE* 0.45) |
| 212 | Score range at one rating | 1.283, 1.436 | 1.229, 1.430 |
| 216 | τ~b~; reversed | .832, .815; .042, .067 | .833, .818; .041, .066 |
| 218 | Lowest correlation with GRM | .975 | .977 |
| 218 | M1 quintile; shift | .202; .042 | .206; .042 |
| 218 | M3 quintile; shift | .075; .017 | .081; .016 |
| 244 | Largest score change | 0.16246 | 0.35026 |

Lines 202 and `author_todo.md` line 71 quote the projection. Line 305 (supplement note) is unchanged apart from any numbers the notebook shows.

## 6. Rater IDs

IDs are now permanent (`README.md`, `AUDIT.md`). Existing raters keep the IDs used in the manuscript; this was checked against all 7,844 earlier cleaned ratings.

| ID | Ratings | Status |
|---|---|---|
| R23 | 589 | new |
| R24 | 190 | new |
| R25 | 138 | new |
| R26 | 46 | new |
| R27 | 47 | new |
| R28 | 7 | new, excluded (< 15) |
| R16 | 268 (was 52) | existing, the only rater with added ratings |

- The numbers no longer follow workload order, so do not imply that they do.
- A summary of 2026-11-03 used a different temporary numbering for some raters. Ignore it; use the notebooks.

## 7. Decisions for the author at checkpoint 1

- **D1. Keep the GRM as the scoring model?** Recommended: yes. It has the lowest AIC and SABIC, beats M3 on every criterion, and the cumulative link suits the scale. Say openly that BIC favours M1 by 4.161, and rely on the existing comparison with M1 (*r* = .977, .206 changing quintile). This gap is small and also moved slightly between runs that differed by one rating, so it should not carry an argument either way.
- **D2. Wording for C2.** Is "rejected by the LR test and AIC but not by BIC" acceptable in the abstract and conclusion?
- **D3. Delete or rephrase the crossed-block sentence (C4)?** Recommended: delete.
- **D4. "Only slightly" for the exclusion sensitivity (C12)?** Keep or rephrase, given the largest change of 0.35026.
- **D5. New raters.** Are R23–R28 from the same student pool, and how were their actions assigned (C8, C13)?
- **D6. Preliminary draft.** Update `preliminary_draft/manuscript.qmd` as well (see below)?

## 8. Checks after writing

Search `manuscript.qmd` for these stale strings. Each hit should be explained or removed:

`7,820`, `3,668`, `9,148`, `1,290`, `7,844`, `.672`, `.960`, `.928`, `.658`, `.392`, `.520`, `.698`, `.815`, `.842`, `0.16246`, `R20 to R22`, `R01 to R19`, `last entry`, `No rater had`, `lowest AIC, BIC`, `all information criteria`, `each further rating`, `lay close`.

Also check:

- R16 is never described as a rater with few ratings.
- R23–R27 appear wherever the text lists raters.
- No sentence refers to an earlier data set.
- The manuscript renders with 38 embeds, all resolving, and no unresolved citations.
- Claims in `author_todo.md` match the new text.

## 9. Other files with old values

These are outside `manuscript.qmd`. Do not change them unless the author agrees (D6).

**`submission/3_PACA.md` line 18** quotes 19 raters, 7,820 ratings and 3,668 products.

**`preliminary_draft/manuscript.qmd`** is the author's own shorter draft of 2026-10-30. Its framing ("more data are needed before the model-based analyses") may also need rethinking.

| Line | Old | Expected |
|---|---|---|
| 8 | 7,820 ratings of 3,668 actions by 19 raters | 9,046 / 3,669 / 24 |
| 69 | 19 raters, R01 to R19, 50–1,174; excluded R20 to R22 | 24 raters, R01–R19 and R23–R27, 46–1,174; excluded R20–R22 and R28 |
| 85 | 9,148; 1,290; twelve pairs; last entry; 13 rows; 7,844 by 22 | 10,447; 1,347; 21 pairs; latest entry; 22 rows; 9,077 by 28 |
| 87 | R20, R21, R22; 24 ratings | add R28 (7); 31 ratings |
| 89 | 7,820 / 3,668 / 19 | 9,046 / 3,669 / 24 |
| 115 | Median 383; four raters (R16 to R19) with 50–55 | Median 318.5; six raters (R15, R17, R18, R19, R26, R27) with 46–73 |
| 115 | Mean 2.132; harmonic 1.726; max 10 | 2.466; 1.806; 13 |
| 115 | 897 (.245); 2,080 (.567); 691 (.188) | 832 (.227); 2,107 (.574); 730 (.199) |
| 115 | Fill .112; 17 of 171; overlap 13 | .103; 30 of 276; 19 |
| 121 | "A quarter of the actions" | just under a quarter; review the TO DO on collecting more ratings |
| 125 | 2,029; 2,113; 109; five raters; no internal gap | 2,179; 2,355; 128; eight raters; R27 has an internal gap |
| 131 | α .392 [.362, .417], 19 raters, 2,771 products | .391 [.363, .417], 24 raters, 2,837 products |
| 131 | Crossed .658 [.526, .756], 139 products | .750 [.684, .800], 261 products |
