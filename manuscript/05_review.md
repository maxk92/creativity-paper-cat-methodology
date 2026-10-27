# 05_review.md: Peer review, SECOND ROUND (reviewer-critic, Phase 7)

Manuscript reviewed: `manuscript/manuscript.qmd` (revised draft, after commit 91c2e6d; 352 lines).
Checked against:
- `03_findings.md` (authoritative numbers, re-run after 91c2e6d);
- `02_artifacts.md` (42 labels);
- the first-round review (previous version of this file);
- the R source, read only to see how two statistics are computed: `R/07_reliability_projection.R` (rater sets of the projection) and `R/03_grm_information.R` (raw mean vs GRM, lines 124–164).

Venue: Creativity Research Journal (profile imrad-apa). Line numbers refer to `manuscript.qmd`.

Not criticised here, per the author's constraints:
- the sparse design is not foregrounded;
- the Methods FILL INs on allocation, raters, stimuli, ethics, software versions and data availability;
- the author-supplied cause of the "not recognised" ratings.

APA leading-zero formatting and *p* < .001 are treated as intended and are not counted as mismatches.

---

## 1. Summary and recommendation

The revision is substantial and mostly well done.

**What the revision fixed.**
- **Raw-mean comparison.** The tie artefact (C1) is gone. The raw-mean comparison now uses Kendall's τb, discordant pairs and a tie-resolved quintile change. The plain share is no longer quoted.
- **Reliability by number of ratings.** A model-based projection (C3) replaces the observational by-n table as the basis for planning.
- **Rater differences.** The three kinds of rater difference (severity, category structure, discrimination) are now kept apart in the Introduction and the Discussion. The missing severity test is disclosed.
- **Claims.** The normative and causal claims have been softened: "the scores differ, not which is more accurate", "In these data".
- **Limitations.** They are now unusually complete.
- **Numbers.** Every number I checked matches `03_findings.md`, and no value that is no longer printed is quoted.

**What the revision introduced.** The new projection, which is now the paper's main applied deliverable, brings its own problems:
- Its "most informative" and "least informative" rater sets are chosen by point estimates of average information. At small k, those sets consist of the most poorly determined raters: R19, R16 and R18, each with about 50 ratings.
- The abstract's headline ".754 for one rating from the most informative raters" is therefore essentially the point estimate for R19 (*a* = 3.71, *SE* 2.22; information interval [0.410, 11.017]). It is treated as known.
- The Discussion itself says the information shares "are not a ranking of rater quality" (line 234).

**Other new problems.**
- The pooled raw-mean statistics that now lead the abstract and the Discussion (τb .796, .083, .237) mix rater effects with the GRM's differential shrinkage across products with different numbers of ratings. Every pooled value is worse than every within-n value.
- The manuscript cites "the analysis notebook" as an authority twice.
- It tells readers that the projection "will be refreshed when more ratings have been collected".

**Recommendation: major revision.** This is closer to minor than in round 1. Two things separate the draft from a minor revision:
1. The projection issue (N-C1). It can be fixed with the existing fit by restricting or weighting the rater sets, or by adding parameter uncertainty.
2. The deferred Methods FILL INs. These are the author's task, but the paper cannot be submitted without them.

Once these and the five new major issues are addressed, I would expect a minor revision.

**Counts.**
- First-round points (37): **13 resolved, 13 partially resolved, 1 not resolved, 10 deferred to author or analyst.**
- New issues: **1 critical, 5 major, 12 minor.**

---

## 2. Response check (first-round points)

Status categories:
- **R** = resolved;
- **P** = partially resolved;
- **N** = not resolved;
- **D** = deferred to author or analyst (legitimately a FILL IN).

### Critical

| # | Status | Justification | Location |
|---|---|---|---|
| C1 Tie artefact in raw-mean quintiles | **R** | Tie-aware statistics are defined in the Methods. The plain share and the percentile shift are explicitly "not used in the text". The aim-3 evidence is rebuilt around the 1-rating facet. The pooled-row problem is still there and is now raised as N-M1. | 140, 200–204, 238, 242; abstract |
| C2 Methods not reproducible | **D** | All gaps carry FI markers (FI-1–4, 6, 15, 21, 22). FI-4 now asks exactly the right questions: how products came to have 1, 2 or 3+ ratings, and whether the 4+ products differ. This is the author's task by constraint. | 68–84, 146 |
| C3 By-n table used as a planning tool | **P** | A projection was added, and planning now rests on it (226–228, 246). The observational table is demoted, and "mainly" and "We have shown" are gone. However, the projection has new problems: noisy rater selection, uniform random draws, parameters treated as known, and no target-k values. See N-C1 and N-M2. | 126, 162–166, 226–228, 246 |

