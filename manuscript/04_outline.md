# 04_outline.md: Argument architecture (Phase 5), GRM/JRT version

> **Approved at checkpoint 1 (2026-10-23, relayed via coordinating session); updated for commit a97e51d.**

Profile: `imrad-apa`. Venue: *Creativity Research Journal*. Style: APA 7th.
Structure: Abstract, Introduction, Method, Results, Discussion, Conclusion, References.

Sources (all re-read for this update):
- Brief: `~/drive/KNOWLEDGE/Paper_CreativityAssessmentInSportsCAT.md`
- Dossier: `01_dossier.md`
- Labels: `02_artifacts.md` (regenerated after commit a97e51d; **40 labels**, including the new `tbl-raw-mean-vs-grm` and `fig-raw-mean-vs-theta`)
- Numbers: `03_findings.md` (regenerated after commit a97e51d; finding IDs stable; **new F2.9 and F2.10**). This is the ONLY source of numbers.
- Citekeys: `06_web_literature.md`, including the section "Targeted search 2026-10-23 (GRM methods)". Every key used below was checked by grep in `phd_library.bib` or `web_references.bib` during the checkpoint-1 revision. No Bayesian references are used.

Conventions in this file:
- **F…** is a finding ID in `03_findings.md`. Every number below is copied from there exactly, as printed.
- `tbl-…` and `fig-…` are labels from `02_artifacts.md`. **[MAIN]** means embedded in the main text. **[SUPP]** means embedded in the online supplement.
- **[ATC-n]** marks an interpretive or contribution claim that the author must confirm.
- **[FI-n]** marks a FILL IN item: information or an output that is missing and must come from the author or analyst. A FILL IN that needs a number is only usable after it has been added to a notebook and passed through results-interpreter. FI numbers are kept stable; resolved items are listed as resolved, not renumbered.
- **[DD]** marks a **design-dependent number**. These are counts, coverage and every value that will change when more ratings are collected. The author will add ratings (at least 2 per action, as many as possible) before finalising.
  - The writer cites each [DD] number from its finding or embed and never builds framing on it. Avoid wording such as "most products were rated only once or twice" or "in this sparse design".
  - Practically, every Results number is [DD]. The tag marks the places where the *prose* would otherwise hard-code the current design.
- Values marked NOT IN NOTEBOOK in `03_findings.md` are never used. This includes the count of unused end categories behind the LR df gap ("6", AUDIT.md only), any infit/outfit misfit range (e.g. 0.7–1.3, REPORT.md only), RMSEA or any other global fit index, and the definition of a "computable" Q3 pair.
- Numbers are quoted **as printed** and never rounded by the writer. The response styles (F0.8) are now printed at 3 decimals and are quoted at 3 decimals; the earlier 6-decimal values must not be quoted. The sensitivity values in F2.8 are printed with 5 decimals and are quoted that way.
- **Timing (OD7):** drafting proceeds now with the current [DD] values; every [DD] value is refreshed after the data update [FI-19].

---

## Working title (D1; OD1: kept)

**Number of ratings, rater differences, and score reliability in creativity ratings of football actions: A judge response theory analysis**

The author kept this working title at checkpoint 1. It follows the three aims, uses retrievable keywords (creativity ratings, football, judge response theory, reliability, rater differences) and does not mention the design's sparsity.

Alternatives (kept for reference only):
- (b) *Rater differences and score reliability in consensual creativity ratings of football actions: A judge response theory analysis*
- (c) *Modeling rater differences in creativity ratings of football actions with judge response theory*

## Terminology (D2)

- **Raters.** Say once, at the first mention of the CAT in the Introduction (P3), that the CAT and JRT literature calls raters "judges". Use **"rater"** everywhere after that. "Judge" survives only in the fixed term *judge response theory* (JRT) and in quotations.
- **Product / action.** "Product" is the analytic term. It is introduced once in Method 2.3: "each rated product was a single football action".
  - "Action" appears in the title, in the Introduction's sport framing and in the description of the stimulus material.
  - In RQ1 and the practical implications, the first mention may read "ratings per product (i.e., per action)". After that, use "ratings per product".
- **Notebook terms.** NB01 captions and axis text now say "products" (resolved). "Action" survives only in the label `tbl-overview-ratings-per-action` (not embedded) and in NB00 (`action_id`, `tbl-cleaning-log`, not embedded). Do not edit captions in the manuscript.

---

## Central contribution [ATC-1]

The study applies judge response theory (JRT) to CAT-style creativity ratings of football actions. The final data are given in @tbl-design-summary (F0.3 [DD]). The study demonstrates three things.

1. **The number of ratings governs the reliability of the scores actually used.**
   - The reliability of the product scores obtained with the ratings each product actually received is the empirical marginal reliability: 0.672 [0.649, 0.687] (F1.12 [DD]).
   - This is far below the model-based reliability of a hypothetical full panel, 0.960 [0.953, 0.968], and below the pairwise Cronbach's α of the unweighted rater mean, 0.928 [0.891, 0.943] (F1.12, F1.18 [DD]).
   - Product-level reliability rises with the number of ratings per product: mean rel_post 0.520 at one rating, 0.698 at two, 0.810 at four, up to 0.919 at ten (F1.14 [DD]). This is an observational comparison.
2. **Raters differ substantially in how they rate creativity.** The differences appear in every parameter, and their uncertainty is quantified.
   - Severity: first thresholds b1 range from −6.565 to 0.295 (F2.2).
   - Discrimination: 0.631 to 3.709 (F2.1).
   - Category use and response styles: raw means range from 1.760 to 3.836, and floor rates from 0.016 to 0.579 (F0.8).
   - Information per rating: 0.123 to 3.539, with 95% intervals that are wide for raters with few ratings (F2.4).
3. **Treating raters as equivalent does not hold, and it changes the scores.**
   - Likelihood-ratio tests reject a shared category structure and equal discrimination (F1.2). AIC supports the second step; BIC does not (F1.1).
   - Scoring products by their raw mean rating, as common practice does, moves 0.350 of products to another quintile relative to the GRM score (Pearson 0.906, Spearman 0.932; F2.9 [DD]).
   - Product rankings under the MFRM/RSM also differ from those under the retained GRM: 0.202 of products change quintile, although Pearson r = 0.975 (F2.7 [DD]).

Implication for sport-science creativity research [ATC-5, ATC-14, ATC-15]: plan the number of ratings per action for a target score reliability, link raters through a common calibration set, and model rater differences (JRT) instead of averaging ratings.

## Core argument (5 sentences)

1. Reliability of CAT ratings is conventionally reported as the consistency of a mean over a panel of raters, and it grows with panel size (amabile1982; kaufman2008; cseh2019). In applied studies that rate many actions, however, each action receives only a certain number of ratings, so the precision of each score depends on that number and on which raters gave them.
2. JRT treats raters as items with their own severity, scale use and discrimination (myszkowski2019; myszkowski2021). The fitted model therefore gives (a) the reliability of the scores actually obtained, for each product and in total, and (b) an explicit, uncertainty-quantified description of how raters differ.
3. In the football ratings:
   - the reliability of the actual scores is well below the full-panel value and rises with ratings per product (F1.12, F1.14);
   - raters differ widely in severity, scale use, discrimination and information (F0.8, F2.1–F2.4).
4. The Rasch/MFRM constraints that would make raters interchangeable are rejected (F1.2). Scoring by the raw mean, which ignores rater differences altogether, shifts product rankings more than any of the model choices does (F2.9 vs F2.7), and the scoring model chosen also shifts rankings noticeably even when overall correlations are high (F2.7).
5. Rater differences therefore need to be acknowledged in the design (ratings per action, a common calibration set) and in the scoring (JRT rather than averaging) of creativity research in sport [ATC-3, ATC-6, ATC-7].

## Research questions (D3: exploratory; no confirmatory hypotheses)

The analyses were not guided by hypotheses fixed before the analysis. The study is framed as **exploratory**, and the RQs below are answered descriptively. The writer must not use the words "hypothesis", "supported" or "confirmed" for them. The only exception is the D13 wording for the LR/AIC evidence (see RQ3). [ATC-20: confirm the exploratory framing and the RQ wording; FI-15: preregistration status.]

**Primary RQs (one per aim)**

- **RQ1 (aim 1): number of ratings and reliability.** How does the reliability of creativity scores depend on the number of ratings per product (i.e., per action)? How does the reliability of the scores actually obtained compare with the reliability of a hypothetical full panel and with conventional agreement and consistency indices?
  - Evidence: F1.12, F1.13, F1.14, F1.16, F1.17, F1.18.
- **RQ2 (aim 2): rater differences.** How do raters differ empirically in their rating behaviour? This covers severity (threshold location), scale use (threshold spacing, category use, response styles), discrimination, and their contribution to information. How precisely are these differences estimated?
  - Evidence: F0.6, F0.7, F0.8, F2.1, F2.2, F2.3, F2.4, F2.5.
- **RQ3 (aim 3): do rater differences need to be modelled?** Two questions:
  - (a) Are the constraints that treat raters as equivalent tenable for these ratings? These are a shared category structure (RSM/MFRM) and equal discrimination (PCM).
  - (b) How far do product scores and rankings change when rater differences are ignored (raw mean ratings) or constrained (RSM/MFRM, PCM, GPCM)?
  - Evidence: (a) F1.1, F1.2, F1.4, F1.5, F1.11; (b) **F2.9, F2.10** (raw mean vs GRM; main-text support, OD3), F2.6, F2.7.
  - D13 wording: rater-specific discriminations (M2 → M3) are reported as **supported by the LR test and AIC**. The BIC disagreement is reported factually.

**Supporting RQs (secondary)**

- **SQ1: model choice and adequacy.** Which scoring model describes the ratings best: the cumulative GRM or the adjacent-category ladder? What fit evidence is available for it?
  - Evidence: F1.1, F1.3, F1.7, F1.8, F1.9, F1.10.
- **SQ2: model dependence of scores.** How strongly do product scores depend on the choice among the four models?
  - Evidence: F2.6, F2.7, plus F2.8 for the robustness of scores to the rater exclusion.
  - SQ2 supplies part of the evidence for RQ3(b), so the two are reported together in Results 3.4.

