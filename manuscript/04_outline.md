# 04_outline.md: Argument architecture (Phase 5), REVISION 2026-11-21 (final data: 9,831 ratings / 3,841 products / 25 raters)

> Replaces the outline of 2026-11-09 in full. It applies sections B, C and D of `revision_brief_2026-11-21.md` to draft 7 (`manuscript.qmd`, 370 lines, one paragraph per line). This outline goes to **human checkpoint 1**. The questions for the author are collected in "Decisions for the author" at the end; the "Evidence gaps" section directly before it tells the orchestrator whether a targeted search is needed.

Profile: `imrad-apa`. Venue: *Creativity Research Journal*. Style: APA 7th.
Structure: Abstract, Introduction, Method, Results, Discussion, Conclusion, References, Supplementary Material.

Sources (precedence in this order where they disagree):
1. `revision_brief_2026-11-21.md` (sections B, C, D, E; governing)
2. `03_findings.md` of 2026-11-21 (the ONLY source of numbers; its "Flags", "Not found" and "Not quotable" sections are binding)
3. `07_rater_number_evidence.md` (binding citation rules, key map, resolutions)
4. `revision_brief_2026-11-09.md` (five-move Introduction arc; valid where not superseded)
5. `02_artifacts.md` of 2026-11-21 (53 labels: NB00 1, NB01 6, NB02 14, NB03 32)
6. `01_dossier.md`, `06_web_literature.md` (literature support; a key is usable only if it resolves in `/home/max/drive/phd_library.bib`)
7. Concept note `~/drive/KNOWLEDGE/Paper_CreativityAssessmentInSportsCAT.md` (intent, not results); `05_review.md` (round 8); `author_todo.md`; `kolloq-presentation/kolloq-slides.qmd` (author facts of section D only; its numbers are not a source)
8. `~/drive/utils/writing-models/` (introduction, methods, results, discussion-conclusion, abstract)

---

## Central contribution [ATC-1]

The study adapts judge response theory (JRT) to consensual creativity ratings of single football actions, a class of nonverbal, time-pressured products rated in a pool-based sparse design (many raters, each rating a subset; one to a few ratings per action). In such a design the classic question "how many raters does a panel need" becomes "how many ratings per action, and from which raters". The contribution is empirical and has four parts, all on the final data of @tbl-design-summary (F2.1: 9,831 ratings of 3,841 products by 25 raters).

1. **Four rater models compared on this product class (RQ3a).** Rater-specific thresholds and rater-specific discrimination are supported by the likelihood-ratio tests (χ²(110) = 878.581 and χ²(24) = 177.440, both *p* < .001; F3.19) and by AIC and SABIC (GRM lowest on both; F2.3). BIC does not follow: within the ladder it is lowest for M1 (M2 29.303 and M3 49.946 above it), and M1 and the GRM are tied (GRM 0.416 above M1; F2.3).
2. **With one or two ratings per action, raters differ too much for raw means to stand for the action (RQ2, RQ3b).** M1 severity spans 2.388 logits (F2.6); GRM discrimination runs from 0.65 to 4.17 (F2.7); Krippendorff's ordinal α for single ratings is .402 (F3.14); raw means and GRM scores agree at Kendall's τ-b = .773 (one rating) and .818 (two), with .076 and .066 of pairs in reversed order (F2.11), whereas the four models order the products almost identically (Spearman ρ .980 to .997; F3.23).
3. **Reliability as a function of the number of ratings, observed and simulated (RQ1).** The empirical reliability of the obtained scores is .695 [.673, .711] against a model-based full-panel reliability of .970 [.966, .973] (F3.12). Observed product-level reliability is .526 with one rating and .703 with two (F2.4). In simulation from this rater pool, the smallest number of ratings at which simulated reliability reached .80 was four (.832 [.825, .838]; F2.5, F3.15); the actual design topped up to at least four ratings per product gives .837 [.832, .842] (F3.10).
4. **JRT adapted to single actions in sport**, yielding rater-adjusted scores with standard errors (EAP scores with posterior SDs; product-level reliability from .071 to .955, median .706; F3.13). No accuracy claim is made for these scores.

Implication [ATC-3, ATC-5, ATC-14, ATC-15, ATC-30, ATC-31, ATC-57]: studies of such products should report the reliability of the scores actually used and the agreement of single ratings, plan the number of ratings per action from evidence for their own product class and rater pool (here: four for .80, by simulation), give each rater enough ratings and link raters through a common calibration set, and consider a scoring model that adjusts for rater differences, reporting how far its ordering departs from raw means.

## Core argument (6 sentences)

1. Creative products are judged by the consensus of independent raters (CAT), and the field lacks established assessment standards, so the design of a rating study has to be justified by evidence (amabile1982; barbot2019).
2. How many raters are enough is conditional on the reliability target, the object of measurement, the raters, the scale and the domain; published figures run from two or three trained raters for short divergent-thinking responses to 10 novices who do not reach an adequate alpha for expert-domain products, and none was located for sport (07).
3. That evidence comes largely from verbal and static material and from complete panels; football actions are nonverbal behaviour under time pressure, and thousands of them can only be rated in a sparse design in which each action gets one to a few ratings from changing raters.
4. In such a design the question becomes how many ratings per action, and from which raters; only a model that estimates each rater's severity, thresholds and discrimination can answer both parts, and whether that flexibility is needed is testable (myszkowski2019; myszkowski2021).
5. In 9,831 ratings of 3,841 actions by 25 raters, the obtained scores had a reliability of .695 against .970 for the full panel; four ratings per action were needed for .80 in simulation; raters differed strongly; the LR tests and AIC/SABIC supported rater-specific thresholds and discrimination while BIC did not; the models ordered actions almost identically, the raw mean did not.
6. The gap between .695 and .970 is a property of the design; rating-design evidence has to be collected for the product class and rater pool at hand, and modelling the raters matters more than which rater model is chosen [ATC-45, ATC-46].

## Research questions (exploratory; no hypotheses) [ATC-20]

Wording unchanged from draft 7 lines 66–68.

- **RQ1 (number of ratings and reliability).** How reliable are the creativity scores obtained in this study, how does product-level reliability vary with the number of ratings an action received, and how many ratings per action are needed for reliable estimates in this rater pool, (a) as observed and (b) as simulated from the fitted model? How do these figures compare with a hypothetical full panel and with conventional agreement and consistency indices?
  - Evidence: F2.4, F2.5, F3.9, F3.10, F3.12, F3.13, F3.14, F3.15.
- **RQ2 (rater differences).** How do raters differ in severity, threshold location, scale use, discrimination and information, and how precisely are these differences estimated?
  - Evidence: F1.4, F1.5, F2.2, F2.6–F2.10, F3.4, F3.16–F3.18.
- **RQ3 (model constraints and consequences for scores).** (a) Are the Rasch-family constraints of a shared category structure and of equal discrimination tenable for these ratings? (b) How far do product scores and rankings depend on the scoring model, from the raw mean through the constrained models to the graded response model?
  - Evidence (a): F2.3, F3.19–F3.22. Evidence (b): F2.11, F2.12, F3.23, F3.24.

Supporting analyses (not RQs): model adequacy (F3.5–F3.8); sensitivity to the rater exclusion (F3.2).

---

## Conventions in this file (carried forward and updated)