### Major

| # | Status | Justification | Location |
|---|---|---|---|
| M1 GRM as reference standard | **P** | The text now says "show that the scores differ, not which score is more accurate" (212, 242, 250) and calls the GRM "not a validated reference" (266). The held-out check (FI-26) is deferred. Callout item 4 and the Conclusion still recommend modelling over averaging without a criterion. This is marked, but it remains the paper's weakest normative link. | 212, 242, 250, 258, 266, 278 |
| M2 Severity vs category structure vs discrimination | **P** | Three kinds of rater difference are separated (50, 238–240). "Even the weaker constraints" is removed, and the missing severity test is disclosed (110, 238). The M0 vs M1 test (FI-24) is deferred. Residual problem: the 1-rating spread is still presented as the "clearest case" of *severity* (238), although it also reflects discrimination and shrinkage (see N-M5). | 50, 110, 238–240 |
| M3 Cross-package M1–M2 LR test | **D** | Disclosed as approximate, with nesting "assumed rather than shown" (110, 272). The sirt handling of unused categories and a same-package test are FI-25. | 102, 110, 272 |
| M4 b1 extremes read as severity | **P** | R18's b1 is out of the abstract. R18 is flagged as poorly determined (182), and the conflation of spacing with discrimination is stated (100, 182, 232). A comparable severity metric (FI-29) is deferred. b1 is still the only severity summary, and line 100 still says "higher thresholds indicate a stricter rater" without qualification. | 100, 182, 232 |
| M5 Truncated parameter draws | **D** | Disclosed in the Methods, Results, Discussion and Limitations as "conditional on valid parameter sets and approximate" (124, 134, 234, 268). The diagnostics and redraw are FI-28. | 124, 134, 234, 268 |
| M6 Dependence on the normal prior | **D** | The prior dependence of rel~post~ is stated (128, 228), and a latent-distribution limitation is added (268). The sensitivity refit is FI-27. | 128, 228, 268 |
| M7 "Not recognised" missingness | **D** | MAR caveat added to the Limitations (264). Rates by rater are FI-22. The cause is author-supplied (constraint). | 88, 264 |
| M8 Student raters and CAT "appropriate judges" | **D** | Scope caveats added to the abstract ("for this kind of rater pool"), the implications (246) and the Limitations (270). The pool description is FI-21. | 9, 72, 246, 270 |
| M9 "15 ratings is a lower limit" | **R** | Callout item 3 and line 252 now say that about 50 ratings still left parameters imprecise. The 15-rating cut-off is called a "technical estimation criterion only", and FI-23 asks for its source. | 90, 252, 257 |
| M10 Confirmatory and normative wording | **R** | RQ3 is reworded descriptively. SQ1 and SQ2 are folded into the Methods. The Conclusion opens with "In these data". | 56–60, 278 |
| M11 Results as a number dump, with interpretation | **P** | The interpretive sentences have moved to the Discussion, the information-criterion deltas are reduced to one contrast, and the 6-decimal shares are gone. The Results are still long and list-like (162, 178, 204, 208). There are still 10 main-text objects, including the 19-row `tbl-grm-rater-parameters`, which is now compact; the forest plot (FI-29) is deferred. | 150–216 |
| M12 Render blockers and display problems | **P** | The pipe blocker is fixed (`02_artifacts.md`). The snake_case headers, "theta", tol 0.000, the "1000 replications" wording and the stale captions of `tbl-raw-mean-vs-grm` and `tbl-grm-reliability-projection` are all FI-18. These are analyst tasks, but they would still cause a desk return. | comment block line 32 |

### Minor

