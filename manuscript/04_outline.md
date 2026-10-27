# 04_outline.md: Argument architecture (Phase 5), GRM/JRT version

> **Revision plan after checkpoint 2 (2026-10-26, relayed via coordinating session); notebooks at 91c2e6d.**

Profile: `imrad-apa`. Venue: *Creativity Research Journal*. Style: APA 7th.
Structure: Abstract, Introduction, Method, Results, Discussion, Conclusion, References.

Sources (all re-read for this update):
- Brief: `~/drive/KNOWLEDGE/Paper_CreativityAssessmentInSportsCAT.md`
- Dossier: `01_dossier.md`
- Labels: `02_artifacts.md` (regenerated after commit 91c2e6d; **42 labels**, including the new `tbl-grm-reliability-projection` and `fig-grm-reliability-projection`)
- Numbers: `03_findings.md` (regenerated after commit 91c2e6d; finding IDs stable; **new F1.20**; **revised F2.9** (tie-aware columns) and **F2.1/F2.2** (2 decimals)). This is the ONLY source of numbers.
- Review: `05_review.md` (draft 1; 3 critical, 12 major, 22 minor). Every point is mapped in "Revision plan vs 05_review.md" at the end of this file.
- Citekeys: `06_web_literature.md`, including "Targeted search 2026-10-23 (GRM methods)". Every key below was grep-verified in `phd_library.bib` or `web_references.bib` during the checkpoint-1 revision. No new keys are added in this update. No Bayesian references are used.

Conventions in this file:
- **F…** is a finding ID in `03_findings.md`. Every number below is copied from there exactly, as printed, apart from the APA leading-zero rule below.
- `tbl-…` and `fig-…` are labels from `02_artifacts.md`. **[MAIN]** means embedded in the main text. **[SUPP]** means embedded in the online supplement.
- **[ATC-n]** marks an interpretive or contribution claim that the author must confirm.
- **[FI-n]** marks a FILL IN item: information or an output that is missing and must come from the author or analyst. A FILL IN that needs a number is only usable after it has been added to a notebook and passed through results-interpreter. FI numbers are kept stable; resolved items are listed as resolved, not renumbered.
- **[DD]** marks a **design-dependent number**. These are counts, coverage and every value that will change when more ratings are collected (this now includes the projection, F1.20, because it is simulated from the fitted parameters). The author will add ratings before finalising.
  - The writer cites each [DD] number from its finding or embed and never builds framing on it. Avoid wording such as "most products were rated only once or twice" or "in this sparse design".
  - Practically, every Results number is [DD]. The tag marks the places where the *prose* would otherwise hard-code the current design.