- **F…** = finding ID in `03_findings.md` (F0.1–F0.4, F1.1–F1.6, F2.1–F2.12, F3.1–F3.24). Every number below is copied from there as printed and converted to APA form only as stated next.
- `tbl-…` / `fig-…` = labels from `02_artifacts.md`. **[MAIN]** embedded in the main text; **[SUPP]** embedded in the supplement. Embed syntax: `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/<notebook>.ipynb#<label> >}}` (snippets per label in `02_artifacts.md`); cross-reference `@<label>`.
- **[ATC-n]** = interpretive or contribution claim, or author fact from the talk, that the author must confirm; not marked in the text, listed with its sentence in `author_todo.md` section 2. **[FI-n]** = FILL IN placeholder the author must supply, written `[\[FILL IN: … (FI-n)\]]{.mark}`. Numbers are stable; closed items are listed as closed, never renumbered.
- **APA number format.** Values that cannot exceed 1 drop the leading zero: reliabilities, correlations (incl. Q3, τ-b), α, shares, *p*. Values that can exceed 1 keep it: *a*, *b*~k~, information, θ̂ and θ̂ ranges, PSD, infit/outfit, means, SDs, entropy, severity, χ², information criteria and their differences (0.416), |Δθ̂|, |Δa|, the Q3 criterion 0.2, the flag bounds 0.7–1.3. Numbers ≥ 1,000 take a comma, also where the notebook prints none ("11323" → 11,323; "1174" → 1,174). Seeds and identifiers take no comma (seed 20260713). **No rounding, no added or removed decimals.** One sanctioned exception: the median overlap of rater pairs, printed 22.500, is written 22.5 (as in the brief, B9). *p* is written *p* < .001.
- **Precision as printed.** GRM *a* and *b*~k~: 2 decimals. Information with intervals: 2 decimals (`tbl-grm-rater-information-ci`); 3 without (`tbl-grm-information-summary`); shares 3. M1 severity: 2 decimals from `tbl-rater-overview`, except the two extremes and the span, which print at 3 decimals (−1.005, SE 0.059, R19; 1.383, SE 0.058, R06; 2.388 logits). M3 discriminations 3 decimals. Response styles 3 decimals; R09's mean is **3.643** (never 3.642). Sensitivity table 5 decimals. Projection and top-up: 3 decimals with ranges. Category shares of F1.4 (6 decimals) are not quoted; quote the counts.
- **Read-off statements.** Comparisons marked *(read off printed values)* in `03_findings.md` may be written as descriptions of a table ("lowest", "above 1", "inside the range"), never as a test or as a printed result. Read-off counts allowed in this form: 14 raters flagged for GRM infit or outfit below 0.7; nine and eight raters with unordered steps; observed means inside or below the simulated range.
- **Never quote:**
  - any value that exists only in a non-source: `01_data_overview_new_ratings.ipynb`, `04_score_analysis.ipynb`, `local_rater_lookup.ipynb`, `results/krippendorff_by_n_ratings.csv` and its R script (**no Krippendorff-by-n value**), `results/figures/rating_progress.png`, `reports/`, the talk and its `scripts/`, `AUDIT.md`, the README freeze facts, archived data, the previous `03_findings.md`, the briefs' "expected values";
  - the **IDs of the three raters of the fully crossed block** (the brief names R07, R23, R24; no notebook prints them) and the rule by which seven raters were dropped from the pairwise α (FI-9);
  - the talk's "25 raters and 3,841 actions" for Krippendorff's α (the notebook prints 25 raters, 2,984 products);
  - any value of an earlier data set (the stale-string list in the change map) and any statement that data were added or that estimates changed;
  - the md5 fingerprint; the data-collection period (FI-32); per-rater non-recognition counts (FI-22); rater background, recruitment and allocation (FI-4, FI-21, FI-31);
  - CIs or SEs that are not printed: for rel~post~ by number of ratings, for the sensitivity differences, for the raw-mean-vs-GRM statistics, for M1 severities other than R19 and R06, for the per-model reliabilities of F3.24; any significance test of reliability differences between models;
  - the median GRM *a* (drawn only) and any GRM max/min discrimination ratio; "ten-fold" for the M3 ratio (quote 10.254); "2.39 logits" (quote 2.388); "about 0.4" (quote 0.416); "about .70" and "about .97" (quote .695 and .970);
  - **pairwise information-criterion differences that are not printed**: only Δ to the best model is printed. Quotable: GRM lower than M3 by 49.530 on AIC and on SABIC; M2 29.303 and M3 49.946 above M1 on BIC; GRM 0.416 above M1 on BIC. Not quotable: M2 − M3 on any criterion, M1 − M2 on AIC or SABIC, GRM − M3 on BIC (give the two printed values instead);
  - "below the simulated range" at **k = 6** (observed .879 equals the printed lower bound .879); simulated reliability for k > 10; the first k reaching .70 or .90; workload-weighted or selected rater sets; a seed for the top-up simulation;
  - **"logits" for the θ̂ range at equal raw mean** (2.129 is printed without a unit; write "on the GRM score scale");
  - any statement that the notebook compares observed with simulated reliability (it juxtaposes them; the comparison is the authors' reading, ATC-32);
  - the latent variances of F3.24 (author position of round 6); the 26 flagged Q3 pairs that are not listed; the count of 53 duplicated rows (printed but not needed; write 26 pairs, 27 rows);
  - the model labels "M1 (RS-MFRM)", "M2 (PC-MFRM)", "M1 (RSM)", "M2 (PCM)"; the glyph † (write "flagged").
- **Simulation-assumption rule (C4).** The procedure of both simulations is stated in full **once**, in Method 2.10, following the notebook notes (F2.5, F3.10, F3.15). Projection: products with θ ~ N(0, 1); each receives *k* ratings (*k* = 1 to 10) from *k* distinct raters of the panel drawn at random, each rater equally likely; ratings generated from the fitted GRM and scored with its parameters, treated as known; 50 replications of 2,000 products per *k*; seed 20260713. Top-up: the actual assignment of raters to products is kept, not the ratings; products with fewer than four ratings get additional raters drawn at random with equal probability and without replacement from the panel raters who had not rated them, until they have four; in each of 50 replications every real product receives θ ~ N(0, 1), all ratings are generated from the fitted GRM, products are scored by EAP with the parameters treated as known; the actual-design row is a validation. The clause "so the draws do not reproduce the raters' actual workloads" and the word "distinct" are the authors' statements (the first follows from equal drawing probability, the second was confirmed from the code on 2026-11-09), not notebook quotations: **[ATC-35]**. Results, Discussion, Limitations and the supplement refer to Method 2.10 and do not restate the procedure.
- **Final data only.** No "notebook", "output", "pipeline", "freeze", "re-run"; no mention of an earlier data set, a data update, a "latest collection" or how estimates changed. Statements taken from notebook notes become the authors' wording, [ATC] where interpretive.
- **Terminology (C6).**
  - "Rater" everywhere; one sentence at the first CAT mention says the CAT and JRT literature calls raters "judges".
  - "Product" in Method and Results; "action" in the Introduction's sport framing, the stimulus description, the practical implications and the Conclusion. Defined once in Method 2.3.
  - Model labels glossed **once**, at first use in Method 2.7: "M1, the rating-scale many-facet Rasch model; M2, the partial-credit MFRM; M3, the generalized partial credit model; GRM, the graded response model". Afterwards only "M1", "M2", "M3", "GRM"; the long forms "M1 (rating-scale MFRM)" etc. appear only in table captions and cells, as printed. The Introduction, which precedes the gloss, uses the spelled-out model names and no labels. "RSM"/"PCM" only where andrich1978 / masters1982 are cited. "A shared category structure" is a property of M1 only.
  - **One name per reliability quantity:** "empirical reliability of the obtained scores" (the tables print "empirical marginal reliability"; say so once in Method 2.10); "model-based full-panel reliability" (tables: "model-based marginal reliability"); "product-level reliability (rel~post~)"; "simulated reliability" (the empirical reliability of simulated scores, in the projection and the top-up). Cronbach's α and Krippendorff's α keep their names; "panel-level alpha" is not used as a synonym in Method and Results.
  - "First and third quartiles", never Q1/Q3 (Q3 is Yen's statistic).
  - Response styles: "share of ratings in the lowest category (1)", "in the highest category (7)", "in the extreme categories (1, 7)", "in the middle categories (3–5)".
  - "Average information" = information integrated over θ ~ N(0, 1).
  - Severity: "severity (M1)", 0 = average rater, higher = stricter. In the GRM, "threshold location", not severity [ATC-6].
  - "Rating-design evidence" for the sport gap; never "no evidence"; no "by convention".
  - Author names typed in prose keep their particles ("de Ayala", "ten Hove", "de Joode", "de Sa Fardilha", "van Hooijdonk").
- **Rater-ID rules.** Final raters: R01–R19, R23–R27 and R30 (25). Excluded: R20, R21, R22, R28, R29 (five). IDs do not follow workload order. Two pools: R01–R19, and R23–R27 with R30 (D). **Raters with about 50 ratings: R17 (52), R18 (55), R27 (47), R30 (47).** R15 has 73 and is named with its count where it is an extreme. **R26 (136), R16 (357) and R24 (481) are never described as raters with few ratings.**
- **Figure annotations.** The values printed inside `fig-grm-reliability-observed-vs-simulated` are quoted from the tables (.837 from `tbl-grm-reliability-min-ratings`; .970 from `tbl-grm-reliability-ci`; 25 raters from `tbl-design-summary`), never from the image.
- **No accuracy claim.** Nowhere does the paper say that model-based scores are more accurate than raw means or than the constrained models.
- **Exploratory framing.** No "hypothesis", "supported", "confirmed" for the RQs, except the LR/AIC/BIC wording of RQ3(a) [ATC-20].
- **07 rules.** Every rater-number figure is given with its reliability target and object of measurement; no over-attribution to Cseh and Jeffries; author-synthesis statements are not placed under a citation; verification levels "excerpts" and "abstract" stay under FI-17.

---

## Title

Stays as in draft 7 line 2 (brief E): *How many ratings, and from whom: Reliability, rater differences, and the number of ratings needed in creativity ratings of football actions, a judge response theory analysis*. `shorttitle` unchanged. The Introduction now states the question the title asks (P12).

## Word budget (main text about 8,000–9,000 words excl. references, tables and box; FI-16 checks the CRJ limit)

| Section | Words | Notes |
|---|---|---|
| Abstract | ≤ 250 | hard limit until FI-16 says otherwise |
| Introduction | 1,600–1,850 | five moves; evidence paragraph split; contributions paragraph added (about 110 words), paid for by a shorter analytic-route sentence and a tighter P1 |
| Method | 2,100–2,400 | grows by the definition block (about 110 words) and the app description |
| Results | 1,600–1,900 | information criteria once; no separate sensitivity section |
| Discussion | 1,800–2,100 | no summary paragraph; simulation and sensitivity by cross-reference |
| Conclusion | 150–200 | one paragraph |

---

## Section outline

Paragraph IDs (P1 …, M1 …, R1 …, D1 …) are for this outline and the change map only; the manuscript has no numbered sections (`number-sections: false`).

### Abstract (one paragraph, ≤ 250 words, no citations, no markers) [FI-16]

Abstract model: background and gap → method → results with numbers → implication. Draft 7 has 249 words, so the additions of C5 need cuts. Content, in order:

- **Background/gap (2 short sentences).** Consensus ratings; the number of raters needed and rater differences studied mostly with verbal and static material; rating-design evidence lacking for nonverbal, time-pressured products such as football actions [ATC-2, ATC-28].
- **Method (1–2 sentences).** 25 raters, 9,831 ratings of 3,841 football actions, 7-point scale, incomplete connected design (F2.1); a GRM and a ladder from the rating-scale many-facet Rasch model to the generalized partial credit model; reliability by number of ratings, observed and simulated.
- **Results.**
  - RQ1: empirical reliability of the obtained scores .695 against .970 for a hypothetical full panel (F3.12); **new (C5):** single ratings agreed at Krippendorff's α = .402 while Cronbach's α was .959 (F3.14); .526 with one rating and .703 with two (F2.4); the smallest number of ratings at which simulated reliability reached .80 was four (F2.5) [ATC-35].
  - RQ2: raters differed in severity (2.388 logits; F2.6), category use, thresholds, discrimination and information; parameters of raters with about 50 ratings were imprecise.
  - RQ3a: LR tests rejected a shared category structure and equal discrimination (both *p* < .001), whereas the Bayesian information criterion favoured the constrained models in both cases (supported by the printed BIC values M1 30,617.021 < M2 30,646.324 < M3 30,666.967; F2.3; see Decision 9 for the M1–GRM tie).
  - RQ3b **(new, C5):** raw means and GRM scores agreed at Kendall's τ-b = .773 (one rating) and .818 (two), with .076 and .066 of pairs in reversed order (F2.11).
- **Implication (1 sentence).** Report the reliability of the scores actually used, plan several ratings per action from domain-specific evidence, link raters through a common calibration set, consider rater-adjusting scoring models [ATC-5, ATC-14, ATC-15, ATC-30].
- **Cuts to stay within 250 words, in this order:** the category-use parenthesis (.579 to .016); the second gap sentence merged into the first; "in this exploratory study"; the method sentence shortened; then, if still over, the "(two)" halves of the τ-b clause (.818, .066); last, the severity span.
- **Do not use:** "student raters"; any projection value other than "four"; any R-number; "we show"; any accuracy claim.

### 1 Introduction (five moves; introduction model: importance and background → research map → gap → present paper)

Purpose: lead from "creativity is judged by consensus and the field lacks assessment standards" through "how many raters depends on the conditions" and "sport is a nonverbal, time-pressured domain without rating-design evidence" to "in a sparse design the question becomes how many ratings per action and from whom, and JRT can answer it", ending in RQ1–RQ3 and the contributions. Each move ends with a hand-over sentence.

**Move 1 — Why rating-design evidence matters (about 230 words; C1)**

- **P1 (rewritten; tight motivation).** Creativity as a core competence: workforce skill (wef2025), PISA 2022 (oecd2024), a quality to develop and evaluate in sport (safardilha2019; santos2016). Standard definition: a creative product is original and effective (stein1953; runco2012). Why design evidence matters: enduring conceptual and methodological issues and the lack of established assessment standards limit creativity research (barbot2019, editorial of the 2019 special issue). No facet theory, no CAT definition, no terminology note in this paragraph. [FI-17: wef2025, oecd2024, safardilha2019, santos2016; barbot2019 quotation, p. 131; stein1953]
- **P2 (new paragraph, split from draft 7 line 36).** The four Ps, person, process, press and product, attributed to rhodes1961; in the framework of batey2012 this study is located at the individual level, the product facet and ratings by others [FI-17: wording of the three framework cells]; each facet requires its own measurement approach (barbot2019b). Creative products are assessed by the consensus of independent raters who know the domain: the CAT (amabile1982; hennessey2011; kaufman2024). Terminology sentence (judges = raters). Hand-over: the consensus is only as good as the panel that produces it.

**Move 2 — How many raters are enough is conditional (about 520 words)**

- **P3 Aggregation (draft 7 line 40, kept).** Spearman–Brown logic (amabile1982); a high alpha from a large panel can mask low agreement between single raters: 106 novices, alpha .94, *r* = .22 with experts (kaufman2008a) [FI-17]; consistency and absolute agreement seldom distinguished (cseh2019; stefanic2015).
- **P4a Person-level evidence (first half of draft 7 line 42; C1 split).** Opening sentence with the conditions: target, object of measurement, rater expertise and training, scale and scoring format, product heterogeneity, domain. Then, each figure with target and object: D-studies projected two trained student raters for unusual uses and instances and three for consequences for a relative generalizability coefficient of at least .80 under average scoring (silvia2008); five graduate-student raters with 15 captions for relative and absolute coefficients of .80 (kaufman2007; captions are creative writing, not divergent thinking; training not recorded, m8-3); where person-by-task variance is large, adding raters stops helping: with two divergent-thinking items no panel of one to 10 lay raters reached .80, rater main effects 26.6% and 56.9% of the variance (hass2018); two trained raters needed five tasks for a relative coefficient of .70, more for absolute decisions (vanhooijdonk2022); low dependability for all rater groups on science tasks (long2015). [FI-17]
- **P4b Product-level evidence (second half of draft 7 line 42).** Novices rating expert-domain products with Cronbach's alpha as the criterion: Spearman–Brown projection to 10 novices .58 for poems (kaufman2008a); 100 random panels of 10 novices averaged .53 (range .35–.75) for short stories and .66 for five engineering designs, against .93 and .86 for 10 experts; 10-novice panels correlated .56 with experts on stories (kaufman2013). Non-experts rating open-ended products: seven or more for fashion outfits to exceed inter-rater and test-retest intraclass correlations of .70 consistently (barth2021); 10–15 undergraduates for design products against a test-retest intraclass correlation of .70, 15–20 for composite indices (terai2026). [FI-17]
- **P5 Conclusion of the move (draft 7 line 44 plus the practice sentences of line 42).** Practice does not follow these figures: most of 84 reviewed studies used fewer than 10 raters, about five on average (long2022); common recommendation five to 10 (kaufman2008); reported panels from two to 134 (cseh2019). We located no study of the required number of raters for sport, music as a headcount, mathematics, advertising or programming [ATC-2]. No general number exists; cseh2019 list the number of raters among the open questions of the CAT (no "must be established per domain"); each assessment procedure needs its own G- and D-study (vanhooijdonk2022). Hand-over: the evidence comes from a narrow range of material.

**Move 3 — The verbal bias and the sport case (about 320 words; draft 7 lines 48–52, kept)**

- **P6 Material type [ATC-28].** Largely verbal material and static products inspected at leisure (amabile1982; kaufman2008a; reiterpalmon2019; saidmetwaly2017b; paca2019; acar2023; acar2024); standard tests in sport are generalist and verbal or drawn (safardilha2019) [FI-17]. No percentage (C7: no PACA shares).
- **P7 Football actions as a product class [ATC-39].** Nonverbal behaviour under time pressure in a complex, dynamic environment (orth2017; hristovski2011; hristovski2012; vaughan2019; rasmussen2019; raab2007; memmert2011b); argued to be more ecologically valid when observed in competition (safardilha2019; memmert2011b; joode2023; cotter2019); ratings of such actions exist (kempe2018; joode2023; zahno2023; zahno2024) [FI-17].
- **P8 The gap in sport [ATC-2, ATC-29].** Process measures dominate (memmert2007; memmert2010; memmert2013; furley2015; roca2018; fink2018; safardilha2019; memmert2011b); the few studies with expert ratings relied on three or four coaches or trained experts, described per study with the m8-2 hedges (kempe2018; joode2023; memmert2010; roca2018) [FI-17]; none examined how many raters are needed, how raters differ or which scoring model suits the ratings. Hand-over: these questions require a method that treats the raters as the object of study.

**Move 4 — From averages to judge response theory (about 370 words; draft 7 lines 56–60, kept; model names spelled out, no M-labels)**

- **P9 Averages to G-theory.** primi2019; myszkowski2019; kaufman2013; barth2021; terai2026; silvia2008; hass2018; vanhooijdonk2022; saidmetwaly2017b.
- **P10 MFRM.** linacre1989; eckes2015; primi2019 (severity confounds scores when raters score different subsets; workload cut by about a third); equal discrimination and, in the rating-scale form, a shared category structure (myford2004; myszkowski2021) [FI-17].
- **P11 JRT.** myszkowski2019; myszkowski2021; applications barbot2023, pellegrino2025, forthmann2025, goecke2024, myszkowski2025 [FI-17]; no application to ratings of sport actions located, apart from shin2025 [ATC-2]; the constraints become testable.

**Move 5 — The present study (about 330 words)**

- **P12 Design and the question it poses (draft 7 line 64, rewritten; C1) [ATC-56, ATC-20].** A large set of CAT-style ratings of football actions by 25 raters. Thousands of actions cannot be rated by every rater, so the study used a pool-based sparse design: many raters, each rating a subset, one to a few ratings per action (planned-missing rating designs: primi2019; forthmann2025; goecke2024). Indicative wording for the reframing: "In such a design, the question of how many raters a panel needs becomes the question of how many ratings each action needs, and from which raters." RQ1 answers the first part, RQ2 the second. Exploratory; no confirmatory hypotheses. Do not state that the sparse design was planned as such unless FI-4 confirms it; "used" is safe.
- **RQ1–RQ3** as bullets (wording above).
- **P13 Analytic route (draft 7 line 70, cut to one or two sentences).** GRM and an adjacent-category ladder by marginal maximum likelihood; reliability overall and by number of ratings; two simulations; rater parameters with uncertainty; GRM scores against raw means and the constrained models. Scope: rater expertise and the design of the rating scale are not analysed.
- **P14 Contributions (new; C2) [ATC-44].** Four contributions, hedged: (i) four rater models compared on a nonverbal, time-pressured product class, with rater-specific thresholds and discrimination supported by the likelihood-ratio tests and by AIC and SABIC, but not by BIC, which was lowest for the most constrained model and nearly identical for the GRM (modified wording, Decision 9); (ii) with one or two ratings per action, raters differed too much for raw means to stand for the action; (iii) reliability as a function of the number of ratings, observed and simulated, with four ratings reaching .80 in this rater pool; (iv) JRT adapted to single actions in sport, yielding rater-adjusted scores with standard errors. No numbers other than "four" and ".80". "To our knowledge" for (iv).

### 2 Method (methods model: overview → details and justification → relation to prior methods → problems; all FILL INs visible)

**2.1 Overview (M1; draft 7 line 76).** CAT-style rating study: independent raters, relative judgements, randomised order (amabile1982; hennessey2011). [FI-1: larger project, ethics, consent] [FI-15: preregistration]. Exploratory.

**2.2 Raters (M2; draft 7 line 80, rewritten; D) [ATC-54].**
- Two pools: R01–R19, Bachelor's and Master's students rating as part of thesis projects [FI-1: confirm, recruitment, number at start]; R23–R27 and R30 from a different pool [FI-31: background, recruitment, allocation]. [FI-21: rater-pool description for both pools or a statement that it was not recorded.]
- Final data: 25 raters, pseudonymised R01–R19, R23–R27 and R30; the gaps arise because five raters were excluded (2.6); numbers do not reflect workload. Between 47 and 1,174 ratings each (F1.2; @tbl-grm-rater-parameters).
- No mention of the planned open recruitment (it is a plan, not part of this study; it only shapes the Limitations wording, ATC-55).

**2.3 Products and stimulus material (M3; draft 7 line 84; D) [ATC-49].**
- Definition of the product term (kept).
- Author fact: single actions from matches of the men's and women's European Championships and World Cups, the Africa Cup of Nations and the Copa América, cut as short video clips and linked to event data (StatsBomb; statsbomb2024 resolves in the library, check that it is the intended reference, FI-17).
- [FI-2, reduced: action-selection rule, clip length, video source, number of matches.]

**2.4 Rating procedure (M4–M6; draft 7 line 88, rewritten; D).**
- **M4 Software and procedure [ATC-50].** Browser-based, open-source rating app written in Streamlit (repository named: github.com/maxk92/streamlit-creativity-rating-app; see Decision 19 on masked review). Metadata and a pitch sketch identify the action; the clip loops; three 7-point scales (creativity, technical correctness, aesthetic appeal) and an "action not recognised" option are shown with it; clip order randomised; familiarisation clips precede the rating; the definition is available at any time; progress saved per participant. [FI-32: data-collection period.] [FI-34, proposed: session length and breaks, number of familiarisation clips, language version used; no timing statements for single raters.]
- **M5 Definition [ATC-51, ATC-19].** Lead-in: the text raters read before the familiarisation clips, in German or English, after stein1953 and runco2012. Verbatim as an indented block:
  > Creativity is defined as the product of originality and functionality. A creative solution must be original (novel, rare, unusual) as well as functional (it must provide a solution to the given problem). Creativity in soccer describes the ability to choose solutions or execute actions in a given game situation that deviate from the norm, appear surprising, and are potentially advantageous for one's own team. It arises from the conscious perception of the situation and the recognition of possibilities that others do not see, or see only later. A creative action must be functional: it must (potentially) bring one's own team closer to the game objective (scoring, preventing goals). What matters is the intention or idea and the expected probability of success, not the actual outcome.

  Keep the sentence that showing a definition departs to a minor degree from the CAT rule that raters receive no criteria (hennessey2011) and resembles trained-rater studies in sport (kempe2018; memmert2010).
- **M6 Scale and other dimensions [ATC-48, ATC-52, ATC-53].** Unipolar 7-point scale with verbal labels at the endpoints only, 1 "not creative" and 7 "very creative" (replaces "anchors at 1, 4 and 7"). One sentence on the choice: the rating-scale literature places the optimum at about seven categories (preston2000; lozano2008), and the scale is unipolar because creativity is an amount of a property, not a valence around a neutral point [FI-17: both sources; the dossier marks them unverified]. No further scale-length literature (C7). Technical correctness and aesthetic appeal were rated on the same 7-point format so that construct validity can be examined later, as amabile1982 recommends for a new domain; not analysed here.

**2.5 Rating design (M7; draft 7 line 92).**
- [FI-4, reworded without "latest collection": allocation of products to raters in both pools; planned overlap or common set; how products came to have one, two or more ratings; whether products with different numbers of ratings were rated by different raters or differ systematically.] Do not write an allocation rule the author has not confirmed.
- Incomplete but connected: one component (F1.3, F2.1; eckes2015); MML assumes ignorable missingness [ATC-18].
- Distribution of ratings per product (@fig-design-ratings-per-product [SUPP]; F1.2): 857 products with one rating, 2,227 with two, 73 three, 93 four, 143 five, 185 six, 124 seven, 77 eight, 25 nine, 22 with 10, 8 with 11, 5 with 12, 1 with 13 and 1 with 14. Ratings per rater in @fig-overview-degree-distributions [SUPP]; jointly rated products per rater pair in @fig-overview-rater-overlap [SUPP, new embed].

**2.6 Data preparation and final data (M8–M10; draft 7 lines 96–100).**
- **M8 Cleaning (F0.2, F0.3, F2.1).** 11,323 raw rows; 1,432 ratings marked "action not recognised" removed [ATC-40: cause; FI-22]; one out-of-range value (0.0, R04) removed; 26 rater–product pairs entered more than once, one with conflicting values; the entry with the latest timestamp kept, removing 27 rows; 9,863 ratings by 30 raters remained (F0.4).
- **M9 Exclusion (F1.1, F3.1; @tbl-excluded-raters [SUPP]).** Raters with fewer than 15 ratings: R20 (13), R21 (9), R22 (2), R28 (7) and R29 (1), together 32 ratings; one product rated only by them dropped [FI-23]. **The sensitivity result is not given here (C4):** one clause says that the effect of the exclusion was examined by refitting the GRM with the excluded raters, reported under Model adequacy in the Results.
- **M10 Final data (F2.1; @tbl-design-summary [MAIN]).** 9,831 ratings of 3,841 products by 25 raters; scale 1–7, coded 0–6; mean 2.559 ratings per product (median 2, range 1–14, harmonic mean 1.819); 857 products with a single rating; fill .102; one component; 23 of the 300 rater pairs without a common product; median overlap 22.5. Category use (F3.4; @tbl-category-usage [SUPP]; @fig-category-usage-shares [MAIN]): eight raters never used at least one category; category 7 never used by R01, R03, R06, R18, R25 and R26; categories 6 and 7 by R17; categories 5 and 7 by R27 (internal gap). R17 and R27 have four thresholds, R01, R03, R06, R18, R25 and R26 five, all others six; R27's thresholds are not directly comparable (F2.7).

**2.7 Measurement models (M11–M14; draft 7 lines 106–112).**
- M11 IRT basics (kept): lord1980; embretson2013; ayala2022; rasch1960; bond2020; andrich1978; masters1982; muraki1992; samejima1969.
- M12 JRT frame (kept): myszkowski2019; myszkowski2021; threshold and discrimination definitions [ATC-6].
- M13 Ladder, **with the one-time gloss of the labels (C6)** in the first sentence; M1 in `sirt::rm.facets` (linacre1989; eckes2015; primi2019; robitzsch2025); M2, M3 and the GRM in mirt (chalmers2012). "Many-facet Rasch models (MFRM)" is expanded in Introduction P10 (m8-5).
- M14 **Scoring model, with forward reference (C3) [ATC-8].** The product scores of all analyses come from the GRM: rater-specific discriminations and thresholds, thresholds ordered by construction, cumulative link plausible for a unipolar scale; it had the lowest AIC and SABIC of the four models and a BIC within 0.416 of the lowest (see the comparison under RQ3 in the Results; @tbl-model-fit). Estimation (F3.5; @tbl-grm-convergence [SUPP]): MML with the EM algorithm, 61 quadrature points, tolerance 0.0001, Oakes standard errors (chalmers2018). The convergence result (550 iterations) moves to Results R1.

**2.8 Model comparison (M15; draft 7 line 116).** LR tests M1 vs M2 and M2 vs M3; log-likelihood, AIC, BIC, SABIC with the difference to the best model; GRM compared by information criteria only (F2.3). Caveats: M1–M2 crosses software, approximate [ATC-41]; its degrees of freedom (110) lie below the formula value (*J* − 1)(*K* − 2) = 120, smaller by the number of categories raters never used, unused end categories and any internal gap (F3.19 note); nesting approximate because of R27's gap [ATC-41]; no model without rater effects.

**2.9 Model adequacy (M16; draft 7 line 120).** Infit and outfit (wright1982) under M1 and the GRM; values outside 0.7–1.3 are flagged (@tbl-rater-overview [SUPP]); with about two ratings per product values below 1 are expected [ATC-33]. S-X² (orlando2000; kang2008), 20 imputations, about 90% of cells imputed, conservative [ATC-11]. Q3 (yen1984) for pairs with at least three jointly rated products (256 of 300 pairs computable; F3.7); negatively biased (christensen2017); flagged at ≥ 30 shared products and a deviation from the mean of more than 0.2; no reference distribution. C2 (cai2014) not computable because 23 of 300 rater pairs share no products (F3.8; no table embedded).

**2.10 Scores, reliability and the two simulations (M17–M20; draft 7 lines 124–130).**
- **M17** EAP scores with PSD; **names the two reliabilities (C6)**: the empirical reliability of the obtained scores, Var(θ̂)/[Var(θ̂) + mean PSD²], called empirical marginal reliability in the tables, as the primary index; the model-based full-panel reliability (green1984), for a hypothetical product rated by all raters, with a grid check. Intervals from 200 accepted parameter draws; products also resampled for the empirical reliability; 53 draws rejected (F3.12).
- **M18** Product-level reliability rel~post~ = 1 − PSD² (partly reflects the prior with one or two ratings); rel~info~ as a check (@tbl-grm-reliability-by-n).
- **M19** Conventional indices (hove2024; cronbach1951; hayes2007): Cronbach's α from pairwise covariances over the usable raters and on the largest fully crossed block; Krippendorff's ordinal α for single ratings; bootstrap over products, 1,000 replications; for the pairwise α 513 of 1,000 replications computable, 487 not; interval approximate [ATC-11]. [FI-9, updated: why seven raters (R26, R12, R19, R14, R02, R27, R17) were not usable for the pairwise alpha; which three raters form the crossed block.] The pair overlaps are shown in @fig-overview-rater-overlap.
- **M20 The two simulations, stated in full here and nowhere else (C4) [ATC-35, ATC-42].** Criterion .80 with the m8-7 clause (silvia2008; kaufman2007; hass2018). Projection and top-up exactly as in the simulation-assumption rule above. Closing sentences: ranges reflect simulation variability only; the observed data remain primary; "simulated reliability" is the name used from here on; observed mean rel~post~ and simulated reliability are different quantities (@fig-grm-reliability-observed-vs-simulated; @tbl-grm-reliability-observed-vs-simulated).

**2.11 Rater parameters, severity, information and response styles (M21; draft 7 line 134).** As draft 7, with the object changes: severity values in @tbl-rater-overview [SUPP]; information in @fig-grm-rater-information-ci [MAIN] and @tbl-grm-rater-information-ci [SUPP]; response styles in @tbl-overview-rater-response-styles [SUPP].

**2.12 Score agreement and sensitivity (M22; draft 7 line 138).** Raw mean vs GRM score by number of ratings (τ-b, share of pairs in reversed order, mean and maximum range of GRM scores at equal raw mean); correlations of EAP scores between models, percentile shift, share changing quintile; M1 grid check; **new:** empirical reliability of the scores of each model (@tbl-marginal-reliability-models [SUPP]). **Sensitivity stated once as a procedure:** the GRM was refitted with all raters who could be estimated (29; R29 gave one rating and could not be estimated; F3.2).

**2.13 Software and availability (M23; draft 7 line 142).** R with mirt and sirt, psych and a Krippendorff package, Python for display [FI-6]; data and code availability; the rating app repository may be named [FI-15].

### 3 Results (results model: overview → objects and key results → problems → one hedged pointer; descriptive only; **RQ order, model adequacy first**, C3)

**R0 Lead (2 sentences; draft 7 line 146).** RQ order; all analyses use @tbl-design-summary; model adequacy first. No "scoring model" announcement.

**3.1 Model adequacy (R1, one short paragraph; replaces "Scoring model", lines 148–150, and absorbs "Sensitivity", lines 214–216)** — F3.5–F3.8, F3.2. Cross-refs [SUPP]: `tbl-grm-convergence`, `tbl-grm-rater-fit`, `tbl-rater-overview`, `tbl-grm-q3-flagged`, `tbl-sensitivity-rater-exclusion`. **No information criteria here.**
- Convergence after 550 EM iterations, information matrix positive definite.
- No rater's S-X² significant (*p* from .362 to .601).
- GRM infit from 0.315 (R26) to 0.983 (R18), outfit from 0.303 (R26) to 0.973 (R18), all below 1; 14 raters flagged, all for values below 0.7 (read off @tbl-rater-overview; R15 and R01 print an outfit of 0.70 there and 0.697 and 0.698 in @tbl-grm-rater-fit, so cite the fit table for them).
- Mean Q3 −.188 over 256 computable pairs; 36 pairs flagged; of the 10 shown, eight deviate negatively and two positively (R09–R23, R17–R24).
- C2 not computable (Method).
- **Sensitivity, numbers once (C4):** refit with 29 raters (9,862 ratings, 3,842 products): empirical reliability .69490 → .69453; model-based full-panel reliability .97008 → .97207; over the 3,841 common products *r* = .99997, mean absolute difference 0.00187, maximum 0.16518, .00364 of products changing quintile; over the 25 common raters *a* correlated at .99796, maximum absolute difference 0.21451. No evaluative adjective.

**3.2 Reliability of the scores and number of ratings (RQ1; R2–R6; draft 7 lines 156–172)** — embeds [MAIN]: `tbl-reliability-overview`, `tbl-grm-reliability-by-n`, `fig-grm-reliability-observed-vs-simulated`.
- **R2 Obtained scores, full panel, conventional indices** (@tbl-reliability-overview; F3.9, F3.12, F3.14). Empirical reliability of the obtained scores .695 [.673, .711]; model-based full-panel reliability .970 [.966, .973], grid check .970 (@tbl-grm-reliability-ci; @fig-grm-panel-information); pairwise Cronbach's α .959 [.931, .970] (18 raters, 1,948 products; interval approximate, 513 of 1,000 replications computable; @tbl-naive-indices); fully crossed block α .785 [.736, .823] (3 raters, 270 products; no rater IDs); Krippendorff's ordinal α .402 [.375, .427] (25 raters, 2,984 products). State what each refers to ("Refers to" column). Do not discuss the M1–M3 rows; no closeness claim.
- **R3 Observed product-level reliability by number of ratings** (@tbl-grm-reliability-by-n; @fig-grm-rel-post-by-n; F2.4). Mean rel~post~ .526 for the 857 products with one rating, .703 for the 2,227 with two, .770 for the 73 with three and .815 for the 93 with four, the first row at or above .80 (read-off); it rose to .955 at 14 ratings with one exception, .915 at 10 ratings after .917 at nine. Mean PSD fell from 0.683 to 0.211 and was equal at nine and 10 ratings (0.286). The rows from 10 ratings upward rest on 22, 8, 5, 1 and 1 products. No mean reached .970. Products with the same number of ratings differed. Observed, not a design manipulation [FI-4].
- **R4 Simulated reliability by number of ratings** (@fig-grm-reliability-observed-vs-simulated; values in @tbl-grm-reliability-projection, @tbl-grm-reliability-observed-vs-simulated and @fig-grm-reliability-projection [SUPP]; F2.5, F3.15). Simulated reliability rose at every step: .526 [.511, .538] at one rating, .702 [.691, .712] at two, .785 [.776, .793] at three, .832 [.825, .838] at four, .928 [.925, .932] at 10; the smallest number of ratings at which simulated reliability reached .80 was four. **B5 wording per the findings [ATC-32]:** the observed means lay inside the simulated 95% range at one, two and nine ratings, below it at three, four, five, seven, eight and 10 ratings, and at its lower bound at six (.879). Different quantities (one clause, reference to Method).
- **R5 Top-up design** (@tbl-grm-reliability-min-ratings [SUPP]; row also in @tbl-reliability-overview; F3.10). Simulated actual design .691 [.684, .699] (mean rel~post~ .693), next to the observed .695 [ATC-32]; design with at least four ratings per product .837 [.832, .842], with 7,098 rater–product pairs added in 3,157 products (16,929 simulated ratings in total; m8-4 wording). **No restatement of the procedure.**
- **R6 Distribution and consistency** (@tbl-grm-reliability-summary; @fig-grm-rel-post-histogram; @fig-grm-rel-post-by-theta; @fig-grm-rel-consistency; F3.13). rel~post~ median .706, interquartile range .195 (first and third quartiles .601 and .796), range .071 to .955; rel~post~ and rel~info~ *r* = .947; 274 products differ by more than .1.

**3.3 Rater differences (RQ2; R7–R11; draft 7 lines 176–194)** — embeds [MAIN]: `fig-category-usage-shares`, `fig-m1-rater-severity`, `tbl-grm-rater-parameters`, `fig-grm-rater-discrimination-ci`, `fig-grm-rater-information-ci`. Rule: ranges over all 25 raters; when an extreme comes from a rater with 73 or fewer ratings, give the number of ratings and the SE.
- **R7 Response styles and category use** (@fig-category-usage-shares; @tbl-overview-rater-response-styles, @fig-overview-rater-response-styles, @fig-overview-rating-distribution [SUPP]; F1.4, F1.5, F3.4). Means 1.760 (R06) to 4.012 (R19); SDs 1.022 (R01) to 1.841 (R02); share in the lowest category .579 (R06) to .016 (R13); share in the highest category highest for R19 (.064); eight raters gave no 7 (R01, R03, R06, R17, R18, R25, R26, R27), R27 also no 5; middle categories highest for R13 (.799), then R18 (.764) and R12 (.735), lowest for R06 (.192); entropy 1.191 (R06) to 1.903 (R09; mean rating 3.643). Across all ratings, category 1 received 2,278 and category 2 received 2,501 ratings, frequencies fell from category 2 to category 7, which received 149. No per-rater uncertainty.
- **R8 Severity (M1)** (@fig-m1-rater-severity; values in @tbl-rater-overview [SUPP]; F2.6, F3.16). From −1.005 (*SE* 0.059, R19) to 1.383 (*SE* 0.058, R06), a span of 2.388 logits; R19 also had the highest and R06 the lowest raw mean. **New illustration (B2):** the order of severities did not follow the order of raw means exactly: R14 had a higher raw mean (2.22) than R01 (2.16), R17 (2.08) and R27 (2.06) but a higher severity (0.84 against 0.76, 0.68 and 0.80), the second-highest after R06. Drop the "13 below and 11 above" sentence (not printed; R03 prints 0.00).
- **R9 Thresholds** (@tbl-grm-rater-parameters; @fig-grm-category-response-functions [SUPP]; F2.7). *b*~1~ from −6.39 (R18, 55 ratings, *SE* 2.92) to 0.24 (R06, *SE* 0.05); next lowest −3.43 (R13, *SE* 0.49); R06 the only rater with a positive *b*~1~; spacing for example from −0.68 to 2.02 for R02 and from −3.43 to 4.39 for R13; spacing is partly discrimination (Method). Threshold counts as in Method; R27 not compared.
- **R10 Discrimination (B3)** (@fig-grm-rater-discrimination-ci; F2.7). *a* from 0.65 (R18, 55 ratings, *SE* 0.26) to 4.17 (R26, 136 ratings, *SE* 1.49). Next highest, from raters with many ratings as well as few: R06 3.15 (520 ratings, *SE* 0.45), R25 3.03 (138, *SE* 0.45), R12 2.91 (264, *SE* 0.50), R27 2.85 (47, *SE* 0.82); next lowest R09 0.95 (400 ratings, *SE* 0.15). Largest standard errors of *a*: R26 (1.49), R27 (0.82) and R30 (0.69, 47 ratings). R26 is not a rater with few ratings; say only what the table shows.
- **R11 Information** (@fig-grm-rater-information-ci; @tbl-grm-rater-information-ci, @fig-grm-rater-information, @tbl-grm-information-summary, @fig-grm-information-shares [SUPP]; F3.17, F3.18). Average information from 0.13 [0.00, 0.37] (R18) to 3.96 [0.66, 8.40] (R26); shares from .004 [.000, .011] to .112 [.021, .205]; raters with many ratings, for example 0.29 [0.16, 0.49] (R09), 0.84 [0.61, 1.09] (R01), 1.83 [1.09, 2.48] (R02); widest intervals R26, R27 (1.78 [0.57, 3.68]) and R30 (1.74 [0.57, 3.52]). Location of maximum information highest for R01 (2.850), R16 (2.550) and R06 (2.300), lowest for R13 (−0.600). Shares vary with θ: R06 .001 at θ = −2 and .078 at θ = 2; largest shares at θ = −2 from R12 (.151), R24 (.107) and R15 (.105). Intervals conditional on valid draws.

**3.4 Model constraints and consequences for the scores (RQ3; R12–R17; draft 7 lines 198–212)** — embeds [MAIN]: `tbl-model-fit` (moved here), `tbl-raw-mean-vs-grm`, `fig-raw-mean-vs-theta`, `tbl-score-agreement`.
- **R12 RQ3a: LR tests and information criteria, reported once (C3, B1, B7)** (@tbl-lr-tests [SUPP]; @tbl-model-fit; F3.19, F2.3). M1 against M2 (shared category structure): χ²(110) = 878.581, *p* < .001; AIC lower for M2 (29,764.582 vs. 30,423.163), BIC lower for M1 (30,617.021 vs. 30,646.324, a difference of 29.303). M2 against M3 (equal discrimination): χ²(24) = 177.440, *p* < .001; AIC lower for M3 (29,635.141 vs. 29,764.582), BIC lower for M2 (30,646.324 vs. 30,666.967). Summary sentence: both constraints rejected by the LR test and AIC, not by BIC. Then the GRM: lowest AIC (29,585.612) and SABIC (30,093.144) of the four models; same number of parameters as M3 (165), log-likelihood −14,627.806 against −14,652.571, lower than M3 by 49.530 on AIC and on SABIC; on BIC, M1 (30,617.021) and the GRM (30,617.437) differed by 0.416. Parameter counts 31, 141, 165 and 165. Leave the remaining Δ values to the table. Caveats are in Method.
- **R13 Ladder rater detail** (@tbl-discrimination-m3; @tbl-discrimination-summary; @tbl-threshold-order; @tbl-rater-fit-m1 [SUPP]; F3.20–F3.22). M3 discriminations from 0.298 (R18, *SE* 0.138) to 3.056 (R26, *SE* 1.372), median 1.213, ratio of the largest to the smallest 10.254, standard deviation 0.634. Nine raters with unordered steps under M2, eight under M3. Under M1, infit and outfit above 1 for R09 (infit 1.147, outfit 1.123), R17 (1.371, 1.182), R18 (1.233, 1.307) and R30 (1.136, 1.051); for R11 only the infit was above 1 (infit 1.011, outfit 0.954); lowest values for R12 (0.259, 0.276).
- **R14 RQ3b: raw mean vs GRM (B4)** (@tbl-raw-mean-vs-grm; @fig-raw-mean-vs-theta; F2.11). Three printed rows only:

  | Ratings per product | Products | Kendall's τ-b | Pairs in reversed order | Mean / maximum range of GRM scores at equal raw mean |
  |---|---|---|---|---|
  | 1 | 857 | .773 | .076 | 1.240 / 1.420 |
  | 2 | 2,227 | .818 | .066 | 1.558 / 2.129 |
  | 3+ | 757 | .861 | .065 | 0.507 / 1.306 |

  Describe what the table shows: τ-b rose and the share of reversed pairs fell from one rating to two and to three or more; the largest range at equal raw mean occurred with two ratings. Keep the descriptive sentence on what the range reflects [ATC-21]. No pooled value. Ranges are "on the GRM score scale", no unit.
- **R15 RQ3b: choice among the models** (@tbl-score-agreement; @tbl-theta-correlations [SUPP]; F2.12, F3.23). Relative to the GRM: M1 *r* = .978, ρ = .980, .188 of products changing quintile, mean percentile shift .040; M2 .986 and .984, .155, .032; M3 .996 and .997, .073, .016. Among the ladder models Pearson .982 to .993 and Spearman .985 to .996; M1 grid check 1.000.
- **R16 RQ3b: reliability by model (new; Decision 3)** (@tbl-marginal-reliability-models [SUPP]; F3.24). Empirical reliability of the scores .663 (M1), .669 (M2), .682 (M3) and .695 (GRM); no test of these differences; latent variances not quoted.
- **R17 Problems and pointer (draft 7 line 212, kept).** No confidence intervals for the agreement statistics; the M1–GRM contrast combines constraints and link; the comparisons show that scores differ, not which is more accurate.

### 4 Discussion (discussion model: revisit → map → contribution and implications → limitations and future; **interprets, does not restate**, C4; every interpretive claim [ATC]; "in these data", "in this rater pool")

**No opening summary paragraph** (draft 7 line 220 is deleted). Each RQ subsection opens with the answer in one sentence, which is the model's "revisit" move, and then interprets.

**4.1 RQ1: Reliability and the number of ratings per action (D1–D3; draft 7 lines 224–230)** [ATC-3, ATC-4, ATC-5, ATC-32, ATC-35, ATC-36, ATC-45, ATC-31]
- **D1 Answer, then the sharp point (C4) [ATC-45, ATC-3, ATC-36].** Answer sentence: the obtained scores were far less reliable than the panel (.695 against .970), and four ratings per action were needed for .80. Interpretation: the gap is a property of the design, not of the raters. With the same raters and the same fitted parameters, simulated reliability was .691 for the actual assignment and .837 once every action had four ratings (top-up simulation), and it reached .928 with 10 ratings per action (projection); the full-panel figure describes a product that every rater rated, which no product was. Spearman–Brown explanation in one sentence (amabile1982). What the raters contribute is the level at a given number of ratings: single ratings agreed at Krippendorff's α = .402 while the pairwise Cronbach's α was .959, the pattern kaufman2008a describe and the consistency–agreement distinction (stefanic2015; cseh2019) [FI-17]. No restatement of the simulation procedure; "under the assumptions stated in the Method".
- **D2 Observed and simulated figures [ATC-4, ATC-5, ATC-32].** One or two ratings give limited precision for single action scores (.526, .703). The observed means reach .80 at four ratings (.815, 93 products) as the simulation does; from three ratings on they lie at or below the simulated range except at nine. Possible readings, as possibilities only: different quantities; products with several ratings were rated by particular raters, not by random draws [FI-4]; small rows. By-n values are observational; precision also differs within the same number of ratings and along θ.
- **D3 Mapping with target and object (draft 7 line 230, shortened) [ATC-31].** Four ratings for .80 in product-level scores from this pool, beside two or three trained raters for divergent-thinking responses at the person level (relative G ≥ .80; silvia2008), 10 novices not reaching an adequate alpha for expert-domain products where 10 experts did (kaufman2008a; kaufman2013), and 7 to 15 non-experts for fashion and design products (ICC .70; barth2021; terai2026). Sport panels of three or four raters (kempe2018; joode2023; memmert2010; roca2018, with the m8-2 hedge) rated every product, so their figures are panel figures; whether coaches need fewer ratings is untested here.

**4.2 RQ2: Raters differ (D4–D5; draft 7 lines 234–236)** [ATC-6, ATC-12, ATC-16, ATC-38]
- **D4 Answer and size.** Answer sentence: raters differed in severity, scale use, discrimination and information, and for raters with about 50 ratings these differences were imprecisely estimated. Severity span 2.388 logits (R19 to R06), larger than the ranges of primi2019 (−1.18 to .64; about 0.9), only indicatively comparable [ATC-38; FI-17]; severity of this size confounds raw means when raters rate different actions (primi2019; hass2018). Discrimination differences exceed the standard errors for raters with many ratings (R09 0.95, *SE* 0.15, against R06 3.15, *SE* 0.45); high discrimination is not confined to imprecisely estimated raters (R06, R25 and R12 had 520, 138 and 264 ratings), so the spread is not mainly estimation noise [ATC-6]. Imprecision: the largest standard errors belong to R18 for its thresholds and to R26, R27 and R30 for their discriminations; R27 and R30 had 47 ratings, R26 had 136, so a larger number of ratings did not by itself give a precise discrimination estimate here [ATC-16]. Information shares are not a ranking of rater quality; read literally, one rating by the most informative rater (3.96) carries as much information as several by the least informative (0.13), but the former's interval runs from 0.66 to 8.40 [ATC-12].
- **D5 Scale use and literature (draft 7 line 236, kept, shortened).** Raw response styles carry the model-independent evidence on scale use; eight raters never used the top category; R27's gap. long2015; engelhard1994; myford2003; myford2004; myszkowski2021 (central vs extreme responding, e.g., R13 vs R06); primi2019; hickey2001; storme2014; ceh2022; wind2018; wind2019; reise1990 [FI-17].
- **Optional product-class link (C4) [ATC-47]:** see D9.

**4.3 RQ3: Constraints and consequences for scoring (D6–D8; draft 7 lines 240–244)** [ATC-7, ATC-8, ATC-9, ATC-10, ATC-15, ATC-21, ATC-22, ATC-34, ATC-46]
- **D6 Answer and main point first (C4) [ATC-46].** Answer sentence: the Rasch-family constraints were rejected by the LR tests and AIC but not by BIC, and the choice among the four models changed the ordering of actions far less than the choice between a model and the raw mean. Evidence: the model scores correlate at Spearman ρ = .980 to .997 with the GRM scores, and the empirical reliability of the scores is similar across the models (.663 to .695), whereas raw means and GRM scores agree at τ-b = .773 to .861 within groups of equal numbers of ratings, with .065 to .076 of pairs in reversed order and products with the same raw mean up to 2.129 apart on the GRM score scale. **Two caveats in the same paragraph:** (a) the raw mean was compared with the GRM scores only, and τ-b on a heavily tied score is not the same statistic as Spearman's ρ, so the contrast is indicative (see Evidence gaps 1); (b) none of this shows that model-based scores are more accurate; the GRM is not a validated criterion [ATC-15, ATC-22]. With one rating a product's GRM score depends only on that rating and the rater's parameters, which is where agreement with the raw mean was lowest (.773; .076) [ATC-21]. Reversals matter wherever actions are selected or ranked.
- **D7 The constraints (B1, B7) [ATC-7, ATC-34, ATC-9, ATC-8].** The shared category structure concerns M1 only (eckes2015); equal discrimination is shared by the whole Rasch family. The criteria disagree: LR tests and AIC reject both constraints; BIC is lowest for M1, and the GRM, with 165 parameters against 31, lies 0.416 above it, a practical tie. Possible explanation, as a hypothesis: the BIC penalty grows with the number of parameters (31, 141, 165, 165), which weighs against rater-specific parameters within the ladder; that the GRM nevertheless matches M1 on BIC shows how much better it fits. M3 discriminations from 0.298 to 3.056 (ratio 10.254). **Misfit-as-discrimination illustration, one metric (the M3 discriminations of F3.20 against the M1 fit values of F3.22):** the three raters with the lowest M3 discriminations, R18 (0.298), R09 (0.316) and R17 (0.775), had M1 infit and outfit above 1; the two raters with the highest M3 discriminations, R26 (3.056) and R12 (2.421), had the two lowest M1 infit values (0.366 and 0.259). Two cases do not fit: R30 (M3 discrimination 1.307, above the median of 1.213) also had M1 infit and outfit above 1 (1.136, 1.051), and R11 (M3 discrimination 0.990) had an M1 infit just above 1 (1.011) with an outfit below it (0.954). The account is therefore illustrative (myford2004; myszkowski2021). Step order is not evidence for either family (andrich1978; bond2020). GRM: lowest AIC and SABIC, tied on BIC; cumulative link plausible for a unipolar scale; pellegrino2025 retained a GRM. The cross-software caveat stands.
- **D8 Model choice in detail [ATC-10].** Quintile changes .188 (M1; mean percentile shift .040) and .073 (M3; .016) although all correlations with the GRM are .978 or higher; a quintile change can be a small move across a boundary; the M1–GRM contrast mixes constraints and link.

**4.4 Designing creativity-rating studies for nonverbal, time-pressured products (D9–D10 and box; draft 7 lines 248–257)** [ATC-30, ATC-31, ATC-43, ATC-14, ATC-16, ATC-23, ATC-57, ATC-47]
- **D9 Scope and argument (rewritten; no "five points").** Scope: one rater pool, one 7-point scale, one product class [FI-21]. Then two interpretive points that the box cannot carry. (a) The number of ratings needed could not have been read off the existing evidence, and the figure found here differs from the published ones for reasons these data cannot separate (domain, rater pool, scale, target, object); to our knowledge these are the first rating-design figures for football actions; evidence has to be collected, not assumed (cseh2019; vanhooijdonk2022; long2022 with the m8-1 wording) [ATC-31, ATC-43]. M7-1 wording stays. (b) In a pool-based sparse design the design decision is the number of ratings per action and the linking of raters, not the size of a panel; with single ratings agreeing weakly and raters differing strongly, panels of three or four raters without a rater model would carry unquantified rater effects in such a pool [ATC-30]. **Optional product-class link [ATC-47]:** categories 1 and 2 were the most frequent and category 7 the rarest (2,278, 2,501 and 149 of 9,831 ratings), and eight raters never used category 7; one hedged sentence that this is the pattern to expect if creative actions are rare in competition, and that scales for such products then separate actions mainly at their upper end. Use only if the author confirms and a source is supplied (Evidence gaps 2); otherwise the domain-specificity hedge of draft 7 stands alone.
- **D10 Calibration set and the standards link.** A common calibration set is distinct from rater training (hennessey2011; dollinger2005; storme2014) [ATC-14]. Recommendation 1 is tied back to the Introduction: reporting the reliability of the scores actually used, and what each index refers to, is an instance of the transparency that barbot2019 call for [ATC-57; FI-17]. Then: "The six recommendations are summarised in the box."
- **Box "Design recommendations for creativity ratings of actions in sport" (six items; the prose announces six; every item [ATC-23]; whether CRJ accepts boxes is FI-16):**
  1. Report the reliability of the scores actually used and the agreement of single ratings, not only alpha or full-panel values (@tbl-reliability-overview: .695 against .959 and .970; Krippendorff's alpha .402) [ATC-3, ATC-36, ATC-57].
  2. Plan the number of ratings per action with the precision of single scores in mind: one or two ratings gave .526 and .703 here; in this rater pool the smallest number of ratings at which simulated reliability reached .80 was four (@tbl-grm-reliability-by-n; @fig-grm-reliability-observed-vs-simulated) [ATC-5, ATC-35].
  3. Let all raters rate a sufficiently large common calibration set (the present design was connected; [\[FILL IN: confirm that no set of actions was rated by all raters; the largest fully crossed block comprised three raters and 270 actions (FI-4)\]]{.mark}) [ATC-14, ATC-18]. No rater IDs.
  4. Give each rater enough ratings for stable parameters; about 50 ratings per rater left them imprecise here, and the least precise discrimination belonged to a rater with 136 ratings (@tbl-grm-rater-parameters) [ATC-16].
  5. Consider scoring with a model that adjusts for rater differences, under its assumptions, and report how far its ordering departs from the raw mean (@fig-m1-rater-severity; @tbl-raw-mean-vs-grm); the choice among such models mattered less here than the choice to model; this study does not show that model-based scores are more accurate [ATC-15, ATC-22, ATC-46].
  6. Treat these figures as specific to this product class, rater pool and scale [ATC-31].

**4.5 Limitations and future research (D11–D19; draft 7 lines 261–275)**
- L1 Design and missingness: incomplete design, allocation [FI-4, FI-31]; ignorable missingness assumed; "not recognised" ratings removed [FI-22]; by-n reliabilities observational.
- L2 Simulations **(shortened, C4):** refer to the Method for the procedure; state only the consequences: equal-probability draws do not reproduce workloads; parameters treated as known, so the ranges omit parameter uncertainty; all ratings generated from the fitted GRM with θ ~ N(0, 1), so the simulations presuppose the model; one to 10 ratings only; no selected or workload-weighted rater sets. A figure for this pool under these assumptions [ATC-35].
- L3 Fit evidence limited [ATC-11, ATC-33]: S-X² conservative, C2 not computable, Q3 biased without reference distribution, flags below 0.7 expected; absence of detected misfit is not evidence of fit. **B1:** the GRM had the lowest AIC and SABIC and was tied with M1 on BIC; it is not a validated reference.
- L4 Model comparison [ATC-34, ATC-41]: BIC disagrees with the LR tests and AIC on both constraints; explanation a hypothesis; M1–M2 cross-software with 110 degrees of freedom against the formula value of 120; M1–GRM mixes constraints and link.
- L5 Uncertainty and assumptions: raters with about 50 ratings imprecise (R17, R18, R27, R30), and R26's discrimination as well; intervals conditional on valid draws; normal latent distribution although ratings concentrate in the low categories; response styles and agreement statistics without intervals; R27's thresholds not comparable.
- L6 Rater pool **(D; worded to stay true for an open pool) [ATC-55]:** the raters came from two pools [FI-1, FI-21, FI-31]; they were not selected for football expertise, and whether they meet the CAT's requirement of domain familiarity was not established; expertise not analysed (kaufman2009; kaufman2013; ceh2022; hickey2001). No mention of future recruitment.
- L7 Rater exclusion **(cross-reference only, C4) [ATC-26]:** technical criterion [FI-23]; the refit with the excluded raters left the product scores virtually unchanged (see Model adequacy); no numbers repeated, or at most *r* = .99997.
- L8 Two facets, one dimension: no time or session facet (barth2021; terai2026; leckie2011; myford2009; forthmann2017); no differential rater functioning (wind2019a); patz2002; uto2020.
- Future research (compact): severity test on its own; M1–M2 within one package; held-out predictive check of model-based against raw-mean scores; a like-for-like comparison of the raw mean with every model; projections with parameter uncertainty and selected rater sets; a prospective calibration-set design; rater covariates incl. football expertise and coach panels; other sports and other nonverbal, time-pressured products; a G- and D-study of the same data. Closing sentence of draft 7 line 275 kept [ATC-30, ATC-31].

### 5 Conclusion (1 paragraph, 150–200 words; "action") [ATC-1]

- In these data: empirical reliability of the obtained scores .695 against panel figures of .959 and .970, a gap that belongs to the design; one or two ratings per action gave limited precision (.526, .703); the smallest number of ratings at which simulated reliability reached .80 was four. Raters differed in severity, scale use, discrimination and information. The constraints were rejected by the LR tests and AIC but not by BIC; the models ordered actions almost identically, the raw mean did not.
- Close: rating-design figures from verbal or static material cannot be assumed to hold; they have to be collected for the product class and rater pool at hand; report the reliability of the scores used, plan several ratings per action, link raters, consider rater-adjusting models; whether such scores are more accurate remains to be examined [ATC-5, ATC-14, ATC-15, ATC-30, ATC-31, ATC-45, ATC-46].

### References
APA 7th via CSL; `/home/max/drive/phd_library.bib` only; YAML, filters and `citeproc: false` unchanged.

### Supplementary Material
Sections and order in the placement table below. The note of draft 7 line 336 is cut to a pointer (C4): two or three sentences that say what the three tables and the figure of the section show and refer to the Method for the procedure. Lead sentence of draft 7 line 288 stays.

---

## Placement of all 53 labels

**MAIN 13 (7 tables, 6 figures) · SUPP 37 (23 tables, 14 figures) · not embedded 3.** Every embedded label is referenced in the prose at the place named.

### Main text (13)

| # | Label | Notebook | Embedded after | Referenced in |
|---|---|---|---|---|
| 1 | `tbl-design-summary` | NB02 | M10 | M10, R0 |
| 2 | `tbl-reliability-overview` | NB03 | R2 | R2, R5, box 1 |
| 3 | `tbl-grm-reliability-by-n` | NB02 | R3 | M18, R3, box 2 |
| 4 | `fig-grm-reliability-observed-vs-simulated` | NB02 | R4 | M20, R4, box 2 |
| 5 | `fig-category-usage-shares` | NB02 | R7 | M10, R7 |
| 6 | `fig-m1-rater-severity` | NB02 | R8 | M21, R8, box 5 |
| 7 | `tbl-grm-rater-parameters` | NB02 | R9 | M2, M21, R9, box 4 |
| 8 | `fig-grm-rater-discrimination-ci` | NB02 | R10 | M21, R10 |
| 9 | `fig-grm-rater-information-ci` | NB02 | R11 | M21, R11 |
| 10 | `tbl-model-fit` | NB02 | R12 | M14, R12 |
| 11 | `tbl-raw-mean-vs-grm` | NB02 | R14 | R14, box 5 |
| 12 | `fig-raw-mean-vs-theta` | NB02 | R14 | R14 |
| 13 | `tbl-score-agreement` | NB02 | R15 | R15 |

### Supplement (37)

| Section | Label | Notebook | Referenced in |
|---|---|---|---|
| Data, design and rater exclusion | `tbl-excluded-raters` | NB03 | M9 |
| | `tbl-sensitivity-rater-exclusion` | NB03 | R1 |
| | `fig-design-ratings-per-product` | NB03 | M7 |
| | `fig-overview-degree-distributions` | NB01 | M7 |
| | `fig-overview-rater-overlap` **(new embed)** | NB01 | M7, M19 |
| | `tbl-category-usage` | NB03 | M10, M15 |
| | `fig-overview-rating-distribution` | NB01 | R7 |
| | `tbl-overview-rater-response-styles` | NB01 | M21, R7, D5 |
| | `fig-overview-rater-response-styles` | NB01 | R7 |
| Estimation and fit of the graded response model | `tbl-grm-convergence` | NB03 | M14, R1 |
| | `tbl-grm-rater-fit` | NB03 | R1 |
| | `tbl-grm-q3-flagged` | NB03 | R1 |
| Reliability (observed) | `fig-grm-rel-post-by-n` | NB03 | R3 |
| | `tbl-grm-reliability-ci` | NB03 | R2 |
| | `tbl-grm-reliability-summary` | NB03 | R6 |
| | `tbl-naive-indices` | NB03 | R2 |
| | `fig-grm-rel-post-histogram` | NB03 | R6 |
| | `fig-grm-rel-post-by-theta` | NB03 | R6 |
| | `fig-grm-rel-consistency` | NB03 | R6 |
| | `fig-grm-panel-information` | NB03 | R2 |
| Simulated reliability by number of ratings | `tbl-grm-reliability-projection` | NB03 | R4 |
| | `fig-grm-reliability-projection` | NB03 | R4 |
| | `tbl-grm-reliability-observed-vs-simulated` | NB03 | M20, R4 |
| | `tbl-grm-reliability-min-ratings` **(from main)** | NB03 | R5 |
| Rater parameters, information and category use | `tbl-rater-overview` **(from main)** | NB03 | M16, M21, R1, R8 |
| | `fig-grm-category-response-functions` | NB02 | R9 |
| | `tbl-grm-rater-information-ci` | NB03 | M21, R11 |
| | `fig-grm-rater-information` | NB02 | R11 |
| | `fig-grm-information-shares` | NB03 | R11 |
| | `tbl-grm-information-summary` | NB03 | M21, R11 |
| Adjacent-category ladder and model scores | `tbl-lr-tests` | NB03 | R12 |
| | `tbl-discrimination-m3` | NB03 | R13, D7 |
| | `tbl-discrimination-summary` | NB03 | R13 |
| | `tbl-threshold-order` | NB03 | R13 |
| | `tbl-rater-fit-m1` | NB03 | R13, D7 |
| | `tbl-theta-correlations` | NB03 | R15 |
| | `tbl-marginal-reliability-models` **(new embed)** | NB03 | M22, R16 |

### Not embedded (3)

| Label | Reason |
|---|---|
| `tbl-cleaning-log` (NB00) | Headers and step values are code names and NB00 may not be re-run; all five steps are stated in M8 from F0.2. |
| `tbl-overview-ratings-per-action` (NB01) | Duplicates `tbl-design-summary` and `fig-design-ratings-per-product`; code-name row labels. |
| `tbl-grm-global-fit` (NB03) | A single row saying "not computable"; M16 says the same with the count (23 of 300). |

### Reasons for the moves

- **`tbl-grm-reliability-min-ratings` → SUPP.** Its headline row is now a row of `tbl-reliability-overview` (.837, range, pairs added), the figure shows the value as a reference line, and R5 quotes both rows; it sits in the supplementary notebook.
- **`tbl-rater-overview` → SUPP, `fig-grm-rater-information-ci` → MAIN.** This follows the notebook split. The main text then has one object per facet of RQ2 (scale use, severity, thresholds and discrimination, information); the overview table (25 rows by 8 columns, overlapping three main objects) becomes the look-up table in the supplement.
- **`tbl-reliability-overview` stays MAIN** although it sits in the supplementary notebook: it is the table behind recommendation 1 and the abstract's contrast of indices (Decision 2).
- **`fig-grm-category-response-functions` and `fig-grm-rater-information` stay SUPP** although they sit in the main notebook: 25 small panels and 25 lines in one panel are not legible at journal width, and they would raise the main text to 15 objects (Decision 1).
- **`tbl-model-fit`** moves from the former "Scoring model" section to R12 (C3).

### Notes for the writer

- Embed lines for the two new supplement objects and for every label are in `02_artifacts.md`. `fig-overview-rater-overlap` is in notebook 01, `tbl-marginal-reliability-models` in notebook 03.
- 50 embeds, each exactly once: 13 in the main text, 37 in the supplement.
- Display items for the analyst (FI-18, unchanged in kind): code-name headers and row labels (`tbl-grm-reliability-by-n`, `tbl-grm-reliability-projection`, `tbl-grm-reliability-min-ratings`, `tbl-grm-reliability-observed-vs-simulated`, `tbl-grm-reliability-summary`, `tbl-discrimination-summary`, `tbl-marginal-reliability-models`, `tbl-sensitivity-rater-exclusion`, `tbl-design-summary`); `tbl-sensitivity-rater-exclusion` lists R29 twice; `tbl-rater-overview` prints 0.70 with a flag for R15 and R01; `fig-m1-rater-severity` colours not explained in the caption; `tbl-lr-tests` caption says only "end categories"; `tbl-reliability-overview` has a long note column and code-style row labels, which matters more now that it is the main RQ1 table.

---

## Change map: draft 7 → revision (by line of `manuscript.qmd`)

Reason codes: **N** new number; **B1–B9** changed meaning (brief section B); **C1–C7** storytelling directive; **D** author fact; **S** stale string; **R8** open point of review round 8; **P** placement.

| Line | Passage | Change | Reason |
|---|---|---|---|
| 2–7 | Title, YAML | None. | brief E |
| 9 | Abstract | 24 → 25 raters; 9,046 → 9,831; 3,669 → 3,841; .689 → .695; .969 → .970; .522 → .526; .699 → .703. Add Krippendorff .402 vs Cronbach .959 and the τ-b clause (.773, .818; .076, .066); add span 2.388 if space; cut the category-use parenthesis. BIC clause re-checked and kept. "have been studied" (m8-9). | S, N, C5, B1, R8 |
| 36 | Intro P1 | Split into P1 (motivation, stein1953 + runco2012, barbot2019) and P2 (rhodes1961, batey2012 placement, barbot2019b, CAT, terminology). | C1 |
| 40 | Aggregation | Kept. | — |
| 42 | Evidence paragraph | Split into P4a (person-level) and P4b (product-level); kaufman2007 described as captions rated by graduate students (m8-3); practice sentences and "located none" move to P5. | C1, R8 |
| 44 | Conclusion of move 2 | Receives the practice sentences; otherwise kept. | C1 |
| 48–52 | Verbal bias, football actions, sport gap | Kept; no percentages added. | C7 |
| 56–60 | Methods ladder | Kept; spelled-out model names, no M-labels before the Method gloss. | C6 |
| 64 | Present study | "24 raters" → 25; pool-based sparse design and the reframed question added. | S, C1 |
| 66–68 | RQs | Wording kept. | — |
| 70 | Analytic route | Cut to one or two sentences; followed by the new contributions paragraph P14. | C2 |
| 76 | Overview | Kept (FI-1, FI-15). | — |
| 80 | Raters | Two pools: R01–R19; R23–R27 and R30. "24 raters" → 25; "R23 to R27" → with R30; "four raters were excluded" → five; "46 and 1,174" → 47 and 1,174. FI-31 placeholder updated to name R30. | S, D, B9 |
| 84 | Products | Material fact written in; FI-2 reduced. | D |
| 88 | Rating procedure | Rewritten as M4–M6: app, verbatim definition block, endpoint labels (replaces "anchors at 1, 4 and 7"), scale-choice sentence, other dimensions with the amabile1982 rationale. The two malformed placeholders disappear; remaining placeholders in correct syntax. | D, S, brief E |
| 92 | Rating design | Counts per number of ratings: 857, 2,227, 73, 93, 143, 185, 124, 77, 25, 22, 8, 5, 1, 1 (up to 14). FI-4 reworded without "latest collection". Reference to `fig-overview-rater-overlap` added. | N, B9, P |
| 96 | Cleaning | 10,447 → 11,323; 1,347 → 1,432; 21 pairs / 22 rows → 26 pairs / 27 rows; 9,077 by 28 → 9,863 by 30. | S, B9 |
| 98 | Exclusion | Adds R29 (1); 31 → 32 ratings. **Sensitivity sentence removed here** (numbers once, in R1). | S, B9, C4 |
| 100 | Final data | 9,831 / 3,841 / 25; 2.559; range 1–14; 1.819; 857; .102; 23 of 300; 22.5. Category use unchanged. | S, B9 |
| 106–110 | Models | One-time gloss of M1, M2, M3, GRM in the ladder paragraph. | C6 |
| 112 | Scoring model | Adds the reason for the GRM and the forward reference to RQ3; "436 iterations" leaves the Method (550 in R1). | C3, N |
| 116 | Model comparison | 105 → 110; 115 → 120. | S, B7 |
| 120 | Model adequacy | 222 of 276 → 256 of 300; 30 of 276 → 23 of 300. `tbl-rater-overview` now a supplement reference. | N, B9, P |
| 124 | Reliability definitions | 43 → 53 rejected draws; the two reliability names introduced. | N, C6 |
| 128 | Conventional indices | FI-9: six → seven raters (adds R17); 647 / 353 → 513 / 487. No crossed-block IDs. | B6, N |
| 130 | Simulations | Kept as the single full statement; "simulated reliability" named. | C4, C6 |
| 134 | Rater parameters | Object references updated (overview table and information table in the supplement, information figure in the main text). | P |
| 138 | Score agreement and sensitivity | "all 28 raters" → all raters who could be estimated (29); per-model reliability added. | S, B8 |
| 142 | Software | Kept; app repository may be named under FI-15. | D |
| 146 | Results lead | "We first report the scoring model" → model adequacy. | C3 |
| 148–152 | "Scoring model" | Section replaced by "Model adequacy" (R1): 550 iterations; *p* .362–.601; infit 0.315–0.983, outfit 0.303–0.973; 14 flagged; Q3 −.188, 256 pairs, 36 flagged, R17–R24 instead of R10–R11. **All information criteria move to R12; the `tbl-model-fit` embed moves to RQ3.** "4.161", "27,258.550", "28,235.202", "28,239.363", "158", "49.381" removed. | C3, B1, S, N |
| 156 | Reliability overview | .695 [.673, .711]; .970 [.966, .973], grid .970; α .959 [.931, .970], 1,948 products, 513 of 1,000; block .785 [.736, .823], 270 products; Krippendorff .402 [.375, .427], 25 raters, 2,984 products. | S, N, B6 |
| 160 | Observed by number of ratings | .526 (857), .703 (2,227), .770 (73), .815 (93); to .955 at 14; **one** exception (.915 at 10 after .917 at nine); PSD 0.683 to 0.211, equal at nine and 10; rows on 22, 8, 5, 1, 1 products; .970. | S, B5 |
| 164 | Simulated by number of ratings | .526 [.511, .538]; .702 [.691, .712]; .785 [.776, .793]; .832 [.825, .838]; .928 [.925, .932]. Inside at one, two, nine; below at three, four, five, seven, eight, 10; at the lower bound at six. | N, B5 |
| 168–170 | Top-up | .691 [.684, .699], rel~post~ .693, observed .695; .837 [.832, .842]; 7,098 pairs, 3,157 products, 16,929. Embed moves to the supplement; no procedure restated. | S, N, P, C4 |
| 172 | Distribution | .706; .195; .601 and .796; .071 to .955; 274. | N |
| 176 | Response styles | 4.012 (R19) replaces 3.836 (R18); 1.841 (R02) replaces 1.953 (R19); .064 replaces .080; 2,278, 2,501, 149. | N, B2 |
| 180 | Severity | −1.005 (0.059, R19); 1.383 (0.058); 2.388. R18 illustration replaced by R14. "13 … and 11" dropped. | S, B2 |
| 182 | Embed `tbl-rater-overview` | Moves to the supplement. | P |
| 186 | Thresholds | "all 24 raters" → 25; −6.39 (2.92); 0.24; −3.43 (0.49); −0.68 to 2.02; −3.43 to 4.39. | S, N |
| 190 | Discrimination | Rewritten: 0.65 (R18, 0.26) to 4.17 (R26, 136 ratings, 1.49); R06 3.15, R25 3.03, R12 2.91, R27 2.85; R09 0.95; largest SEs R26, R27, R30. R26 and R24 no longer low-count; "46 ratings" gone. | S, B3 |
| 194 | Information | 0.13 [0.00, 0.37] to 3.96 [0.66, 8.40]; shares to .112 [.021, .205]; R09 0.29, R01 0.84, R02 1.83; widest R26, R27, R30; maxima 2.850, 2.550, 2.300; R06 .078 at θ = 2; R12 .151, R24 .107, R15 .105 at θ = −2. New main embed `fig-grm-rater-information-ci`. | S, N, B3, P |
| 198 | LR tests | χ²(110) = 878.581; χ²(24) = 177.440; AIC and BIC values per model; **GRM comparison and the BIC tie added here**; `tbl-model-fit` embedded here. | S, B1, B7, C3 |
| 200 | Ladder detail | 0.298 to 3.056 (R26 replaces R27), 1.213, 10.254, 0.634; M1 values above 1 for R09, R17, R18, R30 and R11 (infit only). | N, B7 |
| 202 | Raw mean vs GRM | 857: .773, .076, 1.240, 1.420; 2,227: .818, .066, 1.558, 2.129; 757: .861, .065, 0.507, 1.306. | S, B4 |
| 208 | Model choice | .978/.980, .188, .040; .986/.984, .155, .032; .996/.997, .073, .016; .982–.993; .985–.996. New sentence R16 on reliability per model. | N, P |
| 212 | Problems | Kept. | — |
| 214–216 | "Sensitivity" section | Heading removed; numbers move to R1 with the new values (29 raters; 9,862; 3,842; .69490, .69453; .97008, .97207; .99997; 0.00187; 0.16518; .00364; 25; .99796; 0.21451). | S, B8, C4 |
| 220 | Discussion summary | **Deleted.** | C4 |
| 224 | RQ1, indices | Rewritten as D1 around "a property of the design"; .695, .970, .959, .402; Spearman–Brown in one sentence. | C4, S |
| 226 | RQ1, observed | .526, .703; one dip (10 ratings, 22 products); .815 at four. | S, B5 |
| 228 | RQ1, simulations | .832, .837; no assumption list (reference to Method); k list per B5; "the lower dashed line" (m8-8). | C4, S, B5, R8 |
| 230 | RQ1, mapping | Shortened; kept with targets and objects. | — |
| 234 | RQ2 | 2.388, R19 to R06; R09 0.95 vs R06 3.15; largest SEs R18 (thresholds), R26, R27, R30; R06, R25, R12 with 520, 138, 264 ratings; 3.96 and 0.13, interval 0.66 to 8.40. "46–55" and R24 as lenient extreme gone. | S, B2, B3 |
| 236 | RQ2, literature | Kept, shortened. | C4 |
| 240 | RQ3, constraints | Opens with the answer and the modelling-vs-averaging point (D6) in a new first paragraph; BIC tie; parameter counts 31, 141, 165, 165; M3 0.298 to 3.056, 10.254; misfit illustration in the M3 metric with R18 0.298, R09 0.316, R17 0.775 (M1 values above 1) and R26 3.056, R12 2.421 (lowest M1 infit), and the two cases that do not fit (R30, R11); GRM discriminations no longer needed. | B1, B7, C4 |
| 242 | RQ3, raw means | The sentence explaining more reversals with two ratings than with one is removed; describe .076 with one rating as the lowest agreement; 1.240 / 1.420. | B4 |
| 244 | RQ3, model choice | .978; .188 (.040); .073 (.016). | N |
| 248 | Design argument | "Five points follow" removed; rewritten as D9–D10; Krippendorff .402; raters with about 50 ratings R17, R18, R27, R30; barbot2019 link. | C4, C1, S, B3 |
| 250–257 | Box | Six items announced as six; item 1 .695, .959, .970, .402; item 2 .526, .703; item 3 270 actions, no IDs; item 4 adds the 136-rating case; item 5 adds the modelling-vs-averaging clause. | C4, S, B6, B3 |
| 261 | L1 | Kept. | — |
| 263 | L2 | Shortened to consequences; procedure by reference. | C4 |
| 265 | L3 | "BIC favoured M1" → tied with M1 on BIC. | B1 |
| 267 | L4 | 105 → 110; 115 → 120. | S, B7 |
| 269 | L5 | Names R17, R18, R27, R30 and R26. | B3 |
| 271 | L6, L7 | L6 reworded (two pools; not selected for expertise). L7 cross-reference; "0.35026" and ".99994" removed. | D, S, B8, C4 |
| 273–275 | L8, future | Kept; one item added (like-for-like raw-mean comparison). | — |
| 279 | Conclusion | .695; .959; .970; .526; .703; BIC wording; design point; models vs raw mean. | S, B1, C4 |
| 288–332 | Supplement, first three sections | `fig-overview-rater-overlap` added. | P |
| 334–342 | Supplement, simulations | Note cut to a pointer; `tbl-grm-reliability-min-ratings` added. | C4, P |
| 344–356 | Supplement, raters | `tbl-rater-overview` added; `fig-grm-rater-information-ci` removed (now main). | P |
| 358–370 | Supplement, ladder | `tbl-marginal-reliability-models` added; heading "Adjacent-category ladder and model scores". | P |

### Stale strings (brief section B): where they occur in draft 7 and what replaces them

| String | Lines | Replacement |
|---|---|---|
| `9,046` | 9, 100 | 9,831 |
| `3,669` | 9, 100, 216 | 3,841 |
| `24 raters` | 9, 64, 80, 100, 186, 216 ("24 common raters") | 25 |
| `10,447` | 96 | 11,323 |
| `1,347` | 96 | 1,432 |
| `9,077` | 96, 216 | 9,863 (cleaning); 9,862 (refit) |
| `28 raters` | 96, 138, 216 | 30 raters (cleaning); 29 raters (refit) |
| `.689` | 9, 156, 168, 224, 251, 279 | .695 |
| `.969` | 9, 156, 160, 224, 251, 279 | .970 |
| `.949` | 156, 224, 251, 279 | .959 |
| `.750` | 156 | .785 |
| `.391` | 156, 224, 248, 251 | .402 |
| `.522` | 9, 160, 226, 252, 279 | .526 |
| `.699` | 9, 160, 226, 252, 279 | .703 |
| `.756` | 160 | .770 |
| `4.161` | 150, 220 | 0.416, with tie wording |
| `840.447` | 198 | 878.581 |
| `156.593` | 198 | 177.440 |
| `(105)` | 116, 198; "105 degrees" 267 | 110 |
| `(23)` | 198 | (24) |
| `2.247` | 180, 234 | 2.388 |
| `3.19` | 190 | 4.17 |
| `2.52` | 194, 234 | 3.96 |
| `.833` | 202 | .773 |
| `.041` | 202, 242 | .076 |
| `.849` | 202 | .861 |
| `0.35026` | 98, 216, 271 | 0.16518 (R1 only) |
| `.99994` | 98, 216, 271 | .99997 |
| `261` | 156, 253 | 270 |
| `27,258` | 150 | 29,585.612 |
| `28,235` | 150, 198 | 30,617.021 |
| `28,239` | 150 | 30,617.437 |
| `6,778` | 168 | 7,098 |
| `3,007` | 168 | 3,157 |
| `15,824` | 168 | 16,929 |
| `.835` | 168, 228 | .837 |
| `.686` | 168 | .691 |
| `R23 to R27` / `R23–R27` | 80 (three times) | R23–R27 and R30 |
| `four raters` (excluded) | 80 | five raters |
| `46 ratings` / "46 and" / "46–55" | 80, 190, 234 | 47 (R27, R30); R26 has 136 |
| `R24` as the most lenient rater | 180, 234 | R19 |
| `anchors at 1, 4 and 7` | 88 | labels at the endpoints only |

Further stale values found outside the brief's list, all covered in the change map: 436; 115; 222 of 276; 30 of 276; 43 draws; 647 and 353; 1,946; 2,837; 832, 2,107, 68, 730; 2.466; 1.806; .103; 31 ratings; 21 pairs and 22 rows; .328–.665; 15 flagged; −.202; 28 pairs; R10–R11; 3.836; 1.953; .080; 2,179; 2,355; 128; 7.277; 2.221; 158, 135, 30; .206; .081; 49.381; 3,670. Legitimate after the revision: ".928" (simulated reliability at 10 ratings).

---

## FILL IN items

**Open (15):**
- **FI-1** Larger project; ethics approval and consent; recruitment and number of raters at the start of the first pool.
- **FI-2 (reduced by D)** Action-selection rule, clip length, video source, number of matches.
- **FI-4** Allocation of products to raters in both pools; planned overlap or common set; how products came to have their number of ratings; whether products with different numbers of ratings were rated by different raters. Also box item 3 (no set rated by all raters; crossed block of three raters and 270 actions).
- **FI-6** Versions of R, mirt, sirt, psych; name and version of the Krippendorff package.
- **FI-9 (updated, B6)** Why seven raters (R26, R12, R19, R14, R02, R27, R17) were not usable for the pairwise alpha; which three raters form the crossed block. The IDs are not printed by any notebook: either the author supplies them here or the analyst adds them to the notebook; until then no IDs in the text.
- **FI-15** Preregistration; data and code availability (the app repository may be named).
- **FI-16** CRJ requirements: abstract limit, word count, number of main objects (13), supplement policy, boxes, heading format, masked review.
- **FI-17** Citation checks against the PDFs. New items: rhodes1961 (four Ps); batey2012 (the three framework cells); barbot2019 (quotation p. 131; transparency and homogenisation); stein1953; preston2000 and lozano2008 (seven categories); statsbomb2024; amabile1982 (rating further dimensions in a new domain). All items of the 2026-11-09 list stay.
- **FI-18** Display fixes in the notebooks (list in "Notes for the writer"); no placeholder.
- **FI-21** Rater-pool description for both pools.
- **FI-22** Non-recognition rate by rater (and product).
- **FI-23** Rationale for the 15-rating exclusion criterion.
- **FI-31 (updated, D)** Background, recruitment and allocation of the second pool (R23–R27 and R30).
- **FI-32** Data-collection period as a sentence.
- **FI-34 (new, proposed; Decision 17)** Residual procedure details not covered by D: session length and breaks, number of familiarisation clips, language version used by the raters.

**Closed in this revision:** **FI-3** (software, definition, scale labels, "not recognised" option, randomisation, other dimensions: filled by D; residue in FI-34). **Never assigned:** FI-33. **Closed or retired earlier:** FI-5, FI-7, FI-8, FI-10–FI-14, FI-19, FI-20, FI-24–FI-30.

## AUTHOR TO CONFIRM items

**Open (51).** (rw) = reworded for the new findings; new items are ATC-44 to ATC-57.
- **ATC-1 (rw)** Central contribution in four parts; Conclusion.
- **ATC-2** Gap and novelty statements ("we located no …"; "to our knowledge").
- **ATC-3** The empirical reliability of the obtained scores is the figure that matters when scores are used.
- **ATC-4** Precision depends on the number of ratings, the raters and θ.
- **ATC-5** One or two ratings give limited precision; "four" from the simulations under their assumptions.
- **ATC-6** Threshold gloss; spacing partly discrimination; discrimination differences exceed SEs for raters with many ratings.
- **ATC-7** Raw means confounded with severity in incomplete designs; shared category structure concerns M1 only.
- **ATC-8 (rw)** GRM as scoring model: lowest AIC and SABIC, BIC 0.416 above M1 read as a practical tie; cumulative link plausible for a unipolar scale.
- **ATC-9 (rw)** Misfit-as-discrimination illustration in the M3 metric (R18, R09, R17 with M1 values above 1; R26, R12 with the lowest M1 infit), with the two cases that do not fit (R30, R11).
- **ATC-10** Model choice: high correlations, quintile shifts read with percentile shifts.
- **ATC-11** Fit evidence limited; pairwise alpha interval approximate.
- **ATC-12 (rw)** Information shares are not a ranking of rater quality; 3.96 against 0.13 read literally.
- **ATC-14** Calibration set, conditional, distinct from training.
- **ATC-15** "Consider" a rater-adjusting model; no accuracy claim.
- **ATC-16 (rw)** About 50 ratings (R17, R18, R27, R30) left parameters imprecise; R26 with 136 ratings had the least precise discrimination; no number recommended.
- **ATC-18 (rw)** Realised design against any planned common set; crossed block of three raters and 270 actions, no IDs.
- **ATC-19** Showing a definition departs to a minor degree from the CAT rule.
- **ATC-20** Exploratory framing; RQ wording.
- **ATC-21 (rw)** What the range of GRM scores at equal raw mean reflects; with one rating the score depends only on the rating and the rater's parameters.
- **ATC-22 (rw)** Reversals matter for selection; the earlier explanation of more reversals with two ratings is withdrawn.
- **ATC-23** Box: selection and wording of the six items.
- **ATC-26 (rw)** Exclusion sensitivity wording "virtually unchanged" with *r* = .99997 and a largest change of 0.16518 in view (Decision 12).
- **ATC-28** Material-type claim (largely verbal and static), qualitative.
- **ATC-29** Which key carries "divergent thinking in sport".
- **ATC-30** Closing design argument for nonverbal, time-pressured products.
- **ATC-31** Domain-specificity argument and the cross-domain mapping with targets and objects.
- **ATC-32 (rw)** Readings of observed against simulated values: inside the range at one, two and nine ratings, below at three, four, five, seven, eight and 10, at the lower bound at six; observed means reach .80 at four ratings as the simulation does; .691 next to .695.
- **ATC-33** Flags below 0.7 read as expected rather than as misfit.
- **ATC-34 (rw)** BIC explanation (31, 141, 165, 165 parameters) as a hypothesis; the tie of M1 and the GRM.
- **ATC-35** Simulations as RQ1 evidence; the assumption statement incl. "distinct raters" and the workload clause.
- **ATC-36 (rw)** Krippendorff .402 against Cronbach .959 as an illustration of kaufman2008a and of consistency vs agreement.
- **ATC-38 (rw)** Severity span 2.388 logits compared with primi2019.
- **ATC-39** Ecological validity reported as an argument of the cited authors.
- **ATC-40** Cause of non-recognition.
- **ATC-41** Cross-software LR test and nesting judged approximate.
- **ATC-42** .80 as the target of the cited generalizability studies, applied to product scores.
- **ATC-43** long2022 synthesis clause.
- **ATC-44 (new, C2)** Contributions paragraph P14, all four items and their hedges.
- **ATC-45 (new, C4)** The gap between .695 and .970 is a property of the design, not of the raters.
- **ATC-46 (new, C4)** The choice among the models matters far less than the choice between modelling and averaging; indicative, with the two caveats of D6.
- **ATC-47 (new, C4)** Product-class link: the concentration of ratings in categories 1 and 2 read as fitting rare creative actions in competition (optional; needs a source).
- **ATC-48 (new, D)** Scale-choice sentence: about seven categories as the optimum; unipolar because creativity is an amount of a property.
- **ATC-49 (new, D)** Material: competitions, short clips, link to StatsBomb event data.
- **ATC-50 (new, D)** Rating app and procedure as described in M4.
- **ATC-51 (new, D)** Definition text quoted verbatim; language versions.
- **ATC-52 (new, D)** Scale labels at the endpoints only (1 "not creative", 7 "very creative").
- **ATC-53 (new, D)** Other dimensions rated for a later construct-validity analysis, as amabile1982 recommends.
- **ATC-54 (new, D)** Two rater pools: R01–R19; R23–R27 and R30.
- **ATC-55 (new, D)** Limitations wording on domain familiarity that stays true for an open pool.
- **ATC-56 (new, C1)** The reframing of the panel-size question for a pool-based sparse design; "used", not "planned".
- **ATC-57 (new, C1)** Recommendation 1 as an instance of the transparency standard of barbot2019.

**Retired or closed:** ATC-13 (retired 2026-11-09); ATC-17, ATC-24, ATC-25, ATC-27 (closed earlier); ATC-37 never assigned.

---

## Conflicts found and how this outline resolves them

1. **Brief B5 against the findings.** The brief places the observed means below the simulated range at three to eight and 10 ratings. At six ratings the observed .879 equals the printed lower bound. The outline follows the findings (R4, D2, ATC-32).
2. **Brief B6 against the findings.** The crossed-block rater IDs are in the brief only. They are on the never-quote list; FI-9, box item 3 and ATC-18 carry no IDs.
3. **Brief C4 "about 2 logits".** The notebook prints 2.129 without a unit. The outline writes "on the GRM score scale".
4. **Brief C4 "the raw mean differs from all of them".** The notebooks compare the raw mean with the GRM scores only. The outline limits the claim (D6) and records the gap.
5. **Brief C2 (i) "BIC tied".** The tie concerns M1 and the GRM; within the ladder BIC favours the constrained model at both steps. The outline states both (P14, R12, D7).
6. **Brief C4 "about .70" and "about .97".** The prose quotes .695 and .970.
7. **Talk slide against the notebook.** The slide gives Krippendorff's α "over 25 raters and 3,841 actions"; the notebook prints 2,984 products. The notebook wins.
8. **Notebook split against draft 7.** Three supplementary-notebook objects sat in the main text and three main-notebook figures in the supplement. Resolved in the placement table, with Decisions 1 and 2.
9. **Round-6 author decision on `tbl-marginal-reliability-models`** (not embedded) against brief E (candidate for RQ3b). The outline embeds it in the supplement and asks (Decision 3).
10. **C4 "state the simulation once" against the round-7 decision to keep the supplement note standalone.** The outline applies C4 and asks (Decision 13).
11. **Old rule "about 50 ratings = imprecise".** R26 has 136 ratings and the largest standard error of *a*. The wording of D4, L5 and box item 4 no longer ties imprecision to about 50 ratings alone.
12. **Misfit illustration of B7.** The pattern holds for the three lowest and the two highest M3 discriminations but not for R30 and R11, which the brief lists among the M1 values above 1. The outline names both exceptions (D7, ATC-9).

---

## Evidence gaps

Two gaps cannot be closed from `01_dossier.md` and `06_web_literature.md`. Neither blocks the writing; each has a fallback that needs no new evidence.

1. **Like-for-like comparison of the raw mean with all four models (analysis gap, not a literature gap).** Directive C4 wants the Discussion to say that the raw mean differs from all four models while the models agree with one another. The notebooks print the raw mean against the GRM only (`tbl-raw-mean-vs-grm`: τ-b and reversed pairs within groups of equal numbers of ratings) and the models against one another with other statistics (Pearson and Spearman over all products, quintile changes). No notebook prints τ-b or reversed pairs between models, or the raw mean against M1, M2 or M3. A vault or web search cannot supply this; only the analyst can, by adding the comparison to the notebooks. Fallback used in this outline: the claim is limited to "raw mean against GRM" and marked indicative (D6, ATC-46).
2. **A source for the rarity of creative actions in competition (literature gap).** The optional product-class link of C4 (D9, ATC-47) reads the concentration of ratings in categories 1 and 2 as fitting rare creative actions in match play. The findings support the distribution (F1.4); neither the dossier nor the web file holds a source for the rarity itself. A targeted search (for example the rating distribution in kempe2018, or base rates of creative actions in match analyses) would be needed to state it with a citation. Fallback: leave the link out and keep the domain-specificity hedge of draft 7.

Verification items that are not search gaps (the keys resolve; the content comes from the brief and the talk and is unchecked against the PDFs): the two standards attributed to barbot2019, of which the web file could not retrieve the abstract; the framework cells of batey2012; rhodes1961; stein1953; preston2000 and lozano2008, which the dossier marks as unverified. All are under FI-17.

No web key outside `phd_library.bib` is used. `decastellarnau2018`, cited on a backlog slide, was not checked against the library and is not used (C7).

---

## Decisions for the author

1. **Main-text objects: 13 (7 tables, 6 figures).** I follow your notebook split with two exceptions. `tbl-rater-overview` and `tbl-grm-reliability-min-ratings` move to the supplement, and `fig-grm-rater-information-ci` moves into the main text. `fig-grm-category-response-functions` and `fig-grm-rater-information` stay in the supplement although they sit in the main notebook, because 25 panels or 25 lines are not legible at journal width. Alternative: follow the split fully (15 main objects). Confirm or choose.
2. **`tbl-reliability-overview` stays in the main text** although it sits in the supplementary notebook. It is the table behind recommendation 1 and the abstract's contrast of indices. Its long note column and code-style row labels need a display fix (FI-18). Alternative: move it to the supplement and give the five values in prose.
3. **`tbl-marginal-reliability-models` is embedded in the supplement**, and the empirical reliability per model (.663, .669, .682, .695) is reported in one sentence under RQ3b. This reverses your round-6 decision not to embed it. The latent variances stay unquoted. Confirm or keep it out.
4. **Three labels stay unembedded:** `tbl-cleaning-log` (code names; the steps are in the Method text), `tbl-overview-ratings-per-action` (duplicate) and `tbl-grm-global-fit` (one row saying "not computable"). The embedder recommended the supplement for the first and third. `fig-overview-rater-overlap` is newly embedded in the supplement. Confirm.
5. **B5 wording follows the findings, not the brief.** At six ratings the observed mean (.879) equals the printed lower bound of the simulated range. The text says: inside the range at one, two and nine ratings; below it at three, four, five, seven, eight and 10; at its lower bound at six.
6. **Crossed-block rater IDs are not quotable.** No notebook prints them. FI-9, box item 3 and ATC-18 name only "three raters and 270 actions". If you want the IDs in the paper, the analyst has to print them in notebook 03, or you supply them under FI-9.
7. **C4 "about 2 logits" modified.** The notebook prints a maximum range of 2.129 without a unit. The text says "up to 2.129 apart on the GRM score scale".
8. **C4, RQ3 main point, modified.** The directive says the raw mean differs from all four models. The notebooks compare the raw mean with the GRM only, and with a different statistic (τ-b within groups) from the one used between models (Spearman over all products). The Discussion therefore makes the point as "raw mean against GRM", marks the contrast as indicative, and keeps the accuracy caveat (ATC-46). If you want the full claim, the comparison has to be added to the notebooks (Evidence gaps 1).
9. **C2 (i) and the abstract: "BIC tied" modified.** BIC is tied only between M1 and the GRM (0.416). Within the ladder it favours the constrained model at both steps (M2 29.303 and M3 49.946 above M1). The contributions paragraph and RQ3 state both. The abstract keeps "the Bayesian information criterion favoured the constrained models in both cases", which the printed values support; the tie is left to the main text for reasons of length. Alternative for the abstract: "whereas the Bayesian information criterion did not". Choose.
10. **Exact values instead of "about .70" and "about .97"** in the Discussion: .695 and .970.
11. **B2, new illustration of raw mean against severity.** Recommended: R14 (raw mean 2.22, higher than R01, R17 and R27, yet severity 0.84, the second-highest). Alternative: drop the illustration. The sentence "13 raters lay below and 11 above the average rater" is dropped because the count is not printed and R03 prints 0.00.
12. **Exclusion sensitivity wording (former D4, ATC-26).** With *r* = .99997 and a largest change of 0.16518, I propose "virtually unchanged". The numbers appear once, in the Model adequacy paragraph. Confirm the adjective.
13. **C4, simulation stated once.** The supplement note is cut to a pointer to the Method. The supplement then no longer stands alone, which reverses the round-7 choice that waited for FI-16. If CRJ publishes the supplement as a separate file, you may want the full note back.
14. **Sensitivity results placed in "Model adequacy"** at the start of the Results, and the separate "Sensitivity to the rater exclusion" section is removed, so that the Results end with RQ3. Alternative: report it in the Method instead.
15. **Box: six items, and the prose announces six.** The running text no longer lists five parallel points; it makes two arguments the box cannot carry and then points to the box. Item 4 now adds that the least precise discrimination belonged to a rater with 136 ratings (R26), and item 5 that the choice among models mattered less than the choice to model. Confirm both additions.
16. **C4, product-class link, adopted only as an option (ATC-47).** The distribution supports it (2,278 and 2,501 ratings in categories 1 and 2, 149 in category 7), but there is no source for the rarity of creative actions in competition (Evidence gaps 2). Decide: include it as the authors' reading without a citation, ask for a targeted search, or leave it out.
17. **FI-3 is closed by your facts from the talk.** What they do not cover I have collected as a new FI-34: session length and breaks, number of familiarisation clips, and which language version the raters used. Confirm that you want this placeholder, or say that these were not recorded.
18. **The definition is quoted in the Method as an indented block** (about 110 words). Alternative: supplement, with a one-sentence paraphrase in the Method. The block is the English version; say whether the German original should appear as well.
19. **The app repository URL names you.** If CRJ reviews masked, the URL has to be blinded in the submitted version (FI-16).
20. **Abstract within 250 words.** Added: Krippendorff .402 against Cronbach .959, and τ-b .773 and .818 with .076 and .066 of pairs reversed. Cut first: the category-use parenthesis, the second gap sentence, "in this exploratory study". If still over: the two-rating halves of the τ-b clause, then the severity span. Confirm the order of the cuts.
21. **RQ1, a new observed fact.** The observed mean product-level reliability first reaches .80 at four ratings (.815, 93 products), the same number as in the simulation. I use it in Results and Discussion as a read-off, with the reminder that the two are different quantities (ATC-32). Confirm.
22. **Discussion opens without a summary paragraph**, as C4 asks. The one-sentence answer at the head of each RQ subsection takes the place of the "revisit" move of the discussion model.
23. **Model labels in the Introduction.** Because the gloss sits in the Method (C6), the Introduction and the contributions paragraph use the spelled-out model names and no M-labels.
24. **Scale-choice sentence.** preston2000 and lozano2008 resolve in the library, but the dossier marks the underlying vault note as unverified. The sentence is written and carries FI-17 and ATC-48.
25. **Not rejected, not adopted:** C7 is respected in full (no worked two-action example, no automated-assessment motivation, no PACA shares, no scale-length literature beyond one sentence, no rating evening or recruitment material). The planned open recruitment appears nowhere in the text; it only shapes the Limitations wording on domain familiarity (ATC-55).
26. **Median overlap written 22.5** (printed 22.500), the one place where trailing zeros are dropped. Say if you prefer the printed form.
27. **Misfit illustration in the Discussion (B7, ATC-9).** In the M3 metric the account holds for the three lowest discriminations (R18, R09, R17: M1 fit above 1) and the two highest (R26, R12: lowest M1 infit), but R30 and R11 also show M1 values above 1 without a low discrimination. I keep the illustration and name both exceptions. Alternative: drop the illustration.