| # | Status | Justification | Location |
|---|---|---|---|
| m1 APA leading zeros | **R** | Applied consistently in the text. The tables are optional under FI-18. | throughout |
| m2 Exact p-values | **R** | *p* < .001. | 196 |
| m3 Over-precise values | **P** | The 6-decimal shares are gone. The 5-decimal sensitivity values remain (216; FI-18 optional reprint). | 216 |
| m4 "Did not change the scores" | **P** | Still reads "did not change the scores", although the same sentence reports a maximum change of 0.16246. ATC-26 offers the fix, so just apply it. | 90 |
| m5 S-X² called "conservative" | **R** | Now "has little power" (ATC-11). | 114 |
| m6 Q3 | **P** | The negative bias and the lack of a reference distribution are stated. What makes 137 of 171 pairs "computable" is still undefined. | 116, 156 |
| m7 Pairwise α CI | **R** | "approximate and may also be biased". | 130 |
| m8 "Range CAT studies usually report" | **R** | Sentence removed. | — |
| m9 "First football-specific evidence" | **R** | Removed. Novelty is now routed through ATC-2. | 226 |
| m10 Cause of "not recognised" ratings | **D** | Author-supplied by constraint. FI-22 covers the rates. | 88 |
| m11 FI-17 verification list | **R** | Markers added for kaufman2008a, the ".70" claim, and the kempe/zahno/dejoode characterisation. The verification itself is pending. | 44, 46, 52 |
| m12 "Labels for automated rating" | **R** | Removed. | — |
| m13 R01 information maximum | **P** | The phrasing is fixed. There is still no note that R01's maximum at θ = 2.7 comes from a rater who never used category 7. | 192 |
| m14 Pooling in the "all" row | **P** | The 2.252 is no longer quoted, and FI-20 asks about grouping. However, the pooled τb, discordant share and tie-resolved quintile change now lead the abstract and the Discussion (N-M1). FI-20 can be answered from `R/03_grm_information.R`: subgroup rows rank within the subgroup (lines 151–153), and the "all" row pools equal raw means across n (lines 157–159). | 9, 200, 242 |
| m15 Point the mechanism sentence to the 1-rating facet | **R** | Done. | 238 |
| m16 "Products" vs "actions" | **P** | The equivalence is defined (58, 76, 246). The Results still say "products" and the abstract and Discussion say "actions". This is acceptable if it is stated once, but line 246 defines it a second time. | 58, 76, 246 |
| m17 "Information per rating" | **R** | Renamed "average information" and defined (134). The caption fix is FI-18. | 134 |
| m18 Supplement S-numbering | **D** | Render configuration (comment block line 35). | — |
| m19 `tbl-marginal-reliability-models` unused | **N** | Still neither embedded nor cited. It would directly show the cost of constrained scoring in empirical reliability (M1 .626 → GRM .672), which is relevant to RQ3. | — |
| m20 Drift and collection timespan | **D** | FI-3 now asks for the timespan. | 80 |
| m21 Abstract density | **P** | Better: the plain share is gone and the b1 extremes are gone. It is still about 250 words and dense with numbers. Check the CRJ limit (FI-16). | 9 |
| m22 Figure captions and legends | **D** | FI-18. | — |

**Tally:**

| Status | Critical | Major | Minor | Total |
|---|---|---|---|---|
| Resolved | 1 | 2 | 10 | **13** |
| Partially resolved | 1 | 5 | 7 | **13** |
| Not resolved | 0 | 0 | 1 | **1** |
| Deferred | 1 | 5 | 4 | **10** |

---

## 3. New issues introduced by the revision

### Critical

#### N-C1. The projection's "most" and "least informative" rater sets are chosen by noisy point estimates, so the headline values rest on the least well-determined raters (abstract; lines 126, 162, 166, 226, 234, 246, 255)

**Problem.**
- `R/07_reliability_projection.R` (lines 39, 48) orders raters by the point estimate `info_weighted_area` and takes the head or the tail.
- By `tbl-grm-information-summary` (F2.3), the top of that order is:
  - R19 (3.539, 50 ratings);
  - R16 (3.300, 52 ratings);
  - then R12, R14 and R15 (73 ratings).
- The bottom is R18 (0.123, 55 ratings), R09 and R17 (52 ratings).
- So "one rating from the most informative raters gave .754" is the point estimate for R19 alone. R19's discrimination *SE* is 2.22 and its information interval is [0.410, 11.017]. "One rating from the least informative raters gave .108" is R18 alone, whose b1 *SE* is 3.05.
- The projection treats these parameters as known (line 126), so the most-informative curve carries a selection effect: it selects on noise, a winner's-curse effect.