- **APA number format (checkpoint 2, review m1/m2).**
  - Values that cannot exceed 1 are written **without a leading zero**: correlations (incl. Q3, Kendall's τ-b), reliabilities (incl. rel_post, rel_info, α), shares and proportions (incl. information shares, percentile shifts on the 0–1 scale, floor/ceiling rates), and p. Example: F1.12 "0.672 [0.649, 0.687]" is written ".672 [.649, .687]".
  - Values that can exceed 1 keep the leading zero: a, b_k, information, θ̂ and θ̂ ranges, PSD, infit/outfit, raw means, SDs, entropy, X², Δ information criteria, |Δθ̂|, |Δa|, the Q3 deviation criterion 0.2.
  - Dropping the leading zero is the only change allowed. **No rounding, no added or removed decimals.** "1" stays "1".
  - p-values: never scientific notation in the text. Write *p* < .001. The exact values 4.22e-105 and 1.79e-17 stay in `tbl-lr-tests` [SUPP] and are not quoted.
  - All values in this outline are already written in APA form, except inside the F-ID references themselves.
- Values marked NOT IN NOTEBOOK in `03_findings.md` are never used. This includes the count of unused end categories behind the LR df gap ("6", AUDIT.md only), any infit/outfit misfit range (e.g. 0.7–1.3, REPORT.md only), RMSEA or any other global fit index, and the definition of a "computable" Q3 pair.
- **Precision as printed.**
  - Rater parameters (F2.1, F2.2) are now printed at **2 decimals** as "estimate (SE)". The earlier 3-decimal values (e.g., 3.709, −6.565, 0.295) are no longer printed and must **not** be quoted anywhere.
  - Response styles (F0.8) are quoted at 3 decimals.
  - Sensitivity values (F2.8) are printed with 5 decimals and are quoted that way (see FI-18 for an optional 3-decimal reprint).
  - Category shares (F0.6) are printed with 6 decimals. Do not quote them; quote the printed counts instead (review m3).
- **Timing (OD7):** drafting proceeds now with the current [DD] values; every [DD] value is refreshed after the data update [FI-19].

---

## Working title (D1; OD1: kept)

**Number of ratings, rater differences, and score reliability in creativity ratings of football actions: A judge response theory analysis**

The author kept this working title at checkpoint 1. It follows the three aims, uses retrievable keywords (creativity ratings, football, judge response theory, reliability, rater differences) and does not mention the design's sparsity. The projection (F1.20) strengthens the "number of ratings" part, so no change is needed.

Alternatives (kept for reference only):
- (b) *Rater differences and score reliability in consensual creativity ratings of football actions: A judge response theory analysis*
- (c) *Modeling rater differences in creativity ratings of football actions with judge response theory*

## Terminology (D2; review m16, m17)

- **Raters.** Say once, at the first mention of the CAT in the Introduction (P3), that the CAT and JRT literature calls raters "judges". Use **"rater"** everywhere after that. "Judge" survives only in the fixed term *judge response theory* (JRT) and in quotations.
- **Product / action (D2 kept; m16).** "Product" is the analytic term. It is introduced once in Method 2.3: "each rated product was a single football action".
  - "Action" appears in the title, in the Introduction's sport framing, in the description of the stimulus material, and in the practical recommendations (Discussion 4.5, box, Conclusion), where the first mention reads "ratings per action (i.e., per product)".
  - Results and Method use "product" only. The writer checks that no Results or Method sentence switches to "action" (m16).
- **Average information (m17).** The quantity info_weighted_area is called "average information" (information integrated over θ ~ N(0, 1)). Define it once in Method 2.11. Do not write "information per rating" in the text, since it is not per observed rating. The caption of `tbl-grm-rater-information-ci` still says "Average information per rating" [FI-18].
- **Notebook terms.** NB01 captions and axis text say "products". "Action" survives only in the label `tbl-overview-ratings-per-action` (not embedded) and in NB00 (not embedded). Do not edit captions in the manuscript.

---

## Central contribution [ATC-1]

The study applies judge response theory (JRT) to CAT-style creativity ratings of football actions. The final data are given in @tbl-design-summary (F0.3 [DD]). In these data, the study shows three things.

1. **How many ratings, and from whom, determines the reliability of the scores [ATC-24].**
   - The reliability of the product scores actually obtained (empirical marginal reliability) is .672 [.649, .687]. A hypothetical full panel would reach .960 [.953, .968], and the pairwise Cronbach's α of the unweighted rater mean is .928 [.891, .943] (F1.12, F1.18 [DD]).
   - A projection from the fitted GRM (F1.20 [DD]) shows how reliability rises with the number of ratings per product (k) *and* how much it depends on which raters give them:
     - random raters: .508 at k = 1, .688 at k = 2, .857 at k = 5, .925 at k = 10;
     - the k most informative raters: .754 at k = 1 to .947 at k = 10;
     - the k least informative raters: .108 at k = 1 to .884 at k = 10.
   - One rating from the most informative raters (.754) gives a higher projected reliability than two ratings from randomly drawn raters (.688). This links RQ1 to RQ2: who rates matters as much as how many [ATC-24].
   - The projection treats the model parameters as known (F1.20 note).
2. **Raters differ in severity, scale use and discrimination, and the uncertainty of each difference is quantified.**
   - Among the raters with at least 400 ratings, discrimination ranges from 0.86 (R09, SE 0.15) to 2.81 (R06, SE 0.42) (F2.1). The "at least 400" grouping is the writer's descriptive choice, read off the printed n column; state it as such.
   - Threshold locations and raw category use differ widely: for example, the floor rate (share of ratings of 1) runs from .579 (R06) to .016 (R13) (F0.8), and R06 is the only rater with a positive first threshold, 0.29 (SE 0.06) (F2.2).
   - Average information varies between raters, e.g., R09 0.238 [0.110, 0.419] vs R02 1.705 [0.903, 2.558] (F2.4).
   - Parameters of raters with few ratings are imprecise (e.g., R19 a 3.71, SE 2.22) and are not used as headline values.
3. **Treating raters as equivalent is not tenable for category structure and discrimination, and the scores change when rater differences are ignored.**
   - Likelihood-ratio tests reject a shared category structure and equal discrimination (both *p* < .001; F1.2). AIC supports the second step; BIC does not (F1.1).
   - Raw mean ratings, the common-practice score, order products differently from the GRM scores (F2.9 [DD]):
     - Kendall's τ-b = .796, and .083 of product pairs with different raw means are ordered the other way round by the GRM score;
     - even with raw-mean ties broken in the GRM's favour, .237 of products change quintile (the smallest change any tie-breaking can give);
     - with a single rating, products with the same rating receive GRM scores up to 1.436 apart.
   - Product rankings under the constrained models also differ from the GRM: .202 of products change quintile under the MFRM/RSM, although Pearson r = .975 (F2.7 [DD]).
   - These are differences between scores, not evidence that one score is more accurate (review M1). The GRM *adjusts for* the modelled rater differences [ATC-15, ATC-22].

Implication for sport-science creativity research [ATC-5, ATC-14, ATC-15, ATC-24]: plan the number of ratings per action, and the raters who give them, for a target score reliability; link raters through a common calibration set; and model rater differences (JRT) instead of averaging ratings. These implications refer to this student rater pool and this scale [FI-21].

## Core argument (5 sentences)

1. Reliability of CAT ratings is conventionally reported as the consistency of a mean over a panel of raters, and it grows with panel size (amabile1982; kaufman2008; cseh2019). In applied studies that rate many actions, however, each action receives only a certain number of ratings, so the precision of each score depends on that number and on which raters gave them.
2. JRT treats raters as items with their own severity, scale use and discrimination (myszkowski2019; myszkowski2021). The fitted model therefore gives (a) the reliability of the scores actually obtained, (b) a projection of the reliability for any number of ratings and any choice of raters, and (c) an explicit, uncertainty-quantified description of how raters differ.
3. In the football ratings:
   - the reliability of the actual scores is well below the full-panel value (F1.12);
   - the projection shows that reliability rises with the number of ratings and depends strongly on which raters give them (F1.20);
   - raters differ in severity, scale use, discrimination and information (F0.8, F2.1–F2.4).
4. The Rasch/MFRM constraints that treat raters as equivalent in category structure and discrimination are rejected (F1.2). Scoring by the raw mean, which ignores rater differences altogether, orders a non-trivial share of products differently from the GRM, and with a single rating the same rating maps to clearly different scores depending on the rater (F2.9, F2.10). The scoring model chosen also shifts rankings even when overall correlations are high (F2.7). **No comparison is made between the raw-mean and the model-choice statistics** (F2.9 comparability note).
5. Rater differences therefore need to be acknowledged in the design (ratings per action, choice of raters, a common calibration set) and in the scoring (JRT rather than averaging) of creativity research in sport [ATC-3, ATC-6, ATC-7, ATC-24].

## Research questions (D3: exploratory; no confirmatory hypotheses; review M10)

The analyses were not guided by hypotheses fixed before the analysis. The study is framed as **exploratory**, and the RQs below are answered descriptively. The writer must not use the words "hypothesis", "supported" or "confirmed" for them. The only exception is the D13 wording for the LR/AIC evidence (see RQ3). [ATC-20: confirm the exploratory framing and the RQ wording; FI-15: preregistration status.]

**Research questions (one per aim)**

- **RQ1 (aim 1): number of ratings and reliability.** How does the reliability of creativity scores depend on the number of ratings per product (i.e., per action), and on which raters give them? How does the reliability of the scores actually obtained compare with the reliability of a hypothetical full panel and with conventional agreement and consistency indices?
  - Primary evidence: **F1.20** (projection), F1.12, F1.18, F1.19.
  - Secondary, descriptive: F1.13, F1.14, F1.16, F1.17.
- **RQ2 (aim 2): rater differences.** How do raters differ empirically in their rating behaviour? This covers severity (threshold location), scale use (threshold spacing, category use, response styles), discrimination, and their contribution to information. How precisely are these differences estimated?
  - Evidence: F0.6, F0.7, F0.8, F2.1, F2.2, F2.3, F2.4, F2.5.
- **RQ3 (aim 3): how much do the scores depend on whether rater differences are modelled?** (Reworded descriptively, review M10.) Two parts:
  - (a) Are the constraints that treat raters as equivalent in category structure (RSM/MFRM) and in discrimination (PCM) tenable for these ratings?
  - (b) How far do product scores and rankings change when rater differences are ignored (raw mean ratings) or constrained (RSM/MFRM, PCM, GPCM)?
  - Evidence: (a) F1.1, F1.2, F1.4, F1.5, F1.11; (b) **F2.9, F2.10** (raw mean vs GRM), F2.6, F2.7.
  - D13 wording: rater-specific discriminations (M2 → M3) are reported as **supported by the LR test and AIC**. The BIC disagreement is reported factually.
  - RQ3(a) does not test severity differences as such (review M2). Severity is described under RQ2 and in the raw-mean comparison; a formal test is an optional analyst action [FI-24].

**Supporting analyses (no longer research questions; review M10)**

The former SQ1 and SQ2 are now analysis steps in the Method, not research questions. Their results are reported briefly where the RQs need them.
- **Model choice and adequacy** (former SQ1): which scoring model describes the ratings best, and what fit evidence is available (Method 2.8–2.9; Results 3.1). Evidence: F1.1, F1.3, F1.7, F1.8, F1.9, F1.10.
- **Model dependence of scores** (former SQ2): how strongly product scores depend on the choice among the four models (Method 2.12; Results 3.4, as part of RQ3(b)). Evidence: F2.6, F2.7; F2.8 for robustness to the rater exclusion.

---

## Section outline

### Abstract (single paragraph, unstructured, ≤ 250 words; check the CRJ limit [FI-16]; review m21)

Purpose: a standalone summary that persuades CRJ and sport-science readers. It follows abstract Model 2: background/aim → method → results with naked numbers → implications. It has no citations and **no sparse-design framing**. Results numbers are [DD], so the writer re-copies them from the findings after each data update. **Fewer numbers than draft 1** (m21): at most two numbers per aim. No R18 values (author constraint; review M4).

- **Background/gap (1–2 sentences).**
  - CAT ratings are the standard way to assess creative products and are increasingly used for actions in sport.
  - However, it is unknown how many ratings an action needs for a reliable score, and how much raters differ when they judge creativity in sport.
- **Aim/method (1–2 sentences).**
  - Student raters rated football actions on a 7-point creativity scale. Counts come from F0.3 [DD].
  - Judge response theory models were fitted by marginal maximum likelihood: a graded response model (GRM), compared with an adjacent-category ladder from the many-facet Rasch model to the generalized partial credit model. Reliability by number of ratings was projected from the fitted GRM.
- **Results (3–4 sentences, naked numbers).**
  - Aim 1:
    - The empirical reliability of the obtained scores was .672, against .960 for a hypothetical full panel (F1.12).
    - In the projection, reliability with randomly drawn raters rose from .508 for one rating to .857 for five, and one rating from the most informative raters reached .754 (F1.20).
  - Aim 2: among raters with at least 400 ratings, discrimination ranged from 0.86 to 2.81 (F2.1); raters also differed in threshold location and category use.
  - Aim 3:
    - LR tests rejected a shared category structure and equal discrimination (both *p* < .001; F1.2).
    - Raw mean ratings and GRM scores agreed only partly (Kendall's τ-b = .796; F2.9); with a single rating, the same rating corresponded to GRM scores up to 1.436 apart.
- **Implications (1–2 sentences, hedged) [ATC-5, ATC-14, ATC-15, ATC-24].** For this kind of rater pool, creativity studies in sport should plan both the number of ratings per action and who gives them, link raters through a common calibration set, and model rater differences rather than average them.
- Do **not** use: 0.350 / .350, the comparison with .202, any b1 value, "we show that … depends on" (causal wording; C3), "must be modelled" as a finding.

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
  - Independent raters usually reach α > .70 (baer2004; kaufman2008; hennessey2011) [FI-17: verify against PDFs, review m11]. Other studies report much lower agreement (long2015; cseh2019).
  - CAT requires raters familiar with the domain (amabile1982). Mention this neutrally here, so that the rater-pool description in Method 2.2 and Limitation L4 can refer back to it (review M8). Do not claim that the present raters meet or miss the requirement [FI-21].
- P4. **Reliability rests on the number of raters (sets up aim 1).**
  - Spearman–Brown reliability depends on the mean inter-rater correlation and on the number of raters (amabile1982). A high α from a large panel can mask low single-rater agreement (kaufman2008).
  - The number of raters needed is domain-specific and must be established per domain (cseh2019). The "5–10 judges" rule of thumb comes from kaufman2008a [FI-17: verify, review m11].
  - Key distinction, worded neutrally and in general terms (not about this data set): a panel coefficient describes the mean over all raters. When many products are rated and each receives only some ratings, what matters is the precision of each product's score given *its* ratings, and a fitted model can project that precision for other numbers of ratings (forthmann2023; primi2019).
- P5. **Raters differ (sets up aim 2).**
  - Raters differ in severity, use of the scale and beliefs about creativity (long2015). Their tendencies drift over time (barth2020).
  - The classic rater-effect taxonomy covers severity, central tendency, restriction of range and halo (engelhard1994; myford2003; myford2004).
  - In judged sports, judges' differences in accuracy and bias have been monitored with Rasch/MFRM or statistical models, for performance quality rather than creativity (looney2004; anderlucci2021; heiniger2021).
- P6. **From averaging to JRT: successive relaxation of rater assumptions (sets up aim 3; review M2).** Condense the brief's paragraph and keep its logic, but keep the three kinds of rater difference separate:
  - **Severity.** Unweighted means treat raters as interchangeable. When different raters rate different products, the means are confounded with rater severity (primi2019). The MFRM adds a severity facet that corrects for this (linacre1989; eckes2015; primi2019).
  - **Category structure and discrimination.** Beyond severity, the MFRM still assumes a shared category structure and equal discrimination; unequal discrimination appears only as misfit (myford2004; myszkowski2021). Means and α additionally assume (essentially) τ-equivalent raters (myszkowski2019).
  - Do **not** call the Rasch constraints "weaker" than essential τ-equivalence (review M2).
  - IRT basics: lord1980; embretson2013; deayala2022. Rasch models and polytomous extensions: rasch1960; bond2020; RSM andrich1978; PCM masters1982.
  - JRT treats raters as items with their own discrimination and thresholds, via the GPCM (muraki1992) or the GRM (samejima1969) (myszkowski2019; myszkowski2021).
  - Applications: barbot2023; pellegrino2025, who also retained a GRM; forthmann2023 on planned-missing rating designs.
  - Adjacent-category vs cumulative link (from the brief's "Methodological choices"):
    - RSM/PCM/GPCM are nested, so their constraints are testable by LR.
    - The GRM is cumulative and arguably matches a cumulative "amount of creativity" scale [ATC-8]. The families are compared by information criteria.

**Move 3: Gap (1 paragraph, opened with "However")**
- P7. **Creativity in sport, and the gap.**
  - Research has focused on the creative process, such as divergent thinking (memmert2011).
  - Product ratings of football actions exist: kempe2018 (trained experts; face validity via proximity to goals); memmert2007 (expert-rating scale for tactical creativity); zahno2023; dejoode2023.
  - These studies average ratings and report ICCs or agreement only [FI-17: verify this characterisation against the PDFs, review "Citations"]. A Rasch validation exists only for a coach-completed creativity questionnaire, not for ratings of actions (shin2025).
  - "However" sentence, three gaps:
    - (i) there is no evidence on how many ratings per action are needed for a reliable creativity score in sport (cseh2019);
    - (ii) there is no evidence on how raters differ when they judge the creativity of sport actions;
    - (iii) to our knowledge, no study has modelled these rater differences with IRT/JRT for creativity ratings in sport [ATC-2]. The search was not systematic, so phrase the claim cautiously.

**Move 4: Present study (1 short paragraph)**
- P8.
  - Data: a large set of CAT-style creativity ratings of football actions by multiple raters. Give the counts only by reference to Method/@tbl-design-summary [DD].
  - Exploratory aim: (1) number of ratings and reliability, (2) rater differences, (3) how much the scores depend on whether rater differences are modelled.
  - State RQ1–RQ3 (wording above). Say explicitly that no confirmatory hypotheses were formulated. Do not list SQs (review M10).
  - One sentence on the analytic route: JRT model ladder plus GRM, estimated by MML in mirt; reliability of the obtained scores and a model-based projection by number of ratings and choice of raters; rater parameters with intervals; comparison of GRM scores with raw mean ratings.
  - Scope sentence (D10): rater expertise and the design of the rating scale are not analysed in this paper.
  - Do **not** mention "labels for automated rating" anywhere (review m12).

### 2 Method

Purpose: allow replication and justify the analytic choices. The section runs top-down (writing-models/methods.md): overview → details → relation to prior methods → problems. The sparse-design issues appear **here, briefly**, and in Limitations, but nowhere in the framing. All FILL IN items stay as FILL IN in the draft (author constraint).

**2.1 Overview and study context (move 1)**
- One paragraph:
  - CAT-style rating study: independent raters, relative judgements, randomised order (amabile1982; hennessey2011).
  - The products are football actions, rated as part of a larger project [FI-1, FI-2].
  - Ethics approval and consent [FI-1].
  - Exploratory analysis; preregistration status [FI-15; ATC-20].

**2.2 Raters (move 2)**
- Recruitment: Bachelor's and Master's students rating as part of thesis projects (vault background; the author must confirm and give the numbers) [FI-1].
- **Rater-pool description [FI-21]:** number of raters who started; football playing or coaching experience; any instruction or practice before rating; number of sessions per rater; demographics; compensation. If something was not recorded, say so in one sentence; this links to Limitation L4 (review M8).
- Final number of raters, and ratings per rater from 50 to 1174 (F0.3 [DD]).
- Pseudonyms R01–R19.

**2.3 Products and stimulus material (move 2)**
- Introduce the product term: "each rated product was a single football action".
- Source of matches and competitions, the action-selection rule (event data), clip length and number of matches [FI-2]. The vault describes FIFA, AFCON, UEFA and Copa América matches with StatsBomb events; the author must confirm.

**2.4 Rating procedure (moves 2–3)**
- Rating software [FI-3].
- Instruction and the creativity definition shown to raters (originality × functionality in game context; runco2012) [FI-3].
- Relate showing a definition to the "no criteria" CAT rule (hennessey2011) and to trained-rater sport studies (kempe2018; memmert2007) [ATC-19].
- 7-point unipolar scale with anchors 1 / 4 / 7 [FI-3 confirm the anchors], plus an off-scale "action not recognised" option [FI-3: wording].
- Randomised order; session length and breaks; data-collection period (timespan; review m20) [FI-3].
- Other dimensions rated (technical correctness, aesthetic appeal), which are not analysed here [FI-3].

**2.5 Rating design (moves 2 and 4, brief; review C2)**
- How products were allocated to raters: planned overlap, a common/benchmark set, randomisation, thesis-specific subsets or rater dropout [FI-4]. State explicitly **how products came to have 1, 2 or 3+ ratings**, and whether products with 4+ ratings differ systematically (match, action type, rater composition) [FI-4]. This is needed for the ignorable-missingness assumption of MML.
- Not every rater rated every product. The design is incomplete but connected (one component; F0.3 [DD]). The coverage numbers are given in @tbl-design-summary; do not elaborate on them here.
- If the planned benchmark set was not realised as a fully crossed block, state this neutrally [ATC-18].

**2.6 Data preparation and final data (moves 2 and 4)**
- Cleaning, in the text only (D6: no cleaning-log table). From F0.1 [DD]:
  - 9148 raw rows;
  - 1290 ratings marked "action not recognised" removed;
  - 1 out-of-range value removed (0.0 by R04);
  - 13 rows removed when resolving duplicate rater–product pairs (12 pairs, 1 with conflicting values; the last entry kept; F0.3 duplicate rows);
  - result: 7844 rows.
- **D12 sentence (exactly one, short; author's meaning), now marked (review M7, m10):** "The 1290 ratings marked 'action not recognised' were removed; such ratings result from video cutting and imperfect material, where close-ups or other TV artefacts render the action non-visible." **[AUTHOR TO CONFIRM; ATC-27]**
  - Add one sentence with the non-recognition rate by rater (and, if available, whether it concentrates on particular products) **[FILL IN; FI-22]**. The overall count (1290 of 9148 raw rows) is printed in F0.1; do not compute a percentage from it in the text.
  - Do not discuss non-recognition further except in Limitation L1.
- **Rater exclusion (D6; OD4 wording, revised at checkpoint 2):**
  - Facts (F0.2; `tbl-excluded-raters` [SUPP]): R20 (13), R21 (9) and R22 (2), together 24 ratings; one product rated only by them was dropped.
  - Rationale, as a technical estimation criterion only (author's OD4 wording, first half verbatim): "Raters with fewer than 15 ratings were excluded because their up to seven rater-specific parameters cannot be estimated reliably." Add the source or rationale for the value 15 **[FILL IN; FI-23]** (review M9). Do not present 15 as sufficient or as a recommendation anywhere.
  - Robustness, second half of the OD4 sentence, now marked and paired with the largest change: "excluding them did not change the scores **[AUTHOR TO CONFIRM; ATC-26]** (largest change in a product score 0.16246; see @tbl-sensitivity-rater-exclusion)". The reviewer's alternative "changed them negligibly" (m4) is offered to the author as an option under ATC-26.
  - Point forward to the sensitivity analysis in Results 3.5 (F2.8).
- **Final data** (F0.3; `tbl-design-summary` [MAIN]; all [DD]):
  - 7820 ratings of 3668 products by 19 raters; scale 1–7, coded 0–6 internally.
  - Ratings per product: mean 2.132, median 2, range 1–10, harmonic mean 1.726.
  - Matrix fill .112; one connected component; 17 of 171 rater pairs without a common product; median pairwise overlap 13.
  - Writer: quote these once, via the table, and do not repeat them as framing elsewhere. The distribution of ratings per product is in `fig-overview-degree-distributions` [SUPP] and in the n_products column of `tbl-grm-reliability-by-n` [SUPP].
- **Category gaps** (F0.7; `tbl-category-usage` [SUPP]):
  - five raters left top categories unused: category 7 by R01, R03, R06 and R18; categories 6–7 by R17;
  - no rater has an internal gap;
  - consequence: these raters have fewer thresholds in mirt.

**2.7 Measurement models (moves 2–3)**
- Common JRT frame (myszkowski2019; myszkowski2021):
  - raters are items and products are persons;
  - unidimensional creativity θ ~ N(0, 1);
  - b_k is "the θ at which a rating above category k becomes more likely than a rating of k or below; higher b means a stricter rater" (F2.2 note, revised wording); scale use is the threshold spacing, and discrimination is a.
  - In the GRM, thresholds are expressed relative to discrimination, so a low-discrimination rater has widely spaced thresholds. State this once here, so that Results 3.3 does not read spacing as separate evidence of scale use (review M4) [ATC-6].
- Adjacent-category ladder:
  - M1: RSM (andrich1978), equivalent to a two-facet MFRM (linacre1989; eckes2015; primi2019), estimated with sirt::rm.facets (robitzsch2025);
  - M2: PCM (masters1982);
  - M3: GPCM (muraki1992).
  - M2 and M3 are estimated in mirt (chalmers2012).
  - How sirt treats raters with unused end categories under the shared category structure of M1 **[FILL IN; FI-25]** (review M3).
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
  - M1 vs M2 is a cross-software comparison (sirt vs mirt). The two packages may differ in quadrature and constants, so the test is approximate (review M3). A same-package check is an optional analyst action [FI-25]; if it is not done, keep this sentence and Limitation L6.
  - **df of the M1–M2 test (F1.2):** the formula value (J − 1)(K − 2) = 90 assumes that every rater used all 7 categories. A rater who never used an end category has one step parameter fewer in M2, so the observed df (84) is smaller by the number of unused end categories; the unused categories are listed per rater in @tbl-category-usage. **Do not quote the number of unused end categories** (NOT IN NOTEBOOK; the writer must not count it from the table either).
  - No model without rater severity (M0) was fitted, so severity differences are not tested formally (review M2) [FI-24].

**2.9 Model adequacy (moves 2 and 4, brief, with the limits stated here once)**
- Rater infit/outfit mean squares (wright1982) for M1 and the GRM; expected value 1. **No misfit cut-offs are applied** (F1.7, F1.11). Do not mention any cut-off range. Note (F1.7 caveat): with about 2 ratings per product, values below 1 are expected because the score is estimated from the ratings being checked.
- S-X² (orlando2000; kang2008), with missing ratings multiply imputed (20 imputations). The notebook calls the test conservative because most cells are imputed (F1.8 caveat; "about 90%" is the notebook wording, [DD]). Add, plainly: because the imputed cells come from the fitted model itself, the test has little power to detect misfit (review m5) [ATC-11].
- Yen's Q3 (yen1984): the correlation of two raters' residuals over the products both rated. Q3 is negatively biased with few raters per product (christensen2017), so pairs are compared by their deviation from the mean Q3 over all computable pairs. **Flag criterion (F1.9):** a pair is flagged when it has at least 30 jointly rated products and its Q3 deviates from the mean Q3 by more than 0.2. Say that this criterion has no reference distribution (review m6). Do not define "computable" (not in the notebook).
- C2 (cai2014), a limited-information test of overall fit, **could not be computed: it needs the joint distribution of every rater pair, which is undefined for the 17 of 171 rater pairs that share no products** (F1.10 [DD]). State this once, neutrally, here; refer back to it in Limitations. Do not embed `tbl-grm-global-fit`.

**2.10 Scores and reliability (move 2; aim 1)**
- Product scores: EAP θ̂ with the posterior SD (PSD) as the conditional standard error.
- **Empirical marginal reliability** (primary for the actual scores): Var(θ̂) / (Var(θ̂) + mean PSD²). It refers to the scores actually obtained.
- **Model-based marginal reliability** (green1984; mirt marginal_rxx) refers to a hypothetical product rated by all raters. A grid computation serves as a check.
- **95% intervals (F1.12):** both come from 200 accepted draws of the model parameters from their asymptotic normal distribution (estimates and Oakes covariance matrix). For the empirical reliability, products are also resampled in each draw. A draw was rejected and replaced when it was not a valid GRM, i.e., when some discrimination was ≤ 0 or some rater's thresholds were out of order.
  - Quote the 87 rejected draws once, here ("87 draws were rejected and replaced") [DD].
  - Add (review M5): the intervals are therefore conditional on valid parameter sets and are approximate, especially for raters with few ratings. Which raters caused the rejections, draws on a transformed scale, and more draws are optional analyst actions [FI-28].
- **Projected reliability by number of ratings (NEW; primary evidence for RQ1; F1.20; notebook note `94cdcfeb`, stdout `368bd615`):**
  - Products with θ ~ N(0, 1) are simulated; each gets k ratings (k = 1 to 10) drawn from the fitted GRM, and is scored with the fitted parameters.
  - Raters are either drawn at random for each product, or fixed to the k most or the k least informative raters (by average information; see 2.11 and `tbl-grm-information-summary`).
  - "50 replications of 2000 simulated products per k and rater set; seed 20260713" (stdout `368bd615`).
  - Three measures per k and rater set: the empirical marginal reliability (as for the real scores), the squared correlation with the true θ, and the mean product-level reliability. Bands are the 2.5% and 97.5% quantiles over replications.
  - **Limitation stated here: "Model parameters are treated as known"** (notebook note). The bands therefore reflect simulation variability only, not parameter uncertainty, and are not the same kind of interval as the parameter-draw intervals above. A version with parameter uncertainty is an optional analyst action [FI-28].
  - Do not quote the notebook phrase "which brackets the effect of who rates" here; if the author wants it, it goes to the Discussion under [ATC-25].
- **Product-level reliability (descriptive, secondary):**
  - rel_post = 1 − PSD². State explicitly that rel_post is defined relative to the unit prior variance of θ, so with one or two ratings it partly reflects the prior (review M6). A latent-distribution sensitivity check is an optional analyst action [FI-27];
  - rel_info = I/(I + 1), from the information of the product's own raters at θ̂;
  - consistency check between the two;
  - summaries by the number of ratings each product actually received (observed; not used for planning).
- **Conventional indices** (reference values for common practice; not used downstream, F1.18 note):
  - Cronbach's α (cronbach1951) from pairwise covariances over all usable raters, and on the largest fully crossed block. State why 5 raters were not usable for the pairwise version [FI-9].
  - Krippendorff's ordinal α (hayes2007).
  - 95% bootstrap CIs over products (1000 replications). **The pairwise Cronbach CI is approximate:** replications in which a rater pair loses all shared products cannot be computed; 361 of the 1000 replications failed, and the interval uses the remaining ones (F1.18 [DD]). Add (review m7): the successful replications are not a random subset of all resamples, so the interval may also be biased [ATC-11].
  - Optionally cite tenhove2024 on indices in incomplete designs.

**2.11 Rater parameters, information and response styles (move 2; aim 2)**
- GRM a and b_k with Oakes SEs.
- **Average information** (m17): rater information integrated over N(0, 1). Each rater's share of full-panel information, weighted and at selected θ.
- 95% intervals for average information and share from the same parameter draws as in 2.10 (F2.4), with the same caveat (conditional on valid draws; approximate for raters with few ratings).
- Descriptive response styles on the raw 1–7 scale (F0.8):
  - mean, SD, categories used, entropy (natural log), floor (share of 1s) and ceiling (share of 7s) rates, extreme (1, 7) and central (3–5) rates;
  - not adjusted for which products each rater saw.

**2.12 Score agreement and sensitivity (move 2; RQ3b)**
- **Raw mean vs GRM (F2.9; revised for ties, review C1):** each product's unweighted mean rating, the common-practice score that treats raters as interchangeable, is compared with its GRM EAP score, overall and by number of ratings per product (1, 2, 3+):
  - Pearson and Spearman correlations, and **Kendall's τ-b**;
  - **share of discordant pairs:** among product pairs with different raw means, the share that the GRM orders the other way round;
  - **share of products changing quintile with ties resolved:** raw-mean ties ordered by the GRM score, "the smallest change any tie-breaking can give" (notebook `8620cb46`);
  - share of products whose raw mean is shared by another product;
  - range of GRM scores among products with the same raw mean (mean and maximum).
  - State, with the notebook: the raw mean has many ties (with one rating it takes only 7 values), and tied products share one percentile rank, so the plain share changing quintile and the percentile shifts overstate the disagreement. These plain columns stay in the table but are not quoted in the text.
  - Describe the grouping only as the notebook does. Whether percentiles/quintiles in the subgroups are computed within each subgroup, and how the equal-raw-mean groups are formed in the pooled "all" row, is not documented [FI-20].
- Pearson and Spearman correlations of EAP scores between all models.
- Relative to the GRM (F2.7):
  - absolute shift in percentile rank (0–1 scale);
  - share of products changing quintile, and changing by ≥ 2 quintiles.
- The two comparisons are reported separately. The notebook states that the plain raw-mean quintile share is not comparable with the model comparison, and it says nothing about the tie-resolved share, so **no statistic from `tbl-raw-mean-vs-grm` is compared with `tbl-score-agreement`.**
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

**Revision rules for Results (review M11):**
- Report key contrasts and point to the tables for the rest. No lists of a dozen deltas.
- No interpretive sentences. The draft-1 summary sentence "raters were heterogeneous in all parameters", the phrase "also differed" without a test, the second half of the information-interval sentence ("Wide intervals indicate …") and the closing ATC-10 conclusion of 3.4 all move to the Discussion.
- APA numbers: no leading zero for values that cannot exceed 1; *p* < .001 only.

Statistics follow APA. **Order:** the scoring model first, briefly (supporting, because RQ1 and RQ2 use the GRM). Then RQ1 → RQ2 → RQ3 → sensitivity. Every number is [DD].

**3.0 Overview (1 short paragraph, move 1)**
- Echo the three aims. All analyses use the final data in @tbl-design-summary.
- Give a descriptive one-line preview, with no evaluative words:
  - the GRM retained;
  - the reliability of the actual scores below the full-panel value; projected reliability rising with the number of ratings and differing by which raters give them;
  - rater parameters and their uncertainty;
  - the LR tests of rater-equivalence constraints, and the agreement of raw mean scores with GRM scores.

**3.1 Scoring model (supporting analysis; kept short)**
- Findings: F1.1, F1.3, F1.7, F1.8, F1.9, F1.10.
- Embed: `tbl-model-fit` [MAIN].
- Cross-reference:
  - `tbl-grm-convergence` [SUPP]
  - `tbl-grm-rater-fit` [SUPP]
  - `tbl-grm-q3-flagged` [SUPP]
- Not embedded: `tbl-grm-global-fit`.
- Bullets:
  - Information criteria (@tbl-model-fit): the GRM has the lowest AIC, BIC and SABIC. The GRM and M3 have the same number of parameters (127), so the comparison reduces to logLik: −11733.227 vs −11756.510, a difference of 46.566 on all three criteria (F1.1). Leave all other Δ values to the table (M11).
  - The GRM converged after 165 EM iterations; information matrix positive definite (F1.3).
  - Fit, in one or two sentences with pointers to [SUPP]:
    - No rater's S-X² was significant (*p* from .294 to .671; F1.8); Method 2.9 states why this carries little information.
    - Infit ranges from 0.334 (R19) to 0.971 (R18) and outfit from 0.322 (R19) to 0.961 (R18); all below 1 (F1.7).
    - Q3 (F1.9): the mean Q3 over 137 computable rater pairs is −.238; 20 pairs are flagged. The 10 pairs shown in @tbl-grm-q3-flagged (largest deviation from the mean Q3) are 10 of the 20; 9 deviate negatively and 1 (R10–R11) positively.
    - C2 was not computable (see Method 2.9; F1.10).
  - Move 3: point to the limits stated in Method 2.9 in one clause.
  - Do not quote RMSEA or any misfit range (none in the notebook; no cut-offs applied).

**3.2 Number of ratings, choice of raters and reliability of the creativity scores (RQ1; aim 1, the central subsection)**
- Findings: **F1.20 (primary)**, F1.12, F1.18, F1.19; secondary F1.13, F1.14, F1.16, F1.17.
- Embed:
  - `fig-grm-reliability-projection` [MAIN] (NEW; primary)
  - `tbl-reliability-overview` [MAIN]
- Cross-reference:
  - `tbl-grm-reliability-projection` [SUPP] (NEW); its values are quoted in the text
  - `tbl-grm-reliability-by-n` [SUPP] (moved from MAIN)
  - `fig-grm-rel-post-by-n` [SUPP] (moved from MAIN; justification in the object plan)
  - `tbl-grm-reliability-ci` [SUPP]; its CIs are quoted in the text
  - `tbl-grm-reliability-summary` [SUPP]
  - `tbl-naive-indices` [SUPP]
  - `fig-grm-rel-post-histogram` [SUPP]
  - `fig-grm-rel-post-by-theta` [SUPP]
  - `fig-grm-rel-consistency` [SUPP]
  - `fig-grm-panel-information` [SUPP]; its caption keeps "hypothetical"
- Bullets, in this order:
  - **(1) Projected reliability by number of ratings and choice of raters** (@fig-grm-reliability-projection, @tbl-grm-reliability-projection; F1.20 [DD]). Report the empirical marginal reliability only:
    - It rises with every additional rating in all three rater sets.
    - Random raters: .508 (k = 1), .688 (k = 2), .857 (k = 5), .925 (k = 10).
    - Most informative raters: .754 (k = 1) to .947 (k = 10). Least informative raters: .108 (k = 1) to .884 (k = 10).
    - At every k, the most informative raters give the highest value and the least informative the lowest; the gap narrows with k (k = 1: .754 / .508 / .108; k = 5: .920 / .857 / .701; k = 10: .947 / .925 / .884).
    - Within the same table: one rating from the most informative raters (.754) exceeds two ratings from randomly drawn raters (.688). This is a descriptive comparison of printed values; its reading ("who rates matters as much as how many") goes to the Discussion [ATC-24].
    - The other two measures (squared correlation with the true θ, mean product-level reliability) agree with the empirical value to within .003 in every row; say so once and refer to the supplement table.
    - No projected value reaches the full-panel value of .960; the highest is .947.
    - Move 3: parameters are treated as known, so the bands show simulation variability over 50 replications only (Method 2.10); the rater sets behind "most" and "least informative" are not printed; k runs to 10 only. **Do not derive or state a number of ratings needed for any target reliability** (not printed).
  - **(2) Actual vs hypothetical vs conventional** (@tbl-reliability-overview; CIs from F1.12, F1.18):
    - empirical marginal reliability (actual scores): .672 [.649, .687];
    - model-based marginal reliability (hypothetical full panel): .960 [.953, .968]; grid check .960;
    - Cronbach's α, pairwise covariances: .928 [.891, .943], 14 raters, 1900 products. The CI is approximate (Method 2.10; @tbl-naive-indices);
    - Cronbach's α, fully crossed block: .658 [.526, .756], 3 raters, 139 products;
    - Krippendorff's ordinal α: .392 [.362, .417], 19 raters, 2771 products.
    - State what each index refers to, as in the table's "refers to" column. Do not discuss the M1–M3 marginal reliabilities that the overview table also lists (D5).
  - **(3) Observed reliability by number of ratings (descriptive, secondary)** (@tbl-grm-reliability-by-n, @fig-grm-rel-post-by-n [SUPP]; F1.14 [DD]). Two or three sentences:
    - Among the products as rated, mean rel_post was .520 for products with 1 rating (897 products), .698 with 2 (2080) and .810 with 4 (125); the full series to .919 at 10 ratings (3 products) is in the supplement table. Mean PSD falls from 0.686 to 0.285.
    - Products with the same number of ratings differ in rel_post (figure, SUPP); the notebook relates precision to where a product lies relative to its raters' thresholds (F1.17) [ATC-4; Discussion only].
    - Move 3: these values are observational; products were not assigned a number of ratings at random [FI-4]. If the notebook's statement is used ("The observed relation above is confounded, because products with more ratings were also rated by different raters", `94cdcfeb`), mark it **[AUTHOR TO CONFIRM; ATC-25]**.
    - **No side-by-side comparison of projected and observed values** (e.g., k = 2 vs n = 2). The notebook makes none (Flag 15). If the author wants one, it must be marked as the writer's own juxtaposition [ATC-25] and kept to the Discussion.
  - **(4) Distribution and consistency (one sentence each, SUPP pointers):**
    - rel_post median .698, IQR .173 (Q1 .596, Q3 .769); range .057–.929 (F1.13).
    - rel_post and rel_info correlate r = .935; 320 products differ by more than .1 (F1.16).
  - Writer: `tbl-reliability-overview` still says "bootstrap, 1000 replications" for the pairwise Cronbach CI without mentioning the failed replications. The Method text states the 361 failures; the notebook wording should be aligned before render [FI-18].

**3.3 Rater differences (RQ2; aim 2)**
- Findings: F0.6, F0.7, F0.8, F2.1, F2.2, F2.3, F2.4, F2.5.
- Embed:
  - `fig-overview-rater-response-styles` [MAIN]: descriptive entry point
  - `tbl-grm-rater-parameters` [MAIN] (now compact: 9 columns, "estimate (SE)" at 2 decimals)
  - `tbl-grm-rater-information-ci` [MAIN]
- Cross-reference:
  - `tbl-category-usage` [SUPP]
  - `fig-overview-rating-distribution` [SUPP]
  - `fig-grm-category-response-functions` [SUPP]
  - `fig-grm-rater-information` [SUPP]
  - `fig-grm-information-shares` [SUPP; **optional MAIN if space allows**, OD2]
  - `tbl-grm-information-summary` [SUPP]
- **Rule for raters with few ratings (author constraint; review M4, M5):** R15–R19 have 50–73 ratings (F0.5). Their parameters are reported in the tables but are not used as range endpoints or headline values in the text. Where they are mentioned, give the SE alongside and say only that the estimate is imprecise.
- Bullets:
  - **Descriptive response styles** (@fig-overview-rater-response-styles; F0.8; raw scale, not adjusted for which products each rater saw; 3 decimals as printed):
    - Rater means range from 1.760 (R06) to 3.836 (R18). (Raw means are descriptive counts, not model parameters, so R18 may appear here.)
    - SD ranges from 1.022 (R01) to 1.953 (R19).
    - Floor rate ranges from .579 (R06) to .016 (R13). The ceiling rate is highest for R19 (.080); five raters (R06, R17, R01, R03, R18) print .000.
    - The central (3–5) rate is high for R13 (.799) and R12 (.735), and low for R06 (.192).
    - Any other value may be taken from the full F0.8 table, at 3 decimals.
  - **Overall category use** (F0.6; @fig-overview-rating-distribution [SUPP]): ratings concentrate at the low end: category 1 has 2029 ratings and category 2 has 2113; category 7 is rarest (109). Quote counts, not the 6-decimal shares (m3). Five raters left top categories unused (F0.7).
  - **Severity and scale use** (@tbl-grm-rater-parameters; F2.2; 2-decimal values as printed):
    - First thresholds of raters with several hundred ratings range from −3.38 (R13, SE 0.49) and −2.21 (R09, SE 0.36) to 0.29 (R06, SE 0.06). R06 is the only rater with a positive b1 ("higher b means a stricter rater").
    - Threshold spacing differs, e.g., R02 from −0.71 (b1) to 2.03 (b6) vs R13 from −3.38 to 4.43. Say in one clause that spacing in the GRM is partly the same fact as discrimination (Method 2.7), so it is not read as separate evidence (review M4).
    - R18's thresholds have the largest SEs (b1 SE 3.05); they are not interpreted. **No R18 threshold value is quoted in the text** (author constraint).
    - R17 has 4 thresholds; R01, R03, R06 and R18 have 5; the others 6.
    - A comparable severity summary (e.g., expected rating at θ = 0 with intervals) is not in the notebook [FI-29]; do not construct one.
  - **Discrimination** (F2.1; 2 decimals as printed):
    - Among raters with at least 400 ratings (R01–R09), a ranges from 0.86 (R09, SE 0.15) to 2.81 (R06, SE 0.42). Other well-measured values: R01 1.96 (SE 0.16), R02 2.50 (SE 0.33); R13 (254 ratings) 1.50 (SE 0.22).
    - The two highest estimates, R19 3.71 (SE 2.22) and R16 3.70 (SE 1.36), come from raters with 50 and 52 ratings and have the largest SEs. R18 (55 ratings) has the lowest, 0.63 (SE 0.26). State these facts with the SEs; no reading.
  - **Average information and share, with 95% intervals** (@tbl-grm-rater-information-ci; F2.4):
    - Well-measured examples: R09 0.238 [0.110, 0.419]; R01 0.979 [0.723, 1.219]; R02 1.705 [0.903, 2.558]. Shares: R01 .037 [.022, .050]; R02 .065 [.035, .098].
    - The widest intervals belong to the raters with about 50 ratings, e.g., R19 3.539 [0.410, 11.017], share .135 [.017, .331]; R16 3.300 [0.728, 6.489].
    - The notebook's reading of wide intervals goes to the Discussion (M11).
  - **Where on θ raters inform** (F2.3; [SUPP] objects; review m13 rephrased):
    - The θ of maximum information is highest for R01 (2.700) and R06 (2.400) and lowest for R13 (−0.550). Do not explain the R01 value.
    - Shares vary with θ, e.g., R06 .001 at θ = −2 vs .083 at θ = +2; R12 .221 at θ = −2.
  - Move 3: the information intervals use the same 200 accepted parameter draws as F1.12 (Method 2.10). The raw response styles have no per-rater uncertainty.
  - Optional analyst action (review M11): a compact forest plot of a and severity with SEs [FI-29]. Not required; `tbl-grm-rater-parameters` stays MAIN (checkpoint 2).

**3.4 How much do the scores depend on modelling rater differences? (RQ3)**
- Findings: F1.1, F1.2, F1.4, F1.5, F1.11, F2.6, F2.7, **F2.9, F2.10**.
- Embed:
  - `tbl-raw-mean-vs-grm` [MAIN]
  - `fig-raw-mean-vs-theta` [MAIN]
  - `tbl-score-agreement` [MAIN]
- Cross-reference:
  - `tbl-lr-tests` [SUPP]; the statistics are quoted in the text
  - `tbl-model-fit` [MAIN, from 3.1]
  - `tbl-discrimination-m3` [SUPP]
  - `tbl-threshold-order` [SUPP]
  - `tbl-rater-fit-m1` [SUPP]
  - `tbl-theta-correlations` [SUPP]
- Bullets:
  - **RQ3(a), shared category structure** (F1.2): M1 vs M2 X² = 737.457, df = 84, *p* < .001. The df explanation and the cross-software caveat are in Method 2.8; do not repeat them here.
  - **RQ3(a), equal discrimination** (F1.2, F1.1):
    - M2 vs M3: X² = 121.958, df = 18, *p* < .001.
    - AIC also favours M3 (23767.020 vs 23852.978); BIC ranks M2 (24529.585) below M3 (24555.360).
    - D13 wording: "Rater-specific discriminations were supported by the LR test and AIC, but not by BIC." Report this factually.
  - Supporting detail, one sentence each, pointing to [SUPP]:
    - M3 discriminations range from 0.283 (R09, SE 0.055) to 2.606 (R16, SE 1.419) (F1.4).
    - Unordered step parameters in 9 raters under M2 and 9 under M3 (F1.5). GRM thresholds are ordered by construction.
    - Under M1 (MFRM), only R17 (infit 1.328, outfit 1.190) and R18 (1.009, 1.071) are at or above 1. The lowest values are R12's (0.238, 0.255) (F1.11). No cut-offs applied.
    - Do not state in Results that misfit "reflects" unequal discrimination. That reading belongs in the Discussion [ATC-9].
  - **RQ3(b), raw mean vs GRM score** (@tbl-raw-mean-vs-grm, @fig-raw-mean-vs-theta; F2.9, F2.10). Descriptive only. Lead with the tie-aware statistics:

    | ratings per product | n products | Pearson / Spearman | Kendall's τ-b | discordant pairs | quintile change, ties resolved | products with tied raw mean | mean / max θ̂ range at equal raw mean |
    |---|---|---|---|---|---|---|---|
    | all | 3668 | .906 / .932 | .796 | .083 | .237 | .995 | 0.814 / 2.252 |
    | 1 | 897 | .921 / .940 | .832 | .042 | .104 | 1 | 1.283 / 1.436 |
    | 2 | 2080 | .922 / .933 | .815 | .067 | .220 | 1 | 1.537 / 2.196 |
    | 3+ | 691 | .954 / .959 | .842 | .070 | .220 | .971 | 0.619 / 1.396 |

    - Overall: Kendall's τ-b = .796; .083 of product pairs with different raw means are ordered the other way round by the GRM score; with raw-mean ties ordered by the GRM score, .237 of products still change quintile, the smallest change any tie-breaking can give (F2.9). Pearson .906, Spearman .932.
    - Nearly every product shares its raw mean with another product (.995 overall).
    - **Single ratings** (the cleanest case; review C1 point 3): products rated once with the same rating received GRM scores up to 1.436 apart (mean range 1.283); .042 of pairs are discordant; .104 change quintile with ties resolved. Say what the figure's 1-rating panel shows: at a given single rating, GRM scores spread vertically (F2.10, notebook statement `035c9318`). Points are jittered horizontally.
    - By group, describe the mixed pattern factually without a trend claim: correlations and τ-b are highest in the 3+ group; discordant pairs and tie-resolved quintile changes are lowest in the 1-rating group. No test across groups exists.
    - Within-group maxima of the θ̂ range: 1.436 (1), 2.196 (2), 1.396 (3+). **Do not headline the pooled 2.252** (review m14); if it is quoted, add that the pooled row mixes products with different numbers of ratings and that its grouping is not documented [FI-20]. Do not comment on the "all" row's mean range or τ-b being lower than the subgroup values (Flag 13).
    - **Do not quote** the plain share changing quintile (.350 overall), the percentile shifts or the ≥ 2-quintile share from this table. One clause may say that the table also lists the plain share, which the notebook notes overstates the disagreement because of ties.
    - **Do not compare any value in this table with `tbl-score-agreement`** (author constraint; F2.9 comparability note).
    - **Do not state the mechanism** ("rated by raters of different severity or discrimination", notebook `8620cb46`) in Results. It goes to Discussion 4.4 only [ATC-21].
  - **RQ3(b), model choice** (@tbl-score-agreement; F2.7). Relative to the GRM:

    | model | Pearson / Spearman | mean abs. percentile shift | p95 | max | share changing quintile | by ≥ 2 quintiles |
    |---|---|---|---|---|---|---|
    | M1 | .975 / .978 | .042 | .130 | .432 | .202 | .004 |
    | M2 | .985 / .983 | .033 | .117 | .413 | .150 | .003 |
    | M3 | .996 / .996 | .017 | .044 | .234 | .075 | .001 |

    - Among the ladder models: Pearson .980–.993, Spearman .983–.996 (F2.6; @tbl-theta-correlations [SUPP]).
    - Grid check: M1 vs the sirt default grid 1.000 (F2.6). Explain the `rm_facets_default_grid` row/column in the table note [FI-18].
  - Move 3 (problems, descriptive):
    - No CIs exist for the correlations, the agreement statistics or the raw-mean comparison.
    - The M1–GRM contrast combines the rater constraints with the change of link function. M3 and the GRM have the same number of parameters and differ only in the link.
    - All shifts are differences from the GRM; they show that the scores differ, not which score is more accurate (review M1).
  - **No move-4 closing sentence in Results** (M11). The draft-1 sentence comparing raw-mean and model-choice shifts is deleted, not moved.

**3.5 Sensitivity to the rater exclusion (brief; 2–3 sentences)**
- Findings: F2.8.
- Cross-reference: `tbl-sensitivity-rater-exclusion` [SUPP] (D7). This is the target of the exclusion sentence in Method 2.6.
- Bullets (values as printed, 5 decimals; APA leading zero dropped where the value cannot exceed 1):
  - Refitting the GRM with all 22 raters (7844 ratings, 3669 products):
    - empirical marginal reliability .67199 → .67186;
    - model-based reliability .95986 → .96186.
  - Over the 3668 common products:
    - θ̂ Pearson .99997, Spearman .99996;
    - mean |Δθ̂| 0.00171, **max 0.16246** (quote this wherever "did not change the scores" is used; ATC-26);
    - share changing quintile .00491.
  - Over the 19 common raters: a Pearson .99880; max |Δa| 0.19820.
  - No CIs exist for these differences. No evaluative adjective in Results ("negligible" etc. stays in the ATC-26 sentence).

### 4 Discussion

Purpose: interpret, map to the literature, and draw the implications for sport-science creativity research. The section mirrors the Introduction's three aims and uses four moves (writing-models/discussion-conclusion.md). **Every interpretive claim is [ATC].** The sparse design appears only in 4.6 Limitations. Wording: "in these data", "for this rater pool"; no "we have shown" (review M10).

**4.1 Summary of the answers (move 1, 1 paragraph)**
- Echo RQ1–RQ3 in the Introduction's wording, descriptively:
  - the reliability of the obtained scores is below the full-panel value; projected reliability rises with the number of ratings and depends on which raters give them;
  - raters differ in threshold location, category use, discrimination and information, with imprecise estimates for raters with few ratings;
  - the equivalence constraints on category structure and discrimination are rejected (LR and AIC; not BIC for discrimination);
  - raw mean scores and GRM scores order a non-trivial share of products differently, and the model choice also shifts rankings.
- Mention the GRM's retention in one clause.

**4.2 How many ratings per action, and from whom? (aim 1) [ATC-3, ATC-4, ATC-5, ATC-13, ATC-24, ATC-25]**
- The conventional figures describe the mean of a large or complete panel: the full-panel reliability (.960) and the pairwise Cronbach's α (.928). The scores actually obtained have an empirical reliability of .672 [.649, .687]. This is what matters for any downstream use [ATC-3].
- **The projection is the planning evidence** [ATC-5, ATC-24]:
  - Under the fitted model, reliability rises with each additional rating (F1.20).
  - Who rates matters as much as how many: one rating from the most informative raters gives a higher projected reliability (.754) than two from randomly drawn raters (.688), and with the least informative raters even ten ratings stay below .9 (.884) [ATC-24].
  - This links aim 1 to aim 2: the rater differences reported under aim 2 are what make the choice of raters matter.
  - If the author wants it, the notebook phrase that the three schemes "bracket the effect of who rates" can be used here, marked [ATC-25].
- **The observed by-n values** (F1.14, SUPP) describe the products as rated. If the notebook's "confounded" statement is used, it is marked [ATC-25]. Any comparison of observed and projected values is the writer's own juxtaposition: avoid it, or mark it [ATC-25] and say that the notebook makes none.
- Map to the literature:
  - Spearman–Brown logic (amabile1982);
  - kaufman2008: a high α can hide low single-rater agreement. Krippendorff's .392 vs Cronbach's .928 illustrates this [ATC-13];
  - cseh2019: the number of raters must be established per domain. The projection gives such values for this football rating task and this rater pool [ATC-4]. Do not call it "first football-specific evidence" without the ATC-2 hedge (review m9).
- The crossed-block α (.658, 3 raters) lies close to the empirical reliability. Treat this as a cautious observation and do not claim equivalence [ATC-13].
- Product-level precision depends on the number of ratings, on *which* raters gave them (F1.20 schemes) and on where a product lies on θ (F1.17, F2.3) [ATC-4]. Do **not** say "mainly" (review C3; no decomposition exists).
- rel_post is defined relative to a unit prior variance; with one or two ratings it partly reflects the prior (Method 2.10; review M6).
- Reporting implication: report the reliability of the scores actually used (empirical marginal reliability, product SEs), not only α or full-panel values [ATC-15].
- Drop the draft-1 sentence "both lie in the range that CAT studies usually report" unless it cites baer2004/kaufman2008 from the Introduction (review m8).

**4.3 Raters differ (aim 2) [ATC-6, ATC-12]**
- The raters span a wide range of threshold locations, category use (raw floor and central rates) and discrimination. For raters with many ratings, the differences are clearly larger than the SEs (e.g., R09 0.86, SE 0.15, vs R06 2.81, SE 0.42; F2.1) [ATC-6].
- Threshold spacing in the GRM is partly the same fact as discrimination (b relative to a), so wide or narrow spacing is not separate evidence of scale use. The raw response styles (F0.8) give the scale-use evidence that is independent of the model, with the caveat that they are not adjusted for which products each rater saw [ATC-6].
- Map to the literature: long2015 (scale use, beliefs); rater-effect taxonomy (engelhard1994; myford2003; myford2004); central tendency vs extreme responding (myszkowski2021). primi2019 left response styles to future work; this study describes them for football [ATC-6].
- **Uncertainty (moved here from Results, M11).**
  - "Wide intervals mean that a rater's informativeness is not yet well determined, typically for raters with few ratings" (notebook `37ecc203`; F2.4).
  - For raters with about 50 ratings (R16, R19), the highest discriminations and information shares come with the widest intervals (F2.1, F2.4). Information shares are therefore not a ranking of rater quality [ATC-12].
  - The parameter-draw intervals are conditional on valid draws and approximate for these raters (Method 2.10; review M5).
  - Link to wind2018 and wind2019a (rater estimates depend on the linking set), reise1990 (GRM recovery) and ceh2022 (rater characteristics predicting discernment).
- Raters inform different regions of θ (e.g., R06 at high creativity, R12 at low; F2.3). This is relevant for assigning raters [ATC-16].

**4.4 Why rater differences matter for scoring creativity in sport (aim 3) [ATC-7, ATC-8, ATC-9, ATC-10, ATC-15, ATC-21, ATC-22]**

Restructured into three steps that keep the kinds of rater difference apart (review M2):
- **(i) Severity and the raw mean** [ATC-7, ATC-21]:
  - Unweighted means treat raters as interchangeable; when different raters rate different actions, the means are confounded with rater severity (primi2019).
  - In these data, the clearest case is a single rating: the same rating corresponds to GRM scores up to 1.436 apart (F2.9, 1-rating row; @fig-raw-mean-vs-theta). With one rating, a product's GRM score depends only on the rating and on that rater's parameters, so this spread reflects differences between raters as modelled [ATC-21] (review m15).
  - Mechanism sentence, from notebook `8620cb46`, used here only and marked: "Products with the same raw mean get different GRM scores when they were rated by raters of different severity or discrimination." **[AUTHOR TO CONFIRM; ATC-21]**
  - Severity differences were not tested formally (no M0; FI-24). Say so here in one clause and in L6.
- **(ii) Beyond severity: category structure and discrimination** [ATC-7, ATC-9]:
  - The LR tests concern the MFRM's shared category structure and equal discrimination, which remain even after severity is modelled. Both are rejected (F1.2); discrimination is supported by LR and AIC, not by BIC (D13).
  - This bears on the Rasch/MFRM constraints, not directly on raw-mean averaging. Delete the draft-1 sentences "The LR tests rejected even the weaker constraints of the Rasch family" and "Averaging therefore treats raters as interchangeable [as shown by the LR tests]" (review M2).
  - Part of the discrimination heterogeneity may be estimation noise for raters with few ratings (F1.4, F2.1) [ATC-7].
  - The M1 misfit pattern fits the account that the MFRM expresses discrimination differences only as misfit (myford2004; myszkowski2021): R17 has values above 1 under M1 and a low GRM a (1.45); R12 has the lowest M1 values and a high GRM a (2.90) (F1.11, F2.1). Cautious and descriptive; no cut-offs, so speak of values above and below 1 [ATC-9].
  - The GRM is preferred by information criteria. A cumulative link is plausible for a unipolar scale, and pellegrino2025 also retained a GRM [ATC-8]. Neither the unordered PCM/GPCM steps nor the ordered GRM thresholds count as evidence for either family (andrich1978; bond2020) [ATC-9].
- **(iii) Score consequences** [ATC-10, ATC-22]:
  - Raw mean vs GRM: τ-b = .796, .083 discordant pairs, and at least .237 of products in a different quintile (F2.9). In applications that select actions, e.g., the top quintile of creative actions for training material, this is consequential [ATC-22].
  - Model choice: overall correlations between models are high (≥ .975), yet .202 of products change quintile under the MFRM/RSM vs the GRM, and .075 under the GPCM (F2.7). Keep the link-function confound explicit [ATC-10].
  - **Do not rank the two comparisons against each other** (no "more than", no "most"). They rest on different statistics, and the notebook does not state that they are comparable.
  - **What the comparison does not show (review M1):** the GRM is not a validated criterion. The shifts show that the scores differ; the GRM *adjusts for* the modelled rater differences, but whether it predicts unseen ratings better than the raw mean is not tested [FI-26]. Replace the draft-1 phrase "direct evidence that this choice changes which actions rank high" with this wording [ATC-15, ATC-22].
  - Map to primi2019 and myszkowski2019.
- Drop "labels for automated rating" (review m12).

**4.5 Practical implications for sport science (move 4: applications) [ATC-5, ATC-14, ATC-15, ATC-16, ATC-24]**
- Scope sentence first: these implications are drawn from one pool of student raters and one 7-point scale [FI-21] (review M8).
- **Ratings per action for a target reliability, and who gives them** [ATC-5, ATC-24]:
  - Read the projection (F1.20) for the rater pool at hand: how reliability grows with k, and how much it depends on the raters chosen.
  - No number of ratings "needed" is stated (not printed); no extrapolation beyond k = 10; no Spearman–Brown projection.
  - The projection treats the parameters as known and refers to this rater pool and this scale. It will be refreshed after the data update [DD].
- **Calibration/anchor set rated by all raters** [ATC-14]. This:
  - links raters and makes their parameters comparable;
  - stabilises the a of raters with few ratings (wind2019a; forthmann2023);
  - makes fully crossed reliability and absolute fit checks estimable.
  - Distinguish it from rater *training*, which conflicts with the CAT "no criteria" rule (storme2014; dollinger2005; hennessey2011).
- **Model rater differences instead of averaging** [ATC-15]:
  - JRT scores (EAP with PSD) rather than raw means. The raw-mean comparison (F2.9) shows that the choice changes the ordering of actions; it does not show that the JRT score is more accurate [ATC-22].
  - Report the empirical marginal reliability and product SEs, and carry the SEs into downstream uses.
- **Rater workload and assignment** [ATC-16]:
  - In these data, raters with about 50 ratings still had imprecise parameters (F2.1, F2.4). Plan enough ratings per rater for stable parameters. **Do not state that 15 ratings, or any other number, is enough** (author constraint; review M9). The 15-rating exclusion is a technical estimation criterion only.
  - Optionally, use rater information to assign raters (F2.3; F1.20 schemes).
- **Boxed design recommendations (OD6: yes; kept at checkpoint 2).** A short box titled e.g. "Design recommendations for creativity ratings in sport". **Every item is [AUTHOR TO CONFIRM; ATC-23]**, and each item also carries the ATC of the claim it rests on. The projection is now the primary evidence behind items 1 and 3:
  1. Plan the number of ratings per action, and who gives them, from the reliability you need; a projection from a fitted rater model shows both (@fig-grm-reliability-projection) [ATC-5, ATC-24].
  2. Let all raters rate a common calibration set so that raters are linked and their parameters comparable [ATC-14].
  3. Give each rater enough ratings for stable rater parameters; in these data, about 50 ratings per rater still left the parameters imprecise (F2.1, F2.4) [ATC-16]. (No "15" anywhere in the box.)
  4. Score actions with a model that adjusts for rater differences rather than the raw mean, and report how much the ordering changes (F2.9) [ATC-15, ATC-22].
  5. Report the reliability of the scores actually used (empirical marginal reliability, product SEs), not only α or full-panel values (F1.12) [ATC-3, ATC-15].
  - Keep the box to these 5 items; no numbers inside the box except "about 50", which is a reading of the n column, and by reference to the figure/tables, since all are [DD]. The reviewer notes that CRJ rarely uses boxes; the box stays per OD6 unless the author decides otherwise at the next checkpoint.

**4.6 Limitations and future research (move 4)**
- L1. **Design and missingness** (review C2, M7):
  - The rating design is incomplete: not every rater rated every product, and the allocation is described in [FI-4]. Missingness is assumed ignorable.
  - Ratings marked "action not recognised" were removed; if non-recognition depended on the action or the rater, missingness is not ignorable [FI-22; ATC-27].
  - The observed reliability by number of ratings is observational (F1.14) [DD]; the projection addresses this but rests on the model (L2, L3).
- L2. **Fit evidence is limited by the design** [ATC-11]:
  - S-X² has little power with most cells imputed from the fitted model (F1.8);
  - C2 could not be computed because some rater pairs share no products (F1.10; Method 2.9);
  - Q3 is negatively biased with few raters per product (christensen2017), and the flag criterion has no reference distribution;
  - infit/outfit values below 1 are expected when θ̂ is estimated from the same few ratings (F1.7), and no cut-offs are applied.
  - Absence of detected misfit is not evidence of fit. The GRM is therefore the best-fitting of the compared models, not a validated reference (review M1); a held-out check is future work [FI-26].
- L3. **Uncertainty and model assumptions** (review M5, M6):
  - Parameters of raters with few ratings are imprecise (F2.1, F2.4); the parameter-draw intervals are conditional on valid draws and approximate for these raters [FI-28].
  - The projection treats the parameters as known (F1.20), so its bands understate the uncertainty [FI-28].
  - θ ~ N(0, 1) is assumed; EAP scores, rel_post and the projection depend on it, and the ratings are concentrated at the low end of the scale (F0.6). A latent-distribution check was not done [FI-27].
  - The response-style indices are raw and have no uncertainty.
- L4. **Rater pool** (review M8). One pool of student raters [FI-1, FI-21], with no rater covariates. Whether these raters meet the CAT's domain-familiarity requirement is not established here; the projection, the rater differences and the recommendations may be specific to this pool. Expertise is not analysed in this paper (D10); future work: kaufman2009; kaufman2013; ceh2022.
- L5. **Rater exclusion.** Raters with fewer than 15 ratings were excluded as a technical estimation criterion [FI-23]; the largest change in a product score from the exclusion was 0.16246 (F2.8; @tbl-sensitivity-rater-exclusion) [ATC-26]. No claim that 15 ratings suffice.
- L6. **Model comparison caveats** (review M2, M3):
  - cross-software LR test (sirt vs mirt) for M1 vs M2; likelihoods may not be on exactly the same scale, and nesting is assumed rather than shown [FI-25]; its df is below the formula value because of unused end categories (Method 2.8);
  - severity differences were not tested formally (no M0) [FI-24];
  - BIC vs LR/AIC disagreement on discrimination;
  - the score-agreement contrasts mix rater constraints and link function (F2.7);
  - the raw-mean comparison has no CIs, and its subgroup and equal-raw-mean grouping definitions are not documented [FI-20].
- L7. **Two facets and one dimension only.**
  - No time, session or fatigue facet: barth2020; leckie2011; myford2009; workload forthmann2017. The data-collection timespan is reported in Method 2.4 [FI-3] (review m20).
  - No differential rater functioning (wind2019b).
  - Extensions: patz2002; uto2020.
  - Unidimensionality is assumed; only the creativity dimension is analysed.
- **Future research:**
  - a prospective anchor-set design;
  - projections that include parameter uncertainty and other rater pools (forthmann2023);
  - predictive validation of model-based vs raw-mean scores, e.g., on held-out ratings;
  - rater covariates, including football expertise;
  - replication in other sports.

### 5 Conclusion (1 paragraph)

- Restate the three findings in 3–4 sentences, worded "in these data" (review M10) [ATC-1]:
  1. the reliability of the obtained scores is far below conventional panel figures, and the projection shows that it depends on both the number of ratings per action and the raters who give them;
  2. raters differ in threshold location, category use, discrimination and information;
  3. constraints treating raters as equivalent in category structure and discrimination are rejected, and both raw means and constrained models order actions differently from the GRM.
- End with the design and scoring message, scoped to this kind of rater pool: plan ratings per action and choose raters with a projection, link raters through a calibration set, and model raters with JRT [ATC-5, ATC-14, ATC-15, ATC-24].
- No "We have shown" (review M10).

### References

APA 7th via CSL; citekeys only. Mechanical, with no hand formatting.

---

## Figure/table plan (D4, D5, D6, D9; OD2, OD3; checkpoint 2 applied)

There are **10 main-text objects** (7 tables, 3 figures), plus **1 optional main-text figure** (`fig-grm-information-shares`, counted under the supplement). There are **27 supplement objects** (17 tables, 10 figures) and **5 objects not embedded**. Total: 42.

Supplement numbering: configure the crossref prefixes so that supplement objects are numbered S1, S2, … (review m18). This is a paper-config/render setting, not a writer edit.

### Main text (10)

| # | Label | Section | Role |
|---|---|---|---|
| 1 | `tbl-design-summary` | 2.6 | Final data; single place for the design numbers [DD] (Table 1) |
| 2 | `tbl-model-fit` | 3.1 | Model choice: information criteria with Δ (Table 2) |
| 3 | `fig-grm-reliability-projection` | 3.2 | **RQ1 primary:** projected reliability by k for random, most and least informative raters (Figure 1) |
| 4 | `tbl-reliability-overview` | 3.2 | RQ1: actual vs hypothetical vs conventional indices, with what each refers to (Table 3) |
| 5 | `fig-overview-rater-response-styles` | 3.3 | RQ2: raw response styles (descriptive entry point) (Figure 2) |
| 6 | `tbl-grm-rater-parameters` | 3.3 | RQ2: thresholds and discrimination as "estimate (SE)", 2 decimals, 9 columns (Table 4; "Table 5" in draft 1) |
| 7 | `tbl-grm-rater-information-ci` | 3.3 | RQ2: average information and share with 95% intervals (Table 5) |
| 8 | `tbl-raw-mean-vs-grm` | 3.4 | RQ3(b): raw mean vs GRM score, led by the tie-aware columns (Table 6) |
| 9 | `fig-raw-mean-vs-theta` | 3.4 | RQ3(b): spread of GRM scores at equal raw mean; 1-rating panel is the key display (Figure 3) |
| 10 | `tbl-score-agreement` | 3.4 | RQ3(b): ranking consequences of the model choice (Table 7) |

Optional main text, if space allows (OD2): `fig-grm-information-shares` (3.3). If promoted, main = 11 and supplement = 26.

### Justification of the placements

- **Checkpoint-2 decisions (RQ1):**
  - `fig-grm-reliability-projection` → **MAIN.** It is the primary evidence for RQ1 and for the design-recommendation box. It shows both "how many" (x axis) and "who" (three rater sets), which links RQ1 to RQ2 in one display. It plots only the `empirical` measure, which is the measure quoted in the text.
  - `tbl-grm-reliability-projection` → **SUPP.** 30 rows × 11 columns; the text quotes its values, and the other two measures agree with `empirical` to within .003.
  - `tbl-grm-reliability-by-n` → **SUPP** (was MAIN). The observed by-n values are now descriptive and secondary; the projection replaces them as planning evidence.
  - `fig-grm-rel-post-by-n` → **SUPP (decision).** Reasons:
    - Its role in draft 1 was to show that products with the same n differ, which bridged aim 1 to aim 2. The projection now carries that bridge more directly (most vs least informative raters at fixed k) and without the confounding that the notebook notes for the observed relation.
    - Two reliability-by-number figures in the main text, one simulated and one observed, would invite the projected-vs-observed juxtaposition that the notebook does not make (Flag 15).
    - It reduces the main-text load that the reviewer criticised (M11): main text goes from 11 to 10 objects.
    - It stays in the supplement as the observed description and is cited in Results 3.2 (3).
- **Checkpoint-1 decisions (OD2), still in force:**
  - `tbl-score-agreement` → MAIN; `tbl-theta-correlations` → SUPP.
  - `fig-grm-information-shares` → SUPP, promoted to MAIN only if space allows.
- **Raw mean vs GRM (OD3):**
  - `tbl-raw-mean-vs-grm` → MAIN. The text leads with its tie-aware columns. The plain quintile and percentile columns remain in the display; the caption must name the tie-aware columns and explain that the plain share overstates disagreement [FI-18]. The author may also ask the analyst to drop the plain columns from the display [FI-18, optional].
  - `fig-raw-mean-vs-theta` → MAIN. Its 1-rating panel is the cleanest display of rater effects on scores (review C1 point 3). If space becomes tight, this figure still moves to SUPP before any table does.
- **Other placements (unchanged):**
  - `tbl-grm-rater-parameters` → MAIN (checkpoint 2: compact Table). The reviewer's alternative, a forest plot, is an optional analyst action [FI-29].
  - `tbl-grm-rater-information-ci` → MAIN, instead of `tbl-grm-information-summary` (→ SUPP). Aim 2 requires rater differences *with uncertainty*.
  - `tbl-grm-reliability-ci` → SUPP; its CIs are quoted in the text.
  - `tbl-sensitivity-rater-exclusion` → SUPP, with a 2–3-sentence mention in Results 3.5 and the cross-reference in Method 2.6.
  - `tbl-lr-tests` → SUPP. It has only two rows; X², df and *p* < .001 are quoted in the text.
  - `fig-grm-category-response-functions` → SUPP (19 panels).
- **NB01 objects (D9):**
  - `fig-overview-rater-response-styles` → MAIN: it serves aim 2 directly.
  - `fig-overview-rating-distribution` → SUPP.
  - `fig-overview-degree-distributions` → SUPP.
  - `tbl-overview-ratings-per-action` and `fig-overview-rater-overlap` are not embedded.

### Supplement (27)

- **Tables (17):**
  - `tbl-excluded-raters`
  - `tbl-sensitivity-rater-exclusion`
  - `tbl-category-usage`
  - `tbl-grm-convergence`
  - `tbl-grm-rater-fit`
  - `tbl-grm-q3-flagged`
  - `tbl-grm-reliability-projection` (NEW)
  - `tbl-grm-reliability-by-n` (moved from MAIN)
  - `tbl-grm-reliability-ci`
  - `tbl-grm-reliability-summary`
  - `tbl-naive-indices`
  - `tbl-grm-information-summary`
  - `tbl-lr-tests`
  - `tbl-discrimination-m3`
  - `tbl-threshold-order`
  - `tbl-rater-fit-m1`
  - `tbl-theta-correlations`
- **Figures (10):**
  - `fig-grm-rel-post-by-n` (moved from MAIN)
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
- `tbl-marginal-reliability-models`: D5, dropped entirely. The reviewer (m19) suggests adding it to the supplement with one sentence; this is left to the author (open option, not applied).
- `tbl-grm-global-fit`: it holds only a "not computable" row with the cause; Method 2.9 says the same.
- `tbl-overview-ratings-per-action`: it duplicates `tbl-design-summary`.
- `fig-overview-rater-overlap`: a sparse-design display, not needed for the aims.

### Notes for the writer and embedder

- The pipe bug in `tbl-grm-rater-parameters` is resolved (`02_artifacts.md`). Its values are now 2-decimal; replace every 3-decimal a/b value from draft 1.
- `manuscript.qmd` currently embeds `tbl-grm-reliability-by-n` and `fig-grm-rel-post-by-n` in the main text; move both to the supplement and add `fig-grm-reliability-projection` (main) and `tbl-grm-reliability-projection` (supplement).
- Captions still to fix in the notebook [FI-18]: `tbl-raw-mean-vs-grm` (tie-aware columns, "all" row), `tbl-grm-reliability-projection` (three measures, quantile columns, "parameters treated as known", replications/seed), plus the open items in `02_artifacts.md` §2–§5.

---

## Effect sizes and uncertainty: inventory (updated for commit 91c2e6d)

| Quantity | Uncertainty available? | Where |
|---|---|---|
| Empirical / model-based marginal reliability | **Yes:** 95% intervals from 200 accepted parameter draws (87 rejected and replaced); conditional on valid draws | F1.12, `tbl-grm-reliability-ci` |
| **Projected reliability by k and rater set** | **Simulation bands only:** 2.5%/97.5% quantiles over 50 replications; parameters treated as known, so no parameter uncertainty | F1.20, `tbl-grm-reliability-projection`, `fig-grm-reliability-projection` → FI-28 (optional) |
| Cronbach's α (pairwise; crossed block) | **Yes:** bootstrap CIs. The pairwise CI is approximate and possibly biased; n_boot_failed = 361 of 1000 | F1.18, `tbl-naive-indices` |
| Krippendorff's α | Yes: bootstrap CI | F1.18 |
| Product scores | PSD per product; mean PSD by n | F1.13, F1.14 |
| Observed rel_post by n | Means and medians only; **no CIs** | F1.14 → FI-12 (optional) |
| GRM discriminations a | Yes: Oakes SEs (2 decimals) | F2.1 |
| GRM thresholds b_k | Yes: SEs (2 decimals) | F2.2 |
| Rater average information and share | **Yes:** 95% intervals (same draws) | F2.4 |
| M3 discriminations | Yes: SEs | F1.4 |
| Model comparison | ΔAIC/ΔBIC/ΔSABIC; LR X², df, *p* < .001 | F1.1, F1.2 |
| θ correlations; score agreement | Point values only; **no CIs** | F2.6, F2.7 → FI-11 (optional) |
| Raw mean vs GRM (incl. τ-b, discordant pairs, tie-resolved share) | Point values only; **no CIs** | F2.9 → FI-11 (optional) |
| Exclusion sensitivity | Point differences; no CIs | F2.8 |
| Raw response styles | No per-rater uncertainty | F0.8 |

---

## FILL IN items (23 open)

Items marked "notebook" must be added to a notebook and passed through results-interpreter before any number is quoted. FI numbers are stable; resolved items are listed at the end. **FI-24 to FI-29 are optional analyst actions:** if they are not done, the Limitations text and softened claims planned above apply, and the writer does not mention the missing analysis beyond that.

- **FI-1** Raters and ethics: recruitment, number at start, informed consent, ethics approval.
- **FI-2** Products: competitions and matches, the action-selection rule (event data), clip length and video source, number of matches.
- **FI-3** Procedure:
  - rating software;
  - verbatim instruction and creativity definition;
  - scale anchors;
  - wording of the "not recognised" option;
  - randomisation, session length and breaks;
  - data-collection period / timespan (timestamps exist, but no summary is printed; review m20);
  - other dimensions rated.
- **FI-4** Allocation of products to raters (review C2): planned overlap, benchmark/common set, randomisation, thesis-specific subsets, rater dropout; **how products came to have 1, 2 or 3+ ratings**; whether products with 4+ ratings differ systematically (match, action type, rater composition; the equal counts of 125 products with 4 and with 5 ratings were noted by the reviewer); how the additional ratings will be allocated.
- **FI-6** Software versions (R, mirt, sirt, psych, Krippendorff package) and the GRM convergence tolerance (it prints as 0.000).
- **FI-9** The reason R19, R14, R02, R16 and R12 were not usable for the pairwise Cronbach's α. Optionally, the identity of the 3 raters in the crossed block (notebook).
- **FI-11** (optional, notebook) CIs for the θ correlations, the score-agreement statistics and the raw-mean vs GRM statistics (incl. τ-b and discordant pairs).
- **FI-12** (optional, notebook) CIs for the observed per-n mean rel_post.
- **FI-15** Preregistration status (expected: not preregistered, which fits the exploratory framing), and the data and code availability statement.
- **FI-16** CRJ requirements: abstract word limit, keywords, word count, figure/table limits, supplement policy (incl. S-numbering), and whether boxes are accepted.
- **FI-17** Verify the Introduction framing claims against the PDFs: worldeconomicforum2025 wording; safardilha2019; memmert2011; batey2012; barbot2019b; **kaufman2008a** ("five to ten" raters); the "α above .70" claim (baer2004; kaufman2008; hennessey2011); the "ICCs or agreement only" characterisation of kempe2018, zahno2023 and dejoode2023 (review m11 and "Citations").
- **FI-18** Notebook display fixes before render:
  - snake_case headers and code names in cells (all NB02 tables, including the long headers of `tbl-raw-mean-vs-grm` and the new `tbl-grm-reliability-projection`; `scheme` values to match the figure legend);
  - captions: `tbl-raw-mean-vs-grm` should mention the "all" row and the four tie-aware columns, and say that the plain share overstates disagreement (optionally drop the plain columns from the display); `tbl-grm-reliability-projection` should name the three measures and the quantile columns, say that parameters are treated as known, and give replications/seed; `tbl-grm-rater-information-ci` "Average information per rating" → "average information" (m17); `tbl-naive-indices` should mention n_boot/n_boot_failed and the approximate pairwise CI; `tbl-grm-reliability-ci` should mention n_draws/n_draws_rejected; `tbl-lr-tests` should mention df_expected_formula/df_matches_formula; `tbl-theta-correlations` should explain the `rm_facets_default_grid` row and column;
  - `tbl-reliability-overview`: align the "bootstrap, 1000 replications" wording for the pairwise Cronbach CI with the 361 failed replications;
  - in-figure facet titles ("theta" vs θ) and missing y-axis labels in `fig-grm-panel-information`; unexplained opacity and legend in `fig-grm-rel-consistency` and `fig-grm-rel-post-by-theta` (m22);
  - optional (m3): print `tbl-sensitivity-rater-exclusion` at 3 decimals; if done, the values pass through results-interpreter again before they are quoted;
  - optional APA leading-zero formatting in the notebook `tidy()` (m1), so tables and text match.
- **FI-19** **Data update.** After the additional ratings are collected, re-run N0–N2, the results-embedder and the results-interpreter. Then refresh every [DD] value in the manuscript (now including the projection), and re-check the qualitative statements: projection ordering of the rater sets, BIC disagreement, exclusion sensitivity, fit results, the raw-mean vs GRM pattern across groups, and the "at least 400 ratings" grouping used for discrimination.
- **FI-20** (notebook or R source) Definitions behind `tbl-raw-mean-vs-grm`, **partly resolved** (tie-aware columns now defined): whether percentiles and quintiles in the 1 / 2 / 3+ rows are computed within each subgroup or over all products; how the equal-raw-mean groups are formed in the pooled "all" row; how many groups there are and how large; the number of pairs behind share_discordant_pairs.
- **FI-21** (NEW) **Rater-pool description** (review M8): number of raters at start; football playing or coaching experience; any instruction or practice; sessions per rater; demographics. If not recorded, say so. Needed for Method 2.2, the scope sentence in 4.5 and Limitation L4.
- **FI-22** (NEW, notebook) **Rate of "action not recognised" ratings** by rater, and if possible by product (review M7). Needed for Method 2.6 and Limitation L1.
- **FI-23** (NEW) **Source or rationale for the 15-rating exclusion cut-off** (review M9).
- **FI-24** (NEW, optional analyst action, notebook) **Severity test** (review M2): M0 (common severity) vs M1 by LR, or M1 severities with SEs and a separation index. If not done: Method 2.8 sentence, Discussion 4.4 (i) clause, Limitation L6.
- **FI-25** (NEW, optional analyst action, notebook) **Same-package LR test** (review M3): M1 refitted in mirt (rating scale or constrained PCM) on the same quadrature; and how sirt handles raters with unused end categories under M1. If not done: Method 2.8 caveat and Limitation L6.
- **FI-26** (NEW, optional analyst action, notebook) **Predictive check** (review M1): held-out ratings among products with 3+ ratings, raw mean vs GRM (and M1 vs GRM). If not done: softened wording in 3.4, 4.4 (iii), 4.5 and Limitation L2.
- **FI-27** (NEW, optional analyst action, notebook) **Latent-distribution sensitivity** (review M6): GRM with an empirical-histogram or Davidian latent distribution; change in empirical reliability and rankings. If not done: Method 2.10 sentence on rel_post and the prior; Limitation L3.
- **FI-28** (NEW, optional analyst action, notebook) **Uncertainty of draws and projection** (review M5, C3): which raters caused the 87 rejected draws; draws on a transformed scale (log a, intercepts); more accepted draws; a projection that includes parameter uncertainty. If not done: Method 2.10 caveats and Limitation L3.
- **FI-29** (NEW, optional analyst action, notebook) **Comparable severity metric and forest plot** (review M4, M11): e.g., each rater's expected rating at θ = 0 and ±1 with intervals, or intercepts d; optionally a forest plot of a and severity with SEs. If not done: severity is described from thresholds as planned in 3.3, with the spacing caveat.

**Resolved and removed in earlier updates:** FI-5, FI-7, FI-8, FI-10, FI-13, FI-14 (see the change log). **Changed in this update:** FI-1 narrowed to raters/ethics (the rater-pool description moved to FI-21); the pipe-escaping item removed from FI-18 (resolved in the notebook); FI-20 partly resolved.

## AUTHOR TO CONFIRM claims (26 open)

- **ATC-1** The central contribution statement: three findings (aims 1–3), with the projection as the primary aim-1 evidence and the tie-aware raw-mean comparison under aim 3.
- **ATC-2** The novelty claim: "to our knowledge, no study has modelled rater differences with IRT/JRT for creativity ratings in sport". The search was not systematic.
- **ATC-3** Conventional CAT indices (α, full-panel reliability) describe a panel mean, not the precision of the scores actually used. The empirical marginal reliability is the relevant figure.
- **ATC-4** (revised) The precision of a product's score depends on its number of ratings, on which raters gave them and on where it lies on θ ("mainly" dropped). The projection gives domain-specific values for this task and rater pool (cseh2019), hedged with ATC-2 (no "first … evidence" without it).
- **ATC-5** (revised) Practical implication: plan ratings per action for a target reliability from a model-based projection (F1.20), without extrapolation and without stating a required number.
- **ATC-6** (revised) Raters differ substantially in threshold location, category use and discrimination; for well-measured raters the differences exceed their SEs; GRM threshold spacing is partly the same fact as discrimination.
- **ATC-7** (revised) Raw means are confounded with rater severity when raters rate different actions (primi2019); beyond severity, the Rasch constraints on category structure and discrimination are rejected. Discrimination heterogeneity is supported by LR and AIC but not by BIC, and is partly uncertain for raters with few ratings. Severity itself was not tested.
- **ATC-8** The GRM is preferred by information criteria, and a cumulative link suits the unipolar creativity scale.
- **ATC-9** The M1 misfit pattern (R17, R12) is consistent with discrimination differences surfacing as misfit in the MFRM. Unordered steps and ordered GRM thresholds are not evidence for either family.
- **ATC-10** (revised) Score consequences of the model choice: high correlations, yet ranking shifts that matter for selection. The M1–GRM contrast mixes constraints and link. No longer includes a Results closing sentence.
- **ATC-11** (extended) The fit evidence is limited by the design (S-X² with little power, C2, Q3 with no reference distribution, infit/outfit); the pairwise Cronbach CI may be biased. Absence of misfit is not evidence of fit.
- **ATC-12** Information shares are not a ranking of rater quality; the intervals are wide for raters with few ratings.
- **ATC-13** The Krippendorff vs Cronbach contrast illustrates kaufman2008. The crossed-block α lies near the empirical reliability (cautious).
- **ATC-14** Recommendation: a calibration/anchor set rated by all raters, distinct from rater training.
- **ATC-15** (revised) Recommendation: model raters with JRT instead of averaging, because JRT adjusts for the modelled rater differences (not "because it is more accurate"); report the empirical reliability and product SEs, and propagate them downstream.
- **ATC-16** (revised) Recommendation: enough ratings per rater for stable parameters (about 50 were not enough for precise parameters in these data); no claim that 15 suffices; rater assignment informed by information functions.
- **ATC-18** The realised design departs from the planned benchmark-set design (if so).
- **ATC-19** Showing raters a creativity definition is a (minor) departure from the CAT "no criteria" procedure.
- **ATC-20** (revised) The exploratory framing (no confirmatory hypotheses), the descriptive rewording of RQ3, and folding the former SQ1/SQ2 into the Method as analysis steps.
- **ATC-21** (extended) The mechanism sentence from notebook `8620cb46` ("… when they were rated by raters of different severity or discrimination"), and the reading of the 1-rating row: with one rating, the spread of GRM scores at the same rating reflects differences between raters as modelled. Discussion 4.4 only.
- **ATC-22** (revised) The interpretation of F2.9: raw-mean scoring orders a non-trivial share of products differently from the GRM, which is consequential for selecting actions. No comparison with F2.7, no "more than any model", and no "rater differences weigh less with more ratings" reading (the tie-aware columns show no clean gradient).
- **ATC-23** The boxed design recommendations in Discussion 4.5 (OD6): the selection and wording of all five items, now based on the projection.
- **ATC-24** (NEW) "Who rates matters as much as how many": the reading of the projection's rater sets (e.g., one rating from the most informative raters .754 vs two from random raters .688), and the projection as the basis for planning ratings per action.
- **ATC-25** (NEW) Notebook framing from `94cdcfeb`: "The observed relation above is confounded, because products with more ratings were also rated by different raters" and "which brackets the effect of who rates"; plus any writer juxtaposition of projected and observed values (avoid; if used, marked as the writer's own).
- **ATC-26** (NEW; reopens the closed ATC-17 for its second half) "Excluding them did not change the scores", always paired with the largest change in a product score (0.16246); the reviewer's alternative "changed them negligibly" is offered.
- **ATC-27** (NEW) The cause of the "action not recognised" ratings (D12 sentence: video cutting and imperfect material, close-ups or TV artefacts), which the data do not show.

---

## Evidence gaps (aims vs findings)

- **Aim 1, number of ratings.**
  - Now addressed by a model-based projection (F1.20), which separates the number of ratings from the choice of raters. Gaps: parameters are treated as known (bands show simulation variability only); the rater sets are not printed; k stops at 10; no "ratings needed for target reliability" figure is printed, so none is stated.
  - The observed by-n values (F1.14) remain observational, without CIs, and are secondary.
  - The projection depends on the N(0, 1) latent distribution and on the fitted parameters of this rater pool [FI-27, FI-21].
- **Aim 2, rater differences.**
  - Well supported for raters with many ratings: parameters with SEs, average information with intervals, and the full response-style table (F0.8).
  - Gaps: no comparable severity metric (only thresholds, whose spacing depends on a) [FI-29]; imprecise parameters for raters with about 50 ratings; draw intervals conditional on valid draws [FI-28]; raw response styles unadjusted and without uncertainty.
- **Aim 3, does modelling rater differences matter?**
  - Supported by the LR tests (F1.2), the model score agreement (F2.7) and the tie-aware raw-mean vs GRM comparison (F2.9, F2.10), most cleanly in the 1-rating row.
  - Remaining gaps: severity not tested formally [FI-24]; cross-software LR test [FI-25]; no criterion showing that GRM scores are more accurate than raw means [FI-26]; no CIs for the raw-mean comparison; pooled-row grouping undocumented [FI-20]; the mechanism is the notebook's explanation [ATC-21]; the raw-mean and model-choice statistics are not comparable, so they are not ranked.
  - The M1–GRM agreement mixes constraints and link function.
- **Absolute model fit.** Not established: C2 is not computable, and S-X², Q3 and infit/outfit are limited by the design. No cut-offs are applied.
- **Methods reproducibility (review C2).** Allocation, raters, stimuli, procedure, ethics, software versions and data availability remain FILL IN [FI-1–FI-4, FI-6, FI-15, FI-21, FI-22]. The paper cannot be submitted until these are filled.
- **Out of scope (D10).** Rater expertise and rating-scale choices are not analysed. Expertise is mentioned only as future work and as a generalisability limit.
- **MFRM fair averages.** No output exists. Fair scores are represented by EAP estimates only.
- **Bibliography.** No new citekeys were added in this update. All keys used were grep-verified in the checkpoint-1 revision.
  - in `web_references.bib`: e.g., robitzsch2025, chalmers2018, orlando2000, kang2008, yen1984, christensen2017, cai2014, wright1982, green1984, cronbach1951, hayes2007, looney2004, heiniger2021, shin2025;
  - in `phd_library.bib`: myszkowski2019, myszkowski2021, primi2019, cseh2019, amabile1982, memmert2007, santos2016, kempe2018, memmert2011, runco2012, embretson2013, myford2003, myford2004, batey2012, barbot2019, barbot2019b, safardilha2019.
  - No Bayesian keys are used.

---

## Revision plan vs 05_review.md

The writer follows this table. "Text" = fixed in the manuscript by the writer as planned above. "Author" / "Analyst" = cannot be fixed in the text; the planned fallback (Limitations text and/or softened claims) is written now and replaced if the action is done.

### Critical

| Point | Action | Where | Type |
|---|---|---|---|
| **C1** Raw-mean quintile/percentile statistics inflated by ties | Notebook now has tie-aware columns (F2.9). Lead with tie-resolved quintile change (.237), discordant pairs (.083), τ-b (.796), within-n θ̂ ranges (1-rating 1.436). Drop .350 and the percentile shifts from the text; drop every comparison with `tbl-score-agreement`. Build the aim-3 illustration on the 1-rating row/panel. | Contribution 3; core argument 4; abstract; Method 2.12; Results 3.4; Discussion 4.4 (i), (iii); box item 4; Conclusion | Text (analysis done) |
| **C2** Methods not reproducible | Keep all FILL INs visible; FI-4 extended (how products got 1/2/3+ ratings; 4+ products); new FI-21, FI-22, FI-23. | Method 2.1–2.6, 2.13; L1, L4 | Author action, not fixable in text |
| **C3** By-n table used as planning tool | Projection (F1.20) is now the primary RQ1 evidence and the basis of the box; by-n table and figure moved to SUPP and described as observational; "mainly" and causal wording removed; rel_post prior caveat added. | RQ1; contribution 1; abstract; Method 2.10; Results 3.2; Discussion 4.2, 4.5; box items 1, 3; object plan | Text (analysis done); parameter uncertainty → FI-28 |

### Major

| Point | Action | Where | Type |
|---|---|---|---|
| **M1** GRM used as reference standard without validity/fit evidence | Soften: "scores differ", "GRM adjusts for modelled rater differences"; delete "direct evidence"; state in Results that shifts show difference, not accuracy; L2 says GRM is best-fitting, not validated. | Contribution 3; 3.4 move 3; 4.4 (iii); 4.5; L2 | Text + optional analyst action FI-26 |
| **M2** Severity vs category structure/discrimination conflated; severity untested | Introduction P6 and Discussion 4.4 restructured into (i) severity/raw mean, (ii) category structure and discrimination, (iii) score consequences; "even the weaker constraints" deleted; untested severity stated in Method 2.8, 4.4, L6; RQ3 note. | P6; RQ3; 2.8; 4.4; L6 | Text + optional analyst action FI-24 |
| **M3** Cross-package M1 vs M2 LR test | Caveat in Method 2.8 (approximate; nesting assumed); FILL IN on sirt handling of unused categories; L6. | 2.7; 2.8; L6 | Text + optional analyst action FI-25 |
| **M4** Severity/spacing read from GRM thresholds; R18 b1 in abstract | R18 thresholds removed from abstract and all headlines; b1 range given for well-measured raters; spacing-is-partly-discrimination clause; R18 flagged as imprecise. | Abstract; contribution 2; 2.7; 3.3; 4.3 | Text + optional analyst action FI-29 |
| **M5** Truncated parameter-draw distribution | Method states intervals are conditional on valid draws and approximate for low-n raters; L3. | 2.10; 2.11; 4.3; L3 | Text + optional analyst action FI-28 |
| **M6** Prior / latent-distribution dependence | State rel_post is relative to unit prior variance; L3 latent-distribution limitation (projection included). | 2.10; 4.2; L3 | Text + optional analyst action FI-27 |
| **M7** "Not recognised" ratings and missingness | D12 cause sentence marked ATC-27; FILL IN for non-recognition rate by rater (FI-22); L1. | 2.6; L1 | Text + author/analyst action FI-22 |
| **M8** Student raters vs CAT "appropriate judges" | Neutral domain-familiarity sentence in P3; rater-pool FILL IN (FI-21); scope sentence "for this rater pool" in abstract implications, 4.5, Conclusion; L4. | P3; 2.2; abstract; 4.5; 5; L4 | Text + author action FI-21 |
| **M9** "15 ratings is a lower limit" unsupported | Advice dropped everywhere; 15 kept only as a technical estimation criterion; FI-23 for its source; box item 3 reworded around "about 50 still imprecise". | 2.6; 4.5; box; L5 | Text + author action FI-23 |
| **M10** Confirmatory/normative wording | RQ3 reworded descriptively; SQ1/SQ2 folded into Method; "in these data", no "we have shown". | RQs; P8; 4; 5 | Text (ATC-20) |
| **M11** Results number dump and interpretation | Results rules added; deltas trimmed; interpretive sentences moved to Discussion; Results closing sentence deleted; 6-decimal shares replaced by counts; main text 11 → 10 objects; Table 4 stays (compact). | 3.0–3.5; 4.3; object plan | Text; forest plot optional (FI-29); word/figure limits FI-16 |
| **M12** Render blockers and display problems | Pipe bug resolved in notebook; remaining headers/captions/wording in FI-18 (incl. new projection and tie-aware captions). | Object plan notes; FI-18 | Analyst action (notebook), not fixable in text |

### Minor

| Point | Action | Type |
|---|---|---|
| m1 APA leading zero | Convention added; all outline values in APA form; values otherwise as printed | Text |
| m2 Exact p-values | *p* < .001 only; 4.22e-105 and 1.79e-17 not quoted | Text |
| m3 Over-precise values | Category shares replaced by printed counts; sensitivity stays at 5 decimals as printed (optional 3-decimal reprint FI-18) | Text + optional analyst |
| m4 "Did not change the scores" | Marked ATC-26 and paired with max |Δθ̂| 0.16246; "changed them negligibly" offered | Text (author confirms) |
| m5 S-X² "conservative" | Plain "little power" wording added (ATC-11); Results reduced to one clause | Text |
| m6 Q3 | No-reference-distribution sentence added; "computable" stays undefined (not in notebook) | Text |
| m7 Pairwise Cronbach CI | "may also be biased" added (ATC-11) | Text |
| m8 Uncited "usual range" claim | Drop, or cite Introduction sources | Text |
| m9 "First football-specific evidence" | Hedged with ATC-2/ATC-4; no unmarked novelty | Text |
| m10 Cause of non-recognition | ATC-27 | Text |
| m11 Citation checks | Added to FI-17 | Author action |
| m12 "Labels for automated rating" | Dropped | Text |
| m13 θ-at-max phrasing | Rephrased; R01 value not explained | Text |
| m14 Pooled "all" row θ̂ range | Not headlined; quoted only with FI-20 caveat; within-n maxima used | Text + FI-20 |
| m15 Mechanism via 1-rating facet | 1-rating row/panel used in 4.4 (i) under ATC-21 | Text |
| m16 Products vs actions | D2 kept; consistency rule tightened | Text |
| m17 "Information per rating" | Renamed "average information"; caption fix in FI-18 | Text + analyst |
| m18 Supplement numbering | S-prefix crossref setting | Config action (paper-config), not writer |
| m19 `tbl-marginal-reliability-models` unused | Left not embedded (D5); offered to author as option | Author decision |
| m20 Data-collection timespan | FI-3; referenced in L7 | Author/analyst action |
| m21 Dense abstract | Max two numbers per aim; awkward .350 sentence gone | Text |
| m22 Figure captions/legends | FI-18 | Analyst action |

---

## Changes in this update (checkpoint 2; notebooks at 91c2e6d)

- Status line: revision plan after checkpoint 2. Sources: 42 labels; findings with F1.20, revised F2.9 and F2.1/F2.2.
- **RQ1:** the projection (F1.20) is the primary evidence for RQ1, contribution 1, abstract, Discussion 4.2/4.5 and the box. `fig-grm-reliability-projection` MAIN; `tbl-grm-reliability-projection` SUPP; `tbl-grm-reliability-by-n` and `fig-grm-rel-post-by-n` moved to SUPP (figure decision justified). Method 2.10 describes the projection and states "Model parameters are treated as known". Confounding statement marked ATC-25; no projected-vs-observed juxtaposition.
- **RQ3 / F2.9:** .350 headline and all comparisons with `tbl-score-agreement` removed; tie-aware statistics lead (.237, .083, τ-b .796, θ̂ range at equal raw mean, 1-rating row first). ATC-22 revised.
- **Rater parameters:** all a/b values replaced by the 2-decimal printed values; R18 threshold removed from the abstract and headlines; headline ranges taken from raters with at least 400 ratings.
- **Author constraints:** tone kept; "15 ratings is enough" dropped (FI-23); Methods FILL INs kept, FI-21 (rater pool) and FI-22 (non-recognition rate) added; APA number format applied; "did not change the scores" marked ATC-26 with 0.16246.
- **Review:** revision plan added; RQ3 reworded and SQs folded into Method (M10); Discussion 4.4 restructured (M2); claims softened (M1); optional analyst actions FI-24 to FI-29 with planned fallbacks.
- FI list: 14 → 23 open (FI-21 to FI-29 added; FI-1 narrowed; FI-18 updated; FI-20 partly resolved).
- ATC list: 22 → 26 open (ATC-24 to ATC-27 added; ATC-4, -5, -6, -7, -10, -11, -15, -16, -20, -21, -22 revised).
- Object plan: 11 → 10 main (7 tables, 3 figures) + 1 optional; 24 → 27 supplement (17 tables, 10 figures); 5 not embedded; total 42.

## Changes in the previous update (commit a97e51d; checkpoint-1 decisions applied; kept for the record)

- Status line set to approved at checkpoint 1; sources updated to 40 labels and the regenerated findings.
- **OD1:** working title kept.
- **OD2:** `tbl-score-agreement` MAIN, `tbl-theta-correlations` SUPP; both reliability-by-n objects MAIN (superseded at checkpoint 2); `fig-grm-information-shares` marked optional MAIN.
- **OD3:** F2.9/F2.10 integrated; `tbl-raw-mean-vs-grm` and `fig-raw-mean-vs-theta` both MAIN.
- **OD4:** author's exclusion sentence in Method 2.6 (second half marked ATC-26 at checkpoint 2).
- **OD5:** response styles quoted at 3 decimals.
- **OD6:** boxed design recommendations added.
- **OD7:** drafting proceeds now; [DD] refresh via FI-19.
- **D12:** the "not recognised" sentence in the author's meaning (marked ATC-27 at checkpoint 2).
- Resolved items written into Method: C2 cause, parameter-draw definition with the 87 rejected draws, LR df mechanism without the count, Q3 flag criterion, n_boot_failed 361, no infit/outfit cut-offs.
- FI-5, FI-7, FI-8, FI-10, FI-13 and FI-14 resolved; FI-20 added. ATC-17 closed; ATC-21 to ATC-23 added.

## Changes from the checkpoint-1 revision (kept for the record)

- The working title and central contribution are organised around the three aims (D1). The sparse design has been removed from the title, framing, abstract and contribution.
- The hypotheses H1a, H1b, H2 and H3 have been removed. The study is exploratory (D3).
- Terminology: a single "judges = raters" sentence in Introduction P3; "product" is the analytic term (D2).
- New outputs used (D8): ΔIC, LR p-values, threshold SEs; reliability CIs, Cronbach CIs; rater information CIs; score agreement.
- Exclusion sensitivity quotable (F2.8), with its own Results subsection 3.5 (D7).
- Main/supplement plan revised (D4, D5, D6, D9). Cleaning steps in the Method text (D12). Fit limitations moved to Method 2.9 and Limitations L2. Scope narrowed (D10).

## Decisions (applied)

**Checkpoint 1:** OD1 title kept; OD2 main-text objects; OD3 raw-mean comparison; OD4 exclusion wording; OD5 3-decimal response styles; OD6 boxed recommendations; OD7 draft now, refresh later.

**Checkpoint 2 (2026-10-26, relayed via coordinating session):** revise against `05_review.md`; projection primary for RQ1 (fig MAIN, tbl SUPP; observed by-n objects SUPP); tie-aware F2.9 statistics lead, no .350 and no comparison with `tbl-score-agreement`; compact 2-decimal rater-parameter table with updated values; tone kept; no over-reading of low-n raters and no R18 threshold in abstract/headlines; no "15 is enough" advice; Methods FILL INs kept, rater-pool and non-recognition FILL INs added; APA number format; "did not change the scores" marked with the 0.16246 maximum.

**Open for the author (no default applied beyond the above):** whether to drop the plain quintile/percentile columns from `tbl-raw-mean-vs-grm` (FI-18); whether to embed `tbl-marginal-reliability-models` in the supplement (m19); whether to keep the box given CRJ conventions (FI-16); which optional analyst actions (FI-24 to FI-29) to commission.
