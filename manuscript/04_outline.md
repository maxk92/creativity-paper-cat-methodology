# 04_outline.md: Argument architecture (Phase 5), REVISION 2026-11-09 (frozen data 9,046 ratings / 3,669 products / 24 raters)

> Replaces the round-5 outline of 2026-10-27. Notebooks at commit 164c146. This outline goes to **human checkpoint 1**; the decisions for the author are collected in "Decisions for checkpoint 1" near the end.

Profile: `imrad-apa`. Venue: *Creativity Research Journal*. Style: APA 7th.
Structure: Abstract, Introduction, Method, Results, Discussion, Conclusion, References, Supplementary Material.

Sources (all re-read for this revision; precedence in this order where they disagree):
1. `revision_brief_2026-11-09.md` (author priorities; §B Introduction arc; §C decisions; §D D1–D6)
2. Coordinator corrections from pause A (rating-design gap wording; C-A qualitative; sport product ratings "three or four licensed coaches"; DT-in-sport citation as an ATC item)
3. `07_rater_number_evidence.md` (binding instructions, key map, resolutions of 2026-11-09)
4. `revision_instructions_new_data.md` (§3 C1–C13; §4; §6; §8; §5 as a locator only)
5. `03_findings.md` incl. "Delta 2026-11-09" (the ONLY source of numbers)
6. `02_artifacts.md` incl. Delta (53 labels: NB00 1, NB01 6, NB02 46)
7. `01_dossier.md` ("Targeted addition 2026-11-09"), `06_web_literature.md` ("Targeted search 2026-11-09")
8. Brief `~/drive/KNOWLEDGE/Paper_CreativityAssessmentInSportsCAT.md`; `author_todo.md`; `manuscript.qmd` (old data; structure only); `05_review.md` (round 6)
9. `~/drive/utils/writing-models/` (introduction, methods, results, discussion-conclusion, abstract, title)

---

## Conventions in this file