**Consequences.**
- The comparisons in lines 162 and 226 inherit this ("one rating from the most informative raters (.754) > two from random raters (.688)"; "ten from the least informative (.884) stayed below three from the most informative (.892)"). So do the abstract and the Discussion claim "who rates therefore matters as much as how many" (ATC-24).
- The paper contradicts itself. Line 234 says the information shares "are not a ranking of rater quality", but the projection uses exactly that ranking to define its "most informative raters".
- Line 166 says the sets "are not listed in the output". They can be read directly off `tbl-grm-information-summary`, so a reviewer will reconstruct them at once. "The output" is also pipeline language.
- The fixed-set schemes also imply that the same one to ten raters rate every action. That is not a feasible design for thousands of clips. They are bounds, as the notebook says ("brackets"), not design options, but line 226 and callout item 1 read them as options.

**Why it matters.** This is now the paper's main applied deliverable (RQ1, the abstract, implication 1, callout item 1). A psychometric reviewer will see that the headline contrast is driven by two raters with about 50 ratings.

**Fix (no new data needed).**
1. Re-run the fixed-set schemes restricted to raters with stable parameters, for example the R01–R09 group the paper already uses for description. Alternatively, rank raters by a lower interval bound rather than the point estimate.
2. Better still, propagate parameter uncertainty by running the projection over the existing 200 parameter draws (FI-28). The bands then become meaningful.
3. List the raters in each set in a table note.
4. Remove ".754" from the abstract, or replace it with the restricted-set value.
5. Reword line 226 and callout item 1 so that the fixed sets are described as bounds, not as designs.

### Major

#### N-M1. The pooled raw-mean statistics mix rater effects with shrinkage across different numbers of ratings (abstract; lines 200, 242)

**Problem.**
- The abstract ("Kendall's τb = .796") and the Discussion ("τb .796, .083 … ordered the other way round, and at least .237 … a different quintile", line 242) quote the "all" row.
- In `R/03_grm_information.R`, the "all" row ranks every product together. The 1 / 2 / 3+ rows rank within the subgroup.
- In the pooled row, a product with one rating of 2 is compared with a product with two ratings averaging 1.5. The GRM shrinks these by different amounts because their posterior precision differs. Some of the reversals therefore come from the number of ratings, not from rater differences.
- The pattern in `tbl-raw-mean-vs-grm` is consistent with this: every pooled value is worse than every subgroup value.
  - τb: .796 pooled vs .832 / .815 / .842 by subgroup.
  - Discordant pairs: .083 vs .042 / .067 / .070.
  - Tie-resolved quintile change: .237 vs .104 / .220 / .220.
  - 03_findings flag 13 notes this as well.
- Line 242 nonetheless introduces these values with "These differences [between raters] have consequences for the scores".

**Fix.**
- Headline the within-n values, for example: τb .832 and .042 discordant pairs for one rating, and τb .815 and .067 for two ratings. These isolate rater effects.
- Alternatively, say explicitly that the pooled values also reflect how the GRM weights products by their number of ratings.
- Answer FI-20 from the source (see m14 above).

#### N-M2. The projection does not yet give the concrete planning answer that a sport-science reader needs (lines 126, 162, 226, 246, 255)

**Problem.**
- The "random" scheme draws raters uniformly (`sample.int(J, k)`). As a result, the five raters with about 50–73 ratings, who together gave fewer than 300 of 7820 ratings, make up 5 of 19 draws. Among them are R19 and R16, with the highest point-estimate information.
- The random curve therefore does not represent the pool as it was actually used. It also inherits the selection noise of N-C1.
- No number of ratings needed for a target reliability (for example .70, .80 or .90) is reported. 03_findings forbids deriving one, so it would have to be printed by the notebook.
- Implication 1 ("can be planned for a target score reliability") thus remains a promise rather than a result.
- The CRJ criterion "practical relevance for sport science" is where this paper will be judged.

**Fix.**
- Add a workload-weighted random scheme.
- Have the notebook print, for each scheme, the smallest k that reaches .70, .80 and .90, with draw-based intervals.
- Quote these values in the Results and in implication 1.

#### N-M3. The manuscript cites "the analysis notebook" as an authority (lines 228, 238)

**Problem.**
- Line 228 says: "In the analysis notebook, this observed relation is described as confounded …".
- Line 238 says: "In the words of the analysis notebook, products with the same raw mean get different GRM scores …".
- A journal article cannot rest a claim on its own analysis notebook. Readers cannot see that notebook, and it is not a citable source. These sentences are pipeline residue.
- The confounding claim at line 228 is also the stated reason for preferring the projection over the observed table. It is asserted, not shown.