---

## Section outline

### Abstract (single paragraph, unstructured, ≤ 250 words; check the CRJ limit [FI-16])

Purpose: a standalone summary that persuades CRJ and sport-science readers. It follows abstract Model 2: background/aim → method → results with naked numbers → implications. It has no citations and **no sparse-design framing**. Results numbers are [DD], so the writer re-copies them from the findings after each data update.

- **Background/gap (1–2 sentences).**
  - CAT ratings are the standard way to assess creative products and are increasingly used for actions in sport.
  - However, it is unknown how many ratings an action needs for a reliable score, and how much raters differ when they judge creativity in sport.
- **Aim/method (1–2 sentences).**
  - Raters rated football actions on a 7-point creativity scale. Counts come from F0.3 [DD].
  - Judge response theory models were fitted by marginal maximum likelihood: a graded response model, compared with an adjacent-category ladder from the many-facet Rasch model to the generalized partial credit model.
- **Results (3–4 sentences, naked numbers).**
  - Aim 1:
    - The empirical reliability of the obtained scores was 0.672 [0.649, 0.687], against 0.960 for a hypothetical full panel (F1.12).
    - Mean product-level reliability rose from 0.520 with one rating to 0.698 with two and 0.810 with four (F1.14).
  - Aim 2: rater discrimination ranged from 0.631 to 3.709 (F2.1), and the most lenient and most severe first thresholds were −6.565 and 0.295 (F2.2).
  - Aim 3:
    - LR tests rejected a shared category structure and equal discrimination (both p < .001; F1.2).
    - Raw mean ratings placed 0.350 of products in a different quintile than the GRM scores (F2.9); the many-facet Rasch model did so for 0.202 (F2.7).
- **Implications (1–2 sentences, hedged) [ATC-5, ATC-14, ATC-15].** Creativity studies in sport should plan the number of ratings per action, link raters through a common calibration set, and model rater differences rather than average them.

### 1 Introduction

Purpose: narrow from the importance of creativity, to the CAT and its two weak points (number of raters; rater differences), to the gap in sport, to the present exploratory study. The section has four moves (writing-models/introduction.md). The sparse design is **not** part of the framing.

**Move 1: Background and importance (1–2 paragraphs)**
- P1. Creativity is a core competence:
  - ranked among core workforce skills (worldeconomicforum2025; check the wording against the PDF [FI-17]);
  - assessed in PISA 2022 (oecd2024).
  - In sport, creativity is a developmental target for players (safardilha2019; santos2016).
- P2. The 4P taxonomy distinguishes person, process, product and press (batey2012). Each facet needs its own measurement approach (barbot2019b; barbot2019). This paper concerns the *product* facet: football actions rated by others.

**Move 2: Previous research (4 paragraphs, ordered to set up aims 1, 2 and 3)**
- P3. **CAT procedure and reliability.**
  - The CAT is the established product measure (amabile1982; hennessey2011; kaufman2024).
  - **Terminology sentence (D2):** "In the CAT and JRT literature, raters are called judges; we use 'raters' throughout."
  - Independent raters usually reach α > .70 (baer2004; kaufman2008; hennessey2011). Other studies report much lower agreement (long2015; cseh2019).
- P4. **Reliability rests on the number of raters (sets up aim 1).**
  - Spearman–Brown reliability depends on the mean inter-rater correlation and on the number of raters (amabile1982). A high α from a large panel can mask low single-rater agreement (kaufman2008).
  - The number of raters needed is domain-specific and must be established per domain (cseh2019). The "5–10 judges" rule of thumb comes from kaufman2008a.
  - Key distinction, worded neutrally and in general terms (not about this data set): a panel coefficient describes the mean over all raters. When many products are rated and each receives only some ratings, what matters is the precision of each product's score given *its* ratings (forthmann2023; primi2019).
- P5. **Raters differ (sets up aim 2).**
  - Raters differ in severity, use of the scale and beliefs about creativity (long2015). Their tendencies drift over time (barth2020).
  - The classic rater-effect taxonomy covers severity, central tendency, restriction of range and halo (engelhard1994; myford2003; myford2004).
  - In judged sports, judges' differences in accuracy and bias have been monitored with Rasch/MFRM or statistical models, for performance quality rather than creativity (looney2004; anderlucci2021; heiniger2021).