- **F…** = finding ID in `03_findings.md` (F0.1–F2.14 plus F1.4a, F1.20a, F2.8a from the Delta). Every number below is copied from there as printed, converted to APA form only as stated next.
- `tbl-…` / `fig-…` = labels from `02_artifacts.md`. **[MAIN]** embedded in the main text; **[SUPP]** embedded in the online supplement. Embed syntax: `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/<notebook>.ipynb#<label> >}}`; cross-reference `@<label>`.
- **[ATC-n]** = interpretive or contribution claim the author must confirm. **[FI-n]** = FILL IN item the author must supply. Numbers are stable; closed items are listed as closed, never renumbered.
- **APA number format.** Values that cannot exceed 1 drop the leading zero: reliabilities, correlations (incl. Q3, τ-b), α, shares/proportions, *p*. Values that can exceed 1 keep it: a, b_k, information, θ̂ and θ̂ ranges, PSD, infit/outfit, means, SDs, entropy, severity (logits), χ², information criteria, |Δθ̂|, |Δa|, the Q3 criterion 0.2, the flag bounds 0.7–1.3. Numbers ≥ 1,000 take a comma (9,046; 3,669; −13,471.275; 28,239.363), also where the notebook prints none ("1174" in `tbl-rater-overview` → 1,174; "222 computable" stays). Seeds and identifiers take no comma (seed 20260713). **No rounding, no added or removed decimals.** *p* is written *p* < .001.
- **Precision as printed.** GRM a and b_k: 2 decimals (`tbl-grm-rater-parameters`). Information with intervals: 2 decimals (`tbl-grm-rater-information-ci`), 3 without (`tbl-grm-information-summary`); shares 3. M1 severity: 2 decimals from `tbl-rater-overview`, except the two extremes and the span, which print at 3 decimals in the stdout line (F2.8a: −0.878, SE 0.066; 1.369, SE 0.057; 2.247 logits). M3 discriminations 3 decimals. Response styles 3 decimals; R09's mean is **3.643** (never 3.642). Sensitivity 5 decimals. Projection/min-4: 3 decimals with ranges. Category shares (F0.6) are not quoted; quote counts.
- **Never quote** (per `03_findings.md` "Not found" / "NOT IN NOTEBOOK", as amended by the Delta):
  - the md5 fingerprint; any value from `01_data_overview_new_ratings.ipynb`, the archive, R scripts, AUDIT/REPORT files, or the report qmd (incl. its roundings "4.2", "840.45", "0.9999", ".688", "10%", "15.5%", "20.6%", "6.8%" in prose — shares are quoted as .068 from `tbl-grm-information-summary`);
  - any *previous* data-set value (7,820; 3,668; 19 raters; .672; .960; .928; .658; .392; .520; .698; .815; .842; 0.16246) and any statement that estimates changed;
  - CIs/SEs that are not printed: for rel_post by n, for the sensitivity differences, for the raw-mean-vs-GRM statistics, for M1 severities other than R24 and R06, for M1/M2 thresholds, for the M1–M3 reliabilities;
  - the median a drawn in `fig-grm-rater-discrimination-ci`; the number of non-computable Q3 pairs (54) and the full list of 28 flagged pairs; the count of never-used categories behind the df reduction ("10"); exact LR *p* values; the first k reaching .70 or .90 in the projection (only .80 is printed); any k > 10; `true_r2`; workload-weighted or selected rater sets; the min-4 seed; whether a rater may rate the same product twice in the top-up; how θ enters the top-up;
  - any **difference, test or "which is larger" statement between observed and simulated reliability** as a notebook result (the notebook juxtaposes them only; a comparison is the authors' reading → ATC-32);
  - the report wording "regardless of how many ratings each rater gave in reality" / "does not use our distribution of ratings per action" as a notebook fact (see the simulation-assumption rule below);
  - "x-fold" for the discrimination ratio (quote 7.277; a rounding such as "about seven-fold" must be marked as a rounding);
  - "2.25 logits" (quote 2.247); the "Assumes"/"Answers" column texts of the report; the model labels "M1 (RS-MFRM)", "M2 (PC-MFRM)", "M1 (RSM)", "M2 (PCM)", "Ratings (n)";
  - the names of the three crossed-block raters and the removal rule of the six raters dropped from the pairwise α (not printed; FI-9);
  - the data-collection timespan (not printed; FI-32).
- **Now quotable (Delta):** the ⚑ rule "infit or outfit outside 0.7–1.3" (note `38b48261`, `tbl-rater-overview` caption); the M3 discrimination summary (`tbl-discrimination-summary`: min 0.305, q1 0.915, median 1.240, q3 1.659, max 2.221, ratio 7.277, SD 0.550); "Smallest k with simulated empirical reliability of at least .80: 4" (stdout `c7a7fe2a`); the M1 severity range line (stdout `411ec44f`); the LR-df rule "categories raters never used (unused end categories and any internal gap)" (note `f43c6651`; quote the note, not the `tbl-lr-tests` caption).
- **Simulation-assumption rule (brief §C).** The Method states the assumptions of the projection and of the min-4 top-up plainly, as the authors' own description of what they did: raters of the panel drawn at random, each rater equally likely to be drawn, so that the draws do not reproduce the raters' actual workloads in the study; ratings generated from the fitted GRM and scored with its parameters, treated as known (no parameter uncertainty in the ranges); θ ~ N(0, 1) for the projection's simulated products; in the top-up the real ratings are kept and all products rescored; 50 replications; the observed data remain primary. The clause on workloads is the authors' methodological statement (it follows from equal drawing probability), not a notebook quotation; it carries **[ATC-35]**.
- **No pipeline wording in the prose.** No "notebook", "output", "pipeline", "will be refreshed"; no mention of an earlier data set, a data update or how estimates changed. Statements taken from notebook notes become the authors' wording, marked [ATC] where interpretive.
- **Terminology.**
  - "Rater" everywhere; one sentence at the first CAT mention says the CAT and JRT literature calls raters "judges".
  - "Product / action": define once in Method 2.3 ("each rated product was a single football action"). Results and Method use "product"; "action" in the title, the Introduction's sport framing, the stimulus description and the practical implications.
  - Model names as printed in the tables: "M1 (rating-scale MFRM)", "M2 (partial-credit MFRM)", "M3 (GPCM)", "GRM"; first mention in Method 2.7 spells them out; "RSM"/"PCM" only where andrich1978 / masters1982 are cited; "the MFRM" alone only for claims true of every member (severity facet, equal discrimination). "A shared category structure" is a property of **M1** only.
  - "First and third quartiles", never Q1/Q3 (Q3 is Yen's statistic).
  - Response styles: "share of ratings in the lowest category (1)", "in the highest category (7)", "in the extreme categories (1, 7)", "in the middle categories (3–5)".
  - "Average information" = information integrated over θ ~ N(0, 1); table header "Information per rating".
  - Column names as printed: "Ratings by rater", "Ratings per product", "Ratings (total)".
  - Severity: "severity (M1)" with "0 = average rater, higher = stricter" (caption wording). In the GRM, speak of "threshold location", not severity, unless the author confirms the stricter-rater gloss [ATC-6].
  - "Rating-design evidence" (rater number, expertise, scoring model) is the term for the sport gap; never "no evidence".
  - Author names typed in prose keep their particles: "de Ayala", "ten Hove", "de Joode", "de Sa Fardilha", "van der Ark", "van Hooijdonk". linacre1989 is the MESA Press book *Many-facet Rasch measurement*; prose says "many-facet".
- **Rater-ID rules (C8, §6).** Final raters: R01–R19 and R23–R27 (24). Excluded: R20, R21, R22, R28. IDs do not follow workload order; never imply they do. **R16 (268 ratings) is never described as a rater with few ratings.** Raters with 73 or fewer ratings: R26 (46), R27 (47), R19 (50), R17 (52), R18 (55), R15 (73) (F0.5). "About 50 ratings" refers to R17, R18, R19, R26, R27.
- **Figure annotations.** The in-image labels of `fig-grm-reliability-observed-vs-simulated` (".835", ".969", "24 raters") are quoted from `tbl-grm-reliability-min-ratings`, `tbl-grm-reliability-ci` / `tbl-reliability-overview` and `tbl-design-summary`, never from the image.
- **No accuracy claim.** Nowhere does the paper say that model-based scores are more accurate than raw means or than the constrained models.
- **Exploratory framing.** No "hypothesis", "supported", "confirmed" for the RQs; the only exception is the LR/AIC/BIC wording under RQ3(a) [ATC-20].

---

## Working title

**Keep (recommended, D7):** *Number of ratings, rater differences, and score reliability in creativity ratings of football actions: A judge response theory analysis*

It states the three RQs in order, names the product class and the method, has no question mark and no value word (title model). "Number of ratings" now carries both the observed by-n reliabilities and the number needed (RQ1).

**Alternative for the author (D7):** *How many ratings, and from whom: Reliability, rater differences, and the number of ratings needed in creativity ratings of football actions, a judge response theory analysis* — longer and closer to the new RQ1, but the colon-free run-on is awkward; the outline recommends keeping the current title. Short title (YAML `shorttitle`): "Rater differences and reliability in creativity ratings of football actions" (unchanged).

---

## Central contribution [ATC-1]

The study applies judge response theory (JRT) to consensual creativity ratings of football actions, an ecologically valid class of nonverbal, time-pressured products for which rating-design evidence (how many raters, of what kind, scored with which model) has been missing. Its contribution is empirical and comes in three parts, all from @tbl-design-summary (F0.3: 9,046 ratings of 3,669 products by 24 raters).

1. **Reliability as a function of the number of ratings, and the number needed in this rater pool (RQ1).**
   - The empirical marginal reliability of the scores actually obtained is .689 [.669, .703]; a hypothetical full panel would reach .969 [.965, .974] (F1.12). Conventional indices give very different pictures of the same ratings: pairwise Cronbach's α .949 [.926, .958], Krippendorff's ordinal α .391 [.363, .417] (F1.18).
   - Observed mean product-level reliability (rel_post) is .522 with one rating (832 products), .699 with two (2,107) and .756 with three (68), rising overall to .948 at twelve ratings, with exceptions at ten and thirteen ratings that rest on 14 and 1 products (F1.14). These are observed values, not a design manipulation (FI-4).
   - Simulated from the fitted GRM with randomly drawn raters of this panel, reliability rises from .530 [.513, .544] at one rating to .928 [.925, .931] at ten; the smallest number of ratings at which it reaches .80 is four (.834 [.827, .841]) (F1.20, F1.20a). Topping the actual design up so that every product has at least four ratings gives .835 [.829, .840], against .686 [.675, .695] for the simulated actual design (F1.21). Assumptions stated plainly (Method 2.10).
2. **Rater differences, with their uncertainty (RQ2).**
   - M1 severity spans 2.247 logits, from −0.878 (SE 0.066, R24) to 1.369 (SE 0.057, R06) (F2.8a). Raters differ in category use (eight raters never used at least one category; R27 has an internal gap; F0.7), in response styles (share of lowest-category ratings .579 for R06 to .016 for R13; F0.9), in GRM thresholds and discrimination (a from 0.66, R18, SE 0.27, to 3.19, R26, SE 1.72; well-estimated raters span 0.93, R09, SE 0.15, to 3.10, R06, SE 0.45; F2.1) and in average information (0.13 [0.02, 0.39] for R18 to 2.52 [0.11, 6.75] for R26; F2.5). In M3 the discriminations range from 0.305 to 2.221, a ratio of 7.277 (F1.4, F1.4a).
3. **Whether the Rasch-family constraints hold, and what the model choice does to the scores (RQ3).**
   - The LR test rejects the shared category structure of M1 (χ²(105) = 840.447, *p* < .001) and equal discrimination (M2 vs M3, χ²(23) = 156.593, *p* < .001); AIC agrees in both cases, BIC in neither (M1 28,235.202 < M2 28,256.560 < M3 28,288.744) (F1.1, F1.2). The GRM has the lowest AIC and SABIC overall; BIC favours M1 by 4.161 (F1.1).
   - Raw means and GRM scores order products partly differently: Kendall's τ-b .833 (one rating), .818 (two), .849 (three or more); .041, .066 and .071 of pairs with different raw means are in reversed order; equal raw means map to GRM scores on average 1.229, 1.531 and 0.537 apart (F2.13). Relative to the GRM, .206 of products change quintile under M1, .155 under M2, .081 under M3, with mean percentile shifts .042, .032, .016, although all correlations are ≥ .977 (F2.10, F2.11).
   - These are differences between scores, not evidence that one score is more accurate [ATC-15, ATC-22].

Implication [ATC-3, ATC-5, ATC-14, ATC-15, ATC-30, ATC-31]: creativity-rating studies of nonverbal, time-pressured products should report the reliability of the scores actually used and the agreement of single ratings; plan the number of ratings per product from domain-specific evidence (here: about four per action in this panel, by simulation); give each rater enough ratings and link raters through a common calibration set; and consider a scoring model that adjusts for rater differences, reporting how far its ordering departs from raw means. Required rater numbers do not transfer across product classes, rater pools or reliability targets.

## Core argument (6 sentences)

1. Creative products are judged by consensus (CAT); the reliability of the consensus depends on how many raters judge each product and how far they agree (amabile1982; kaufman2008a).
2. How many raters are enough is conditional on the reliability target, the object of measurement, rater expertise, scale and domain; across domains the evidence runs from two or three trained raters for short divergent-thinking responses to ten or more lay raters for open-ended products, and no study of this kind exists for sport (07; cseh2019 lists it as an open question; vanhooijdonk2022).
3. That evidence comes almost entirely from verbal and static material; football actions are nonverbal behaviour under time pressure in complex dynamic environments observed in competition, and the few product-rating studies in sport used three or four coaches, averaged, with an ICC (safardilha2019; kempe2018; roca2018; memmert2010; joode2023).
4. Methods for the rater question form a ladder from averages and Spearman–Brown, through resampling and G-theory, to MFRM and JRT; only JRT estimates severity, thresholds and discrimination per rater and gives product-specific precision, and whether that flexibility is needed is itself testable (myszkowski2019; myszkowski2021; primi2019).
5. In 9,046 ratings of 3,669 football actions by 24 raters, the obtained scores had a reliability of .689 against .969 for a full panel; one or two ratings gave .522 and .699, and about four ratings were needed for .80 in simulation; raters differed strongly in severity, scale use, discrimination and information; the Rasch constraints were rejected by LR tests and AIC but favoured by BIC; raw means and model-based scores ordered actions partly differently.
6. Rating-design figures are therefore domain-specific and must be established for each product class; for nonverbal, time-pressured products, studies should plan several ratings per action, report the reliability of the scores used, and consider rater-adjusting models [ATC-30, ATC-31].

## Research questions (exploratory; no hypotheses) [ATC-20]

- **RQ1 (number of ratings and reliability).** How reliable are the creativity scores obtained in this study, how does product-level reliability vary with the number of ratings a product received, and how many ratings per product are needed for reliable estimates in this rater pool, (a) as observed and (b) as simulated from the fitted model? How do these figures compare with a hypothetical full panel and with conventional agreement and consistency indices?
  - Evidence: F1.12, F1.14, F1.18, F1.19, F1.20, F1.20a, F1.21, F1.22, F1.23; descriptive support F1.13, F1.16, F1.17.
- **RQ2 (rater differences).** How do raters differ in severity, threshold location, scale use, discrimination and information, and how precisely are these differences estimated?
  - Evidence: F0.6–F0.9, F2.1–F2.6, F2.8, F2.8a, F2.9.
  - Severity is now promised, because M1 severities with intervals (`fig-m1-rater-severity`) and the printed range exist. GRM thresholds are "threshold location" [ATC-6].
- **RQ3 (model constraints and consequences for scores).** (a) Are the Rasch-family constraints of a shared category structure (M1) and of equal discrimination (M1 and M2) tenable for these ratings? (b) How far do product scores and rankings depend on the scoring model, from the raw mean through M1, M2 and M3 to the GRM?
  - Evidence (a): F1.1, F1.2, F1.4, F1.4a, F1.5, F1.11. Wording: "rejected by the LR test and AIC but not by BIC" (D2).
  - Evidence (b): F2.10, F2.11, F2.13, F2.14.

Supporting analyses (Method/Results, not RQs): scoring-model choice and adequacy (F1.1, F1.3, F1.7–F1.10); sensitivity to the rater exclusion (F2.12).

---

## Word budget (target total ≈ 7,500–8,500 words of main text excl. references, tables and box; FI-16 checks the CRJ limit)

| Section | Words | Notes |
|---|---|---|
| Abstract | ≤ 250 | hard limit (FI-16) |
| Introduction | 1,500–1,800 | five moves; budget per move below |
| Method | 1,900–2,200 | incl. the IRT paragraph moved from the Introduction and the two simulations |
| Results | 1,700–2,000 | descriptive; RQ order |
| Discussion | 2,000–2,300 | incl. box (box text ≈ 180) and Limitations |
| Conclusion | 150–200 | one paragraph |

---

## Section outline

### Abstract (one paragraph, unstructured, ≤ 250 words [FI-16])

Abstract model 2: background/gap → method → results with numbers → implications. No citations, no rendered markers (claims tracked as ATC-2, ATC-5, ATC-14, ATC-15, ATC-30, ATC-35 and FI-1 in the hidden comment block). Keep the numbers few; if the limit bites, compress the method sentence first, then drop the τ-b clause, then the severity span.

- **Background/gap (2 sentences).** Creative products are rated by consensus (CAT); how many raters are needed and how raters differ has been studied mostly with verbal and static material. Football actions are nonverbal behaviour under time pressure, observed in competition, and rating-design evidence for such products is lacking (ATC-2, ATC-28, no rendered marker).
- **Aim/method (1–2 sentences).** 24 raters [FI-1 "student raters", no marker] gave 9,046 ratings of 3,669 football actions on a 7-point creativity scale in an incomplete design (F0.3). JRT models were fitted: a GRM and a ladder from the rating-scale many-facet Rasch model to the GPCM; reliability was studied by the number of ratings per action, observed and simulated.
- **Results.**
  - RQ1: empirical reliability of the obtained scores .689, against .969 for a hypothetical full panel; mean product-level reliability .522 with one rating and .699 with two; in simulation from this panel, at least four ratings per action were needed to reach .80 (F1.12, F1.14, F1.20a) [ATC-35].
  - RQ2: raters differed in severity (span 2.247 logits), category use (share of lowest-category ratings .579 to .016), thresholds, discrimination and information (F2.8a, F0.9, F2.1, F2.5); parameters of raters with about 50 ratings were imprecise.
  - RQ3: LR tests rejected a shared category structure and equal discrimination (both *p* < .001), **although BIC favoured the constrained models in both cases** (D2; F1.1, F1.2); raw means and GRM scores agreed with Kendall's τ-b = .833 and .818 for one and two ratings (F2.13).
- **Implications (hedged).** For such products, studies should report the reliability of the scores actually used, plan several ratings per action from domain-specific evidence, link raters through a common calibration set where rater parameters are imprecise, and consider scoring with a model that adjusts for rater differences, reporting how far it departs from raw means (ATC-5, ATC-14, ATC-15, ATC-30, ATC-31).
- **Do not use:** any projection value other than "four", any R18 value, b_1 values, "we show", "by convention", any accuracy claim, any marker.

### 1 Introduction (1,500–1,800 words; five moves per brief §B; introduction model: moves 1–3 = background and research map, move 3–4 = gap, move 5 = present paper)

Purpose: lead the reader from "creativity is judged by consensus" through "how many raters depends on the domain" and "sport is a nonverbal, time-pressured domain without rating-design evidence" to "JRT is the method that can answer both the rating-number and the rater-difference question, and whether its flexibility is needed is testable", ending in RQ1–RQ3. Every move ends with a sentence that hands over to the next. The IRT tutorial (old manuscript line 48) moves to Method 2.7; the Introduction keeps only what the ladder argument needs.

**Move 1 — Creativity matters; products are judged by consensus (200–250 words)**
- P1. Creativity as a core competence: workforce skill (wef2025), PISA 2022 creative thinking (oecd2024), a quality to develop and evaluate in sport (safardilha2019 [narrative "de Sa Fardilha and Allen (2020)"]; santos2016) [FI-17].
- P2. Of the four facets (person, process, product, press; batey2012), the product is the one that is judged by others, and each facet needs its own measurement approach (barbot2019b). Creative products are assessed by the consensus of independent raters who know the domain: the CAT (amabile1982; hennessey2011; kaufman2024). Terminology sentence: judges = raters. Hand-over: the consensus is only as good as the panel that produces it.

**Move 2 — The reliability problem: how many raters are enough is conditional (450–550 words)**
- P3. **Aggregation.** CAT reliability rests on aggregation: by Spearman–Brown logic the reliability of the mean depends on the mean inter-rater correlation and on the number of raters, so a larger panel compensates for lower agreement (amabile1982). The reverse also holds: a high α from a large panel can mask low agreement between single raters (kaufman2008a: 106 novices reached α = .94 on poems yet correlated .22 with experts) [FI-17 "mask" wording]. Consistency and absolute agreement are seldom distinguished (cseh2019; stefanic2015).
- P4. **What the required number depends on.** State the conditions (07 bottom line): reliability target, object of measurement (persons across tasks vs single products), rater expertise and training, scale and scoring format, product heterogeneity and domain. Then the cross-domain evidence, **each figure with its target and object** (binding instruction of 07; verification levels → FI-17):
  - Trained student raters scoring short, homogeneous divergent-thinking responses (person-level, relative G ≥ .80): two raters for uses and instances, three for consequences under average scoring (silvia2008 [excerpts]); five graduate-student raters with 15 captions for g and φ ≥ .80 (kaufman2007 [excerpts]).
  - Novices judging expert-domain products (product-level, Cronbach's α): for poems, Kaufman et al.'s own Spearman–Brown projection to ten novices gave .58 (kaufman2008a, full text per 06: .575 [.562, .588]); for short stories, 100 random panels of ten novices averaged α = .53 (range .35–.75) and for five engineering designs .66, against .93 and .86 for ten experts, and ten-novice panels correlated .56 with experts on stories (kaufman2013). **Attribute .58 to poetry (kaufman2008a) and .53 to stories (kaufman2013)** (07 resolution).
  - Open-ended products rated by non-experts (ICC ≥ .70): seven or more raters for fashion outfits (barth2021 [excerpts]); 10–15 undergraduates for creativity ratings of design products and 15–20 for composite indices (terai2026 [abstract]).
  - Person-level measurement with large person-by-task variance: with two divergent-thinking items no panel of one to ten lay raters reached .80, and rater main effects (severity) accounted for 26.6% and 56.9% of the variance (hass2018); with two trained raters, five tasks were needed for relative generalizability ≥ .70 and more for absolute decisions (vanhooijdonk2022); dependability was low for all rater groups on science tasks (long2015 [abstract/secondary]).
  - Practice: most of 84 reviewed studies used fewer than ten raters, about five on average (long2022 [excerpts]); the common recommendation is five to ten (kaufman2008, via cseh2019); reported panels run from two (daly2016, cite via cseh2019 only) to 134 (cseh2019).
  - **No rater-number study was located for sport, music (headcount), mathematics, advertising or programming** (07; scope: time-limited search, phrase as "we located none").
- P5. **Conclusion of the move.** No general required number exists; published figures are conditional on target, object, raters, scale and domain. Cseh and Jeffries (2019) list the number of judges needed for reliable consensus among the open questions of the CAT — **do not write that they require domain-by-domain determination** — and G-theory authors argue that each assessment procedure needs its own G- and D-study (vanhooijdonk2022). Hand-over: and the evidence that exists comes from a narrow range of material.

**Move 3 — The verbal bias and the sport case (300–350 words)**
- P6. **Material type (C-A, qualitative) [ATC-28].** The rating-design evidence comes largely from verbal material — divergent-thinking responses, poems, stories, captions, metaphors — and from static products that raters inspect at leisure, such as collages, drawings and designs (amabile1982; kaufman2008a lists the typical CAT tasks; reiterpalmon2019 for the DT scoring tradition; saidmetwaly2017b: the task universe discussed is verbal, figural and mathematical paper-and-pencil material; paca2019 for the measure mix; optional acar2023/acar2024 for text-based scoring). **No percentage.** Within sport, the standard tests are "generalist thinking expressed verbally or through drawing" (safardilha2019 [FI-17: check wording and page]).
- P7. **Football actions as a product class (C-B).** Nonverbal behaviour produced under time pressure in a complex, dynamic environment: creative motor actions emerge from the performer–environment system (orth2017; hristovski2011; hristovski2012; vaughan2019; rasmussen2019); decisions in team sport are time-constrained option generation (raab2007); players process substantial information within a very short time (memmert2011b). Observed in competition, the product class is ecologically valid in a way laboratory and game-test settings are not (safardilha2019; memmert2011b; joode2023; general anchor cotter2019 [FI-17: author field "Cotter & Silvia"; content unverified]); ratings of such actions exist (kempe2018; joode2023; zahno2023; zahno2024).
- P8. **The gap in sport (C-C; coordinator wording).** Sport creativity research has concentrated on process measures, divergent thinking in game situations in particular (memmert2007; memmert2010; memmert2013; furley2015; roca2018; fink2018; reviews safardilha2019; memmert2011b). **DT-in-sport citation: memmert2011 vs memmert2013 vs memmert2011b is the author's choice [ATC-29].** The few studies that rated football actions relied on three or four licensed coaches, averaged the ratings and reported an intraclass correlation (kempe2018; memmert2010; roca2018; joode2023) [FI-17: kempe2018 scale and index; zahno2023/2024 panel sizes]; none examined how many raters are needed, how raters differ, or which scoring model suits the ratings. **Phrase as a lack of rating-design evidence, never "no evidence"; no "by convention".** Hand-over: answering these questions requires a method that treats raters as the object of study.

**Move 4 — The methods ladder (350–400 words)**
- P9. **From averages to G-theory.** Raw averages with α or Spearman–Brown treat raters as interchangeable and conflate panel size with agreement; α ignores severity, which confounds raw means whenever different raters rate different products (primi2019; myszkowski2019). Resampling raters from a large pool shows the distribution of reliability across panels of size k but is pool-specific (kaufman2013; barth2021; terai2026). G-theory decomposes variance into rater, product and interaction components and projects relative and absolute coefficients to k raters in D-studies, but still treats raters as interchangeable, needs near-balanced designs and cannot correct individual raters (silvia2008; hass2018; vanhooijdonk2022). Classical scoring remains the default in creativity measurement, and IRT or G-theory are rarely used (saidmetwaly2017b).
- P10. **MFRM.** Many-facet Rasch models add rater severity as a facet, estimate and correct it in incomplete but connected designs, and flag misfitting raters (linacre1989; eckes2015); Primi et al. (2019) showed that severity confounds scores when raters score different subsets and that rater workload could be cut by about a third with severity-adjusted scores. But every Rasch-family model assumes equal discrimination, and the rating-scale form assumes one shared category structure; discrimination differences surface only as misfit (myford2004; myszkowski2021).
- P11. **JRT.** Judge response theory transposes IRT to multiple-judge data: raters are items whose severity, category thresholds and discrimination are estimated individually, under the GRM or the GPCM; it yields fair scores with product-specific standard errors, reliability conditional on the creativity level, and an explicit model of rater behaviour, in which part of the rater-by-product interaction becomes information rather than error (myszkowski2019; myszkowski2021). Applications since: ratings of 3-D drawings (barbot2023), divergent-thinking ratings with a GRM retained (pellegrino2025 [FI-17]), planning of planned-missing rating designs (forthmann2025; goecke2024), and rubric-coded PISA creative-thinking responses (myszkowski2025, optional, D10). No application to ratings of sport actions was located [ATC-2]. Because the rating-scale and partial-credit models are constrained versions of the GPCM, the constraints become testable by model comparison rather than imposed (myszkowski2021); whether the flexibility of JRT is needed is therefore an empirical question (RQ3).

**Move 5 — The present study (200–250 words)**
- P12. Large set of CAT-style creativity ratings of football actions by 24 raters in a sparse, connected design (the design is named once here and described in Method; no "most products were rated only once or twice" framing outside the Table). Exploratory; no confirmatory hypotheses [ATC-20]. RQ1–RQ3 as worded above, with RQ1 explicitly as reliability as a function of the number of ratings and the number needed for reliable estimates, observed and simulated. One sentence on the analytic route: a GRM and an adjacent-category ladder (M1, M2, M3) by MML; reliability of the obtained scores overall and by number of ratings; a projection and a top-up simulation; rater parameters with uncertainty; GRM scores against raw means and against the constrained models. Scope: rater expertise and the design of the rating scale are not analysed.

### 2 Method (1,900–2,200 words; methods model: overview → details → relation to prior methods → problems; all FILL INs stay visible)

**2.1 Overview.** CAT-style rating study: independent raters, relative judgements, randomised order (amabile1982; hennessey2011). Products are football actions rated within a larger project [FI-1, FI-2]. Ethics and consent [FI-1]. Exploratory; preregistration status [FI-15].

**2.2 Raters.**
- Bachelor's and Master's students rating as part of thesis projects [FI-1]; the raters who joined later (R23–R27) from the same pool? [FI-31; D5]. Rater-pool description or a statement that it was not recorded [FI-21].
- Final data: 24 raters, pseudonyms R01–R19 and R23–R27 (gaps because four raters were excluded, see 2.6), 46 to 1,174 ratings each (F0.3, F0.5; column "Ratings by rater"). IDs do not reflect workload (C8).

**2.3 Products and stimulus material.** Define the product term here. Matches, competitions, selection rule via event data, clip length, source [FI-2].

**2.4 Rating procedure.**
- Software, instruction, creativity definition shown (originality × functionality in game context; runco2012) [FI-3]; relation to the CAT "no criteria" rule (hennessey2011) and to trained-rater sport studies (kempe2018; memmert2010) [ATC-19].
- Unipolar 7-point scale, anchors at 1, 4, 7 [FI-3]; "action not recognised" option [FI-3]; order, sessions, breaks [FI-3; C13: timestamps of R03, R06, R13 up to November 2025 are partly batched, so make no timing claim for them]; data-collection period [FI-32]; other dimensions rated, not analysed [FI-3].

**2.5 Rating design.**
- Allocation of products to raters and how products came to have their number of ratings, including the latest collection in which most new ratings went to products that already had three or more ratings [FI-4, FI-31; C13: **do not write an allocation rule the author has not confirmed**]. Bears on ignorable missingness under MML [ATC-18].
- Incomplete but connected design: one component (F0.3; eckes2015). Coverage numbers in @tbl-design-summary only; `fig-design-ratings-per-product` [SUPP] shows the distribution of ratings per product (F0.4; counts quoted from N1 stdout: 832, 2,107, 68, 153, 198, 137, 95, 36, 22, 14, 4, 2, 1).

**2.6 Data preparation and final data.**
- Cleaning in text (F0.1): 10,447 raw rows; 1,347 ratings marked "action not recognised" removed (author-supplied explanation sentence on video artefacts, no marker; non-recognition rate by rater [FI-22]); 1 out-of-range value (0.0, R04) removed; 21 rater–product pairs entered more than once, 1 conflicting; **the entry with the latest timestamp was kept**, removing 22 rows (C9); 9,077 ratings by 28 raters remained.
- Rater exclusion (F0.2; `tbl-excluded-raters` [SUPP]): raters with fewer than 15 ratings, R20 (13), R21 (9), R22 (2) and R28 (7), together 31 ratings; one product rated only by them dropped; "because their up to seven rater-specific parameters cannot be estimated reliably" [FI-23]. Sensitivity sentence (C12, D4) [ATC-26]: "Excluding them left the product scores nearly unchanged on average (*r* = .99994, mean absolute change 0.00204), with a largest change in one product score of 0.35026 (@tbl-sensitivity-rater-exclusion)." Never "did not change".
- Final data (F0.3; `tbl-design-summary` [MAIN]): 9,046 ratings of 3,669 products by 24 raters; scale 1–7, coded 0–6; ratings per product mean 2.466, median 2, range 1–13, harmonic mean 1.806; 832 products with one rating; fill .103; one component; 30 of 276 rater pairs share no product; median overlap 19. Quote once.
- Category use (F0.7; `tbl-category-usage` [SUPP]; `fig-category-usage-shares` [SUPP]): eight raters never used at least one category; category 7 never used by R01, R03, R06, R18, R25 and R26; categories 6 and 7 by R17; categories 5 and 7 by R27, so R27 has an **internal gap** (C7). Consequences: R17 and R27 have four thresholds, R01, R03, R06, R18, R25 and R26 five, all others six; R27's thresholds separate other category boundaries and are not directly comparable with other raters' (notebook note, factual).

**2.7 Measurement models (receives the IRT paragraph from the old Introduction).**
- IRT basics in three sentences: response probability as a function of a latent attribute and item parameters (lord1980; embretson2013; ayala2022 "de Ayala"); Rasch models constrain discrimination to be equal, which makes the raw score sufficient (rasch1960; bond2020); polytomous forms: rating scale model (andrich1978) and partial credit model (masters1982) differ in whether items share one category structure; GPCM (muraki1992) and GRM (samejima1969) add item-specific discrimination; adjacent-category vs cumulative link.
- JRT frame: raters as items, products as persons, one latent dimension θ, normal with mean 0; variance fixed at 1 in M3 and the GRM, estimated in M1 and M2 (myszkowski2019; myszkowski2021). Threshold definition (neutral): b_k is the θ at which a rating above category k becomes more likely than k or below [ATC-6 for "higher b = stricter"]. Discrimination a. GRM threshold spacing is partly the same fact as a (state once).
- Ladder: M1 (rating-scale MFRM) = rating scale model with raters as items and a rater severity, which corresponds to a two-facet rating-scale MFRM (linacre1989; eckes2015; primi2019), estimated by MML in `sirt::rm.facets` (robitzsch2025); M2 (partial-credit MFRM) = partial credit model with rater-specific thresholds, corresponding to a partial-credit MFRM (eckes2015), still equal discrimination; M3 (GPCM) adds rater-specific discrimination; M2, M3 and the GRM in mirt (chalmers2012). Retained scoring model: GRM, thresholds ordered by construction.
- Estimation (F1.3; `tbl-grm-convergence` [SUPP]): EM, 61 quadrature points, tolerance 10⁻⁴, Oakes SEs (chalmers2018), converged after **436** iterations, information matrix positive definite.

**2.8 Model comparison.**
- LR tests M1 vs M2 and M2 vs M3; log-likelihood, AIC, BIC, SABIC with Δ to the best model; GRM compared by information criteria only (F1.1, F1.2).
- Problems: M1–M2 crosses software (sirt vs mirt), approximate; **df of M1 vs M2 (105) below the formula value (J − 1)(K − 2) = 115 because the observed df is smaller by the number of categories raters never used, unused end categories and any internal gap (C7; quote the note's rule, not the count)**; no model without rater effects, so severity is not tested on its own.

**2.9 Model adequacy.**
- Infit/outfit (wright1982) under M1 and the GRM, expected value 1; **flags mark values outside 0.7–1.3, the rule of the rater-fit output; with about two ratings per product values below 1 are expected because each score is estimated from the ratings being checked, so flags below 0.7 are read as a property of the design rather than as misfit [ATC-33]**; no further cut-offs.
- S-X² (orlando2000; kang2008) with 20 imputations of the missing ratings; about 90% of cells imputed, so the test is conservative [ATC-11].
- Yen's Q3 (yen1984) for pairs with at least three jointly rated products and residual variance in both raters (222 of 276 pairs); negatively biased with few raters per product (christensen2017), so pairs compared by deviation from the mean Q3; flagged if ≥ 30 shared products and |Q3 − mean| > 0.2; no reference distribution. Do not state the number of non-computable pairs.
- C2 (cai2014) not computable: 30 of 276 pairs share no products (F1.10). `tbl-grm-global-fit` not embedded.

**2.10 Scores, reliability and the two simulations (RQ1).**
- EAP θ̂ with PSD. Empirical marginal reliability Var(θ̂)/(Var(θ̂) + mean PSD²) as the primary index; model-based marginal reliability for a hypothetical product rated by all raters (green1984; mirt marginal_rxx) with a grid check. 95% intervals from 200 accepted draws (asymptotic normal, Oakes covariance), products also resampled for the empirical reliability; **43 draws rejected** (invalid GRM) and replaced; intervals conditional on valid draws (F1.12).
- Product-level: rel_post = 1 − PSD² (relative to the unit prior variance; partly reflects the prior with one or two ratings); rel_info = I/(I + 1) as a check; both summarised by "Ratings per product" (F1.13–F1.16).
- Conventional indices, lead sentence optional with hove2024 ("ten Hove et al."): Cronbach's α (cronbach1951) from pairwise covariances over usable raters and on the largest fully crossed block [FI-9: why R26, R19, R14, R02, R12, R27 were not usable; which three raters form the block]; Krippendorff's ordinal α (hayes2007); bootstrap CIs over products (1,000 replications); for the pairwise α **647 of 1,000** replications computable, interval approximate [ATC-11].
- **Projection (F1.20; `tbl-grm-reliability-projection`, `fig-grm-reliability-projection` [SUPP]):** products with θ ~ N(0, 1) simulated; each receives k ratings (k = 1–10) from k raters of the panel drawn at random, each rater equally likely, so the draws do not reproduce the raters' actual workloads [ATC-35]; ratings generated from the fitted GRM and scored with its parameters, treated as known; 50 replications of 2,000 products per k, seed 20260713; outputs the empirical marginal reliability (mean and 95% range over replications) and mean rel_post; the smallest k reaching .80 is reported.
- **Top-up to at least four ratings (F1.21; `tbl-grm-reliability-min-ratings` [MAIN]):** for each actual product with fewer than four ratings the missing ratings are generated from the fitted GRM by raters drawn at random with equal probability, real ratings kept, all products rescored with the GRM (parameters treated as known); 50 replications; the same simulation on the unchanged design serves as a check against the observed empirical reliability. State plainly that the ranges reflect simulation variability only and that the observed data remain primary. Do not state what is not stated (whether a rater can rate the same product twice; how θ enters; seed).
- Observed and simulated values are shown side by side in `fig-grm-reliability-observed-vs-simulated` [MAIN] and `tbl-grm-reliability-observed-vs-simulated` [SUPP]; the two are different quantities (observed mean rel_post vs simulated empirical marginal reliability) — say so here.

**2.11 Rater parameters, severity, information and response styles (RQ2).**
- M1 severity per rater with SE (0 = average rater, higher = stricter) (`fig-m1-rater-severity` [MAIN]; values in `tbl-rater-overview` [MAIN]).
- GRM a and b_k with Oakes SEs; `fig-grm-rater-discrimination-ci` [MAIN] shows a with ±1.96 SE.
- Average information and share of the full-panel information, with 95% intervals from the same draws (`tbl-grm-rater-information-ci` [SUPP]; `fig-grm-rater-information-ci` [SUPP]; `tbl-grm-information-summary` [SUPP]).
- Descriptive response styles on the raw scale (`tbl-overview-rater-response-styles` [SUPP]; `fig-overview-rater-response-styles` [MAIN]; `fig-category-usage-shares` [SUPP]): mean, median, SD, IQR, categories used, entropy (natural log), shares in the lowest, highest, extreme and middle categories; unadjusted, no per-rater uncertainty.
- `tbl-rater-overview` [MAIN] collects per rater: ratings, raw mean, severity (M1), a (GRM), share of panel information with interval, GRM infit/outfit with ⚑ (outside 0.7–1.3), unused categories.

**2.12 Score agreement and sensitivity (RQ3b).**
- Raw mean vs GRM EAP separately for products with 1, 2 and 3+ ratings: Kendall's τ-b; share of pairs with different raw means in reversed order; mean and maximum θ̂ range at equal raw mean (F2.13). No pooled comparison.
- Correlations of EAP scores between models; relative to the GRM the absolute percentile shift and the share changing quintile (F2.10, F2.11); M1 grid check.
- Rater-exclusion sensitivity: GRM refitted with all 28 raters (F2.12).

**2.13 Software and availability.** R with mirt and sirt, psych and a Krippendorff package, Python for display [FI-6]; data and code availability, pseudonymised IDs [FI-15].

### 3 Results (1,700–2,000 words; results model: overview → invite to objects and key results → problems → one hedged pointer; descriptive only)

**3.0 Overview (1 short paragraph).** Echo RQ1–RQ3; all analyses use @tbl-design-summary; scoring model first.

**3.1 Scoring model (brief)** — F1.1, F1.3, F1.7–F1.10; `tbl-model-fit` [MAIN]; cross-ref `tbl-grm-convergence`, `tbl-grm-rater-fit`, `tbl-grm-q3-flagged` [SUPP].
- **C1 wording:** "The GRM had the lowest AIC (27,258.550) and SABIC (27,737.316) of the four models, whereas BIC was lowest for M1 (rating-scale MFRM; 28,235.202), with the GRM 4.161 above it (28,239.363). The GRM and M3 (GPCM) have the same number of parameters (158), so their comparison reduces to the log-likelihood (−13,471.275 vs −13,495.966), and the GRM is lower by 49.381 on AIC, BIC and SABIC alike." Leave the other Δ values to the table.
- Converged after 436 EM iterations, information matrix positive definite.
- Fit: no S-X² significant (*p* from .328 to .665); GRM infit 0.429 (R02) to 0.980 (R18), outfit 0.402 (R02) to 0.971 (R18), all below 1; 15 raters flagged, all for values below 0.7 and none above 1.3 (read off `tbl-rater-overview`; state as a count with the rule); **C11:** mean Q3 −.202 over 222 computable pairs, 28 pairs flagged; of the ten shown, eight deviate negatively and two positively (R09–R23, R10–R11); C2 not computable (Method 2.9).

**3.2 Reliability of the scores and number of ratings (RQ1)** — F1.12–F1.23; embed `tbl-reliability-overview` [MAIN], `tbl-grm-reliability-by-n` [MAIN], `fig-grm-reliability-observed-vs-simulated` [MAIN], `tbl-grm-reliability-min-ratings` [MAIN]; cross-ref [SUPP]: `fig-grm-rel-post-by-n`, `tbl-grm-reliability-ci`, `tbl-grm-reliability-summary`, `tbl-naive-indices`, `tbl-grm-reliability-projection`, `fig-grm-reliability-projection`, `tbl-grm-reliability-observed-vs-simulated`, `fig-grm-rel-post-histogram`, `fig-grm-rel-post-by-theta`, `fig-grm-rel-consistency`, `fig-grm-panel-information`.
- **(1) Obtained scores vs full panel vs conventional indices** (@tbl-reliability-overview; F1.12, F1.18): empirical marginal reliability .689 [.669, .703]; model-based (hypothetical full panel) .969 [.965, .974], grid .969; pairwise Cronbach's α .949 [.926, .958] (18 raters, 1,946 products; 647 of 1,000 replications computable, approximate); crossed block α .750 [.684, .800] (3 raters, 261 products); Krippendorff's ordinal α .391 [.363, .417] (24 raters, 2,837 products). State what each refers to ("Refers to" column). **C4: no closeness claim** (D3). Do not discuss the M1–M3 rows.
- **(2) Observed product-level reliability by number of ratings** (@tbl-grm-reliability-by-n; @fig-grm-rel-post-by-n [SUPP]; F1.14). **C3 wording:** "Mean rel_post was .522 for the 832 products with one rating, .699 for the 2,107 with two and .756 for the 68 with three; it rose overall with the number of ratings, to .948 at twelve, with two exceptions: .897 at ten ratings after .915 at nine, and .947 at thirteen after .948 at twelve. Mean PSD fell from 0.684 to 0.228, with the same exceptions at ten (0.314) and thirteen (0.230). The rows from ten ratings upward rest on 14, 4, 2 and 1 products. No mean reached the full-panel value of .969." Products with the same number of ratings differ (figure). Move 3: observed, not a design manipulation [FI-4].
- **(3) Simulated reliability by number of ratings** (@fig-grm-reliability-observed-vs-simulated; values from @tbl-grm-reliability-projection and @tbl-grm-reliability-observed-vs-simulated [SUPP]; F1.20, F1.20a, F1.22): simulated empirical reliability rose at every step from .530 [.513, .544] at one rating to .705 [.696, .713] at two, .787 [.778, .797] at three, .834 [.827, .841] at four and .928 [.925, .931] at ten; **the smallest k with at least .80 was four** (printed). Observed means lie inside the simulated 95% range at one, two and eight ratings and below it at three to seven, nine and ten (read-off; state as a description of the table, no test, no cause) [ATC-32]. Say the two columns are different quantities.
- **(4) Top-up design** (@tbl-grm-reliability-min-ratings; F1.21): simulated actual design .686 [.675, .695] (mean rel_post .687), against the observed .689; at least four ratings per product: .835 [.829, .840], with 3,007 products topped up and 6,778 ratings added (15,824 in total). No "close" wording unless marked [ATC-32].
- **(5) Distribution and consistency** (one sentence each; F1.13, F1.16): rel_post median .712, IQR .191 (first and third quartiles .599 and .789), range .068–.954; rel_post and rel_info correlate *r* = .947, 229 products differ by more than .1.

**3.3 Rater differences (RQ2)** — F0.6–F0.9, F2.1–F2.9; embed `fig-overview-rater-response-styles` [MAIN], `tbl-rater-overview` [MAIN], `fig-m1-rater-severity` [MAIN], `tbl-grm-rater-parameters` [MAIN], `fig-grm-rater-discrimination-ci` [MAIN]; cross-ref [SUPP]: `tbl-overview-rater-response-styles`, `tbl-category-usage`, `fig-category-usage-shares`, `fig-overview-rating-distribution`, `fig-grm-category-response-functions`, `tbl-grm-rater-information-ci`, `fig-grm-rater-information-ci`, `fig-grm-rater-information`, `fig-grm-information-shares`, `tbl-grm-information-summary`, `tbl-discrimination-m3`, `tbl-discrimination-summary`.
- Rule: ranges over all 24 raters; when an extreme comes from a rater with ≤ 73 ratings, give the number of ratings and the SE; **R16 is never a few-ratings rater (C5)**; no interpretation.
- **Response styles and category use** (F0.9, F0.6, F0.7): means 1.760 (R06) to 3.836 (R18); SD 1.022 (R01) to 1.953 (R19); share in the lowest category .579 (R06) to .016 (R13); share in the highest category highest for R19 (.080), eight raters gave no 7 (R01, R03, R06, R17, R18, R25, R26, R27); middle categories R13 .799, R18 .764, R12 .735, lowest R06 .192; entropy 1.191 (R06) to 1.903 (R09; mean 3.643). Category 1: 2,179 ratings; 2: 2,355; 7: 128. R27's internal gap (C7). No per-rater uncertainty.
- **Severity (M1)** (@fig-m1-rater-severity; @tbl-rater-overview; F2.8, F2.8a): from −0.878 (SE 0.066, R24) to 1.369 (SE 0.057, R06), a span of 2.247 logits; 13 raters below and 11 above the average rater; the order of severities does not follow the order of raw means exactly (e.g., R18 has the highest mean, 3.84, but the second-lowest severity, −0.79). Other raters' severities at 2 decimals.
- **Thresholds** (@tbl-grm-rater-parameters; F2.2): b_1 from −6.25 (R18, 55 ratings, SE 2.86) to 0.25 (R06, SE 0.05); next lowest −3.36 (R13, SE 0.47); R06 the only positive b_1; spacing R02 −0.67 to 1.99 vs R13 −3.36 to 4.31; spacing is partly discrimination (Method 2.7). **C7:** R27's four thresholds are not compared with others'. Threshold counts as in 2.6.
- **Discrimination** (@fig-grm-rater-discrimination-ci; @tbl-grm-rater-parameters; F2.1). **C5 wording:** "a ranged from 0.66 (R18, 55 ratings, SE 0.27) to 3.19 (R26, 46 ratings, SE 1.72). The next highest values came from raters with many ratings as well as few: R06 3.10 (520 ratings, SE 0.45), R27 3.04 (47, SE 0.91), R25 3.01 (138, SE 0.47) and R24 2.89 (190, SE 0.37); the next lowest was R09 at 0.93 (400 ratings, SE 0.15). R16 had 2.47 (268, SE 0.26); R01 1.82 (SE 0.13), R02 2.71 (SE 0.35), R23 1.75 (SE 0.13)." Largest SEs: R26 1.72, R19 1.01, R27 0.91.
- **Information** (@tbl-grm-rater-information-ci [SUPP]; @tbl-rater-overview; F2.4, F2.5): average information 0.13 [0.02, 0.39] (R18) to 2.52 [0.11, 6.75] (R26); shares .004 [.000, .011] to .074 [.003, .178]; R09 0.28 [0.13, 0.48], R01 0.86 [0.66, 1.05], R02 1.96 [1.11, 2.97]; widest intervals R26, R19 (2.03 [0.27, 5.31]) and R27 (2.01 [0.50, 4.12]). **C6:** θ at maximum information highest for R01 (2.800), R16 (2.400) and R06 (2.300) — the clause "neither used category 7" applies to R01 and R06 only, or is dropped — lowest for R13 (−0.600); shares at θ = −2: R12 .137, R24 .120; R06 .001 at θ = −2 and .082 at θ = 2.
- Move 3: intervals from the same 200 accepted draws; conditional on valid draws.

**3.4 Model constraints and consequences for scores (RQ3)** — F1.1, F1.2, F1.4, F1.4a, F1.5, F1.11, F2.10, F2.11, F2.13, F2.14; embed `tbl-raw-mean-vs-grm` [MAIN], `fig-raw-mean-vs-theta` [MAIN], `tbl-score-agreement` [MAIN]; cross-ref [SUPP]: `tbl-lr-tests`, `tbl-discrimination-m3`, `tbl-discrimination-summary`, `tbl-threshold-order`, `tbl-rater-fit-m1`, `tbl-theta-correlations`.
- **Paragraph A, ladder tests (RQ3a). C2 wording:** "M1 (rating-scale MFRM) against M2 (partial-credit MFRM): χ²(105) = 840.447, *p* < .001; AIC favoured M2 (27,418.524 vs 28,048.971), whereas BIC favoured M1 (28,235.202 vs 28,256.560). M2 against M3 (GPCM): χ²(23) = 156.593, *p* < .001; AIC favoured M3 (27,307.931 vs 27,418.524), BIC favoured M2 (28,256.560 vs 28,288.744). Both constraints were thus rejected by the LR test and AIC but not by BIC." Caveats are in Method 2.8.
- **Paragraph B, ladder rater detail:** M3 discriminations 0.305 (R18, SE 0.141) to 2.221 (R27, SE 0.873), median 1.240, ratio of largest to smallest 7.277, SD 0.550 (F1.4, F1.4a); nine raters with unordered steps under M2, eight under M3 (F1.5); **C10:** under M1, R09 (infit 1.083, outfit 1.060), R17 (1.323, 1.167) and R18 (1.170, 1.231) are above 1, R12 lowest (0.260, 0.278) (F1.11).
- **RQ3(b), raw mean vs GRM** (@tbl-raw-mean-vs-grm, @fig-raw-mean-vs-theta; F2.13), three printed rows only:

    | Ratings per product | Products | Kendall's τ-b | reversed order | mean / max θ̂ range at equal raw mean |
    |---|---|---|---|---|
    | 1 | 832 | .833 | .041 | 1.229 / 1.430 |
    | 2 | 2,107 | .818 | .066 | 1.531 / 2.170 |
    | 3+ | 730 | .849 | .071 | 0.537 / 1.317 |

  Descriptive sentence: the range reflects differences in both the threshold location and the discrimination of the raters who gave the ratings and, with two or more ratings, the rating combinations behind the same mean [ATC-21]. No pooled value, no trend claim.
- **RQ3(b), model choice** (@tbl-score-agreement; F2.11): relative to the GRM, M1 *r* = .977 / ρ = .979, .206 change quintile, mean percentile shift .042; M2 .985 / .984, .155, .032; M3 .996 / .996, .081, .016; ladder Pearson .981–.993, Spearman .984–.996; grid check 1.000 (F2.10). Quote the mean shift in the same sentence as each quintile share.
- Move 3: no CIs; the M1–GRM contrast mixes constraints and link; all comparisons show that scores differ, not which is more accurate.

**3.5 Sensitivity to the rater exclusion (2–3 sentences)** — F2.12; `tbl-sensitivity-rater-exclusion` [SUPP]. Refit with all 28 raters (9,077 ratings, 3,670 products): empirical reliability .68896 → .68837; model-based .96893 → .97142; over 3,669 common products *r* = .99994, mean |Δθ̂| 0.00204, **max 0.35026**, .00273 changing quintile; over 24 common raters a *r* = .99802, max |Δa| 0.19349. No evaluative adjective here.

### 4 Discussion (2,000–2,300 words; discussion model: revisit → map → contribution and implications → limitations/future; structured around RQ1–RQ3; every interpretive claim [ATC]; "in these data", "for this rater pool"; never "we have shown")

**4.1 Summary (1 paragraph).** Echo the three RQs descriptively: obtained reliability well below the full panel; one or two ratings insufficient and about four needed in simulation; raters differ in severity, scale use, discrimination and information; constraints rejected by LR/AIC but not BIC; raw means and model-based scores order actions partly differently. **C1:** "These results rest on the GRM, which had the lowest AIC and SABIC, whereas BIC favoured M1 by 4.161" (D1).

**4.2 RQ1: Reliability and the number of ratings per action [ATC-3, ATC-4, ATC-5, ATC-32, ATC-35, ATC-36]**
- The conventional figures describe the mean of a large or complete panel (.969; α .949); the scores actually obtained have .689 [.669, .703], and that is the figure that matters for their use [ATC-3]; Spearman–Brown logic (amabile1982). The contrast of Krippendorff's α for single ratings (.391) with the pairwise α (.949) illustrates that a high α can coexist with low single-rater agreement (kaufman2008a) and the consistency–agreement distinction (stefanic2015; cseh2019) [ATC-36; FI-17]. **C4: the crossed-block sentence is deleted (D3).**
- Observed by-n values: .522 and .699 with one and two ratings; rising overall, with the non-monotonic rows at ten and thirteen ratings resting on 14 and 1 products; observational, not causal (C3). Precision also varies within the same number of ratings and with θ (F1.17) [ATC-4]; rel_post with one or two ratings partly reflects the prior.
- **The number needed in this panel [ATC-35]:** the projection reaches .80 at four ratings (.834) and the top-up of the actual design to at least four ratings gives .835, which is also what the figure's reference line shows; under the stated assumptions (random raters each equally likely, known parameters, GRM-generated ratings) these describe this rater pool and scale. Observed means at three to seven, nine and ten ratings lie below the simulated range; possible readings (different quantities; products with several ratings were rated by particular raters, FI-4; small n) are offered as possibilities only [ATC-32].
- **Mapping to the cross-domain evidence, with target and object stated:** about four ratings for .80 in these product-level ratings by this pool sits between the two or three trained raters for short divergent-thinking responses (person-level relative G ≥ .80; silvia2008) and the ten or more lay raters for expert-domain products (α; kaufman2008a; kaufman2013) or 7–15 non-experts for design products (ICC ≥ .70; barth2021; terai2026) [ATC-31]. Three-rater sport panels (kempe2018; roca2018; memmert2010) and the four-coach panel of joode2023 fall at the lower end; whether licensed coaches need fewer ratings than this pool is untested here (expertise not analysed).

**4.3 RQ2: Raters differ [ATC-6, ATC-12, ATC-38]**
- Severity spans 2.247 logits under M1 (R24 to R06), larger than the ranges Primi et al. (2019) report for metaphor and divergent-thinking ratings (−1.18 to .64 logits; about 0.9) [ATC-38; FI-17]; severity differences confound raw means in incomplete designs (primi2019; hass2018).
- For raters with many ratings, differences in discrimination clearly exceed the SEs (R09 0.93, SE 0.15, vs R06 3.10, SE 0.45) [ATC-6]. **C5 wording:** "The largest standard errors belong to R18 for its thresholds and to R26, R19 and R27 for their discriminations, raters with 46–55 ratings; R26, R19 and R27 also have the widest information intervals. High discrimination is not confined to imprecisely estimated raters (R06, R25, R24), so the spread is not mainly estimation noise." Information shares are not a ranking of rater quality [ATC-12]. "One rating by the most informative rater carries as much information as several by the least informative" is a reading of 2.52 vs 0.13 and gets [ATC-12] if used.
- Threshold spacing is partly discrimination, so the raw response styles carry the model-independent scale-use evidence (unadjusted). Eight raters never used the top category; R27's internal gap (C7).
- Literature: long2015; engelhard1994; myford2003; myford2004; myszkowski2021 (central vs extreme responding; e.g., R13 vs R06) [FI-17]; primi2019 left rater-by-scale interactions to future work [FI-17]; hickey2001 (expert status alone does not guarantee consensus); storme2014 and ceh2022 (training and discernment as levers other than headcount); wind2018/wind2019 (linking) and reise1990 (parameter recovery) [FI-17].

**4.4 RQ3: Constraints and consequences for scoring [ATC-7, ATC-8, ATC-9, ATC-10, ATC-15, ATC-21, ATC-22, ATC-34]**
- **(i) Constraints.** The shared category structure concerns M1 only; M2 relaxes it (eckes2015). Equal discrimination, the constraint shared by the Rasch family, is rejected by the LR test and AIC but favoured by BIC; **C2 wording:** "both constraints were rejected by the LR test and AIC but not by BIC" — the criteria disagree on both. A possible explanation, for the author to confirm [ATC-34]: BIC's penalty grows with the number of parameters (GRM 158, M3 158, M2 135, M1 30), so it weighs heavily against rater-specific parameters as the panel grows. The M3 discriminations span 0.305 to 2.221 (ratio 7.277). **C10:** the M1 misfit pattern is consistent with discrimination differences surfacing as misfit (myford2004; myszkowski2021): R18 (GRM a 0.66) and R09 (0.93), the two lowest discriminations, are the raters above 1 under M1 together with R17; R12 (a 2.72) is lowest under M1 [ATC-9]. Step order is not evidence for either family (andrich1978; bond2020). GRM preferred by AIC and SABIC; cumulative link plausible for a unipolar scale (pellegrino2025) [ATC-8]. The M1–M2 test is cross-software; caveat stands.
- **(ii) Raw means.** Unweighted means treat raters as interchangeable (primi2019; myszkowski2019). Products with the same single rating received GRM scores on average 1.229 and up to 1.430 apart; with one rating the spread reflects the rater's modelled parameters only; with two ratings also the rating pattern (.066 reversals vs .041) [ATC-21, ATC-22]. Matters wherever actions are selected or ranked.
- **(iii) Model choice.** Correlations ≥ .977, yet .206 of products change quintile under M1 (mean shift .042) and .081 under M3 (.016); read together [ATC-10]. Do not rank (ii) against (iii).
- **Limit (C-M1):** the GRM is not a validated criterion; no accuracy claim [ATC-15, ATC-22].

**4.5 Designing creativity-rating studies for nonverbal, time-pressured products [ATC-30, ATC-31, ATC-5, ATC-14, ATC-15, ATC-16, ATC-23]**
- Scope sentence first: one pool of student raters, one 7-point scale, one product class [FI-21].
- Closing argument (the paper's contribution to general creativity assessment): (a) the required number of ratings is domain-specific — this study supplies the first rating-design figures for football actions, and they neither follow from nor transfer to verbal or static domains (cseh2019 open question; vanhooijdonk2022; long2022) [ATC-31]; (b) for products observed under time pressure in competition, single ratings agreed weakly (Krippendorff .391) while raters differed strongly in severity, scale use and discrimination, so panels of three or four without a rater model carry unquantified rater effects [ATC-30]; (c) model-based scoring changes orderings enough to matter for selection; (d) the calibration-set vs training distinction: training conflicts with the CAT rule of judgement without criteria (hennessey2011; storme2014; dollinger2005), a calibration set does not, and it stabilises parameters of raters with few ratings only if they rate it and it is large enough [ATC-14]; (e) about 50 ratings per rater (R17, R18, R19, R26, R27) still left parameters imprecise; no smaller number is recommended [ATC-16].
- **Box "Design recommendations for creativity ratings of actions in sport"** (every item [ATC-23]; each traceable to a finding; whether CRJ accepts boxes is FI-16):
  1. Report the reliability of the scores actually used and the agreement of single ratings, not only α or full-panel values (@tbl-reliability-overview: .689 vs .949 and .969; Krippendorff .391) [ATC-3, ATC-36].
  2. Plan the number of ratings per action with the precision of individual scores in mind: one or two ratings gave .522 and .699 here; in simulation from this panel at least four ratings per action were needed for .80 (@tbl-grm-reliability-by-n; @fig-grm-reliability-observed-vs-simulated; @tbl-grm-reliability-min-ratings) [ATC-5, ATC-35].
  3. Let all raters rate a sufficiently large common calibration set so that raters are linked and parameters of raters with few ratings are estimated more precisely (the present design was connected but used no such set) [ATC-14].
  4. Give each rater enough ratings for stable parameters; about 50 still left them imprecise here (@tbl-grm-rater-parameters; @tbl-rater-overview) [ATC-16].
  5. Raters differed in severity, thresholds and discrimination, and raw means ordered actions partly differently from model-based scores (@fig-m1-rater-severity; @tbl-raw-mean-vs-grm); consider a scoring model that adjusts for rater differences under its assumptions and report how far its ordering departs from the raw mean; this study does not show that model-based scores are more accurate [ATC-15, ATC-22].
  6. Treat these figures as specific to this product class, rater pool and scale; establish rating-design evidence anew for other nonverbal, time-pressured products [ATC-31].

**4.6 Limitations and future research**
- L1 Design and missingness: incomplete design, allocation [FI-4, FI-31]; ignorable missingness assumed; "not recognised" ratings removed [FI-22]; by-n reliabilities observational.
- L2 Simulation assumptions: random raters each equally likely (not the real workloads) [ATC-35]; parameters treated as known, so the ranges omit parameter uncertainty; GRM-generated ratings presuppose the model; the projection uses θ ~ N(0, 1); only k ≤ 10; no selected rater sets. The number needed is a figure for this panel.
- L3 Fit evidence limited [ATC-11]: S-X² conservative, C2 not computable, Q3 biased with no reference distribution, flags below 0.7 expected by design [ATC-33]; absence of detected misfit is not evidence of fit; **C1:** "the GRM had the lowest AIC and SABIC of the compared models, whereas BIC favoured M1; it is not a validated reference."
- L4 Model comparison: BIC disagrees with LR/AIC on both constraints [ATC-34]; M1–M2 cross-software with df 105 vs 115, reduced by categories never used incl. R27's internal gap (C7); M1–GRM mixes constraints and link.
- L5 Uncertainty and assumptions: raters with about 50 ratings imprecise; draw intervals conditional on valid draws; a normal latent distribution (standard normal in M3 and the GRM; estimated variance in M1 and M2) assumed although ratings concentrate at the low end (review N6-1 fix); response styles without uncertainty; no CIs for the agreement statistics; R27's thresholds not comparable.
- L6 Rater pool: one pool of students [FI-1, FI-21, FI-31]; domain familiarity not established; expertise not analysed (kaufman2009; kaufman2013; ceh2022; hickey2001).
- L7 Rater exclusion: technical criterion [FI-23]; largest change in a product score 0.35026 with *r* = .99994 (C12, D4) [ATC-26].
- L8 Two facets, one dimension: no time or session facet (barth2021; terai2026; leckie2011; myford2009; forthmann2017) [FI-3, FI-32]; no differential rater functioning (wind2019a); extensions patz2002; uto2020.
- Future research (compact list): a severity test on its own (model without rater effects vs MFRM); M1–M2 within one package; held-out predictive check of model-based vs raw-mean scores; projections with parameter uncertainty and selected or workload-weighted rater sets; a prospective calibration-set design; rater covariates incl. football expertise and coach panels; other sports and other nonverbal, time-pressured products; G- and D-study of the same data.

### 5 Conclusion (150–200 words; 1 paragraph) [ATC-1]
- In these data: obtained reliability .689 far below panel figures; one or two ratings insufficient, about four needed in simulation for this panel; raters differ in severity, scale use, discrimination and information; **C2:** "the shared category structure of M1 and equal discrimination were rejected by the LR test and AIC but not by BIC"; raw means and constrained models order actions partly differently from the GRM.
- Close with the design message for nonverbal, time-pressured products and the domain-specificity point: rating-design evidence has to be established per product class and rater pool; report the reliability of the scores used; plan ratings per action; link raters; consider rater-adjusting models and report their departure from raw means; accuracy remains to be examined [ATC-5, ATC-14, ATC-15, ATC-30, ATC-31].

### References
APA 7th via CSL; `phd_library.bib` only; not edited by the pipeline. Hand-typed names keep particles.

### Supplementary Material
Sections: Data and rater exclusion; Estimation and fit of the GRM; Reliability (observed); **Simulated reliability by number of ratings** (rename from "Projected reliability (side note)"; carries the assumption note with the projection table/figure, the observed-vs-simulated table); Rater parameters, information and category use; Adjacent-category ladder. Numbering S1, S2, … via crossref prefix (paper-config).

---

## Map of C1–C13 (new wording direction → where it lands)

| # | New wording direction (numbers from 03_findings) | Lands in |
|---|---|---|
| C1 | GRM lowest AIC and SABIC; BIC lowest for M1 (28,235.202), GRM 4.161 above; GRM and M3 same parameters (158), GRM lower by 49.381 on all three; "not a validated reference" | 3.1; 4.1; 4.4(i); 4.6 L3; D1 |
| C2 | "rejected by the LR test and AIC but not by BIC" for both constraints; add M1 vs M2 BIC 28,235.202 vs 28,256.560 and AIC 28,048.971 vs 27,418.524; abstract "BIC favoured the constrained models in both cases"; BIC-penalty explanation [ATC-34] | Abstract; 3.4 A; 4.4(i); 4.6 L4; Conclusion; D2 |
| C3 | overall rise with named exceptions (.897 at 10 after .915 at 9; .947 at 13 after .948 at 12); rows 10–13 on 14, 4, 2, 1 products; 3-rating row 68 products; no mean reached .969; observational | 3.2(2); 4.2 |
| C4 | crossed-block "lay close" sentence deleted (D3); α .750 [.684, .800] (3 raters, 261 products) reported in 3.2(1) with "refers to" only; ATC-13 retired | 3.2(1); 4.2 |
| C5 | extremes: a 3.19 R26 (46, SE 1.72), then R06 3.10 (520, SE 0.45), R27 3.04, R25 3.01, R24 2.89; lowest R18 0.66, R09 0.93; R16 2.47 (268, SE 0.26) never "few ratings"; largest SEs R18 (thresholds) and R26, R19, R27 (discrimination); widest intervals R26, R19, R27; spread not mainly noise; "for example R18" for the score range | 3.3; 4.3; 4.4(ii) |
| C6 | θ at maximum R01 2.800, R16 2.400, R06 2.300; "never used category 7" only for R01 and R06 or dropped; lowest R13 −0.600; R06 .001 at θ = −2, .082 at 2; R12 .137 at θ = −2, R24 .120 | 3.3 |
| C7 | R27 internal gap (categories 5 and 7); eight raters with unused categories; thresholds 4 (R17, R27), 5 (R01, R03, R06, R18, R25, R26), 6 (others); df 105 vs 115 reduced by "categories raters never used (unused end categories and any internal gap)"; R27's thresholds not compared | 2.6; 2.8; 3.3; 4.3; 4.6 L4/L5 |
| C8 | raters R01–R19 and R23–R27; excluded R20, R21, R22, R28; IDs not in workload order; "student raters" reconfirmed [FI-1, FI-31] | Abstract; 2.2; 2.6; every rater list |
| C9 | "the entry with the latest timestamp was kept"; 21 pairs, 1 conflicting, 22 rows removed | 2.6 |
| C10 | M1 above 1: R09 (1.083/1.060), R17 (1.323/1.167), R18 (1.170/1.231); R12 lowest (0.260/0.278); account with R18 (a 0.66) and R09 (0.93), illustrative | 3.4 B; 4.4(i) |
| C11 | mean Q3 −.202 over 222 pairs; 28 flagged; of ten shown, 8 negative, 2 positive (R09–R23, R10–R11) | 3.1 |
| C12 | *r* = .99994; mean 0.00204; max 0.35026; .00273 quintile; "nearly unchanged on average, with a largest change of 0.35026" (D4) | 2.6; 3.5; 4.6 L7 |
| C13 | collection facts → FI-3 (no timing claims for R03, R06, R13), FI-4, FI-31, FI-32; no unconfirmed allocation rule | 2.4; 2.5; 4.6 L1 |

Stale strings to search after writing (§8): `7,820`, `3,668`, `9,148`, `1,290`, `7,844`, `.672`, `.960`, `.928`, `.658`, `.392`, `.520`, `.698`, `.815`, `.842`, `0.16246`, `R20 to R22`, `R01 to R19`, `last entry`, `No rater had`, `lowest AIC, BIC`, `all information criteria`, `each further rating`, `lay close`, `side note`, `by convention`, `has to be established for each domain`, `no evidence`.

---

## Figure/table plan (53 labels)

**MAIN 14 (9 tables, 5 figures) · SUPP 34 (20 tables, 14 figures) · not embedded 5.**

### Main text (14)

| # | Label | Section | Role |
|---|---|---|---|
| 1 | `tbl-design-summary` | 2.6 | final data, single place for the design numbers |
| 2 | `tbl-model-fit` | 3.1 | model choice (C1) |
| 3 | `tbl-reliability-overview` | 3.2 | RQ1: all indices incl. the min-4 row |
| 4 | `tbl-grm-reliability-by-n` | 3.2 | RQ1: observed by number of ratings, with n and PSD (C3) |
| 5 | `fig-grm-reliability-observed-vs-simulated` **(new)** | 3.2 | RQ1: observed dots, simulated line/band, min-4 and full-panel lines |
| 6 | `tbl-grm-reliability-min-ratings` **(new)** | 3.2 | RQ1: top-up design; quotable source of .835 and the check row |
| 7 | `fig-overview-rater-response-styles` | 3.3 | RQ2: raw response styles |
| 8 | `tbl-rater-overview` **(new)** | 3.3 | RQ2: one row per rater (severity, a, share CI, fit flags, gaps) |
| 9 | `fig-m1-rater-severity` **(new)** | 3.3 | RQ2: severity with intervals next to raw means |
| 10 | `tbl-grm-rater-parameters` | 3.3 | RQ2: a and b_k with SEs |
| 11 | `fig-grm-rater-discrimination-ci` **(new)** | 3.3 | RQ2/RQ3a: a with intervals; one value under M1/M2 |
| 12 | `tbl-raw-mean-vs-grm` | 3.4 | RQ3b |
| 13 | `fig-raw-mean-vs-theta` | 3.4 | RQ3b |
| 14 | `tbl-score-agreement` | 3.4 | RQ3b |

### Placement decisions (reasons)
- **Added to MAIN per brief §F:** `fig-grm-reliability-observed-vs-simulated`, `tbl-grm-reliability-min-ratings`, `fig-m1-rater-severity`, `fig-grm-rater-discrimination-ci`, `tbl-rater-overview`.
- **Retired from MAIN → SUPP: `tbl-grm-rater-information-ci`.** Reason: `tbl-rater-overview` now shows each rater's share of panel information with its interval in the main text; the information-per-rating values quoted in 3.3 are traceable to the SUPP table; this keeps the main text at 14 objects after five additions (D8).
- `fig-design-ratings-per-product` → **SUPP**: the per-k counts are needed to read RQ1 but `tbl-design-summary` already carries the design in the main text; `fig-overview-degree-distributions` stays (panel B, ratings per rater, is not shown elsewhere).
- `fig-category-usage-shares` → **SUPP**: the main text already has `fig-overview-rater-response-styles` for raw scale use; author option: swap the two (the shares figure is more legible for 24 raters and marks unused categories) (D8).
- `fig-grm-rater-information-ci` → **SUPP**: plots the table's column.
- `tbl-grm-reliability-observed-vs-simulated` → **SUPP**: the figure is in the main text; the table is the quotable source of the per-k values shown in it (figure-annotation rule).
- `tbl-discrimination-summary` → **SUPP**, directly after `tbl-discrimination-m3`: source of the 7.277 ratio and median 1.240 quoted in 3.4.
- Unchanged: `tbl-grm-reliability-projection` and `fig-grm-reliability-projection` SUPP (quoted in 3.2(3)); `tbl-lr-tests` SUPP (values quoted); `tbl-theta-correlations`, `tbl-sensitivity-rater-exclusion` SUPP.
- Space-saving fallbacks if CRJ limits bite (FI-16): move `tbl-grm-reliability-by-n` to SUPP (the figure and the SUPP observed-vs-simulated table carry the per-k values) and `fig-raw-mean-vs-theta` to SUPP.

### Supplement (34)
- Tables (20): `tbl-excluded-raters`, `tbl-sensitivity-rater-exclusion`, `tbl-overview-rater-response-styles`, `tbl-category-usage`, `tbl-grm-convergence`, `tbl-grm-rater-fit`, `tbl-grm-q3-flagged`, `tbl-grm-reliability-ci`, `tbl-grm-reliability-summary`, `tbl-naive-indices`, `tbl-grm-reliability-projection`, **`tbl-grm-reliability-observed-vs-simulated`**, **`tbl-grm-rater-information-ci`** (from MAIN), `tbl-grm-information-summary`, `tbl-lr-tests`, `tbl-discrimination-m3`, **`tbl-discrimination-summary`**, `tbl-threshold-order`, `tbl-rater-fit-m1`, `tbl-theta-correlations`.
- Figures (14): **`fig-design-ratings-per-product`**, `fig-overview-rating-distribution`, `fig-overview-degree-distributions`, **`fig-category-usage-shares`**, `fig-grm-rel-post-by-n`, `fig-grm-reliability-projection`, `fig-grm-rel-post-histogram`, `fig-grm-rel-post-by-theta`, `fig-grm-rel-consistency`, `fig-grm-panel-information`, `fig-grm-category-response-functions`, `fig-grm-rater-information`, `fig-grm-information-shares`, **`fig-grm-rater-information-ci`**.

### Not embedded (5)
`tbl-cleaning-log` (cleaning in text); `tbl-marginal-reliability-models` (author decision of round 6; the M1–M3 marginal reliabilities .957/.957/.965 appear in `tbl-reliability-overview`); `tbl-grm-global-fit` (Method 2.9 says the same); `tbl-overview-ratings-per-action` (duplicates `tbl-design-summary` and the new figure); `fig-overview-rater-overlap` (design display).

### Notes for the writer
- Embeds by label; NB02 cell ids changed but labels did not. One new embed each for the ten new labels per the lists above; `tbl-grm-rater-information-ci` moves from Results to the Supplement.
- Supplement section "Projected reliability (side note)" becomes "Simulated reliability by number of ratings"; its note states the assumptions (Method 2.10 wording) and names the top-up design too.
- `number-sections: false` stays; section numbers here are for orientation.
- Abstract: no rendered markers; ≤ 250 words.
- Display items for the analyst (FI-18): "Q1 0.596, Q3 0.769" note in `tbl-reliability-overview` must read "first and third quartiles 0.599, 0.789" (values from the new run); code-name labels; `tbl-discrimination-summary` row labels ("q1", "ratio max min"); glyphs ⚑ and ✕ in PDF font; `fig-m1-rater-severity` colours not in caption; `tbl-rater-overview` "Ratings" without separator and "%" only on the estimate; `tbl-lr-tests` caption says only "end categories" (note is correct).

---

## Effect sizes and uncertainty: inventory

| Quantity | Uncertainty | Where |
|---|---|---|
| Empirical / model-based marginal reliability | 95% intervals, 200 accepted draws (43 rejected) | F1.12 |
| Observed rel_post by n | means/medians only, no CIs | F1.14 |
| Projection by k; top-up | 95% range over 50 replications; parameters treated as known | F1.20, F1.21 |
| Cronbach's α (pairwise; block), Krippendorff's α | bootstrap CIs; pairwise approximate (647 of 1,000) | F1.18 |
| M1 severity | SEs drawn; printed only for R24 and R06 | F2.8, F2.8a |
| GRM a, b_k | Oakes SEs | F2.1, F2.2 |
| Average information, share | 95% intervals (same draws) | F2.5 |
| M3 discriminations | SEs; summary without SEs | F1.4, F1.4a |
| Model comparison | Δ criteria; LR χ², df, *p* < .001 | F1.1, F1.2 |
| θ correlations; score agreement; raw mean vs GRM; sensitivity | point values, no CIs | F2.10–F2.13 |
| Response styles | none | F0.9 |

---

## FILL IN items (15 open)

- **FI-1** Raters and ethics: recruitment, number at start, consent, ethics approval; confirms "student raters" in the abstract.
- **FI-2** Products: competitions, matches, selection rule, clip length, source, number of matches.
- **FI-3** Procedure: software; verbatim instruction and definition; anchors; "not recognised" wording; randomisation, sessions and breaks (no timing claims for R03, R06, R13); other dimensions.
- **FI-4** Allocation of products to raters; how products came to have 1, 2 or 3+ ratings, including the latest collection; whether products with different numbers of ratings were rated by different raters; bears on ATC-32 and L1.
- **FI-6** Software versions.
- **FI-9** Why R26, R19, R14, R02, R12 and R27 were not usable for the pairwise α; which three raters form the crossed block (not printed; not quotable without the author).
- **FI-15** Preregistration; data and code availability.
- **FI-16** CRJ requirements: abstract limit, word count (the Introduction grew), figure/table limits (14 main objects), supplement policy, boxes, heading format, APA manuscript format.
- **FI-17** Citation checks against the PDFs (new items in bold): wef2025; safardilha2019 (key quality; "thinking expressed verbally or through drawing"; process-over-action); batey2012; barbot2019b; kaufman2008 "five to ten"; **kaufman2008a: "mask" point, α .83/.94, Spearman–Brown .575 for ten novices, r .22, list of typical CAT tasks**; **cseh2019: number of judges as an open question (no "must be established per domain"); 2–134 judges; consistency vs agreement**; **silvia2008, kaufman2007, barth2021 (excerpts), terai2026 (abstract), long2015, long2022, hass2018, vanhooijdonk2022, kaufman2013 values as used**; **saidmetwaly2017b, reiterpalmon2019, paca2019 (= Snyder et al. 2019) characterisation**; **orth2017, hristovski2011, hristovski2012 (author field), vaughan2019, rasmussen2019, raab2007, memmert2011b, cotter2019 (author field Cotter & Silvia) characterisation**; **kempe2018 (scale 0–10 vs 1–10, reliability index, training), roca2018, memmert2010, joode2023 (3–4 coaches, ICC, averaging), zahno2023/zahno2024 (panel sizes)**; primi2019 (severity ranges −1.18 to .64 and 0.9; workload cut by a third; rater-by-scale interactions left open); myszkowski2021 (central vs extreme); pellegrino2025 (GRM retained); barbot2023 (model); forthmann2025 and goecke2024 (planned-missing designs); **stefanic2015; hickey2001; storme2014; ceh2022**; eckes2015 (partial-credit MFRM); wind2018/wind2019; reise1990; looney2004/anderlucci2021/heiniger2021 only if kept (now optional).
- **FI-18** Display fixes before render (see "Notes for the writer").
- **FI-21** Rater-pool description (also for the raters who joined later).
- **FI-22** Non-recognition rate by rater (and product).
- **FI-23** Source/rationale for the 15-rating exclusion criterion.
- **FI-31 (new; D5)** Raters R23–R27: same student pool? how were actions allocated to them? (feeds 2.2, 2.5, L6).
- **FI-32 (new; C13)** Data-collection period as a sentence in 2.4 (not printed in the notebooks; author-supplied).

**Closed or retired:** **FI-19 retired** (data freeze confirmed, brief §C). FI-30 closed (round 5). FI-11, FI-12 retired. FI-20, FI-24–FI-29, FI-5, FI-7, FI-8, FI-10, FI-13, FI-14 closed earlier.

## AUTHOR TO CONFIRM claims (32 open)

Reworded items are marked (rw); new items are ATC-28 onward.
- **ATC-1** Central contribution in three parts incl. the number needed (rw).
- **ATC-2** (rw) Gap and novelty: rating-design evidence for sport actions is lacking; no JRT/IRT application to ratings of sport actions was located (web and vault search, not a database search); abstract "little rating-design evidence".
- **ATC-3** Conventional indices describe a panel mean; the empirical marginal reliability is the relevant figure.
- **ATC-4** Precision depends on the number of ratings, the raters and θ; no "mainly".
- **ATC-5** (rw) Practical reading: one or two ratings give limited precision; plan several ratings per action; "about four" from the simulations under their assumptions.
- **ATC-6** (rw) Raters differ substantially; differences exceed SEs for well-estimated raters; spacing is partly discrimination; "higher b = stricter" gloss for GRM thresholds.
- **ATC-7** Raw means confounded with severity in incomplete designs; shared category structure concerns M1 only; equal discrimination rejected by LR/AIC not BIC; severity not tested on its own.
- **ATC-8** GRM preferred by AIC/SABIC; cumulative link suits a unipolar scale.
- **ATC-9** (rw) M1 misfit pattern (R18, R09, R17 above 1; R12 lowest) consistent with discrimination surfacing as misfit; illustrative.
- **ATC-10** Model choice: high correlations yet ranking shifts that matter; mean shift read with quintile share; M1–GRM mixes constraints and link.
- **ATC-11** Fit evidence limited; pairwise α CI possibly biased; absence of misfit is not fit.
- **ATC-12** (rw) Information shares are not a ranking of rater quality; largest SEs R18 (thresholds), R26/R19/R27 (discriminations); "one rating by the most informative rater equals several by the least informative" if used.
- **ATC-14** Calibration set, conditional, distinct from training.
- **ATC-15** Scoring recommendation "consider"; no accuracy claim.
- **ATC-16** (rw) Enough ratings per rater; about 50 (R17, R18, R19, R26, R27) not enough; 15 never recommended.
- **ATC-18** Realised design vs planned benchmark set (if any).
- **ATC-19** Showing a definition departs from the CAT rule.
- **ATC-20** Exploratory framing; RQ wording incl. the new RQ1 and the severity promise in RQ2.
- **ATC-21** θ̂ range at equal raw mean reflects threshold location and discrimination of the raters; with 2+ ratings also rating patterns; set by extreme raters.
- **ATC-22** Within-n reversals matter for selection; part of the 2-rating reversals is rating pattern.
- **ATC-23** (rw) Box: selection and wording of all six items.
- **ATC-26** (rw) Exclusion sensitivity wording "nearly unchanged on average … largest change 0.35026" (D4).
- **ATC-28 (new)** C-A: "rating-design evidence comes largely from verbal material and static products inspected at leisure" — qualitative, no percentage; anchors as in P6.
- **ATC-29 (new)** Which key carries "divergent thinking in sport": memmert2011 (JSS), memmert2013, or memmert2011b (Encyclopedia chapter, states the DT equation).
- **ATC-30 (new)** The closing argument: what these results say about designing creativity-rating studies for nonverbal, time-pressured products (4.5, Conclusion, abstract implication).
- **ATC-31 (new)** The domain-specificity conclusion: required rater numbers are conditional and do not transfer across product classes; this study provides the figures for football actions; mapping of "about four" against silvia2008 / kaufman2013 / barth2021 / terai2026 with targets and objects stated.
- **ATC-32 (new)** Any reading of observed vs simulated values (observed below the simulated range at k = 3–7, 9, 10; "close" for .686 vs .689): the notebook makes no comparison; offered readings are possibilities.
- **ATC-33 (new)** Flags below 0.7 read as "expected rather than misfit" given about two ratings per product.
- **ATC-34 (new)** BIC explanation: penalty grows with the number of parameters (158/158/135/30), so BIC weighs against rater-specific parameters as the panel grows.
- **ATC-35 (new)** Use of the simulations as RQ1 evidence: "smallest k reaching .80 = 4", min-4 .835, and the assumption statement incl. "each rater equally likely, so the draws do not reproduce actual workloads" as the authors' Method description.
- **ATC-36 (new; from retired ATC-13)** Krippendorff .391 vs Cronbach .949 illustrates kaufman2008a's point and the consistency–agreement distinction (stefanic2015; cseh2019).
- **ATC-38 (new)** Severity span 2.247 logits as substantial, compared with primi2019's ranges; "lenient–strict" reading of M1 severity.

**Closed:** **ATC-13 retired** (crossed-block closeness; C4). ATC-17, ATC-24, ATC-25, ATC-27 closed earlier.

---

## Decisions for checkpoint 1

Proposed answers from the brief (§D) and this outline:
- **D1** Keep the GRM as the scoring model: **yes**; state that BIC favours M1 by 4.161; rely on the M1–GRM comparison (*r* = .977; .206 changing quintile).
- **D2** Wording "rejected by the LR test and AIC but not by BIC" for both constraints, abstract "BIC favoured the constrained models in both cases": **acceptable**.
- **D3** Crossed-block "lay close" sentence: **delete**; ATC-13 retired.
- **D4** Exclusion sensitivity: **rephrase** to "nearly unchanged on average (*r* = .99994, mean absolute change 0.00204), with a largest change in one product score of 0.35026"; ATC-26 remains at the sentence.
- **D5** New raters R23–R27: pool and allocation → **FI-31** (with FI-1, FI-4); the abstract keeps "student raters" only if confirmed.
- **D6** `preliminary_draft/manuscript.qmd` and `submission/3_PACA.md`: **not touched**; listed in author_todo with the stale values (19 raters, 7,820 ratings, 3,668 products at 3_PACA line 18; draft lines 8, 69, 85, 87, 89, 115, 121, 125, 131).

New decisions raised by this outline:
- **D7 Title:** keep the current title (recommended); alternative offered above.
- **D8 Main-text objects:** add the five objects of §F; **retire `tbl-grm-rater-information-ci` to SUPP** (reason stated); `fig-category-usage-shares`, `fig-design-ratings-per-product`, `fig-grm-rater-information-ci`, `tbl-grm-reliability-observed-vs-simulated`, `tbl-discrimination-summary` to SUPP; MAIN 14 / SUPP 34 / not embedded 5. Option: swap `fig-category-usage-shares` for `fig-overview-rater-response-styles` in the main text. Fallbacks for space: `tbl-grm-reliability-by-n`, `fig-raw-mean-vs-theta` to SUPP.
- **D9 RQ1 headline:** use "smallest k with simulated empirical reliability ≥ .80 = 4" (printed) and the top-up value .835 as the headline of RQ1 in the abstract, 3.2, 4.2 and box item 2, with the assumptions stated in Method 2.10 and L2 (recommended: yes) [ATC-35].
- **D10 Cite myszkowski2025** in the JRT applications list (one clause; rubric-coded PISA responses, generalized IRTree): recommended yes; myszkowski2026 and beaty2026 are not imported and not cited.
- **D11 NEEDS IMPORT:** none essential. fardilha2020 exists as `safardilha2019` (year 2020); memmert2015/memmert2017 are cited only through safardilha2019; brown1967/harrison2016 are second-hand and not needed; johnson2003 not needed (raab2007 carries the time-pressure point).
- **D12 Abstract content:** the numbers listed in the Abstract plan (.689/.969; .522/.699; "at least four"; 2.247 logits; .579–.016; τ-b .833/.818) within 250 words; drop order if over the limit: τ-b clause, severity span.
- **D13 Design wording:** the sparse design is named once in Introduction Move 5 and described in Method 2.5 (brief §B5); the old rule "never foreground the sparse design" is relaxed to this extent; no "most products were rated only once or twice" framing outside the Table.
- **D14 Cross-domain detail in the Introduction:** state the per-domain figures from 07 in prose with targets and objects (recommended) rather than only in summary form; about 200 words of Move 2.
- **D15 Box item 6** (domain-specificity recommendation) added to the box: keep or merge into item 2.
- **D16 `tbl-marginal-reliability-models`:** stays unembedded (round-6 author decision); confirm.

---

## Evidence gaps

- **RQ1.** Supported by F1.12, F1.14, F1.18, F1.20, F1.20a, F1.21, F1.22. Gaps: by-n values observational, without CIs, and not separating the number of ratings from which raters gave them (FI-4); the simulations treat parameters as known, draw raters with equal probability and cover k ≤ 10 only; the notebook prints no comparison between observed and simulated values (ATC-32); .70 and .90 thresholds are not printed; the three crossed-block raters are not named (FI-9).
- **RQ2.** Well supported for well-estimated raters (SEs, intervals, printed severity range). Gaps: M1 severity SEs printed only for R24 and R06 and no severity test; raters with ≤ 55 ratings imprecise; response styles unadjusted and without uncertainty; R27's thresholds not comparable; the "x-fold" reading of 7.277 is a rounding.
- **RQ3.** Supported by F1.1, F1.2, F1.4a, F2.11, F2.13. Gaps: BIC disagrees with LR/AIC on both constraints; M1–M2 cross-software with reduced df; no accuracy criterion (hence "consider"); no CIs for agreement statistics; the BIC-penalty explanation is a hypothesis (ATC-34).
- **Introduction claims.** C-A has no quantitative review behind it (qualitative wording, ATC-28). C-C's second half rests on four studies (three or four coaches); zahno2023/2024 panel sizes unverified (FI-17). Several 07 values are at verification level "excerpts" or "abstract" (silvia2008, kaufman2007, barth2021, terai2026, kaufman2008a's "mask" wording, long2015) → FI-17. The "no rater-number study for sport" statement is a search result with a scope note, not a proven absence.
- **Methods.** FI-1–4, 6, 9, 15, 21–23, 31, 32 open; the paper cannot be submitted before they are filled.
- **Out of scope.** Rater expertise and training; scale design; MFRM fair averages (EAP only); G- and D-study of these data.

---

## Conflicts found and how this outline resolves them

1. Brief §D1 "BIC favours M1 by 4.16" → the printed value is 4.161 (F1.1); quote 4.161.
2. Brief §B3 "about three raters by convention" → coordinator correction wins: "three or four licensed coaches, ratings averaged, agreement reported as ICC" (kempe2018, memmert2010, roca2018, joode2023); no "by convention".
3. Brief §B2 "random panels of 10 novices average α ≈ .53–.66" → 07's resolution: .58 (.575) is Kaufman et al.'s (2008) Spearman–Brown projection for poetry, .53 the ten-novice mean for stories and .66 for engineering designs in Kaufman et al. (2013); attribute accordingly, and say "projection" for kaufman2008a.
4. Concept note, old outline and old manuscript attribute "the number of raters has to be established for each domain" to cseh2019 → 07's binding caveat wins: Cseh and Jeffries list it as an open question; domain-specificity is argued via vanhooijdonk2022 and the cross-domain evidence. FI-17 item changed accordingly; the stale paraphrase is on the stale-string list.
5. Brief §C "raters drawn at random with equal probability regardless of their real workload" vs 03_findings (the notebook says only "each equally likely"; the "regardless of workload" wording is the report's) → stated as the authors' own methodological description (it follows from equal drawing probability), not as a notebook quotation, with ATC-35.
6. Revision instructions C4 name the crossed-block raters (R07, R11, R23) and C13 the collection span (2025-10-09 to 2026-11-02) → neither is printed in a notebook; both become author items (FI-9, FI-32), not quoted from §5/§3.
7. Brief §B5 names a "sparse design" in the present-study move vs the old rule "the sparse design is not foregrounded" → relaxed to one mention (D13).
8. Old outline: RQ2 did not promise severity because no severity measure was printed → the new `fig-m1-rater-severity`, `tbl-rater-overview` and the printed range make severity reportable; RQ2 now includes it (ATC-6, ATC-38).
9. Brief §A1 "pull every result shown in `jrt_results_summary.qmd`" vs 03_findings' never-quote list → everything is now available except the md5, the report's "Assumes/Answers" texts, its roundings and the interpretive "one rating by the top rater carries as much as several" (which becomes an ATC-12 reading of printed values, not a quoted result).
10. `02_artifacts.md` lists the old NB02 cell ids and 52 labels in its main table; its Delta section adds `tbl-discrimination-summary` (53) → embeds use labels, so nothing breaks; the writer must take the embed line for the new table from the Delta.
11. Review N6-1 ("standard normal" in Limitations) → L5 wording fixed in this outline so the writer does not regress.

---

## Changes in this revision (summary)

- New five-move Introduction architecture (1,500–1,800 words) with the cross-domain rater-number evidence, the verbal-bias and sport-case moves, the methods ladder and the present study; IRT tutorial moved to Method 2.7.
- RQ1 reworded to include the number of ratings needed (observed and simulated); RQ2 includes severity; RQ3 split (a)/(b).
- Results in RQ order with the two simulations and five new main-text objects; Discussion restructured around RQ1–RQ3 and closing with the nonverbal/time-pressure and domain-specificity arguments; box updated (six items).
- C1–C13 mapped; stale-string list extended.
- Objects: MAIN 14, SUPP 34, not embedded 5 (total 53); `tbl-grm-rater-information-ci` retired to SUPP with reason.
- FI: 15 open (FI-19 retired; FI-31, FI-32 new; FI-17 extended). ATC: 32 open (ATC-13 retired; ATC-28–36 and ATC-38 new; ten reworded).
- Decisions D1–D6 with proposed answers; new D7–D16.