**Fix.**
- Turn both into the authors' own claims, keeping the ATC markers.
- Support line 228 with data. For example, show that the rater composition differs by number of ratings: the share of ratings from R01–R09 among products with 1, 2 and 3+ ratings, printed by the notebook.
- Otherwise, write: "products were not assigned a number of ratings at random, so the observed relation may be confounded with which raters rated them".

#### N-M4. The paper tells readers that its data will change (line 246; comment block FI-19)

**Problem.** Line 246 says the projection "will be refreshed when more ratings have been collected". An editor will read this as "the data are not final", and reviewers will ask why the paper is being submitted now. Every design-dependent number would change.

**Fix.** Do one of the following:
- submit after the data update and delete the sentence;
- if the current data are final for this paper, delete the sentence and mention the future data only as future work.

#### N-M5. The 1.436 single-rating spread is presented as evidence of severity, and as a maximum over point estimates without uncertainty (abstract; lines 204, 238)

**Problem.**
- Line 238 opens with "The first is severity … In these data, the clearest case is a single rating".
- With one rating, the EAP depends on the rater's thresholds *and* discrimination, and on shrinkage toward the N(0,1) prior. A low-*a* rater's ratings are all pulled toward 0.
- ATC-21 in the same paragraph says "severity or discrimination". So the spread is not specifically severity evidence, and the M2 confusion returns in a milder form.
- 1.436 is also a maximum over raters. It is likely driven by the extreme and poorly determined raters (R18: *a* 0.63, b1 *SE* 3.05; R19), and it is reported in the abstract without any interval.

**Fix.**
- Describe the spread as "differences between raters as modelled (severity and discrimination)", which line 238 nearly does already.
- Move it out of the "severity" sentence.
- Report the mean range (1.283) alongside the maximum, as the Results already do.
- Optionally, have the notebook print the range without the five raters who gave fewer than 75 ratings.

### Minor

- **N-m1. Selective listing of the central rate (line 178).** "The central rate … was high for R13 (.799) and R12 (.735)" leaves out R18 (.764), which lies between them (F0.8). Name all three, or say "highest for R13".
- **N-m2. APA thousands separators.** APA 7 (§6.38) uses commas in numbers of 1,000 or more: 7,820; 3,668; 9,148; 1,290; 1,174; 2,029; 2,113; 2,080; −11,733.227; 23,767.020; and so on. This is formatting, not rounding. Apply it consistently, ideally in the notebook `tidy()` (FI-18).
- **N-m3. The τ-equivalence sentence in the Introduction (line 50).** "Mean scores and coefficient alpha additionally assume (essentially) τ-equivalent raters" follows the MFRM sentence and reads as an assumption *beyond* the MFRM's.
  - Essential τ-equivalence allows rater-specific intercepts, i.e., severity.
  - What makes raw means confounded in incomplete designs is that they ignore those intercepts.
  - Reword to separate the two points. The paragraph is also about 350 words long; split it.
- **N-m4. Unverified citation for a methodological claim (line 46).** "A fitted measurement model can project that precision for other numbers of ratings [@primi2019; @forthmann2023]" has no FI-17 marker. Check that both sources support projection; forthmann2023 is a simulation of planned-missing designs.
- **N-m5. Novelty claims in the abstract (line 9).** "It is unknown how many ratings …" and "increasingly applied to actions in sport" are stronger than the hedge in the Introduction ("to our knowledge", ATC-2). The abstract's marker block does not include ATC-2.
- **N-m6. Unmarked judgement at the opening of the Discussion (line 220).** "Ordered a non-trivial share of products differently" has no marker. Quote τb instead, or mark it.
- **N-m7. A new number first appears in the Discussion (line 226).** ".892" (most informative raters, k = 3) is not in the Results. Report it in the Results (line 162) or drop it.
- **N-m8. The "at least 400 ratings" grouping is post hoc (abstract; lines 182, 186).** The cut sits exactly at R09 (400) and excludes R10 (383), R12 and R14. The abstract's "0.86 to 2.81" depends on it. Give a rationale (for example, a precision criterion based on the SE), or describe the range by SE.
- **N-m9. "Not listed in the output" (line 166).** This is pipeline phrasing, and the sets are determinable anyway (see N-C1). List them.
- **N-m10. Selective by-n values (line 172).** The values for n = 1, 2 and 4 are quoted and n = 3 (.757, 357 products) is skipped. Quote 1, 2 and 3, or 1, 2 and 3+, to match the raw-mean grouping.
- **N-m11. Two different statistics side by side (line 242).** ".237 … a different quintile" is followed in the next sentence by ".202 … between the MFRM/RSM and the GRM". The text adds that they are "not ranked against each other", but placing them together still invites the comparison. The notebook does not state that the tie-resolved share is comparable with `tbl-score-agreement`. Put them in separate paragraphs.
- **N-m12. The callout box duplicates the implications (lines 246–259).** The five callout items repeat implications 1–4 almost word for word, plus the reporting point from line 228, and every item carries a marker. Keep either the box or the paragraphs. CRJ does not normally use boxes (FI-16).