- P6. **From averaging to JRT: successive relaxation of rater assumptions (sets up aim 3).** Condense the brief's paragraph and keep its logic.
  - Means and α treat raters as (essentially) τ-equivalent (myszkowski2019). Means are confounded with rater severity whenever different raters rate different products (primi2019).
  - IRT basics: lord1980; embretson2013; deayala2022.
  - Rasch models and polytomous extensions: rasch1960; bond2020; RSM andrich1978; PCM masters1982.
  - MFRM:
    - linacre1989; eckes2015; creativity application primi2019;
    - additive severity, but equal discrimination;
    - unequal discrimination appears only as misfit (myford2004; myszkowski2021).
  - JRT treats raters as items with their own discrimination and thresholds, via the GPCM (muraki1992) or the GRM (samejima1969) (myszkowski2019; myszkowski2021).
  - Applications: barbot2023; pellegrino2025, who also retained a GRM; forthmann2023 on planned-missing rating designs.
  - Adjacent-category vs cumulative link (from the brief's "Methodological choices"):
    - RSM/PCM/GPCM are nested, so their constraints are testable by LR.
    - The GRM is cumulative and arguably matches a cumulative "amount of creativity" scale [ATC-8]. The families are compared by information criteria.

**Move 3: Gap (1 paragraph, opened with "However")**
- P7. **Creativity in sport, and the gap.**
  - Research has focused on the creative process, such as divergent thinking (memmert2011).
  - Product ratings of football actions exist: kempe2018 (trained experts; face validity via proximity to goals); memmert2007 (expert-rating scale for tactical creativity); zahno2023; dejoode2023.
  - These studies average ratings and report ICCs or agreement only. A Rasch validation exists only for a coach-completed creativity questionnaire, not for ratings of actions (shin2025).
  - "However" sentence, three gaps:
    - (i) there is no evidence on how many ratings per action are needed for a reliable creativity score in sport (cseh2019);
    - (ii) there is no evidence on how raters differ when they judge the creativity of sport actions;
    - (iii) to our knowledge, no study has modelled these rater differences with IRT/JRT for creativity ratings in sport [ATC-2]. The search was not systematic, so phrase the claim cautiously.

**Move 4: Present study (1 short paragraph)**
- P8.
  - Data: a large set of CAT-style creativity ratings of football actions by multiple raters. Give the counts only by reference to Method/@tbl-design-summary [DD].
  - Exploratory aim: (1) number of ratings and reliability, (2) rater differences, (3) whether rater differences need to be modelled.
  - State RQ1–RQ3 and the supporting SQ1–SQ2 (wording above). Say explicitly that no confirmatory hypotheses were formulated.
  - One sentence on the analytic route: JRT model ladder plus GRM, estimated by MML in mirt; reliability of the obtained scores; rater parameters with intervals; comparison of GRM scores with raw mean ratings.
  - Scope sentence (D10): rater expertise and the design of the rating scale are outside the scope of this paper.

### 2 Method

Purpose: allow replication and justify the analytic choices. The section runs top-down (writing-models/methods.md): overview → details → relation to prior methods → problems. The sparse-design issues appear **here, briefly**, and in Limitations, but nowhere in the framing.

**2.1 Overview and study context (move 1)**
- One paragraph:
  - CAT-style rating study: independent raters, relative judgements, randomised order (amabile1982; hennessey2011).
  - The products are football actions, rated as part of a larger project [FI-1, FI-2].
  - Ethics and consent [FI-1].
  - Exploratory analysis; preregistration status [FI-15; ATC-20].

**2.2 Raters (move 2)**
- Recruitment: Bachelor's and Master's students rating as part of thesis projects (vault background; the author must confirm and give the numbers) [FI-1].
- Demographics, football playing or coaching experience and compensation [FI-1]. If none were recorded, say so; this links to the Limitations.
- Final number of raters, and ratings per rater from 50 to 1174 (F0.3 [DD]).
- Pseudonyms R01–R19.

**2.3 Products and stimulus material (move 2)**
- Introduce the product term: "each rated product was a single football action".
- Source of matches and competitions, the action-selection rule (event data), clip length and number of matches [FI-2]. The vault describes FIFA, AFCON, UEFA and Copa América matches with StatsBomb events; the author must confirm.

**2.4 Rating procedure (moves 2–3)**
- Rating software [FI-3].
- Instruction and the creativity definition shown to raters (originality × functionality in game context; runco2012) [FI-3].
- Relate showing a definition to the "no criteria" CAT rule (hennessey2011) and to trained-rater sport studies (kempe2018; memmert2007) [ATC-19].
- 7-point unipolar scale with anchors 1 / 4 / 7 [FI-3 confirm the anchors], plus an off-scale "action not recognised" option.
- Randomised order; session length and breaks; data-collection period [FI-3].
- Other dimensions rated (technical correctness, aesthetic appeal), which are not analysed here [FI-3].

**2.5 Rating design (moves 2 and 4, brief)**
- How products were allocated to raters: planned overlap, a common/benchmark set, randomisation [FI-4]. This is needed for the ignorable-missingness assumption of MML.
- Not every rater rated every product. The design is incomplete but connected (one component; F0.3 [DD]). The coverage numbers are given in @tbl-design-summary; do not elaborate on them here.
- If the planned benchmark set was not realised as a fully crossed block, state this neutrally [ATC-18].

**2.6 Data preparation and final data (moves 2 and 4)**
- Cleaning, in the text only (D6: no cleaning-log table). From F0.1 [DD]:
  - 9148 raw rows;
  - 1290 ratings marked "action not recognised" removed;
  - 1 out-of-range value removed (0.0 by R04);
  - 13 rows removed when resolving duplicate rater–product pairs (12 pairs, 1 with conflicting values; the last entry kept; F0.3 duplicate rows);
  - result: 7844 rows.
- **D12 sentence (exactly one, short; author's meaning):** "The 1290 ratings marked 'action not recognised' were removed; such ratings result from video cutting and imperfect material, where close-ups or other TV artefacts render the action non-visible." Do not discuss this further anywhere.
- **Rater exclusion (D6; OD4 wording, verbatim from the author):**
  - Facts (F0.2; `tbl-excluded-raters` [SUPP]): R20 (13), R21 (9) and R22 (2), together 24 ratings; one product rated only by them was dropped.
  - Rationale and robustness, verbatim: "Raters with fewer than 15 ratings were excluded because their up to seven rater-specific parameters cannot be estimated reliably; excluding them did not change the scores (see supplement)." Pair "(see supplement)" with the cross-reference @tbl-sensitivity-rater-exclusion.
  - Point forward to the sensitivity analysis in Results 3.5 (F2.8).
- **Final data** (F0.3; `tbl-design-summary` [MAIN]; all [DD]):
  - 7820 ratings of 3668 products by 19 raters; scale 1–7, coded 0–6 internally.
  - Ratings per product: mean 2.132, median 2, range 1–10, harmonic mean 1.726.
  - Matrix fill 0.112; one connected component; 17 of 171 rater pairs without a common product; median pairwise overlap 13.
  - Writer: quote these once, via the table, and do not repeat them as framing elsewhere. The distribution of ratings per product is in `fig-overview-degree-distributions` [SUPP] and in the n_products column of `tbl-grm-reliability-by-n` [MAIN].
- **Category gaps** (F0.7; `tbl-category-usage` [SUPP]):
  - five raters left top categories unused: category 7 by R01, R03, R06 and R18; categories 6–7 by R17;
  - no rater has an internal gap;
  - consequence: these raters have fewer thresholds in mirt.

**2.7 Measurement models (moves 2–3)**
- Common JRT frame (myszkowski2019; myszkowski2021):
  - raters are items and products are persons;
  - unidimensional creativity θ ~ N(0, 1);
  - severity is the threshold location ("higher b means a stricter rater", F2.2 note), scale use is the threshold spacing, and discrimination is a.
- Adjacent-category ladder:
  - M1: RSM (andrich1978), equivalent to a two-facet MFRM (linacre1989; eckes2015; primi2019), estimated with sirt::rm.facets (robitzsch2025);
  - M2: PCM (masters1982);
  - M3: GPCM (muraki1992).
  - M2 and M3 are estimated in mirt (chalmers2012).
- Retained scoring model: a GRM with rater-specific a and thresholds (samejima1969), in mirt. Its thresholds are ordered by construction (F1.5 note).
- GRM estimation (F1.3):
  - MML via EM, 61 quadrature points;
  - Oakes standard errors (chalmers2018);
  - converged after 165 iterations, information matrix positive definite (`tbl-grm-convergence` [SUPP]);
  - tolerance prints as 0.000, so do not quote it [FI-6].

**2.8 Model comparison (move 2)**
- LR tests within the nested ladder: M1 vs M2 (rater-specific thresholds) and M2 vs M3 (rater-specific discriminations).
- logLik, AIC, BIC and SABIC for all four models, with Δ to the best model on each criterion (F1.1).
- GRM vs ladder by information criteria only, because the families are not nested.
- Problems, stated briefly:
  - M1 vs M2 is a cross-software comparison (sirt vs mirt);
  - **df of the M1–M2 test (resolved, F1.2):** the formula value (J − 1)(K − 2) = 90 assumes that every rater used all 7 categories. A rater who never used an end category has one step parameter fewer in M2, so the observed df (84) is smaller by the number of unused end categories; the unused categories are listed per rater in @tbl-category-usage. **Do not quote the number of unused end categories** (NOT IN NOTEBOOK; the writer must not count it from the table either).

**2.9 Model adequacy (moves 2 and 4, brief, with the limits stated here once)**
- Rater infit/outfit mean squares (wright1982) for M1 and the GRM; expected value 1. **No misfit cut-offs are applied** (F1.7, F1.11). Do not mention any cut-off range. Note (F1.7 caveat): with about 2 ratings per product, values below 1 are expected because the score is estimated from the ratings being checked.
- S-X² (orlando2000; kang2008), with missing ratings multiply imputed (20 imputations). The notebook states that the test is conservative because most cells are imputed (F1.8 caveat; "about 90%" is the notebook wording, [DD]).
- Yen's Q3 (yen1984): the correlation of two raters' residuals over the products both rated. Q3 is negatively biased with few raters per product (christensen2017), so pairs are compared by their deviation from the mean Q3 over all computable pairs. **Flag criterion (F1.9, resolved):** a pair is flagged when it has at least 30 jointly rated products and its Q3 deviates from the mean Q3 by more than 0.2. The mean Q3 and the flag count are reported in Results 3.1. Do not define "computable" (not in the notebook).
- C2 (cai2014), a limited-information test of overall fit, **could not be computed: it needs the joint distribution of every rater pair, which is undefined for the 17 of 171 rater pairs that share no products** (F1.10, resolved [DD]). State this once, neutrally, here; refer back to it in Limitations. Do not embed `tbl-grm-global-fit`.

**2.10 Scores and reliability (move 2; aim 1)**
- Product scores: EAP θ̂ with the posterior SD (PSD) as the conditional standard error.
- **Empirical marginal reliability** (primary): Var(θ̂) / (Var(θ̂) + mean PSD²). It refers to the scores actually obtained.
- **Model-based marginal reliability** (green1984; mirt marginal_rxx) refers to a hypothetical product rated by all raters. A grid computation serves as a check.
- **95% intervals (F1.12, resolved):** both come from 200 accepted draws of the model parameters from their asymptotic normal distribution (estimates and Oakes covariance matrix). For the empirical reliability, products are also resampled in each draw. A draw was rejected and replaced when it was not a valid GRM, i.e., when some discrimination was ≤ 0 or some rater's thresholds were out of order.
  - **Decision: quote the 87 rejected draws once, here** ("87 draws were rejected and replaced"). Reason: the value is printed in `tbl-grm-reliability-ci`, the rejection rule is now defined, and stating it makes the interval method fully transparent. It is [DD].
- **Product-level reliability:**
  - rel_post = 1 − PSD²;
  - rel_info = I/(I + 1), from the information of the product's own raters at θ̂;
  - consistency check between the two;
  - summaries by number of ratings per product.
- **Conventional indices** (reference values for common practice; not used downstream, F1.18 note):
  - Cronbach's α (cronbach1951) from pairwise covariances over all usable raters, and on the largest fully crossed block. State why 5 raters were not usable for the pairwise version [FI-9].
  - Krippendorff's ordinal α (hayes2007).
  - 95% bootstrap CIs over products (1000 replications). **The pairwise Cronbach CI is approximate:** replications in which a rater pair loses all shared products cannot be computed; 361 of the 1000 replications failed, and the interval uses the remaining ones (F1.18, resolved [DD]).
  - Optionally cite tenhove2024 on indices in incomplete designs.

**2.11 Rater parameters, information and response styles (move 2; aim 2)**
- GRM a and b_k with Oakes SEs.
- Rater information integrated over N(0, 1), i.e., the average information per rating. Each rater's share of full-panel information, weighted and at selected θ.
- 95% intervals for information and share from the same parameter draws as in 2.10 (F2.4).
- Descriptive response styles on the raw 1–7 scale (F0.8):
  - mean, SD, categories used, entropy (natural log), floor (share of 1s) and ceiling (share of 7s) rates, extreme (1, 7) and central (3–5) rates;
  - not adjusted for which products each rater saw.

**2.12 Score agreement and sensitivity (move 2; RQ3b/SQ2)**
- **Raw mean vs GRM (F2.9; OD3):** each product's unweighted mean rating, the common-practice score that treats raters as interchangeable, is compared with its GRM EAP score, overall and by number of ratings per product (1, 2, 3+):
  - Pearson and Spearman correlations;
  - absolute shift in percentile rank (0–1 scale);
  - share of products changing quintile, and changing by ≥ 2 quintiles;
  - range of GRM scores among products with the same raw mean (mean and maximum).
  - Describe the grouping only as the notebook does. Whether percentiles/quintiles in the subgroups are computed within each subgroup, and how the equal-raw-mean groups are formed, is not documented [FI-20].
- Pearson and Spearman correlations of EAP scores between all models.
- Relative to the GRM:
  - absolute shift in percentile rank (0–1 scale);
  - share of products changing quintile, and changing by ≥ 2 quintiles (F2.7).
- Integration-grid check for M1 (F2.6).
- Rater-exclusion sensitivity: the GRM refitted with all 22 raters (F2.8).

**2.13 Software and availability (move 2)**
- R version; versions of mirt, sirt, psych and the Krippendorff package; Python for display [FI-6].
- Data and code availability with pseudonymised rater IDs only [FI-15]. D11: no action on the Google Sheet URL is planned here.

### 3 Results

Purpose: describe, not interpret. The section uses the four moves of writing-models/results.md:
1. revisit the aim and give an overview;
2. invite the reader to the objects and give key results;
3. state problems openly;
4. give at most one hedged pointer to implications per subsection.

Statistics follow APA: p < .001 in the text, and values as printed. **Order:** the scoring model first, briefly (supporting, because RQ1 and RQ2 use the GRM). Then RQ1 → RQ2 → RQ3/SQ2 → sensitivity. Every number is [DD].

**3.0 Overview (1 short paragraph, move 1)**
- Echo the three aims. All analyses use the final data in @tbl-design-summary.
- Give a descriptive one-line preview:
  - the GRM retained;
  - the reliability of the actual scores below the full panel and rising with ratings per product;
  - raters heterogeneous;
  - rater-equivalence constraints rejected, and raw mean scores ranking products differently from GRM scores.

**3.1 Scoring model (SQ1; supporting, kept short)**
- Findings: F1.1, F1.3, F1.7, F1.8, F1.9, F1.10.
- Embed: `tbl-model-fit` [MAIN].
- Cross-reference:
  - `tbl-grm-convergence` [SUPP]
  - `tbl-grm-rater-fit` [SUPP]
  - `tbl-grm-q3-flagged` [SUPP]
- Not embedded: `tbl-grm-global-fit`.
- Bullets:
  - Information criteria (@tbl-model-fit):
    - The GRM has the lowest AIC (23720.455), BIC (24508.795) and SABIC (24105.251).
    - Δ to the GRM: M3 46.566 on all three criteria; M2 ΔAIC 132.524, ΔBIC 20.790, ΔSABIC 77.985; M1 701.980, 68.825, 392.931 (F1.1).
    - The GRM and M3 have the same number of parameters (127), so the comparison reduces to logLik: −11733.227 vs −11756.510 (F1.1).
  - The GRM converged after 165 EM iterations; information matrix positive definite (F1.3).
  - Fit, in one or two sentences with pointers to [SUPP]:
    - S-X² p-values range from 0.294 (R12) to 0.671 (R02) (F1.8).
    - Infit ranges from 0.334 (R19) to 0.971 (R18) and outfit from 0.322 (R19) to 0.961 (R18); all below 1 (F1.7).
    - Q3 (F1.9): the mean Q3 over 137 computable rater pairs is −0.238; 20 pairs are flagged. Of the 10 pairs shown in @tbl-grm-q3-flagged (largest deviation from the mean Q3), 9 deviate negatively and 1 (R10–R11) positively. Say that the table shows 10 of the 20 flagged pairs.
    - C2 was not computable (see Method 2.9; F1.10).
  - Move 3: point to the limits stated in Method 2.9 in one clause. Do not elaborate them here; that belongs in Limitations.
  - Do not quote RMSEA or any misfit range (none in the notebook; no cut-offs applied).

**3.2 Number of ratings and reliability of the creativity scores (RQ1; aim 1, the central subsection)**
- Findings: F1.12, F1.13, F1.14, F1.15, F1.16, F1.17, F1.18, F1.19.
- Embed:
  - `tbl-grm-reliability-by-n` [MAIN]
  - `fig-grm-rel-post-by-n` [MAIN]
  - `tbl-reliability-overview` [MAIN]
- Cross-reference:
  - `tbl-grm-reliability-ci` [SUPP]; its CIs are quoted in the text
  - `tbl-grm-reliability-summary` [SUPP]
  - `tbl-naive-indices` [SUPP]
  - `fig-grm-rel-post-histogram` [SUPP]
  - `fig-grm-rel-post-by-theta` [SUPP]
  - `fig-grm-rel-consistency` [SUPP]
  - `fig-grm-panel-information` [SUPP]; its caption keeps "hypothetical"
- Bullets:
  - **Reliability by number of ratings** (@tbl-grm-reliability-by-n, @fig-grm-rel-post-by-n; F1.14):
    - Mean rel_post rises monotonically: 0.520 (1 rating; 897 products), 0.698 (2; 2080), 0.757 (3; 357), 0.810 (4; 125), 0.820 (5; 125), 0.847 (6; 47), 0.869 (7; 20), 0.875 (8; 11), 0.879 (9; 3), 0.919 (10; 3).
    - Mean PSD falls from 0.686 to 0.285.
    - rel_info means track rel_post: 0.544 at 1 rating to 0.917 at 10.
    - No n reaches a mean rel_post as high as the model-based full-panel value of 0.960 (F1.14 caveat).
    - The product counts per n are [DD]; quote them only from the table.
  - **Spread within n** (move 2, from the figure): products with the same number of ratings differ in rel_post.
    - The notebook states that precision depends on where a product lies relative to its raters' thresholds (F1.17; @fig-grm-rel-post-by-theta [SUPP]).
    - This links forward to RQ2. The interpretation belongs in the Discussion [ATC-4].
  - **Overall distribution** (F1.13): rel_post median 0.698, IQR 0.173 (Q1 0.596, Q3 0.769); p10 0.485, p90 0.813; range 0.057–0.929.
  - **Consistency of the two product-level routes** (F1.16): r = 0.935; mean rel_info − rel_post 0.016; max |diff| 0.413; 320 products differ by > 0.1.
  - **Actual vs hypothetical vs conventional** (@tbl-reliability-overview; CIs from F1.12, F1.18):
    - empirical marginal reliability (actual scores): 0.672 [0.649, 0.687];
    - model-based marginal reliability (hypothetical full panel): 0.960 [0.953, 0.968]; grid check 0.960;
    - Cronbach's α, pairwise covariances: 0.928 [0.891, 0.943], 14 raters, 1900 products. The CI is approximate: 361 of 1000 bootstrap replications failed (Method 2.10; @tbl-naive-indices);
    - Cronbach's α, fully crossed block: 0.658 [0.526, 0.756], 3 raters, 139 products;
    - Krippendorff's ordinal α: 0.392 [0.362, 0.417], 19 raters, 2771 products.
    - State what each index refers to, as in the table's "refers to" column. Do not discuss the M1–M3 marginal reliabilities that the overview table also lists (D5).
  - Move 3 (problems):
    - the per-n means have no CIs (F1.14);
    - the 9- and 10-rating rows rest on 3 products each;
    - the comparison across n is observational, since products were not randomly assigned a number of ratings [FI-4].
  - Writer: `tbl-reliability-overview` still says "bootstrap, 1000 replications" for the pairwise Cronbach CI without mentioning the failed replications. The text states the 361 failures; the notebook wording should be aligned before render [FI-18].

**3.3 Rater differences (RQ2; aim 2)**
- Findings: F0.6, F0.7, F0.8, F2.1, F2.2, F2.3, F2.4, F2.5.
- Embed:
  - `fig-overview-rater-response-styles` [MAIN]: descriptive entry point
  - `tbl-grm-rater-parameters` [MAIN]
  - `tbl-grm-rater-information-ci` [MAIN]
- Cross-reference:
  - `tbl-category-usage` [SUPP]
  - `fig-overview-rating-distribution` [SUPP]
  - `fig-grm-category-response-functions` [SUPP]
  - `fig-grm-rater-information` [SUPP]
  - `fig-grm-information-shares` [SUPP; **optional MAIN if space allows**, OD2]
  - `tbl-grm-information-summary` [SUPP]
- Bullets:
  - **Descriptive response styles** (@fig-overview-rater-response-styles; F0.8; raw scale, not adjusted for which products each rater saw; 3 decimals as printed):
    - Rater means range from 1.760 (R06) to 3.836 (R18).
    - SD ranges from 1.022 (R01) to 1.953 (R19).
    - Entropy ranges from 1.191 (R06) to 1.903 (R09).
    - Floor rate ranges from 0.579 (R06) to 0.016 (R13). The ceiling rate is highest for R19 (0.080); five raters (R06, R17, R01, R03, R18) print 0.000.
    - The central (3–5) rate is high for R13 (0.799), R18 (0.764) and R12 (0.735), and low for R06 (0.192).
    - Any other value may be taken from the full F0.8 table, at 3 decimals. Never quote the earlier 6-decimal values.
  - **Overall category use** (F0.6; @fig-overview-rating-distribution [SUPP]):
    - ratings concentrate at the low end: category 1 share 0.259463, category 2 share 0.270205;
    - category 7 is rarest (0.013939).
    - Five raters left top categories unused (F0.7).
  - **Severity and scale use** (@tbl-grm-rater-parameters; F2.2):
    - b1 ranges from −6.565 (R18, SE 3.047) to 0.295 (R06, SE 0.058). R06 is the only rater with a positive b1 ("higher b means a stricter rater").
    - Threshold spacing differs:
      - narrow for R19 (b1 −0.938 to b6 1.692) and R02 (−0.706 to 2.030);
      - wide for R13 (−3.384 to 4.435) and R18 (−6.565 to b5 4.440).
    - R17 has 4 thresholds; R01, R03, R06 and R18 have 5; the others 6.
    - Threshold SEs are displayed. Use them as the precision statement.
  - **Discrimination** (F2.1):
    - a ranges from 0.631 (R18, SE 0.263) to 3.709 (R19, SE 2.220). Second highest is R16, 3.701 (SE 1.359).
    - Precisely estimated raters with many ratings also differ: R09 0.863 (SE 0.151), R13 1.504 (SE 0.223), R01 1.956 (SE 0.159), R02 2.498 (SE 0.331), R06 2.807 (SE 0.424).
  - **Information and share, with 95% intervals** (@tbl-grm-rater-information-ci; F2.4):
    - Average information per rating ranges from 0.123 [0.008, 0.352] (R18) to 3.539 [0.410, 11.017] (R19).
    - R16: 3.300 [0.728, 6.489]. R09: 0.238 [0.110, 0.419]. R01: 0.979 [0.723, 1.219].
    - Shares: R19 0.135 [0.017, 0.331]; R16 0.126 [0.026, 0.223]; R01 0.037 [0.022, 0.050]; R18 0.005 [0.000, 0.013].
    - The notebook states that wide intervals mean the rater's informativeness is not yet well determined, typically for raters with few ratings (F2.4 note).
  - **Where on θ raters inform** (F2.3; [SUPP] objects):
    - The location of maximum information ranges from R01 at 2.700 and R06 at 2.400 to R13 at −0.550.
    - Shares vary with θ, e.g., R06 0.001 at θ = −2 vs 0.083 at θ = +2; R12 0.221 at θ = −2.
  - Move 3: the information intervals use the same 200 accepted parameter draws as F1.12 (Method 2.10). The raw response styles have no per-rater uncertainty (not found in the notebook).

**3.4 Do rater differences need to be modelled? Constraints, raw means and score consequences (RQ3; SQ2)**
- Findings: F1.1, F1.2, F1.4, F1.5, F1.11, F2.6, F2.7, **F2.9, F2.10**.
- Embed:
  - `tbl-raw-mean-vs-grm` [MAIN] (OD3: the main-text support for RQ3(b))
  - `fig-raw-mean-vs-theta` [MAIN] (see the placement justification below)
  - `tbl-score-agreement` [MAIN]
- Cross-reference:
  - `tbl-lr-tests` [SUPP]; the statistics are quoted in the text
  - `tbl-model-fit` [MAIN, from 3.1]
  - `tbl-discrimination-m3` [SUPP]
  - `tbl-threshold-order` [SUPP]
  - `tbl-rater-fit-m1` [SUPP]
  - `tbl-theta-correlations` [SUPP]
- Bullets:
  - **RQ3(a), shared category structure** (F1.2): M1 vs M2 X² = 737.457, df = 84, p < .001. The exact p (4.22e-105) is in @tbl-lr-tests. The df explanation is in Method 2.8; do not repeat it here.
  - **RQ3(a), equal discrimination** (F1.2, F1.1):
    - M2 vs M3: X² = 121.958, df = 18, p < .001 (exact 1.79e-17).
    - AIC also favours M3 (23767.020 vs 23852.978).
    - BIC ranks M2 (24529.585) below M3 (24555.360).
    - D13 wording: "Rater-specific discriminations were supported by the LR test and AIC, but not by BIC." Report this factually, without hedging it away.
  - Supporting detail, one sentence each, pointing to [SUPP]:
    - M3 discriminations range from 0.283 (R09, SE 0.055) to 2.606 (R16, SE 1.419) (F1.4).
    - Unordered step parameters in 9 raters under M2 and 9 under M3 (F1.5). GRM thresholds are ordered by construction.
    - Under M1 (MFRM), only R17 (infit 1.328, outfit 1.190) and R18 (1.009, 1.071) are at or above 1. The lowest values are R12's (0.238, 0.255) (F1.11). No cut-offs applied.
    - Do not state in Results that misfit "reflects" unequal discrimination. That reading belongs in the Discussion [ATC-9].
  - **RQ3(b), raw mean vs GRM score** (@tbl-raw-mean-vs-grm, @fig-raw-mean-vs-theta; F2.9, F2.10). Descriptive only:

    | ratings per product | n products | Pearson / Spearman | mean abs. percentile shift | share changing quintile | by ≥ 2 quintiles | mean / max θ̂ range at equal raw mean |
    |---|---|---|---|---|---|---|
    | all | 3668 | 0.906 / 0.932 | 0.080 | 0.350 | 0.022 | 0.814 / 2.252 |
    | 1 | 897 | 0.921 / 0.940 | 0.074 | 0.385 | 0.004 | 1.283 / 1.436 |
    | 2 | 2080 | 0.922 / 0.933 | 0.075 | 0.319 | 0.028 | 1.537 / 2.196 |
    | 3+ | 691 | 0.954 / 0.959 | 0.060 | 0.266 | 0.006 | 0.619 / 1.396 |

    - Overall, raw means and GRM scores correlate 0.906 (Pearson) and 0.932 (Spearman); 0.350 of products change quintile; among products with the same raw mean, GRM scores lie up to 2.252 apart (F2.9).
    - The correlations are highest and the quintile changes lowest in the 3+ group (0.954 / 0.959; 0.266), compared with 0.385 for 1 rating and 0.319 for 2 (F2.9).
    - Descriptive cross-table comparison of printed values (F2.9 direction note): the overall share changing quintile for the raw mean (0.350) is higher than for any IRT model vs the GRM (M1 0.202, M2 0.150, M3 0.075; F2.7), and the overall correlations are lower than every model-to-GRM correlation (F2.6).
    - The figure shows the vertical spread of GRM scores at a given raw mean (F2.10, notebook statement `185dc985`). Points are jittered horizontally; say so in the text or rely on the caption.
    - Quote the p95/max percentile-shift columns only from the table if needed. Do not describe how the equal-raw-mean groups are formed, or whether subgroup percentiles are computed within subgroups [FI-20]. Do not comment on the "all" row's θ̂ range being smaller than the 1- and 2-rating rows (F2.9 Flag 13).
    - **Do not state the mechanism** ("rated by raters of different severity or discrimination", notebook markdown `909a8bdd`) in Results. It is interpretive and goes to Discussion 4.4 only [ATC-21].
  - **RQ3(b)/SQ2, model choice** (@tbl-score-agreement; F2.7). Relative to the GRM:

    | model | Pearson / Spearman | mean abs. percentile shift | p95 | max | share changing quintile | by ≥ 2 quintiles |
    |---|---|---|---|---|---|---|
    | M1 | 0.975 / 0.978 | 0.042 | 0.130 | 0.432 | 0.202 | 0.004 |
    | M2 | 0.985 / 0.983 | 0.033 | 0.117 | 0.413 | 0.150 | 0.003 |
    | M3 | 0.996 / 0.996 | 0.017 | 0.044 | 0.234 | 0.075 | 0.001 |

    - Among the ladder models: Pearson 0.980–0.993, Spearman 0.983–0.996 (F2.6; @tbl-theta-correlations [SUPP]).
    - Grid check: M1 vs the sirt default grid 1.000 (F2.6). Explain the `rm_facets_default_grid` row/column in the table note [FI-18].
  - Move 3 (problems, descriptive):
    - No CIs exist for the correlations, the agreement statistics or the raw-mean comparison.
    - The M1–GRM contrast combines the rater constraints with the change of link function. M3 and the GRM have the same number of parameters and differ only in the link.
    - The interpretation goes to the Discussion [ATC-10, ATC-22].
  - Move 4 (one hedged closing sentence) [ATC-10]: "Scoring products by their raw mean changed the ranking more than any of the model constraints did, and constraining raters to equivalence changed it more than the choice of link function did."

**3.5 Sensitivity to the rater exclusion (brief; 2–3 sentences)**
- Findings: F2.8.
- Cross-reference: `tbl-sensitivity-rater-exclusion` [SUPP] (D7). This is the "(see supplement)" target of the OD4 sentence in Method 2.6.
- Bullets (values as printed, 5 decimals):
  - Refitting the GRM with all 22 raters (7844 ratings, 3669 products):
    - empirical marginal reliability 0.67199 → 0.67186;
    - model-based reliability 0.95986 → 0.96186.
  - Over the 3668 common products:
    - θ̂ Pearson 0.99997, Spearman 0.99996;
    - mean |Δθ̂| 0.00171, max 0.16246;
    - share changing quintile 0.00491.
  - Over the 19 common raters: a Pearson 0.99880; max |Δa| 0.19820.
  - No CIs exist for these differences.

### 4 Discussion

Purpose: interpret, map to the literature, and draw the implications for sport-science creativity research. The section mirrors the Introduction's three aims and uses four moves (writing-models/discussion-conclusion.md). **Every interpretive claim is [ATC].** The sparse design appears only in 4.6 Limitations.

**4.1 Summary of the answers (move 1, 1 paragraph)**
- Echo RQ1–RQ3 in the Introduction's wording, descriptively:
  - the reliability of the obtained scores rises with ratings per product and stays below the full panel;
  - raters differ in severity, scale use, discrimination and information;
  - the equivalence constraints are rejected (LR and AIC; not BIC for discrimination);
  - raw mean scores and the model choice both shift rankings, the raw mean most.
- Mention the GRM's retention (SQ1) in one clause.

**4.2 How many ratings per action? Reliability of the scores actually used (aim 1) [ATC-3, ATC-4, ATC-13]**
- The conventional figures describe the mean of a large or complete panel: the full-panel reliability (0.960) and the pairwise Cronbach's α (0.928). The scores actually obtained have an empirical reliability of 0.672 [0.649, 0.687]. This is what matters for any downstream use [ATC-3].
- Map to the literature:
  - Spearman–Brown logic (amabile1982);
  - kaufman2008: a high α can hide low single-rater agreement. Krippendorff's 0.392 vs Cronbach's 0.928 illustrates this [ATC-13];
  - cseh2019: the number of raters must be established per domain. The by-n table gives the first such evidence for football [ATC-4].
- The crossed-block α (0.658, 3 raters) lies close to the empirical reliability. Treat this as a cautious observation and do not claim equivalence [ATC-13].
- Product-level precision depends mainly on the number of ratings (F1.14) but also on *which* raters rated the product and where it lies on θ (F1.17, F2.3). This bridges to aim 2 [ATC-4].
- Reporting implication: report the reliability of the scores actually used (empirical marginal reliability, product SEs), not only α or full-panel values [ATC-15].

**4.3 Raters differ (aim 2) [ATC-6, ATC-12]**
- The raters span a wide range of severity (b1), scale use (threshold spacing; raw floor and central rates) and discrimination. For raters with many ratings, the differences are clearly larger than the SEs (e.g., R09 vs R06; F2.1) [ATC-6].
- Map to the literature: long2015 (scale use, beliefs); rater-effect taxonomy (engelhard1994; myford2003; myford2004); central tendency vs extreme responding (myszkowski2021). primi2019 left response styles to future work; this study describes them for football [ATC-6].
- **Uncertainty.**
  - For raters with about 50 ratings (R16, R19), the highest discriminations and information shares come with the widest intervals (F2.1, F2.4).
  - Information shares are therefore not a ranking of rater quality [ATC-12].
  - Link to wind2018 and wind2019a (rater estimates depend on the linking set), reise1990 (GRM recovery) and ceh2022 (rater characteristics predicting discernment).
- Raters inform different regions of θ (e.g., R06 at high creativity, R12 at low; F2.3). This is relevant for assigning raters [ATC-16].

**4.4 Why rater differences must be modelled in creativity research in sport (aim 3) [ATC-7, ATC-8, ATC-9, ATC-10, ATC-21, ATC-22]**
- Unweighted means and α assume τ-equivalent raters (myszkowski2019). The LR tests reject even the weaker Rasch/MFRM constraints (F1.2). Averaging therefore treats raters as interchangeable when they are not, and severity is confounded with rater assignment whenever raters rate different actions (primi2019) [ATC-7].
- **Raw means vs model-based scores (OD3)** [ATC-21, ATC-22]:
  - Direct evidence: the raw mean moves 0.350 of products to another quintile relative to the GRM score, more than any IRT model does (0.202 at most), and products with the same raw mean receive GRM scores up to 2.252 apart (F2.9, F2.7) [ATC-22].
  - Mechanism, from notebook markdown `909a8bdd`, used here only and marked: "Products with the same raw mean get different GRM scores when they were rated by raters of different severity or discrimination." **[AUTHOR TO CONFIRM; ATC-21]** It is the notebook's explanation, not a tested result.
  - The agreement is higher, and fewer products change quintile, in the 3+ group than with 1 or 2 ratings (F2.9). A cautious reading: with more ratings per product, individual rater differences weigh less in the mean [ATC-22]. Do not present this as a test (no test across groups in the notebook).
  - Map to primi2019 (means confounded with severity in incomplete designs) and myszkowski2019 (τ-equivalence).
- Discrimination:
  - supported by the LR test and AIC, not by BIC (D13);
  - part of the heterogeneity may be estimation noise for raters with few ratings (F1.4, F2.1) [ATC-7].
- The M1 misfit pattern fits the account that the MFRM expresses discrimination differences only as misfit (myford2004; myszkowski2021):
  - R17 underfits under M1 and has a low GRM a;
  - R12 overfits under M1 and has a high GRM a (F1.11, F2.1).
  - This is cautious and descriptive; no cut-offs are applied, so speak of values above and below 1, not of "misfitting raters" [ATC-9].
- The GRM is preferred by information criteria. A cumulative link is plausible for a unipolar scale, and pellegrino2025 also retained a GRM [ATC-8]. Neither the unordered PCM/GPCM steps nor the ordered GRM thresholds count as evidence for either family (andrich1978; bond2020) [ATC-9].
- **Score consequences** [ATC-10]:
  - Overall correlations between models are high (≥ 0.975), yet rankings move: 0.202 of products change quintile under the MFRM/RSM vs the GRM, and 0.075 under the GPCM.
  - For applications that select or label actions, e.g., top-quintile creative actions for training or labels for automated rating, these shifts matter; the raw-mean shifts matter most.
  - Keep the link-function confound explicit.

**4.5 Practical implications for sport science (move 4: applications) [ATC-5, ATC-14, ATC-15, ATC-16]**
- **Ratings per action for a target reliability** [ATC-5]:
  - Use the by-n table descriptively only, e.g., "products with k ratings had a mean rel_post of …" (F1.14).
  - No extrapolation, no Spearman–Brown projection and no D-study (none in the notebook).
  - State that the values refer to this rater pool and this scale. They will be refined as more ratings are collected [DD].
- **Calibration/anchor set rated by all raters** [ATC-14]. This:
  - links raters and makes their parameters comparable;
  - stabilises the a of raters with few ratings (wind2019a; forthmann2023);
  - makes fully crossed reliability and absolute fit checks estimable.
  - Distinguish it from rater *training*, which conflicts with the CAT "no criteria" rule (storme2014; dollinger2005; hennessey2011).
- **Model rater differences instead of averaging** [ATC-15]:
  - JRT scores (EAP with PSD) rather than raw means; the raw-mean comparison (F2.9) is the direct evidence that this choice changes which actions rank high [ATC-22];
  - report the empirical marginal reliability and product SEs;
  - carry the SEs into downstream uses.
- **Rater workload and assignment** [ATC-16]:
  - The exclusion cut-off of 15 ratings is a minimum, and raters with about 50 ratings still have wide intervals (F2.1, F2.4). Plan more ratings per rater.
  - Optionally, use rater information to assign raters (F2.3).
- **Boxed design recommendations (OD6: yes).** A short box titled e.g. "Design recommendations for creativity ratings in sport". **Every item is [AUTHOR TO CONFIRM; ATC-23]**, and each item also carries the ATC of the claim it rests on:
  1. Plan the number of ratings per action from the reliability you need, and report it (F1.14) [ATC-5].
  2. Let all raters rate a common calibration set so that raters are linked and their parameters comparable [ATC-14].
  3. Give each rater enough ratings for stable rater parameters; 15 is a lower limit, not a target (F2.1, F2.4) [ATC-16].
  4. Score products with a JRT model rather than the raw mean (F2.9) [ATC-15, ATC-22].
  5. Report the reliability of the scores actually used (empirical marginal reliability, product SEs), not only α or full-panel values (F1.12) [ATC-3, ATC-15].
  - Keep the box to these 4–5 items; no numbers inside the box except by reference to the tables, since all are [DD].

**4.6 Limitations and future research (move 4)**
- L1. **Design.**
  - The rating design is incomplete: not every rater rated every product, and the allocation is described in [FI-4]. Missingness is assumed ignorable.
  - The comparison across numbers of ratings is observational, and the high-n cells are small (F1.14) [DD].
- L2. **Fit evidence is limited by the design** [ATC-11]:
  - S-X² is conservative with most cells imputed (F1.8);
  - C2 could not be computed because some rater pairs share no products (F1.10; Method 2.9);
  - Q3 is negatively biased with few raters per product (christensen2017);
  - infit/outfit values below 1 are expected when θ̂ is estimated from the same few ratings (F1.7), and no cut-offs are applied.
  - Absence of detected misfit is not evidence of fit.
- L3. **Uncertain parameters for raters with few ratings** (F2.1, F2.4). The response-style indices are raw and have no uncertainty.
- L4. **Rater pool.** One pool of student raters [FI-1], with no rater covariates. Expertise is outside the scope of this paper (D10); future work: kaufman2009; kaufman2013; ceh2022.
- L5. **Rater exclusion.** Raters with fewer than 15 ratings were excluded; excluding them did not change the scores (F2.8; @tbl-sensitivity-rater-exclusion). Reuse the author's OD4 wording; no further hedging needed.
- L6. **Model comparison caveats:**
  - cross-software LR test (sirt vs mirt) for M1 vs M2; its df is below the formula value because of unused end categories (Method 2.8);
  - BIC vs LR/AIC disagreement on discrimination;
  - the score-agreement contrasts mix rater constraints and link function (F2.7);
  - the raw-mean comparison has no CIs, and its subgroup and equal-raw-mean grouping definitions are not documented [FI-20].
- L7. **Two facets and one dimension only.**
  - No time, session or fatigue facet: barth2020; leckie2011; myford2009; workload forthmann2017.
  - No differential rater functioning (wind2019b).
  - Extensions: patz2002; uto2020.
  - Unidimensionality is assumed; only the creativity dimension is analysed.
- **Future research:**
  - a prospective anchor-set design;
  - a simulation or D-study for planning ratings per action (forthmann2023);
  - rater covariates;
  - replication in other sports.

### 5 Conclusion (1 paragraph)

- Restate the three demonstrations in 3–4 sentences [ATC-1]:
  1. score reliability depends on ratings per action, and the reliability of the obtained scores is far below conventional panel figures;
  2. raters differ in severity, scale use, discrimination and information;
  3. treating raters as equivalent is rejected, and both raw means and constrained models shift rankings.
- End with the design and scoring message: plan ratings per action, link raters through a calibration set, and model raters with JRT [ATC-5, ATC-14, ATC-15].

### References

APA 7th via CSL; citekeys only. Mechanical, with no hand formatting.

---

## Figure/table plan (D4, D5, D6, D9; OD2, OD3 applied)

There are **11 main-text objects** (8 tables, 3 figures), plus **1 optional main-text figure** (`fig-grm-information-shares`, counted under the supplement). There are **24 supplement objects** (15 tables, 9 figures) and **5 objects not embedded**. Total: 40.

### Main text (11)

| # | Label | Section | Role |
|---|---|---|---|
| 1 | `tbl-design-summary` | 2.6 | Final data; single place for the design numbers [DD] |
| 2 | `tbl-model-fit` | 3.1 | SQ1: information criteria with Δ |
| 3 | `tbl-grm-reliability-by-n` | 3.2 | RQ1: the planning values (rel_post, rel_info, PSD and n_products by n) |
| 4 | `fig-grm-rel-post-by-n` | 3.2 | RQ1: the spread within n, which links aim 1 to aim 2 |
| 5 | `tbl-reliability-overview` | 3.2 | RQ1: actual vs hypothetical vs conventional indices, with what each refers to |
| 6 | `fig-overview-rater-response-styles` | 3.3 | RQ2: raw response styles (descriptive entry point) |
| 7 | `tbl-grm-rater-parameters` | 3.3 | RQ2: severity, spacing, discrimination with SEs (wide: landscape or reduced columns) |
| 8 | `tbl-grm-rater-information-ci` | 3.3 | RQ2: information per rating and share with 95% intervals |
| 9 | `tbl-raw-mean-vs-grm` | 3.4 | RQ3(b): raw mean vs GRM score; the main-text support for "model, don't average" (OD3) |
| 10 | `fig-raw-mean-vs-theta` | 3.4 | RQ3(b): spread of GRM scores at equal raw mean |
| 11 | `tbl-score-agreement` | 3.4 | RQ3(b)/SQ2: ranking consequences of the model choice |

Optional main text, if space allows (OD2): `fig-grm-information-shares` (3.3). If promoted, main = 12 and supplement = 23.

### Justification of the placements

- **Checkpoint-1 decisions (OD2):**
  - `tbl-score-agreement` → MAIN; `tbl-theta-correlations` → SUPP (approved).
  - Both `tbl-grm-reliability-by-n` and `fig-grm-rel-post-by-n` stay MAIN (approved). The table gives the exact planning values and the [DD] counts per n; the figure shows that products with the same n differ, which bridges to rater differences.
  - `fig-grm-information-shares` → SUPP, promoted to MAIN only if space allows. The θ-dependence of shares is secondary to the CI table.
- **Raw mean vs GRM (OD3):**
  - `tbl-raw-mean-vs-grm` → MAIN. It is the direct, practitioner-relevant comparison of the common-practice score with the model score, and the main-text support for RQ3(b). Its layout matches `tbl-score-agreement`, so the two read together.
  - `fig-raw-mean-vs-theta` → **MAIN (decision).** Reasons:
    - It is the most intuitive display of the aim-3 point for CRJ and sport-science readers: products with the same raw mean sit at visibly different GRM scores.
    - It carries the "same raw mean, different GRM score" observation without depending on the θ̂-range columns of the table, whose grouping definition is not documented [FI-20].
    - It brings the main text to three figures, which is moderate for CRJ.
    - It overlaps with the table (`02_artifacts.md` §7). If space becomes tight, this figure moves to SUPP before any table does, and `fig-grm-information-shares` stays SUPP.
- **Other placements (unchanged):**
  - `tbl-grm-rater-information-ci` → MAIN, instead of `tbl-grm-information-summary` (→ SUPP). Aim 2 requires rater differences *with uncertainty*.
  - `tbl-grm-reliability-ci` → SUPP; its CIs are quoted in the text from F1.12, citing @tbl-grm-reliability-ci.
  - `tbl-sensitivity-rater-exclusion` → SUPP, with a 2–3-sentence mention in Results 3.5 and the OD4 cross-reference in Method 2.6.
  - `tbl-lr-tests` → SUPP. It has only two rows, and their X², df and p are quoted in the text.
  - `fig-grm-category-response-functions` → SUPP. It has 19 panels; `tbl-grm-rater-parameters` plus the response-styles figure carry the scale-use point.
- **NB01 objects (D9):**
  - `fig-overview-rater-response-styles` → MAIN: it serves aim 2 directly.
  - `fig-overview-rating-distribution` → SUPP: overall category use as context.
  - `fig-overview-degree-distributions` → SUPP: the ratings-per-product distribution, which `tbl-design-summary` and the by-n table already cover numerically.
  - `tbl-overview-ratings-per-action` and `fig-overview-rater-overlap` are not embedded (see below).

### Supplement (24)

- **Tables (15):**
  - `tbl-excluded-raters`
  - `tbl-sensitivity-rater-exclusion`
  - `tbl-category-usage`
  - `tbl-grm-convergence`
  - `tbl-grm-rater-fit`
  - `tbl-grm-q3-flagged`
  - `tbl-grm-reliability-ci`
  - `tbl-grm-reliability-summary`
  - `tbl-naive-indices`
  - `tbl-grm-information-summary`
  - `tbl-lr-tests`
  - `tbl-discrimination-m3`
  - `tbl-threshold-order`
  - `tbl-rater-fit-m1`
  - `tbl-theta-correlations`
- **Figures (9):**
  - `fig-overview-rating-distribution`
  - `fig-overview-degree-distributions`
  - `fig-grm-category-response-functions`
  - `fig-grm-rater-information`
  - `fig-grm-information-shares` (optional MAIN if space allows)
  - `fig-grm-panel-information`
  - `fig-grm-rel-post-histogram`
  - `fig-grm-rel-post-by-theta`
  - `fig-grm-rel-consistency`

### Not embedded (5)

- `tbl-cleaning-log`: D6; the cleaning steps are given in the Method text.
- `tbl-marginal-reliability-models`: D5, dropped entirely. Its per-model empirical reliabilities are not quoted.
- `tbl-grm-global-fit`: it now holds only a "not computable" row with the cause. One sentence in Method 2.9 says the same, so the table adds nothing.
- `tbl-overview-ratings-per-action`: it duplicates `tbl-design-summary` (its integer display is now fixed, but the duplication remains).
- `fig-overview-rater-overlap`: a sparse-design display, not needed for the aims.

### Notes for the writer and embedder

- `manuscript.qmd` still embeds the nonexistent `02d_judge_response_theory.ipynb` and references 12 deleted Bayesian labels (`02_artifacts.md` §8). The writer pass must replace them entirely; none of the 34 NB02 labels is referenced yet.
- **High priority display fix:** the `category_boundaries` column of `tbl-grm-rater-parameters` contains unescaped `|` characters that will break the Markdown table at render [FI-18].
- APA relabelling of snake_case headers, the wide tables (including the 11-column `tbl-raw-mean-vs-grm` with very long headers), the in-figure facet titles and the unexplained legend/opacity in two figures are listed in `02_artifacts.md` §2–§5 [FI-18].

---

## Effect sizes and uncertainty: inventory (updated for commit a97e51d)

| Quantity | Uncertainty available? | Where |
|---|---|---|
| Empirical / model-based marginal reliability | **Yes:** 95% intervals from 200 accepted parameter draws (87 rejected and replaced) | F1.12, `tbl-grm-reliability-ci` |
| Cronbach's α (pairwise; crossed block) | **Yes:** bootstrap CIs. The pairwise CI is approximate; n_boot_failed = 361 of 1000, quotable | F1.18, `tbl-naive-indices` |
| Krippendorff's α | Yes: bootstrap CI | F1.18 |
| Product scores | PSD per product; mean PSD by n | F1.13, F1.14 |
| rel_post by n | Means and medians only; **no CIs** | F1.14 → FI-12 (optional) |
| GRM discriminations a | Yes: Oakes SEs | F2.1 |
| GRM thresholds b_k | Yes: SEs displayed | F2.2 |
| Rater information and share | **Yes:** 95% intervals | F2.4 |
| M3 discriminations | Yes: SEs | F1.4 |
| Model comparison | ΔAIC/ΔBIC/ΔSABIC; LR X², df, exact p | F1.1, F1.2 |
| θ correlations; score agreement | Point values only; **no CIs** | F2.6, F2.7 → FI-11 (optional) |
| Raw mean vs GRM | Point values only; **no CIs** | F2.9 → FI-11 (optional) |
| Exclusion sensitivity | Point differences; no CIs | F2.8 |
| Raw response styles | No per-rater uncertainty | F0.8 |

---

## FILL IN items (14 open)

Items marked "notebook" must be added to a notebook and passed through results-interpreter before any number is quoted. FI numbers are stable; resolved items are listed at the end.

- **FI-1** Raters: recruitment, number at start, demographics, football playing/coaching experience, compensation, informed consent, ethics approval.
- **FI-2** Products: competitions and matches, the action-selection rule (event data), clip length and video source, number of matches.
- **FI-3** Procedure:
  - rating software;
  - verbatim instruction and creativity definition;
  - scale anchors;
  - wording of the "not recognised" option;
  - randomisation, session length and breaks;
  - data-collection period (timestamps exist, but no summary is printed);
  - other dimensions rated.
- **FI-4** Allocation of products to raters: planned overlap, benchmark/common set, randomisation, and how the additional ratings will be allocated. This is needed for the ignorable-missingness argument and to qualify the by-n comparison.
- **FI-6** Software versions (R, mirt, sirt, psych, Krippendorff package) and the GRM convergence tolerance (it prints as 0.000).
- **FI-9** The reason R19, R14, R02, R16 and R12 were not usable for the pairwise Cronbach's α. Optionally, the identity of the 3 raters in the crossed block (notebook).
- **FI-11** (optional, notebook) CIs for the θ correlations, the score-agreement statistics and the raw-mean vs GRM statistics.
- **FI-12** (optional, notebook) CIs for the per-n mean rel_post.
- **FI-15** Preregistration status (expected: not preregistered, which fits the exploratory framing), and the data and code availability statement.
- **FI-16** CRJ requirements: abstract word limit, keywords, word count, supplement policy.
- **FI-17** Verify the Introduction framing claims against the PDFs: worldeconomicforum2025 wording; safardilha2019; memmert2011; batey2012; barbot2019b.
- **FI-18** Notebook display fixes before render:
  - **`tbl-grm-rater-parameters`: escape the `|` in `category_boundaries`** (high priority; breaks the table);
  - snake_case headers and code names in cells (all NB02 tables, including the long headers of `tbl-raw-mean-vs-grm`);
  - captions: `tbl-raw-mean-vs-grm` should mention the "all" row; `tbl-naive-indices` should mention n_boot/n_boot_failed and the approximate pairwise CI; `tbl-grm-reliability-ci` should mention n_draws/n_draws_rejected; `tbl-lr-tests` should mention df_expected_formula/df_matches_formula; `tbl-theta-correlations` should explain the `rm_facets_default_grid` row and column;
  - `tbl-reliability-overview`: align the "bootstrap, 1000 replications" wording for the pairwise Cronbach CI with the 361 failed replications (absorbs the former FI-8);
  - in-figure facet titles ("theta" vs θ) and missing y-axis labels in `fig-grm-panel-information`;
  - unexplained opacity and legend in `fig-grm-rel-consistency` and `fig-grm-rel-post-by-theta`.
- **FI-19** **Data update.** After the additional ratings are collected, re-run N0–N2, the results-embedder and the results-interpreter. Then refresh every [DD] value in the manuscript, and re-check the qualitative statements: monotonic by-n trend, BIC disagreement, exclusion sensitivity, fit results, raw-mean vs GRM pattern across groups.
- **FI-20** (new, notebook or R source) Definitions behind `tbl-raw-mean-vs-grm` (F2.9 caveats, Flag 13): whether percentiles and quintiles in the 1 / 2 / 3+ rows are computed within each subgroup or over all products; how the equal-raw-mean groups are formed (in particular in the pooled "all" row) and how many and how large they are. Until resolved, the writer quotes the θ̂-range columns as printed and describes neither the grouping nor the "all" vs subgroup pattern.

**Resolved and removed in this update (with the findings that resolve them):**
- FI-5 (LR df 84 vs 90): F1.2, notebook markdown `f5332a23`. Explained in Method 2.8 without quoting the count of unused end categories. The sirt–mirt cross-check is dropped; the cross-software point stays a limitation (L6).
- FI-7 (parameter draws): F1.12, `6158a1cd`. n_draws = 200 counts accepted draws; 87 rejected draws are defined (a ≤ 0 or unordered thresholds) and quoted once in Method 2.10.
- FI-8 (pairwise Cronbach bootstrap): F1.18. n_boot_failed = 361 is printed and quoted in Method 2.10 and Results 3.2; the remaining wording alignment moved into FI-18.
- FI-10 (response-style values): F0.8 now prints the full table at 3 decimals (OD5).
- FI-13 (C2 cause): F1.10, `ad703efe` note and `9cc72787`. Stated in Method 2.9.
- FI-14 (mean Q3 and flag criterion): F1.9, `45a09376` and `b055ec99`. Criterion in Method 2.9; values in Results 3.1.
- Also resolved without an FI number: no infit/outfit cut-offs are applied (F1.7, F1.11, `7cc24a3b`); the 0.7–1.3 range is dropped everywhere. NB01 "actions" in captions and axes (now "products"); clipped legends (fixed).

## AUTHOR TO CONFIRM claims (22 open)

- **ATC-1** The central contribution statement: three demonstrations (aims 1–3), now including the raw-mean vs GRM comparison under demonstration 3.
- **ATC-2** The novelty claim: "to our knowledge, no study has modelled rater differences with IRT/JRT for creativity ratings in sport". The search was not systematic.
- **ATC-3** Conventional CAT indices (α, full-panel reliability) describe a panel mean, not the precision of the scores actually used. The empirical marginal reliability is the relevant figure.
- **ATC-4** The precision of a product's score depends mainly on its number of ratings, and also on which raters rated it and where it lies on θ. The by-n comparison is observational. It gives first football-specific evidence on the number of raters (cseh2019).
- **ATC-5** Practical implication: ratings per action for a target reliability, read **descriptively** from the by-n table (no extrapolation).
- **ATC-6** Raters differ substantially in severity, scale use and discrimination, and for well-measured raters the differences exceed their SEs.
- **ATC-7** Rater differences must be acknowledged and modelled. Averaging treats raters as interchangeable, which the LR tests reject. Discrimination heterogeneity is supported by LR and AIC but not by BIC, and is partly uncertain for raters with few ratings.
- **ATC-8** The GRM is preferred by information criteria, and a cumulative link suits the unipolar creativity scale.
- **ATC-9** The M1 misfit pattern (R17, R12) is consistent with discrimination differences surfacing as misfit in the MFRM. Unordered steps and ordered GRM thresholds are not evidence for either family.
- **ATC-10** Score consequences: high correlations, yet ranking shifts (quintile changes) that matter for selection or labelling. The M1–GRM contrast mixes constraints and link. Includes the closing sentence of Results 3.4.
- **ATC-11** The fit evidence is limited by the design (S-X², C2, Q3, infit/outfit). Absence of misfit is not evidence of fit.
- **ATC-12** Information shares are not a ranking of rater quality; the intervals are wide for raters with few ratings.
- **ATC-13** The Krippendorff vs Cronbach contrast illustrates kaufman2008. The crossed-block α lies near the empirical reliability (cautious).
- **ATC-14** Recommendation: a calibration/anchor set rated by all raters, distinct from rater training.
- **ATC-15** Recommendation: model raters with JRT instead of averaging; report the empirical reliability and product SEs, and propagate them downstream.
- **ATC-16** Recommendation: a minimum workload per rater, and rater assignment informed by information functions.
- **ATC-18** The realised design departs from the planned benchmark-set design (if so).
- **ATC-19** Showing raters a creativity definition is a (minor) departure from the CAT "no criteria" procedure.
- **ATC-20** The exploratory framing (no confirmatory hypotheses) and the wording of RQ1–RQ3, SQ1 and SQ2 (RQ3(b) now also covers raw means).
- **ATC-21** (new) The mechanism sentence from notebook markdown `909a8bdd`: products with the same raw mean get different GRM scores "when they were rated by raters of different severity or discrimination". Discussion 4.4 only; not in Results.
- **ATC-22** (new) The interpretation of F2.9: scoring by the raw mean is consequential for which actions rank high, more so than the choice among IRT models (cross-table comparison with F2.7), and rater differences weigh less in the mean with more ratings per product (3+ group). Used in Discussion 4.4/4.5 and the Conclusion.
- **ATC-23** (new) The boxed design recommendations in Discussion 4.5 (OD6): the selection and wording of all items.

**Closed in this update:** ATC-17 (exclusion rationale and "insensitive" reading). The author supplied the wording verbatim at checkpoint 1 (OD4); it is used as given in Method 2.6 and L5.

---

## Evidence gaps (aims vs findings)

- **Aim 1, number of ratings.**
  - Addressed observationally via the by-n comparison (F1.14). There is no subsampling, experimental variation, D-study or simulation, and the per-n means have no CIs.
  - The practical "how many ratings" statement must stay descriptive. It will become firmer when the data grow [FI-19].
- **Aim 2, rater differences.**
  - Well supported: parameters with SEs, information with intervals, and the full response-style table (F0.8).
  - The raw response styles are unadjusted and have no uncertainty.
- **Aim 3, "must be modelled".**
  - Supported by the LR tests (F1.2), the model score agreement (F2.7) and now, **directly, by the raw-mean vs GRM comparison (F2.9, F2.10)**. The former gap (no raw-mean comparison) is closed.
  - Remaining gaps: no CIs for the raw-mean comparison; the subgroup and equal-raw-mean grouping definitions are undocumented [FI-20]; no test of the pattern across 1 / 2 / 3+ groups; the mechanism (rater severity/discrimination) is the notebook's explanation, not a tested result [ATC-21].
  - The M1–GRM agreement mixes constraints and link function.
- **Absolute model fit.** Not established: C2 is not computable (cause now documented), and S-X², Q3 and infit/outfit are limited by the design. No cut-offs are applied.
- **Out of scope (D10).** Rater expertise and rating-scale choices are not analysed. Expertise is mentioned only as future work.
- **MFRM fair averages.** No output exists. Fair scores are represented by EAP estimates only.
- **Bibliography.** All citekeys in this outline were grep-verified in the checkpoint-1 revision; no new citekeys were added in this update.
  - in `web_references.bib`: e.g., robitzsch2025, chalmers2018, orlando2000, kang2008, yen1984, christensen2017, cai2014, wright1982, green1984, cronbach1951, hayes2007, looney2004, heiniger2021, shin2025;
  - in `phd_library.bib`: myszkowski2019, myszkowski2021, primi2019, cseh2019, amabile1982, memmert2007, santos2016, kempe2018, memmert2011, runco2012, embretson2013, myford2003, myford2004, batey2012, barbot2019, barbot2019b, safardilha2019.
  - No Bayesian keys are used.

---

## Changes in this update (commit a97e51d; checkpoint-1 decisions applied)

- Status line set to approved at checkpoint 1; sources updated to 40 labels and the regenerated findings.
- **OD1:** working title kept.
- **OD2:** `tbl-score-agreement` MAIN, `tbl-theta-correlations` SUPP; both reliability-by-n objects MAIN; `fig-grm-information-shares` marked optional MAIN.
- **OD3:** new F2.9/F2.10 integrated: RQ3(b) widened to raw means; central contribution, core argument, abstract, Method 2.12, Results 3.4 (descriptive table), Discussion 4.4/4.5, Conclusion, Limitations L6 and Evidence gaps updated. `tbl-raw-mean-vs-grm` and `fig-raw-mean-vs-theta` both MAIN (figure placement justified). The `909a8bdd` mechanism sentence is Discussion-only [ATC-21].
- **OD4:** author's exclusion sentence verbatim in Method 2.6, paired with @tbl-sensitivity-rater-exclusion; L5 aligned; ATC-17 closed.
- **OD5:** response styles quoted at 3 decimals from the full F0.8 table; FI-10 removed; 6-decimal values banned.
- **OD6:** boxed design recommendations added to Discussion 4.5, every item [ATC-23].
- **OD7:** drafting proceeds now; [DD] refresh via FI-19.
- **D12:** the "produced by cutting" sentence replaced with the author's meaning (video cutting and imperfect material; close-ups or other TV artefacts render actions non-visible), with 1290 from F0.1.
- **Resolved items written into Method:** C2 cause (2.9), parameter-draw definition with the 87 rejected draws (2.10), LR df mechanism without the count (2.8), Q3 flag criterion (2.9) with mean Q3 −0.238 / 137 pairs / 20 flagged in Results 3.1, n_boot_failed 361 (2.10, 3.2), no infit/outfit cut-offs (2.9; range dropped).
- FI list: FI-5, FI-7, FI-8, FI-10, FI-13 and FI-14 removed; FI-18 updated (pipe escaping, new captions; absorbs FI-8 wording); FI-11 and FI-19 extended; FI-20 added. 19 → 14 open.
- ATC list: ATC-17 closed; ATC-21, ATC-22, ATC-23 added. 20 → 22 open.
- Object plan: 9 → 11 main (8 tables, 3 figures) + 1 optional; 24 supplement; 5 not embedded; total 40.

## Changes from the previous version (checkpoint-1 revision, kept for the record)

- The new working title and central contribution are organised around the three aims (D1, new main aim). The sparse design has been removed from the title, framing, abstract and contribution.
- The hypotheses H1a, H1b, H2 and H3 have been removed. The study is now exploratory, with RQ1–RQ3 (aims) and SQ1–SQ2 (supporting) (D3).
- Terminology: a single "judges = raters" sentence in Introduction P3; "product" is the analytic term and "action" is used for the stimulus and sport framing (D2).
- All finding IDs were renumbered to the regenerated `03_findings.md`.
- New outputs used (D8): ΔIC, exact LR p-values, threshold SEs; reliability CIs, Cronbach CIs; rater information CIs; score agreement.
- Exclusion sensitivity quotable (F2.8), with its own Results subsection 3.5 (D7).
- Main/supplement plan revised (D4, D5, D6, D9).
- The cleaning steps are given in the Method text, with the single D12 sentence (D12).
- The fit limitations moved from the Results/Discussion framing to Method 2.9 and Limitations L2.
- The scope was narrowed: expertise and the rating scale are left out (D10).

## Checkpoint-1 decisions (applied; no open decisions remain)

- **OD1 Title.** Working title kept.
- **OD2 Main-text objects.** `tbl-score-agreement` MAIN, `tbl-theta-correlations` SUPP; both reliability-by-n objects MAIN; `fig-grm-information-shares` optional MAIN if space allows.
- **OD3 Aim 3 evidence.** Raw-mean vs GRM comparison added to the notebook (F2.9, F2.10); `tbl-raw-mean-vs-grm` is the main-text support for RQ3(b); `fig-raw-mean-vs-theta` placed in MAIN (justified above).
- **OD4 Exclusion rationale.** Author's verbatim sentence in Method 2.6, with @tbl-sensitivity-rater-exclusion.
- **OD5 Response-style values.** 3 decimals as printed (F0.8).
- **OD6 Boxed design recommendations.** Yes; all items [ATC-23].
- **OD7 Timing.** Draft now; refresh [DD] values after the data update [FI-19].