---

## 4. Number and citation check against 03_findings.md

### Numeric mismatches

**None found.** I checked every number in the abstract, Methods, Results, Discussion and Conclusion against `03_findings.md`, allowing for the intended APA leading-zero formatting:
- **Cleaning and design:** 9148 / 1290 / 0.0 R04 / 12 pairs, 13 rows / 7844 / 22; 7820 / 3668 / 19; 2.132, 2, 1–10, 1.726, .112, 17 of 171, 13; category counts 2029 / 2113 / 109.
- **Fit:** the information criteria; 46.566; the LR statistics and df; S-X² *p* .294–.671; infit and outfit ranges; Q3 −.238, 137, 20, 10 / 9 / 1.
- **Projection:** every quoted cell (.508, .688, .857, .925; .754, .947; .108, .884; .920, .701; .892; the "within .003" statement; .947 < .960); 50 replications, 2000 products, seed 20260713.
- **Reliability:** .672 [.649, .687]; .960 [.953, .968]; the grid value .960; the three conventional indices with CIs, rater counts and product counts; 361 / 1000; the by-n values .520 / .698 / .810 / .919 and PSD 0.686 / 0.285; the rel~post~ distribution; *r* = .935; 320.
- **Raters:** response styles; every GRM parameter quoted at 2 decimals; information values and intervals; θ at maximum; shares at θ = ±2.
- **Models:** M3 discriminations; nine / nine unordered; M1 fit.
- **Raw mean vs GRM:** every cell of `tbl-raw-mean-vs-grm` quoted.
- **Score agreement:** `tbl-score-agreement`; ladder correlations .980–.993 / .983–.996; 1.000.
- **Sensitivity:** all values.
- **Discussion:** R17 1.45, R12 2.90.

### Values no longer printed

**None quoted.** The following are all correctly absent:
- the 3-decimal GRM parameters (3.709, −6.565);
- the plain share 0.350 and its old comparison with 0.202;
- the pooled maximum range 2.252;
- AUDIT's "6 unused end categories";
- REPORT's 0.7–1.3;
- any target-k value derived from the projection.

### Correct numbers, questionable use

- **.754 and .108 (abstract, 162, 226).** These are single-rater point estimates (R19, R18) treated as known (N-C1).
- **τb .796, .083 and .237 (abstract, 242).** These are pooled across n (N-M1).
- **1.436 (abstract, 238).** This is a maximum over point estimates and is framed as severity (N-M5).
- **0.86–2.81 (abstract).** This depends on the post hoc ≥400 grouping (N-m8).

### Citations

- All 74 distinct citation keys resolve. Each is defined in exactly one of `phd_library.bib` or `web_references.bib`, with no duplicates across the two files.
- **Still awaiting PDF verification (FI-17, marked):**
  - worldeconomicforum2025;
  - the framing claims for safardilha2019, memmert2011, batey2012 and barbot2019b;
  - the ".70" claim (baer2004, kaufman2008, hennessey2011);
  - kaufman2008a (five to ten raters);
  - the kempe2018 / zahno2023 / dejoode2023 characterisation.
- **Unmarked, should be added to FI-17:**
  - primi2019 and forthmann2023 as sources for model-based projection (line 46; N-m4);
  - pellegrino2025 "retained a GRM" (lines 50, 240).

### Interpretation in the Results

The Results are now essentially descriptive and contain no ATC markers. The remaining evaluative sentences are methodological caveats rather than substantive interpretation, and I consider them acceptable:
- line 156: "The informative value of these statistics is limited";
- line 166: the projection qualifications;
- line 172: "These values are observational";
- line 212: "they show that the scores differ, not which score is more accurate".

---

## 5. Marker check

**Volume.** There are **76 visible markers: 46 [AUTHOR TO CONFIRM] and 30 [FILL IN]**, up from about 40. In addition, the hidden comment block lists FI-16, 18 and 19 and the optional analyst actions FI-11, 12 and 24–29.
- The growth is mostly legitimate: Methods FILL INs are now itemised, and claims carry finer-grained ATCs.
- Still, the Discussion has a marker after nearly every paragraph, and the callout box has one on every line.
- Resolving them is a substantial task. Several ATCs repeat the same point (ATC-6 three times in lines 232; ATC-15 and ATC-22 on lines 242, 250 and 258) and can be resolved together.

**Present and appropriate.**
- All Methods gaps.
- The FI-17 verification items.
- The departure from the CAT rules (ATC-19).
- The cumulative-link rationale (ATC-8).
- The literature-search caveat (ATC-2).
- Every interpretive Discussion paragraph.
- Both notebook-derived mechanism sentences (ATC-21, ATC-25). Their wording still needs fixing (N-M3).
- The "did not change" alternative (ATC-26).

**Over-claims without a marker, or under a marker that does not fit the claim.**

| Location | Claim | Problem |
|---|---|---|
| 9 (abstract) | "it is unknown how many ratings …"; "increasingly applied" | Novelty claim not covered by ATC-2 (N-m5) |
| 9, 226, 255 | ".754" / "who rates matters as much as how many" | Marked (ATC-24), but the evidence is a selection artefact (N-C1). A marker does not cure this. |
| 46 | Projection is supported by primi2019 and forthmann2023 | Citation not verified, no marker (N-m4) |
| 100 | "higher thresholds indicate a stricter rater" | Unqualified severity reading of b_k (M4 residual). The ATC-6 at the paragraph end covers the spacing point only. |
| 220 | "non-trivial share" | No marker (N-m6) |
| 242 | "These differences have consequences …" followed by pooled values | Marked (ATC-22), but the attribution to rater differences is not supported for the pooled values (N-M1) |
| 248 | A calibration set "would … stabilise the discriminations of raters with few ratings" | Only if those raters rate the set and the set is large. Marked ATC-14, but needs that qualification. |

**Missing [FILL IN] items to consider.**
- The identities of the raters in the projection's rater sets (N-C1).
- k-for-target values (N-M2).
- The rater composition by number of ratings, to support the confounding claim (N-M3).
- The definition of a "computable" Q3 pair (m6).

---

## 6. Top 5 remaining points

1. **Fix the projection's rater sets (N-C1, N-M2).** Restrict "most" and "least informative" to raters with stable parameters, or propagate the 200 parameter draws. Add a workload-weighted random scheme, list the raters in each set, and have the notebook print the k needed for .70, .80 and .90. Then rewrite the abstract's ".754" sentence, line 226 ("who rates matters as much as how many") and callout item 1.
2. **Headline the within-n raw-mean statistics (N-M1, N-M5).** Replace the pooled τb .796, .083 and .237 in the abstract and line 242 with the 1- and 2-rating values. Describe the 1.436 spread as reflecting severity and discrimination, report it alongside the mean range, and do not present it as the "clearest case" of severity.
3. **Complete the Methods FILL INs (C2, M7, M8; author).** Above all, cover allocation (FI-4) and the rater pool (FI-21). These also decide whether the projection's "this rater pool" framing and the MAR assumption hold.
4. **Remove the pipeline residue and settle the data status (N-M3, N-M4, N-m9).** Rewrite the two "analysis notebook" sentences as the authors' own claims, supported by data where possible. Delete "will be refreshed when more ratings have been collected", and either submit after the data update or treat the current data as final.
5. **Close the analyst actions that a psychometric reviewer will ask for (M1, M2, M3, M5, M12).** In priority order:
   - the severity test M0 vs M1 (FI-24);
   - the held-out predictive check (FI-26), which would turn "the scores differ" into "the scores are better or worse";
   - the same-package M1–M2 LR test (FI-25);
   - the draw diagnostics (FI-28);
   - the FI-18 display fixes, which would otherwise cause a desk return.
