# 04_outline.md: Argument architecture (Phase 5), GRM/JRT version

> **Revision round 5 (final wording pass) after checkpoint 2 (2026-10-27, relayed via coordinating session); notebooks at 04aefc5.**

Profile: `imrad-apa`. Venue: *Creativity Research Journal*. Style: APA 7th.
Structure: Abstract, Introduction, Method, Results, Discussion, Conclusion, References.

Sources (all re-read for this update):
- Brief: `~/drive/KNOWLEDGE/Paper_CreativityAssessmentInSportsCAT.md`
- Dossier: `01_dossier.md`
- Labels: `02_artifacts.md` (re-run after 04aefc5; **43 labels**; one new label, `tbl-overview-rater-response-styles`; nothing removed or renamed)
- Numbers: `03_findings.md` (re-run after 04aefc5). This is the ONLY source of numbers. Values are unchanged. Display changes: model labels in cells ("M1 (rating-scale MFRM)", "M2 (partial-credit MFRM)", "M3 (GPCM)", "GRM"); the "Ratings (n)" header is replaced by "Ratings by rater", "Ratings per product" and "Ratings (total)"; the Q3 note now defines a computable pair (F1.9); R09's mean prints 3.643 in the new table (3.642 only in an unlabelled cell; never quote that form).
- Review: `05_review.md` (round 4: 0 critical, 0 major, 11 minor; "minor revision, close to acceptance"). Each point is mapped in "Revision plan vs 05_review.md (round 4)" at the end of this file.
- Citekeys: **`phd_library.bib` is the single source.** The author fixed its entries; **the bib is not edited** by the pipeline. Citekeys are unchanged. No new keys are added. No Bayesian references.

**Author priority (checkpoint 2, rounds 3 to 5), overriding earlier plans:**
- The paper reports the actual rating study and its empirical findings. It does not make predictions or explore what-if scenarios about other raters or designs.
- The projection (F1.20, random raters only) appears **only as a side note**: in the supplement, one pointer sentence in Method 2.10 (round 5, m-5), and one or two sentences in the Discussion.
- No analyses that add design choices only to project or extrapolate. Keep it simple.
- The sparse design is not foregrounded. APA number formatting. The Methods FILL INs stay for the author.

Conventions in this file:
- **F…** is a finding ID in `03_findings.md`. Every number below is copied from there as printed, except for the APA formatting below.
- `tbl-…` / `fig-…` are labels from `02_artifacts.md`. **[MAIN]** means the object is embedded in the main text; **[SUPP]** means it is embedded in the online supplement.
- **[ATC-n]** marks an interpretive or contribution claim that the author must confirm. **[FI-n]** marks a FILL IN item that the author must supply. FI and ATC numbers stay stable; closed items are listed as closed, not renumbered.
- **APA number format.**
  - Values that cannot exceed 1 drop the leading zero: correlations (incl. Q3, τ-b), reliabilities, α, shares/proportions, and *p*. Values that can exceed 1 keep it: a, b_k, information, θ̂ and θ̂ ranges, PSD, infit/outfit, means, SDs, entropy, χ², information criteria, |Δθ̂|, |Δa|, and the Q3 criterion 0.2.
  - Numbers of 1,000 or more take a comma: 7,820; 3,668; −11,733.227; 23,720.455. This also applies to values that the notebook prints without a separator in text notes or stdout ("639 of 1000" → 639 of 1,000; "3668 common products" → 3,668). Seeds and identifiers do not (seed 20260713).
  - No other change: **no rounding, and no added or removed decimals**. Never quote *p* in scientific notation; write *p* < .001.
  - All values in this outline are already in APA form.
- **Precision as printed.** Rater parameters (F2.1/F2.2) and rater information with its intervals (F2.4) are printed at **2 decimals**; shares at 3. Response styles (F0.8, `tbl-overview-rater-response-styles`) are at 3 decimals; whole numbers print without decimals there (R08's mean "3"; five raters' share of 7s "0"), so the text describes those cells in words rather than quoting "3.000" or ".000". Sensitivity values (F2.8) are at 5 decimals. Category shares (F0.6) are not quoted; quote the counts instead.
- **Never quote** any value that `03_findings.md` lists as removed or NOT IN NOTEBOOK:
  - the most- or least-informative projection values, `true_r2`, and quantiles of mean rel_post;
  - every pooled raw-mean value, every raw-mean correlation, percentile shift, quintile measure and tied-raw-mean share;
  - 3-decimal rater parameters and 3-decimal information CI bounds;
  - Tolerance "0.000" or "0.0001" (it now prints "10⁻⁴"), and M3 ≥ 2 quintiles "0.000545256" (it now prints "0.001", APA .001);
  - the "confounded" and "not comparable" notebook sentences;
  - "6 unused end categories", the 0.7–1.3 misfit range, and any RMSEA or other global fit index;
  - **R09's mean as 3.642** (unlabelled cell); if R09's mean is quoted, it is **3.643** with @tbl-overview-rater-response-styles;
  - the number of non-computable Q3 pairs as a printed value (it is not printed; do not derive it in the text);
  - the old labels "Ratings (n)", "M1 (RSM/MFRM)" and "M2 (PCM)" in prose.
- **No pipeline wording in the prose.** The text never cites "the analysis notebook" or "the output" as an authority. It never says that values "will be refreshed" or that more data are coming. Statements taken from notebook notes become the authors' own wording, marked [ATC] where they interpret.
- **Design wording.** The sparse design is not foregrounded. The design numbers are given once, via @tbl-design-summary. Avoid framing such as "most products were rated only once or twice" or "in this sparse design".
- **MFRM wording (round 4, N3-M1).** "A shared category structure" is a property of the **rating-scale MFRM (M1)** only. A partial-credit MFRM relaxes it (eckes2015), and M2 corresponds to that model. The constraint that every Rasch/MFRM model imposes is **equal discrimination**, which LR and AIC reject but BIC does not. Never write "the MFRM assumes a shared category structure" without "rating-scale".
- **Author names in hand-written prose (round 5).** Particles stay with the surname: "de Ayala", "ten Hove", "de Joode", "de Sa Fardilha", "van der Ark", "van der Kamp" (e.g., "ten Hove et al." in narrative text). CSL handles the reference list; do not hand-edit it.
- **linacre1989 (round 5).** The entry is the MESA Press book *Many-facet Rasch measurement*. Prose uses "many-facet", never "many-faceted".

---

## Working title (unchanged)

**Number of ratings, rater differences, and score reliability in creativity ratings of football actions: A judge response theory analysis**

The title still fits: "number of ratings" now refers to the observed reliability by number of ratings (F1.14).

## Terminology (round 5: model labels aligned with the tables)

- **Raters.** One sentence at the first CAT mention (Introduction P3) says that the CAT and JRT literature calls raters "judges". After that, use "rater" everywhere, except in the term *judge response theory*.
- **Product / action.** Define the pair **once**, in Method 2.3: "each rated product was a single football action".
  - Results and Method use "product".
  - "Action" appears in the title, the Introduction's sport framing, the stimulus description, and the practical implications.
  - Do not define the pair a second time in the Discussion (round-2 m16).
- **Average information.** Use this term for information integrated over θ ~ N(0, 1), defined once in Method 2.11. The table header reads "Information per rating".
- **Model names (round 5; match the table cells).** The tables print "M1 (rating-scale MFRM)", "M2 (partial-credit MFRM)", "M3 (GPCM)" and "GRM". The prose uses the same names:
  - first mention in Method 2.7: "M1, the rating-scale MFRM", "M2, the partial-credit MFRM (a partial credit model with raters as items)", "M3, the GPCM"; thereafter "M1 (rating-scale MFRM)", "M2 (partial-credit MFRM)", "M3 (GPCM)" or the short forms M1/M2/M3;
  - "RSM" and "PCM" as model names appear only where the original model is cited (andrich1978; masters1982), not as labels;
  - "the MFRM" alone refers to the family and is used only for claims that hold for every member (severity facet, equal discrimination).
- **Ratings headers (round 5).** When the text points to a column, use the printed headers: "Ratings by rater", "Ratings per product", "Ratings (total)". "Ratings (n)" does not exist.
- **Quartiles (round 5, m-3).** Write "first and third quartiles"; never "Q1"/"Q3" for quartiles, because Q3 is Yen's statistic.
- **Response styles (round 5).** Use the table's terms: share of ratings in the lowest category (1), in the highest category (7), in the extreme categories (1, 7) and in the middle categories (3–5). "Floor", "ceiling" and "central" may be used once as glosses in Method 2.11.

---

## Central contribution [ATC-1]

The study applies judge response theory (JRT) to CAT-style creativity ratings of football actions (final data in @tbl-design-summary; F0.3). Its contribution is empirical and comes in three parts.

1. **How reliable the obtained scores are, and how reliability varies with the number of ratings a product received.**
   - The empirical marginal reliability of the scores actually obtained is .672 [.649, .687]. A hypothetical full panel would reach .960 [.953, .968] (F1.12).
   - Conventional indices give quite different values: pairwise Cronbach's α .928 [.891, .943] and Krippendorff's ordinal α .392 [.362, .417] (F1.18).
   - Mean product-level reliability (rel_post) is .520 for products with 1 rating, .698 with 2 and .757 with 3, and rises to .919 with 10 (F1.14). These are observed values, not the result of a design manipulation; how products came to have their number of ratings is FI-4.
2. **How raters differ, with the uncertainty of each difference.**
   - Raters differ in category use, threshold location and discrimination (F0.8, F2.1, F2.2) and in average information (F2.4).
   - Ranges are given over all 19 raters. Their extremes come from raters with few ratings and large SEs, for example a from 0.63 (R18, *SE* 0.26) to 3.71 (R19, *SE* 2.22).
3. **How much the scores depend on whether rater differences are modelled.**
   - The likelihood-ratio test rejects the shared category structure of the rating-scale MFRM (M1 vs M2, *p* < .001; F1.2). Equal discrimination, the constraint shared by all Rasch-family models including the partial-credit MFRM (M2), is rejected by the LR test (*p* < .001) and AIC, but not by BIC (F1.1, F1.2).
   - Raw mean ratings and GRM scores order products differently (F2.9). For products with 1 and 2 ratings, Kendall's τ-b is .832 and .815, and .042 and .067 of the product pairs are in reversed order. With 1 rating, the reversals reflect only the raters' modelled parameters; with 2 ratings, they also reflect the pattern of the two ratings behind the same mean [ATC-21, ATC-22]. Products with the same raw mean receive GRM scores on average 1.283 and 1.537 apart; as ranges, these are set by the most extreme raters, some of whom are imprecisely estimated [ATC-21].
   - The choice among the scoring models also shifts rankings: .202 of products change quintile under M1 (rating-scale MFRM) relative to the GRM, with a mean percentile shift of .042, although Pearson *r* = .975 (F2.7).
   - These are differences between scores, not evidence that one score is more accurate [ATC-15, ATC-22].

Implication [ATC-3, ATC-5, ATC-14, ATC-15]:
- Report the reliability of the scores actually used.
- Plan the number of ratings per action with that reliability in mind.
- Because parameters of raters with few ratings were imprecise, consider linking raters through a common calibration set (round 5: conditional wording, m-1).
- **Re-grounded (C-M1):** because raters differed in thresholds and discrimination in these data, and raw means and model-based scores ordered actions partly differently, consider scoring with a model that adjusts for rater differences (under its assumptions), and report how far its ordering departs from the raw mean. The study does not show that model-based scores are more accurate.

These implications apply to this student rater pool and this scale [FI-21].

## Core argument (5 sentences)

1. CAT reliability is conventionally reported for the mean over a rater panel (amabile1982; kaufman2008a; cseh2019). When each action receives only some of the ratings, the precision of each score depends on how many ratings it received and from whom.
2. JRT treats raters as items with their own severity, scale use and discrimination (myszkowski2019; myszkowski2021). It therefore gives the reliability of the scores actually obtained, the precision of each product's score, and an uncertainty-quantified description of how raters differ.
3. In the football ratings, three things hold:
   - the reliability of the obtained scores is well below the full-panel value (F1.12);
   - product-level reliability is lower for products with one or two ratings than for products with more (F1.14);
   - raters differ in category use, threshold location, discrimination and information (F0.8, F2.1–F2.4).
4. The shared category structure of the rating-scale MFRM is rejected; equal discrimination, which every Rasch-family model assumes, is rejected by LR and AIC but not by BIC (F1.1, F1.2). Within products with the same number of ratings, raw means order products partly differently from GRM scores, and equal raw means map to clearly different GRM scores (F2.9, F2.10). The choice of scoring model also shifts rankings (F2.7). The two comparisons are reported separately and not ranked against each other.
5. Rater differences therefore belong in the design of creativity research in sport (ratings per action; where rater parameters are imprecise, a common calibration set). For scoring, researchers should consider models that adjust for rater differences and report how far their ordering departs from raw means; no accuracy advantage is claimed [ATC-5, ATC-7, ATC-14, ATC-15].

## Research questions (exploratory; no hypotheses) [ATC-20]

The study is exploratory. The writer must not use the words "hypothesis", "supported" or "confirmed" for the RQs. The only exception is the LR/AIC wording under RQ3(a).

- **RQ1 (aim 1): number of ratings and reliability.** How reliable are the creativity scores obtained in this study? How does product-level reliability vary with the number of ratings a product received? How does the reliability of the obtained scores compare with a hypothetical full panel and with conventional agreement and consistency indices?
  - Evidence: F1.12, F1.14, F1.18, F1.19; descriptive support from F1.13, F1.16, F1.17.
  - The projection (F1.20) is not RQ1 evidence; it is a side note (Method pointer, supplement, Discussion).
- **RQ2 (aim 2): rater differences.** How do raters differ in threshold location, scale use (category use, response styles), discrimination and information, and how precisely are these differences estimated?
  - Evidence: F0.6, F0.7, F0.8, F2.1–F2.5.
  - "Severity" is **not** promised in RQ2, because no severity measure or test is reported. If the author resolves ATC-6 in favour of reading thresholds as severity, write "threshold location (severity)" with the GRM caveat of Method 2.7.
- **RQ3 (aim 3): how much do scores depend on whether rater differences are modelled?**
  - (a) Are the constraints of a shared category structure (M1, rating-scale MFRM) and of equal discrimination (all Rasch-family models, including M2, the partial-credit MFRM) tenable? Evidence: F1.1, F1.2, F1.4, F1.5, F1.11.
    - Wording: rater-specific discriminations are "supported by the LR test and AIC, but not by BIC".
    - Severity is described under RQ2. It is not tested on its own.
  - (b) How far do product scores and rankings change when rater differences are ignored (raw mean) or constrained (M1, M2, M3)? Evidence: F2.9, F2.10, F2.6, F2.7.

Supporting analyses, reported in the Method/Results but not as RQs:
- model choice and adequacy: F1.1, F1.3, F1.7–F1.10;
- robustness to the rater exclusion: F2.8.

---

## Section outline

### Abstract (one paragraph, unstructured, ≤ 250 words [FI-16])

Model 2 order: background/aim → method → results with numbers → implications. The abstract has no citations, no sparse-design framing, **no projection values and no R18 values**. Keep the numbers few.

**Round 5 (m-1): no [AUTHOR TO CONFIRM] or [FILL IN] marker is rendered inside the abstract.** The claims they covered stay on the ATC/FI lists (ATC-2 for "little is known"; ATC-5, ATC-14, ATC-15 for the implications; FI-1 for "student raters"). The writer lists them in the hidden (non-rendering) comment block so that the author still sees them. **Hard limit: ≤ 250 words**; if it runs over, compress the method sentence and the per-n reliabilities first, then drop the optional range clause.

- **Background/gap.** CAT ratings are the standard way to assess creative products and are also used for actions in sport. However, little is known about how reliable such creativity scores are when each action receives only some ratings, or how much raters differ when judging creativity in sport (ATC-2, no rendered marker).
- **Aim/method.** Student raters (FI-1, no rendered marker) rated football actions on a 7-point creativity scale (counts from F0.3). Judge response theory models were fitted by marginal maximum likelihood: a graded response model (GRM), compared with an adjacent-category ladder from the rating-scale many-facet Rasch model to the generalized partial credit model.
- **Results.**
  - Aim 1: the empirical reliability of the obtained scores was .672, against .960 for a hypothetical full panel (F1.12). Mean product-level reliability was .520 for actions with one rating and .698 with two (F1.14).
  - Aim 2: raters differed in category use (e.g., the share of lowest-category ratings ranged from .579 to .016; F0.8, traceable to @tbl-overview-rater-response-styles in the supplement), threshold location and discrimination. Parameters of raters with few ratings were imprecise. No numeric parameter range is given, so that R18 stays out.
  - Aim 3:
    - LR tests rejected a shared rating-scale structure and equal discrimination (both *p* < .001; F1.2), **although BIC favoured equal discrimination** (F1.1).
    - Among actions with one and two ratings, raw means and GRM scores agreed with Kendall's τ-b = .832 and .815 (F2.9).
    - Optional, for density (m21): "and actions with the same raw mean received GRM scores on average 1.283 and 1.537 apart". Drop it first if the word limit bites. If kept, its range qualifier lives in Discussion 4.4 (i).
- **Implications (hedged; re-grounded, C-M1; round 5 conditional calibration wording).** For this kind of rater pool, creativity studies in sport should:
  - report the reliability of the scores actually used;
  - plan the number of ratings per action accordingly;
  - **because the parameters of raters with few ratings were imprecise, consider linking raters through a common calibration set** (m-1: conditional, not a flat instruction; the study did not use such a set);
  - and, because raters differed and raw means ordered actions differently from model-based scores, consider scoring with a model that adjusts for rater differences and report how far the ordering departs from raw means.
- **Do not use:** any projection value, the "who rates" idea, any pooled raw-mean value, any b1 value, "we show", "model rather than average" as a finding, any rendered marker, or any wording implying the GRM scores were shown to be more accurate.

### 1 Introduction

Purpose: move from the importance of creativity, through the CAT and its two weak points (number of ratings; rater differences), to the gap in sport and the present exploratory study. Four moves (writing-models/introduction.md). The sparse design is not part of the framing.

**Move 1: Background**
- P1. Creativity as a core competence:
  - ranked among the core workforce skills (wef2025 [FI-17]);
  - assessed in PISA 2022 (oecd2024);
  - a development target in sport (safardilha2019 [narrative form "de Sa Fardilha"]; santos2016).
- P2. 4P taxonomy (batey2012). Each facet needs its own measurement (barbot2019b; barbot2019). This paper concerns the product facet: football actions rated by others.

**Move 2: Previous research**
- P3. **CAT procedure and reliability.**
  - The CAT procedure (amabile1982; hennessey2011; kaufman2024). Add the terminology sentence on judges and raters here.
  - Independent raters usually reach α > .70 (baer2004; kaufman2008a; hennessey2011) [FI-17]. Lower agreement has also been reported (long2015; cseh2019).
  - The CAT requires raters familiar with the domain (amabile1982). State this neutrally, without judging the present raters [FI-21].
- P4. **Reliability rests on the number of raters (aim 1).**
  - Spearman–Brown logic: reliability depends on the mean inter-rater correlation and on the number of raters (amabile1982). A high α can mask low single-rater agreement (kaufman2008a [FI-17: verify the "mask" point; round 5, m-2]).
  - **cseh2019, one paraphrase used in both places (round 5, m-7):** "the number of raters needed for adequate reliability has to be established for each domain" [FI-17: verify against the source]. Use this exact wording here and in Discussion 4.2.
  - The rule of thumb of "five to ten" raters comes from kaufman2008 (the book *Essentials of Creativity Assessment*) [FI-17].
  - The key distinction, stated in general terms: a panel coefficient describes the mean over all raters. When each product receives only some ratings, what matters is the precision of each product's score given its own ratings (primi2019; forthmann2025 [FI-17]).
- P5. **Raters differ (aim 2).**
  - Raters differ in severity, scale use and beliefs (long2015), and their tendencies drift (barth2021).
  - Rater-effect taxonomy (engelhard1994; myford2003; myford2004).
  - Judged sports (looney2004; anderlucci2021; heiniger2021 [FI-17]).
- P6. **From averaging to JRT (aim 3).** Two paragraphs.
  - **Severity and the raw mean.** Unweighted means treat raters as interchangeable. When different raters rate different products, the means are confounded with rater severity (primi2019). The many-facet Rasch model adds a severity facet (linacre1989, *Many-facet Rasch measurement*; eckes2015; primi2019).
    - τ-equivalence sentence as in draft 4.
  - **Category structure and discrimination (N3-M1).**
    - The rating-scale form of the MFRM assumes that all raters share one category structure. A partial-credit MFRM relaxes this with rater-specific thresholds (eckes2015 [FI-17]). Every Rasch-family model, including the partial-credit form, assumes equal discrimination; unequal discrimination shows up only as misfit (myford2004; myszkowski2021).
    - IRT basics: lord1980; embretson2013; ayala2022 (narrative "de Ayala"). Rasch family: rasch1960; bond2020; andrich1978; masters1982.
    - JRT via the GPCM (muraki1992) or the GRM (samejima1969) (myszkowski2019; myszkowski2021). Applications: barbot2023; pellegrino2025 (also retained a GRM [FI-17]).
    - The adjacent-category models are nested and testable by LR. The GRM is cumulative [ATC-8] and is compared by information criteria.

**Move 3: Gap**
- P7. **Creativity in sport.**
  - Prior work centres on the process (memmert2011).
  - Product ratings of football actions: kempe2018; memmert2007; zahno2023; joode2023 (narrative "de Joode et al."). These studies average ratings and report ICCs or agreement [FI-17]. A Rasch analysis exists only for a coach questionnaire (shin2025).
  - "However" sentence with three gaps:
    1. little is known about how the reliability of creativity scores of sport actions depends on the number of ratings each action receives (cseh2019, same paraphrase as P4);
    2. no evidence exists on how raters differ when judging creativity in sport;
    3. to our knowledge, rater differences have not been modelled with IRT/JRT for creativity ratings in sport [ATC-2].

**Move 4: Present study**
- P8.
  - Data: CAT-style creativity ratings of football actions by multiple raters (counts via Method / @tbl-design-summary).
  - The exploratory aims and RQ1–RQ3. Say that no confirmatory hypotheses were formulated.
  - Analytic route in one sentence: a JRT model ladder plus a GRM, estimated by MML in mirt; the reliability of the obtained scores, overall and by number of ratings; rater parameters with uncertainty; and GRM scores compared with raw means.
  - Scope: rater expertise and the design of the rating scale are not analysed.

### 2 Method

Purpose: replication and justification of the analytic choices. Order: overview → details → relation to prior methods → problems (writing-models/methods.md). **All FILL INs stay visible for the author.**

**2.1 Overview.** CAT-style rating study: independent raters, relative judgements, randomised order (amabile1982; hennessey2011). Products are football actions rated within a larger project [FI-1, FI-2]. Ethics [FI-1]. Exploratory analysis; preregistration status [FI-15].

**2.2 Raters.**
- Bachelor's and Master's students rating as part of thesis projects [FI-1].
- Rater-pool description [FI-21]. If something was not recorded, say so in one sentence.
- Final number of raters; ratings per rater from 50 to 1,174 (F0.3; column "Ratings by rater" in the rater tables). Pseudonyms R01–R19.

**2.3 Products and stimulus material.** Define the product term here ("each rated product was a single football action"). Matches, competitions, the selection rule, clip length [FI-2].

**2.4 Rating procedure.**
- Software, instruction and the creativity definition shown to raters (originality × functionality in game context; runco2012) [FI-3].
- Relation to the CAT "no criteria" rule (hennessey2011) and to trained-rater sport studies (kempe2018; memmert2007) [ATC-19].
- 7-point unipolar scale with anchors 1 / 4 / 7, plus an off-scale "action not recognised" option [FI-3].
- Order, sessions and breaks, data-collection timespan, other dimensions rated (not analysed here) [FI-3].

**2.5 Rating design (brief).**
- Allocation of products to raters, and how products came to have 1, 2 or 3+ ratings [FI-4]. This bears on the ignorable-missingness assumption of MML. If FI-4 shows that products with different numbers of ratings were rated by different raters, state it here; otherwise do not state it anywhere.
- The design is incomplete but connected (one component; F0.3). The coverage numbers are in @tbl-design-summary only.
- If the planned benchmark set was not realised as a fully crossed block, state this neutrally [ATC-18].

**2.6 Data preparation and final data.**
- Cleaning, in text only (F0.1): 9,148 raw rows; 1,290 ratings marked "action not recognised" removed; 1 out-of-range value (0.0, R04) removed; 13 rows removed when resolving duplicate rater–product pairs (12 pairs, 1 conflicting; last entry kept). Result: 7,844 rows.
- **Not-recognised sentence (author-supplied; no marker):** "The 1,290 ratings marked 'action not recognised' were removed; such ratings result from video cutting and imperfect material, where close-ups or other TV artefacts render the action non-visible."
  - Add the non-recognition rate by rater [FI-22].
  - Compute no percentage from 1,290 / 9,148.
- **Rater exclusion (F0.2; `tbl-excluded-raters` [SUPP]):**
  - R20 (13), R21 (9) and R22 (2), together 24 ratings; one product rated only by them was dropped.
  - Wording: "Raters with fewer than 15 ratings were excluded because their up to seven rater-specific parameters cannot be estimated reliably" [FI-23 for the source of 15]. 15 is the exclusion criterion only; it is never a recommendation.
  - **Sensitivity sentence (ATC-26):** "Excluding them changed the product scores only slightly (largest change in a product score 0.16246; see @tbl-sensitivity-rater-exclusion) **[AUTHOR TO CONFIRM]**." Do not write "did not change the scores".
- **Final data** (F0.3; `tbl-design-summary` [MAIN]):
  - 7,820 ratings of 3,668 products by 19 raters; scale 1–7, coded 0–6 internally;
  - ratings per product: mean 2.132, median 2, range 1–10, harmonic mean 1.726;
  - matrix fill .112; one connected component; 17 of 171 rater pairs without a common product; median overlap 13.
  - Quote these once. Do not repeat them as framing.
- **Category gaps** (F0.7; `tbl-category-usage` [SUPP]):
  - category 7 unused by R01, R03, R06 and R18; categories 6–7 unused by R17;
  - no internal gaps;
  - these raters therefore have fewer thresholds.

**2.7 Measurement models.**
- JRT frame: raters are items and products are persons; unidimensional θ ~ N(0, 1) (myszkowski2019; myszkowski2021).
- **Threshold definition (neutral):** "b_k is the θ at which a rating above category k becomes more likely than a rating of k or below." Do not add "higher b means a stricter rater" unless the author confirms it **[ATC-6]**.
- In the GRM, thresholds are expressed relative to discrimination, so threshold spacing is partly the same fact as a. State this once here.
- Ladder (round 5 names and m-11 wording):
  - **M1, the rating-scale MFRM:** the rating scale model (andrich1978) with raters as items, which **corresponds to** a two-facet rating-scale MFRM (linacre1989; eckes2015; primi2019), **here estimated by marginal maximum likelihood** with a normal product distribution (sirt::rm.facets; robitzsch2025). Do not write "equivalent to". It is the only model in the ladder with one shared category structure;
  - **M2, the partial-credit MFRM:** the partial credit model (masters1982) with rater-specific thresholds; with raters as items it corresponds to a partial-credit MFRM (eckes2015). Still Rasch: equal discrimination;
  - **M3, the GPCM** (muraki1992), adding rater-specific discrimination.
  - M2 and M3 are fitted in mirt (chalmers2012).
- Retained scoring model: a GRM (samejima1969) in mirt; its thresholds are ordered by construction.
- Estimation (F1.3): MML via EM with 61 quadrature points; Oakes SEs (chalmers2018); converged after 165 iterations; information matrix positive definite (`tbl-grm-convergence` [SUPP]). Tolerance prints "10⁻⁴"; quoting it is optional.

**2.8 Model comparison.**
- LR tests M1 vs M2 (shared vs rater-specific category structure) and M2 vs M3 (equal vs rater-specific discrimination); logLik, AIC, BIC and SABIC with Δ to the best model (F1.1). The GRM is compared with the ladder by information criteria only.
- Problems, stated briefly:
  - M1 vs M2 is a cross-software comparison (sirt vs mirt), so the test is approximate.
  - The df of M1 vs M2 is below the formula value (J − 1)(K − 2) = 90, because raters who never used an end category have fewer step parameters (@tbl-category-usage). Do **not** state the count of unused end categories.
  - Severity differences are not tested on their own (no model without rater effects).

**2.9 Model adequacy (limits stated here once).**
- Infit/outfit (wright1982) for M1 and the GRM, with expected value 1 and **no cut-offs**. Values below 1 are expected because each θ̂ is estimated from the ratings being checked.
- S-X² (orlando2000; kang2008) with the missing ratings imputed 20 times. Most cells are imputed from the fitted model, so the test has little power [ATC-11].
- Yen's Q3 (yen1984): the correlation of two raters' residuals over the products both rated.
  - **Computable pairs (round 5; F1.9 note, FI-30 closed):** "Q3 was computed for rater pairs with at least 3 jointly rated products and residual variance in both raters (137 of 171 pairs)." No [FILL IN] marker. Do not state or derive the number of non-computable pairs, and do not explain them by the 17 pairs without shared products.
  - It is negatively biased with few raters per product (christensen2017), so pairs are compared by their deviation from the mean Q3 over all computable pairs. A pair is flagged when it has at least 30 jointly rated products and |Q3 − mean Q3| > 0.2. This criterion has no reference distribution.
- C2 (cai2014) could not be computed. It needs the joint distribution of every rater pair, and 17 of 171 pairs share no products (F1.10). Do not embed `tbl-grm-global-fit`.

**2.10 Scores and reliability (aim 1).**
- EAP θ̂ with the posterior SD (PSD).
- **Empirical marginal reliability** of the scores actually obtained: Var(θ̂) / (Var(θ̂) + mean PSD²).
- **Model-based marginal reliability** for a hypothetical product rated by all raters (green1984; mirt marginal_rxx), plus a grid check.
- **95% intervals:** from 200 accepted draws of the parameters from their asymptotic normal distribution (estimates and Oakes covariance). For the empirical reliability, products are also resampled. A draw that was not a valid GRM (some a ≤ 0 or thresholds out of order) was rejected and replaced; 87 draws were rejected. The intervals are therefore conditional on valid parameter sets and approximate, especially for raters with few ratings.
- **Product-level reliability:**
  - rel_post = 1 − PSD². It is defined relative to the unit prior variance of θ, so with one or two ratings it partly reflects the prior.
  - rel_info = I/(I + 1) from the information of the product's own raters at θ̂.
  - Both are summarised by the number of ratings each product received (column "Ratings per product").
- **Conventional indices:**
  - Cronbach's α (cronbach1951) from pairwise covariances over the usable raters, and on the largest fully crossed block [FI-9: why 5 raters were not usable];
  - Krippendorff's ordinal α (hayes2007);
  - 95% bootstrap CIs over products (1,000 replications). For the pairwise α, 639 of 1,000 replications could be computed (361 failed); the interval uses the computable ones and is approximate and possibly biased [ATC-11].
  - **hove2024 (round 5, m-10):** no longer placed after Krippendorff's α. Use it, if at all, in the lead sentence of this paragraph, on reliability indices for incomplete designs: "Conventional reliability indices assume, or must be adapted to, a complete design (ten Hove et al., 2024 [@hove2024]); we therefore report them only for comparison." If the author prefers not to invite an ICC request, drop the citation.
- **Projection pointer (round 5, m-5; one sentence, last in 2.10):** "As a side note, the reliability expected for 1 to 10 ratings per product was projected from the fitted GRM, with raters drawn at random from this panel (see Supplement, @tbl-grm-reliability-projection)." Description only: no values, no further detail in the Method; the procedure stays in the supplement note.

**2.11 Rater parameters, information and response styles (aim 2).**
- GRM a and b_k with Oakes SEs.
- **Average information:** rater information integrated over N(0, 1), and each rater's share of the full-panel information. 95% intervals come from the same parameter draws, with the same caveat.
- Descriptive response styles on the raw scale (F0.8; @tbl-overview-rater-response-styles [SUPP], @fig-overview-rater-response-styles [MAIN]): mean, median, SD, IQR, categories used, entropy (natural log), and the shares of ratings in the lowest category (1; floor), the highest category (7; ceiling), the extreme categories (1, 7) and the middle categories (3–5; central). These are not adjusted for which products each rater saw, and have no per-rater uncertainty.

**2.12 Score agreement and sensitivity (RQ3b).**
- **Raw mean vs GRM (F2.9):** each product's unweighted mean rating is compared with its GRM EAP, **separately for products with 1, 2 and 3+ ratings**.
  - The raw mean takes few distinct values (with one rating, only seven), so agreement is measured by:
    - Kendall's τ-b;
    - the share of product pairs with different raw means that the GRM orders the other way round ("reversed order");
    - the mean and maximum range of GRM scores among products with the same raw mean.
  - No pooled comparison across numbers of ratings.
- Correlations of EAP scores between all models. Relative to the GRM (F2.7): the absolute shift in percentile rank (0–1 scale) and the share of products changing quintile.
- Integration-grid check for M1 (F2.6).
- Rater-exclusion sensitivity: the GRM refitted with all 22 raters (F2.8).

**2.13 Software and availability.** R and package versions; Python for display [FI-6]. Data and code availability with pseudonymised rater IDs [FI-15].

### 3 Results

Purpose: describe, not interpret. Moves per writing-models/results.md: aim and overview → objects and key results → problems → at most one hedged pointer. Rules:
- report key contrasts and point to the tables for the rest;
- no interpretive sentences;
- APA numbers.

Order: scoring model (brief) → RQ1 → RQ2 → RQ3 → sensitivity.

**3.0 Overview (1 short paragraph).** Echo the aims. All analyses use @tbl-design-summary. One descriptive preview line, with no evaluative words.

**3.1 Scoring model (supporting; short)**
- Findings: F1.1, F1.3, F1.7–F1.10.
- Embed `tbl-model-fit` [MAIN]. Cross-reference `tbl-grm-convergence`, `tbl-grm-rater-fit` and `tbl-grm-q3-flagged` [SUPP].
- The GRM has the lowest AIC, BIC and SABIC. The GRM and M3 (GPCM) have the same number of parameters (127), so their comparison reduces to the log-likelihood (−11,733.227 vs −11,756.510), "so the GRM is lower by 46.566 on AIC, BIC and SABIC alike". Leave the other Δ values to the table.
- Converged after 165 EM iterations; information matrix positive definite (F1.3).
- Fit, one or two sentences:
  - no S-X² was significant (*p* from .294 to .671);
  - infit 0.334 (R19) to 0.971 (R18) and outfit 0.322 (R19) to 0.961 (R18), all below 1;
  - mean Q3 −.238 over the 137 computable pairs (definition in Method 2.9; no marker); 20 pairs flagged. The table shows 10 of them: 9 deviate negatively, and 1 (R10–R11) positively;
  - C2 was not computable (Method 2.9).

**3.2 Reliability of the creativity scores and number of ratings (RQ1)**
- Findings: F1.12, F1.14, F1.18, F1.19; F1.13, F1.16, F1.17 in one sentence each.
- Embed:
  - `tbl-reliability-overview` [MAIN]
  - `tbl-grm-reliability-by-n` [MAIN]
- Cross-reference [SUPP]:
  - `fig-grm-rel-post-by-n`
  - `tbl-grm-reliability-ci` (its CIs are quoted)
  - `tbl-grm-reliability-summary`
  - `tbl-naive-indices`
  - `fig-grm-rel-post-histogram`
  - `fig-grm-rel-post-by-theta`
  - `fig-grm-rel-consistency`
  - `fig-grm-panel-information` (caption keeps "hypothetical")
- **No projection object or value in the Results** (the Method pointer names the supplement table only).
- Bullets:
  - **(1) Obtained scores vs full panel vs conventional indices** (@tbl-reliability-overview; F1.12, F1.18):
    - empirical marginal reliability: .672 [.649, .687];
    - model-based marginal reliability (hypothetical full panel): .960 [.953, .968]; grid check .960;
    - Cronbach's α, pairwise covariances: .928 [.891, .943] (14 raters, 1,900 products; CI approximate, from 639 of 1,000 computable bootstrap replications);
    - Cronbach's α, fully crossed block: .658 [.526, .756] (3 raters, 139 products);
    - Krippendorff's ordinal α: .392 [.362, .417] (19 raters, 2,771 products).
    - State what each index refers to, using the table's "Refers to" column. Do not discuss the M1–M3 rows.
  - **(2) Product-level reliability by number of ratings** (@tbl-grm-reliability-by-n, column "Ratings per product"; @fig-grm-rel-post-by-n [SUPP]; F1.14). Descriptive:
    - Mean rel_post: .520 with 1 rating (897 products), .698 with 2 (2,080) and .757 with 3 (357). It is higher with each additional rating in the table, up to .919 with 10 ratings (3 products). Quote 1, 2 and 3.
    - Mean PSD falls from 0.686 to 0.285.
    - The 9- and 10-rating rows rest on 3 products each. No mean reaches the full-panel value of .960.
    - Products with the same number of ratings differ in rel_post (@fig-grm-rel-post-by-n).
    - **Move 3:** "These values are observed: products did not receive their number of ratings through a design manipulation (see Rating design) [FILL IN: FI-4]." Do not add "confounded" and do not cite the notebook.
  - **(3) Distribution and consistency (one sentence each):**
    - rel_post median .698, IQR .173 (**first and third quartiles .596 and .769**; round 5, m-3), range .057–.929 (F1.13);
    - rel_post and rel_info correlate *r* = .935, and 320 products differ by more than .1 (F1.16).

**3.3 Rater differences (RQ2)**
- Findings: F0.6, F0.7, F0.8, F2.1–F2.5.
- Embed:
  - `fig-overview-rater-response-styles` [MAIN]
  - `tbl-grm-rater-parameters` [MAIN]
  - `tbl-grm-rater-information-ci` [MAIN]
- Cross-reference [SUPP]:
  - **`tbl-overview-rater-response-styles` (new, round 5)**: the source of every per-rater response-style value quoted in the text and abstract
  - `tbl-category-usage`
  - `fig-overview-rating-distribution`
  - `fig-grm-category-response-functions`
  - `fig-grm-rater-information`
  - `fig-grm-information-shares` (optional MAIN)
  - `tbl-grm-information-summary`
- **Rule:**
  - Ranges are given over **all 19 retained raters**.
  - When an extreme comes from a rater with few ratings (R15–R19: 50–73 ratings; F0.5), name the rater, give the number of ratings and the SE, and say only that the estimate is imprecise.
  - No reading of these extremes in the Results.
- Bullets:
  - **Response styles** (@fig-overview-rater-response-styles; values in @tbl-overview-rater-response-styles [SUPP]; F0.8; raw scale, 3 decimals):
    - means from 1.760 (R06) to 3.836 (R18); if R09 is named (e.g., highest entropy, 1.903), its mean is 3.643;
    - SD from 1.022 (R01) to 1.953 (R19);
    - share of ratings in the lowest category (1) from .579 (R06) to .016 (R13); share in the highest category (7) highest for R19 (.080), while five raters gave no ratings of 7 (R01, R03, R06, R17, R18; consistent with Method 2.6);
    - share in the middle categories (3–5) highest for R13 (.799), followed by R18 (.764) and R12 (.735), and lowest for R06 (.192).
    - Close this paragraph with the sentence that the response styles have no per-rater uncertainty.
  - **Category use** (F0.6, F0.7): category 1 has 2,029 ratings, category 2 has 2,113, and category 7 is rarest (109). Quote counts only. Five raters left top categories unused.
  - **Thresholds** (@tbl-grm-rater-parameters; F2.2; 2 decimals):
    - b1 ranges from −6.56 (R18, 55 ratings, *SE* 3.05) to 0.29 (R06, *SE* 0.06). The next lowest is R13 at −3.38 (*SE* 0.49). R06 is the only rater with a positive b1.
    - Spacing differs, e.g., R02 from −0.71 (b1) to 2.03 (b6) vs R13 from −3.38 to 4.43. Add one clause: spacing is partly the same fact as discrimination (Method 2.7).
    - R17 has 4 thresholds; R01, R03, R06 and R18 have 5; the others have 6.
  - **Discrimination** (F2.1; 2 decimals):
    - a ranges from 0.63 (R18, 55 ratings, *SE* 0.26) to 3.71 (R19, 50 ratings, *SE* 2.22).
    - The second highest is R16 at 3.70 (52 ratings, *SE* 1.36). The second lowest is R09 at 0.86 (400 ratings, *SE* 0.15).
    - Examples from raters with many ratings: R01 1.96 (*SE* 0.16), R02 2.50 (*SE* 0.33), R06 2.81 (*SE* 0.42).
  - **Average information and share, with 95% intervals** (@tbl-grm-rater-information-ci; F2.4; information at 2 decimals, share at 3):
    - Information ranges from 0.12 [0.01, 0.35] (R18) to 3.54 [0.41, 11.02] (R19); R16 is 3.30 [0.73, 6.49].
    - Shares range from .005 [.000, .013] (R18) to .135 [.017, .331] (R19).
    - Examples from raters with many ratings: R09 0.24 [0.11, 0.42]; R01 0.98 [0.72, 1.22]; R02 1.70 [0.90, 2.56].
    - The widest information intervals belong to R19 and R16. R18's interval is narrow in absolute terms; do not group R18 with "the widest intervals".
  - **Where on θ raters inform** (F2.3; [SUPP]):
    - θ at maximum information is highest for R01 (2.700) and R06 (2.400), neither of whom used category 7 (F0.7; a factual juxtaposition with no causal wording), and lowest for R13 (−0.550).
    - Shares vary with θ, e.g., R06 .001 at θ = −2 vs .083 at θ = +2, and R12 .221 at θ = −2.
  - Move 3: the intervals use the same 200 accepted draws (Method 2.10).

**3.4 How much do the scores depend on modelling rater differences? (RQ3)**
- Findings: F1.1, F1.2, F1.4, F1.5, F1.11, F2.6, F2.7, F2.9, F2.10.
- Embed:
  - `tbl-raw-mean-vs-grm` [MAIN]
  - `fig-raw-mean-vs-theta` [MAIN]
  - `tbl-score-agreement` [MAIN]
- Cross-reference [SUPP]:
  - `tbl-lr-tests`
  - `tbl-discrimination-m3`
  - `tbl-threshold-order`
  - `tbl-rater-fit-m1`
  - `tbl-theta-correlations`
- Two ladder paragraphs: "ladder tests" and "ladder rater detail".
- **Paragraph A, ladder tests (RQ3a):**
  - **Shared category structure of M1 (rating-scale MFRM)** (F1.2): M1 vs M2, χ² = 737.457, df = 84, *p* < .001. The df and cross-software caveats are in Method 2.8.
  - **Equal discrimination** (F1.2, F1.1):
    - M2 vs M3, χ² = 121.958, df = 18, *p* < .001;
    - AIC favours M3 (23,767.020 vs 23,852.978); BIC ranks M2 (24,529.585) below M3 (24,555.360);
    - wording: "supported by the LR test and AIC, but not by BIC".
- **Paragraph B, ladder rater detail** (one sentence each):
  - M3 a ranges from 0.283 (R09, *SE* 0.055) to 2.606 (R16, *SE* 1.419) (F1.4);
  - unordered steps for 9 raters under M2 and 9 under M3 (F1.5);
  - under M1, only R17 (infit 1.328, outfit 1.190) and R18 (1.009, 1.071) are at or above 1, and R12 is lowest (0.238, 0.255) (F1.11).
- **RQ3(b), raw mean vs GRM** (@tbl-raw-mean-vs-grm, @fig-raw-mean-vs-theta; F2.9, F2.10). Use the three printed rows only, and lead with 1 and 2 ratings:

    | Ratings per product | products | Kendall's τ-b | pairs in reversed order | mean / max θ̂ range at equal raw mean |
    |---|---|---|---|---|
    | 1 | 897 | .832 | .042 | 1.283 / 1.436 |
    | 2 | 2,080 | .815 | .067 | 1.537 / 2.196 |
    | 3+ | 691 | .842 | .070 | 0.619 / 1.396 |

  - **1 rating:** τ-b = .832, and .042 of the pairs with different raw means are in reversed order. Products with the same single rating received GRM scores on average 1.283 and at most 1.436 apart. The 1-rating panel of the figure shows this vertical spread; points are jittered horizontally.
  - **2 ratings:** τ-b = .815; .067 in reversed order; θ̂ range mean 1.537, maximum 2.196.
  - **3+ ratings:** τ-b = .842; .070 in reversed order; θ̂ range mean 0.619, maximum 1.396.
  - Always give the mean range next to the maximum.
  - Descriptive sentence on the θ̂ range: it reflects differences in both the severity and the discrimination of the raters who gave the ratings. With 2 or more ratings, it also reflects the different rating combinations behind the same mean **[ATC-21]**. Do not call it severity evidence.
  - No pooled value; no trend claim across the groups; no test across groups exists.
- **RQ3(b), model choice** (@tbl-score-agreement; F2.7). **Separate paragraph.** Relative to the GRM:

    | model (as printed) | Pearson / Spearman | mean percentile shift | share changing quintile |
    |---|---|---|---|
    | M1 (rating-scale MFRM) | .975 / .978 | .042 | .202 |
    | M2 (partial-credit MFRM) | .985 / .983 | .033 | .150 |
    | M3 (GPCM) | .996 / .996 | .017 | .075 |

  - **Round 5 (m-9):** quote the mean percentile shift in the same sentence as each quintile-change share ("… .202 of products changed quintile under M1, with a mean percentile shift of .042"). The "≥ 2 quintiles" column (.004 / .003 / .001) may be left to the table. Never quote 0.000545256.
  - Ladder models among themselves: Pearson .980–.993, Spearman .983–.996; grid check 1.000 (F2.6).
- Move 3 (problems):
  - no CIs exist for any agreement statistic;
  - the M1–GRM contrast mixes the rater constraints with the link function;
  - all comparisons show that the scores differ, not which is more accurate.
- No closing interpretive sentence. **No comparison between the raw-mean table and `tbl-score-agreement`.**

**3.5 Sensitivity to the rater exclusion (2–3 sentences)**
- `tbl-sensitivity-rater-exclusion` [SUPP]; F2.8; 5 decimals as printed.
- Refitting with all 22 raters (7,844 ratings, 3,669 products):
  - empirical reliability .67199 → .67186;
  - model-based reliability .95986 → .96186.
- Over the 3,668 common products: θ̂ Pearson .99997; mean |Δθ̂| 0.00171, **max 0.16246**; share changing quintile .00491. Spearman .99996 may be left to the table.
- Over the 19 common raters: a Pearson .99880, max |Δa| 0.19820.
- No evaluative adjective in the Results.

### 4 Discussion

Purpose: interpret, map to the literature, and draw the implications for sport science. The section mirrors the three aims (writing-models/discussion-conclusion.md). **Every interpretive claim is [ATC].** Use "in these data" and "for this rater pool"; never "we have shown". The sparse design appears only in the Limitations. Keep the markers lean: one ATC per paragraph where the same claim recurs.

**4.1 Summary (1 paragraph).** Echo RQ1–RQ3 descriptively:
- the reliability of the obtained scores is below the full-panel value, and product-level reliability is lower for products with fewer ratings;
- raters differ, with imprecise estimates for raters with few ratings;
- the shared category structure of M1 (rating-scale MFRM) is rejected; equal discrimination is rejected by LR and AIC but not by BIC;
- within each number of ratings, raw means and GRM scores order products partly differently (quote τ-b; if "non-trivial share" is used, add **[AUTHOR TO CONFIRM; ATC-22]**).
- Mention the retained GRM in one clause.

**4.2 Reliability and the number of ratings per action (aim 1) [ATC-3, ATC-4, ATC-5, ATC-13]**
- Conventional figures describe the mean of a large or complete panel (.960; pairwise α .928). The scores actually obtained have .672 [.649, .687], and that is the figure that matters for any downstream use [ATC-3].
- Observed product-level reliability (F1.14): actions with one rating had mean rel_post .520, and actions with two had .698. Where individual action scores are used (e.g., to select creative actions), one or two ratings per action give limited precision in these data [ATC-5].
  - These are observed values, not a design experiment (Results 3.2). Do not add a rater-composition claim here.
- Precision also differs among products with the same number of ratings, and with their location on θ (@fig-grm-rel-post-by-n, F1.17, F2.3) [ATC-4]. Do not say "mainly".
- **Projection, side note only (1–2 sentences; SUPP objects):**
  - "A simple projection from the fitted GRM, with raters drawn at random from this panel (each rater equally likely) and the parameters treated as known, gives an empirical reliability of .508 for one rating, .688 for two and .925 for ten ratings per product (@tbl-grm-reliability-projection, @fig-grm-reliability-projection in the supplement)."
  - Optionally add a half-sentence: it gauges the value of adding ratings in this rater pool [ATC-5].
  - **Nothing more:** no comparison with the observed values, no rater sets, no "needed k", no "who rates" claim. Besides this note, only the one-sentence Method pointer (2.10) mentions the projection.
- Literature:
  - Spearman–Brown (amabile1982);
  - kaufman2008a: a high α can hide low single-rater agreement, illustrated by Krippendorff .392 vs Cronbach .928 [ATC-13; FI-17 "mask"];
  - cseh2019, **same paraphrase as P4**: "the number of raters needed for adequate reliability has to be established for each domain"; these data give such values for this task and rater pool, hedged with ATC-2.
- The crossed-block α (.658, 3 raters) lies close to the empirical reliability. Cautious; no claim of equivalence [ATC-13].
- rel_post with one or two ratings partly reflects the prior (Method 2.10).

**4.3 Raters differ (aim 2) [ATC-6, ATC-12]**
- The raters span a wide range of category use, threshold location and discrimination. For raters with many ratings, the differences clearly exceed the SEs (e.g., R09 0.86, *SE* 0.15, vs R06 2.81, *SE* 0.42) [ATC-6].
- **Round 5 (m-8):** "The most extreme estimates (R18, R19, R16) come from raters with about 50 ratings, which also had the largest standard errors (R18 for its thresholds, R19 and R16 for their discriminations); R19 and R16 also have the widest information intervals." Do not say R18 has a large discrimination SE or a wide information interval. Information shares are not a ranking of rater quality [ATC-12].
- Threshold spacing is partly discrimination, so the raw response styles (F0.8, @tbl-overview-rater-response-styles) carry the model-independent scale-use evidence (unadjusted for which products each rater saw).
- Literature:
  - long2015;
  - engelhard1994; myford2003; myford2004;
  - myszkowski2021 (central tendency vs extreme responding) [FI-17];
  - primi2019 left response styles / rater-by-scale interactions to future work [FI-17];
  - wind2018 and wind2019 (Wind & Jones; rater estimates depend on the linking set) [FI-17]; reise1990 (GRM parameter recovery) [FI-17]; ceh2022.
- The draw intervals are conditional on valid draws (Method 2.10).

**4.4 Why rater differences matter for scoring (aim 3) [ATC-7, ATC-8, ATC-9, ATC-10, ATC-15, ATC-21, ATC-22]**
- **(i) Raw means and rater differences** [ATC-7, ATC-21]:
  - Unweighted means treat raters as interchangeable, and with incomplete designs they are confounded with rater severity (primi2019).
  - In these data, products with the same single rating received GRM scores on average 1.283 and up to 1.436 apart (F2.9; @fig-raw-mean-vs-theta). With one rating, a product's GRM score depends only on the rating and on that rater's parameters, so the spread reflects differences between raters as modelled, **in both severity and discrimination**.
  - As a range, it is set by the most extreme raters for each rating, some of whose parameters are imprecise (R18, R19).
  - Write this as the authors' own claim. Severity on its own was not tested (Method 2.8).
- **(ii) Category structure and discrimination (N3-M1)** [ATC-7, ATC-8, ATC-9]:
  - The LR test rejects the shared category structure, but that result concerns M1 (rating-scale MFRM). M2 (partial-credit MFRM) already allows rater-specific category structures (eckes2015).
  - The Rasch/MFRM family as a whole is questioned only by the discrimination result: rater-specific discriminations are supported by LR and AIC but not by BIC (F1.1, F1.2). Part of the discrimination spread may be estimation noise for raters with few ratings. These results bear on the Rasch/MFRM constraints, not directly on raw means.
  - The M1 misfit pattern is consistent with discrimination differences surfacing as misfit (myford2004; myszkowski2021): R17 is above 1 under M1 and has GRM a 1.45; R12 has the lowest M1 values and GRM a 2.90 (F1.11, F2.1). Cautious; no cut-offs [ATC-9].
  - The GRM is preferred by information criteria; a cumulative link is plausible for a unipolar scale (pellegrino2025 [FI-17]) [ATC-8]. Neither the unordered M2/M3 steps nor the ordered GRM thresholds count as evidence for either family.
- **(iii) Score consequences**, two separate paragraphs [ATC-10, ATC-22]:
  - **Raw mean vs GRM**, within the same number of ratings: τ-b .832 (1 rating) and .815 (2 ratings), with .042 and .067 of pairs reversed (F2.9). This matters wherever actions are selected or ranked [ATC-22].
    - With two ratings, the GRM score also depends on the pattern of the ratings, not only their mean, so some of the .067 reversals would occur even among identical raters; the one-rating value (.042) is the one that reflects rater differences alone (as modelled).
    - "These results agree with primi2019 and myszkowski2019 on the limits of averaging" belongs in this paragraph.
  - **Model choice (round 5, m-9):** correlations ≥ .975, yet .202 of products change quintile under M1 (rating-scale MFRM; mean percentile shift .042) and .075 under M3 (GPCM; mean percentile shift .017) (F2.7). A quintile change can also be a small move across a boundary, which is why the mean shift is given alongside. The link-function confound stays explicit [ATC-10].
  - Do not rank the two comparisons against each other.
  - **Limit (C-M1):** the GRM is not a validated criterion. It adjusts for the modelled rater differences; whether it predicts unseen ratings better was not examined [ATC-15, ATC-22]. All scoring recommendations (4.5 box item 5, Conclusion, abstract) must stay consistent with this sentence.

**4.5 Practical implications for sport science [ATC-5, ATC-14, ATC-15, ATC-16, ATC-23]**
- Scope sentence first: one pool of student raters, one 7-point scale [FI-21].
- **Keep this subsection short and let the box carry the list.** The paragraphs add only:
  - **the calibration set vs rater training distinction (round 5, m-10, unambiguous referent):** "A common calibration set is distinct from rater training; training, unlike a calibration set, conflicts with the CAT rule that raters judge without criteria (hennessey2011; storme2014; dollinger2005)." A calibration set stabilises the parameters of raters with few ratings **only if they rate it and it is large enough** [ATC-14]. No sentence-initial or trailing "which" that could refer to either.
  - "about 50 ratings per rater still left the parameters imprecise in these data" (F2.1, F2.4). **No "15", and no other number declared sufficient** [ATC-16].
- **Box "Design recommendations for creativity ratings in sport"** (OD6; every item **[AUTHOR TO CONFIRM; ATC-23]**; all items rest on observed findings; no numbers except "about 50"):
  1. Report the reliability of the scores actually used (empirical marginal reliability, product SEs), not only α or full-panel values (@tbl-reliability-overview) [ATC-3, ATC-15].
  2. Plan the number of ratings per action with the precision of individual scores in mind; in these data, product-level reliability was markedly lower for actions with one or two ratings (@tbl-grm-reliability-by-n) [ATC-5].
  3. Where some raters contribute few ratings, let all raters rate a common calibration set, so that raters are more strongly linked and their parameters more precisely estimated (the design was already connected) [ATC-14].
  4. Give each rater enough ratings for stable parameters; about 50 ratings still left them imprecise here [ATC-16].
  5. **(C-M1)** Raters differed in thresholds and discrimination, and raw means ordered actions partly differently from model-based scores (@tbl-raw-mean-vs-grm). Consider scoring actions with a model that adjusts for rater differences (under its assumptions), and report how far its ordering departs from the raw mean. This study does not show that the model-based scores are more accurate [ATC-15, ATC-22].
  - The projection may be mentioned at most as a parenthetical in item 2 ("a simple projection is given in the supplement"); it is optional.
  - Whether CRJ accepts boxes is FI-16. If it does not, the five items become one paragraph.

**4.6 Limitations and future research**
- L1. **Design and missingness.**
  - The design is incomplete, and allocation is described in Method 2.5 [FI-4]. Missingness is assumed ignorable.
  - "Not recognised" ratings were removed; if non-recognition depended on the action or the rater, the missingness is not ignorable [FI-22].
  - The by-n reliabilities are observational.
- L2. **Fit evidence is limited** [ATC-11]: S-X² power, C2 not computable, Q3 bias and no reference distribution, infit/outfit below 1 by construction. Absence of detected misfit is not evidence of fit. The GRM is the best-fitting of the compared models, not a validated reference.
- L3. **Uncertainty and assumptions.**
  - Parameters of raters with few ratings are imprecise, and the draw intervals are conditional on valid draws.
  - θ ~ N(0, 1) is assumed, while ratings concentrate at the low end (F0.6).
  - The raw response styles have no uncertainty.
  - No CIs exist for the score-agreement and raw-mean statistics.
- L4. **Rater pool.** One pool of student raters [FI-1, FI-21]. Whether they meet the CAT's domain-familiarity requirement is not established here. Expertise is not analysed (kaufman2009; kaufman2013; ceh2022).
- L5. **Rater exclusion.** The 15-rating criterion is technical [FI-23]. The largest change in a product score was 0.16246 [ATC-26].
- L6. **Model comparison.** The M1–M2 LR test (rating-scale vs partial-credit MFRM) is cross-software, with df below the formula value; BIC disagrees with LR/AIC on discrimination, which is the only constraint common to the Rasch family; the M1–GRM agreement mixes constraints and link function.
- L7. **Two facets, one dimension.** No time or session facet (barth2021; leckie2011; myford2009; forthmann2017; timespan in Method 2.4 [FI-3]). No differential rater functioning (wind2019a, Wind & Sebok-Syer). Extensions: patz2002; uto2020.
- **Future research: one short list**, introduced as analyses "beyond the scope of this descriptive study":
  - a formal test of rater severity on its own (a model without rater effects vs the MFRM);
  - the M1–M2 comparison within one software package;
  - a held-out predictive check of model-based vs raw-mean scores;
  - projections that include parameter uncertainty or use selected rater sets;
  - the number of ratings needed for a target reliability.
  - Plus substantive directions: a prospective anchor-set design, rater covariates including football expertise, other sports.
  - Keep the list to one sentence or a compact list; do not elaborate.

### 5 Conclusion (1 paragraph) [ATC-1]

- In these data:
  1. the reliability of the obtained scores is far below conventional panel figures, and product-level reliability is lower for actions with fewer ratings;
  2. raters differ in category use, threshold location, discrimination and information;
  3. the shared category structure of M1 (rating-scale MFRM) is rejected, equal discrimination is rejected by LR and AIC but not by BIC, and both raw means and constrained models order actions differently from the GRM.
- End with the design and scoring message, scoped to this kind of rater pool (C-M1):
  - report the reliability of the scores used;
  - plan ratings per action;
  - where rater parameters are imprecise, consider linking raters through a calibration set;
  - because raters differ and the ordering depends on whether their differences are modelled, consider model-based scoring such as JRT and report how far it departs from raw means [ATC-5, ATC-14, ATC-15].
- No projection. Do not write "We have shown". No accuracy claim for the GRM.

### References

APA 7th via CSL; citekeys only; **`phd_library.bib` only** (author-maintained; not edited by the pipeline).

---

## Bibliography check (round 5)

- **Keys unchanged.** All outline keys were checked against `phd_library.bib` in round 4 and resolve; the author has since fixed the entries. No key is added, removed or swapped in round 5. The writer does not edit the bib.
- **Hand-written names keep particles with the surname:** ayala2022 "de Ayala"; hove2024 "ten Hove, Jorgensen, and van der Ark"; joode2023 "de Joode, van der Kamp, and Savelsbergh"; safardilha2019 "de Sa Fardilha". This applies only to names typed in the prose (e.g., "ten Hove et al. (2024) …" written by hand); citations generated from keys are left to the CSL.
- **linacre1989** = the MESA Press book *Many-facet Rasch measurement*. Any prose that says "Many-faceted" becomes "many-facet".

| Key | Entry | Use in outline |
|---|---|---|
| kaufman2008 | Kaufman, Plucker & Baer (2008), *Essentials of Creativity Assessment* (book) | "five to ten raters" (P4) |
| kaufman2008a | Kaufman, Baer, Cole & Sexton (2008), CRJ | α > .70 (P3); high α can mask low agreement (P4, 4.2) [FI-17] |
| wind2019 / wind2019a | Wind & Jones (2019) / Wind & Sebok-Syer (2019) | linking set (4.3) / DRF (L7) |
| forthmann2025 | Forthmann, Goecke & Beaty (2025) | product-level precision (P4) |
| ayala2022 | de Ayala (2022) | IRT basics (P6) |
| joode2023 | de Joode, van der Kamp & Savelsbergh (2023) | sport product ratings (P7) |
| hove2024 | ten Hove, Jorgensen & van der Ark (2024) | optional: indices in incomplete designs (2.10 lead sentence) |
| linacre1989 | Linacre (1989), *Many-facet Rasch measurement* (MESA Press) | MFRM severity facet (P6, 2.7) |

---

## Figure/table plan (round 5)

**10 main-text objects (8 tables, 2 figures)**, plus 1 optional main figure (counted in the supplement). **28 supplement objects (17 tables, 11 figures).** **5 not embedded.** Total 43.

Supplement numbering S1, S2, …: crossref prefix setting (paper-config, not a writer edit).

### Main text (10)

| # | Label | Section | Role |
|---|---|---|---|
| 1 | `tbl-design-summary` | 2.6 | Final data; single place for the design numbers (Table 1) |
| 2 | `tbl-model-fit` | 3.1 | Model choice (Table 2) |
| 3 | `tbl-reliability-overview` | 3.2 | RQ1: obtained scores vs full panel vs conventional indices (Table 3) |
| 4 | `tbl-grm-reliability-by-n` | 3.2 | RQ1: observed product-level reliability by number of ratings (Table 4) |
| 5 | `fig-overview-rater-response-styles` | 3.3 | RQ2: raw response styles (Figure 1) |
| 6 | `tbl-grm-rater-parameters` | 3.3 | RQ2: a and b_k as "estimate (SE)" (Table 5) |
| 7 | `tbl-grm-rater-information-ci` | 3.3 | RQ2: average information and share with 95% intervals (Table 6) |
| 8 | `tbl-raw-mean-vs-grm` | 3.4 | RQ3(b): raw mean vs GRM, rows 1 / 2 / 3+ (Table 7) |
| 9 | `fig-raw-mean-vs-theta` | 3.4 | RQ3(b): spread of GRM scores at equal raw mean (Figure 2) |
| 10 | `tbl-score-agreement` | 3.4 | RQ3(b): ranking change by model choice (Table 8) |

Optional MAIN (author's choice): `fig-grm-information-shares`; also `fig-grm-rel-post-by-n` if the author prefers a figure alongside, or instead of, the by-n table. If a figure is promoted, MAIN becomes 11 and SUPP 27.

### Placement decisions

- **`tbl-overview-rater-response-styles` → SUPP (new, round 5; F0.8).** Justification:
  - its job is traceability (review m-6): every per-rater response-style value quoted in Method 2.11, Results 3.3 and the abstract (.579/.016, .080, .799/.764/.735/.192, the means and SDs) now points to an embedded object;
  - the main-text figure `fig-overview-rater-response-styles` already shows the pattern (means, SDs, categories used, extreme vs middle shares), so the table would duplicate it in the main text;
  - it is a 19 × 12 table of unadjusted descriptives without uncertainty; the main text already carries 8 tables, and the model-based rater evidence (Tables 5 and 6) is the paper's focus;
  - Results 3.3 cites it at the first quoted lowest/highest/middle share ("values in @tbl-overview-rater-response-styles"); the abstract value is traceable through it (no cross-reference in the abstract itself).
  - If the author prefers it in the main text, swap it for the figure rather than adding it (MAIN stays 10).
- `tbl-grm-reliability-by-n` → MAIN (RQ1 evidence, with product counts per row).
- `fig-grm-rel-post-by-n` → SUPP; cited in 3.2 for the spread within the same number of ratings.
- `fig-grm-reliability-projection` and `tbl-grm-reliability-projection` → SUPP, cited in the one-sentence Method 2.10 pointer and the Discussion side note. The supplement note under the table carries the procedure:
  - θ ~ N(0, 1) simulated products;
  - k raters drawn at random from the panel, each rater equally likely (also in the table caption);
  - ratings generated from the fitted GRM;
  - parameters treated as known;
  - 50 replications of 2,000 products per k; seed 20260713.
- Unchanged:
  - `tbl-score-agreement` MAIN; `tbl-theta-correlations` SUPP;
  - `tbl-raw-mean-vs-grm` and `fig-raw-mean-vs-theta` MAIN (the figure moves to SUPP first if space is tight);
  - `tbl-grm-rater-information-ci` MAIN; `tbl-grm-information-summary` SUPP;
  - `tbl-lr-tests` SUPP (values quoted);
  - `tbl-sensitivity-rater-exclusion` SUPP.

### Supplement (28)

- **Tables (17):**
  - `tbl-overview-rater-response-styles` (**new**; place first among the rater tables, before `tbl-category-usage`)
  - `tbl-excluded-raters`
  - `tbl-sensitivity-rater-exclusion`
  - `tbl-category-usage`
  - `tbl-grm-convergence`
  - `tbl-grm-rater-fit`
  - `tbl-grm-q3-flagged`
  - `tbl-grm-reliability-ci`
  - `tbl-grm-reliability-summary`
  - `tbl-naive-indices`
  - `tbl-grm-reliability-projection`
  - `tbl-grm-information-summary`
  - `tbl-lr-tests`
  - `tbl-discrimination-m3`
  - `tbl-threshold-order`
  - `tbl-rater-fit-m1`
  - `tbl-theta-correlations`
- **Figures (11):**
  - `fig-grm-rel-post-by-n`
  - `fig-grm-reliability-projection`
  - `fig-overview-rating-distribution`
  - `fig-overview-degree-distributions`
  - `fig-grm-category-response-functions`
  - `fig-grm-rater-information`
  - `fig-grm-information-shares` (optional MAIN)
  - `fig-grm-panel-information`
  - `fig-grm-rel-post-histogram`
  - `fig-grm-rel-post-by-theta`
  - `fig-grm-rel-consistency`

### Not embedded (5)

- `tbl-cleaning-log`: the cleaning steps are in the Method text.
- `tbl-marginal-reliability-models`: open author option (review m19; the reviewer still recommends the supplement plus one sentence).
- `tbl-grm-global-fit`: Method 2.9 says the same.
- `tbl-overview-ratings-per-action`: duplicates `tbl-design-summary`.
- `fig-overview-rater-overlap`: a design display, not needed for the aims.

### Notes for the writer (round 5)

- Embeds and captions come from the notebooks at 04aefc5. One new embed: `{{< embed ../data-analysis/creativity-ratings-psychometrics/notebooks/01_data_overview.ipynb#tbl-overview-rater-response-styles >}}` in the supplement.
- Model names in prose follow the table cells (Terminology). Column names in prose follow the printed headers ("Ratings by rater", "Ratings per product", "Ratings (total)").
- Q3: state the computable-pair definition in Method 2.9; remove the FI-30 marker.
- R09's mean, if quoted: 3.643.
- **YAML (m-11):** set `number-sections: false` for the pdf format (APA headings are unnumbered). The section numbers in this outline are for orientation only.
- Abstract: no rendered markers; ≤ 250 words; conditional calibration wording.
- Bibliography: do not edit the bib; check hand-typed name particles and "many-facet".

---

## Effect sizes and uncertainty: inventory (04aefc5)

| Quantity | Uncertainty | Where |
|---|---|---|
| Empirical / model-based marginal reliability | 95% intervals from 200 accepted parameter draws (87 rejected); conditional on valid draws | F1.12 |
| Observed rel_post by n | Means and medians only; no CIs | F1.14 |
| Cronbach's α (pairwise; crossed block), Krippendorff's α | Bootstrap CIs; pairwise CI approximate (639 of 1,000 replications computable; 361 failed) | F1.18 |
| GRM a, b_k | Oakes SEs (2 decimals) | F2.1, F2.2 |
| Rater average information and share | 95% intervals (same draws) | F2.4 |
| M3 discriminations | SEs | F1.4 |
| Model comparison | Δ information criteria; LR χ², df, *p* < .001 | F1.1, F1.2 |
| θ correlations; score agreement | Point values; no CIs | F2.6, F2.7 |
| Raw mean vs GRM (1 / 2 / 3+) | Point values; no CIs | F2.9 |
| Exclusion sensitivity | Point differences; no CIs | F2.8 |
| Raw response styles | None | F0.8 (`tbl-overview-rater-response-styles`) |
| Projection (side note, SUPP) | 95% range over 50 simulation replications only; parameters treated as known | F1.20 |

---

## FILL IN items (14 open)

These are for the author. Any number must first pass through the notebook and results-interpreter.

- **FI-1** Raters and ethics: recruitment, number at start, consent, ethics approval. Also confirms "student raters" in the abstract (no rendered marker there).
- **FI-2** Products: competitions and matches, selection rule (event data), clip length and source, number of matches.
- **FI-3** Procedure: software; verbatim instruction and creativity definition; scale anchors; wording of the "not recognised" option; randomisation, sessions and breaks; data-collection timespan; other dimensions rated.
- **FI-4** Allocation of products to raters: planned overlap, benchmark/common set, randomisation, thesis subsets, dropout; how products came to have 1, 2 or 3+ ratings; whether products with different numbers of ratings were rated by different raters.
- **FI-6** Software versions (R, mirt, sirt, psych, Krippendorff package).
- **FI-9** Why R19, R14, R02, R16 and R12 were not usable for the pairwise Cronbach's α (and, optionally, the 3 raters in the crossed block).
- **FI-15** Preregistration status; data and code availability statement.
- **FI-16** CRJ requirements: abstract limit, keywords, word count, figure/table limits, supplement policy, boxes, heading format.
- **FI-17** Citation checks against the PDFs:
  - wef2025; safardilha2019; memmert2011; batey2012; barbot2019b;
  - kaufman2008 ("five to ten");
  - the α > .70 claim (baer2004; kaufman2008a; hennessey2011);
  - **new (round 5, m-2): kaufman2008a for "a high α from a large panel can mask low agreement among individual raters"** (P4, 4.2); if the CRJ article does not make the point, cite the source that does;
  - **new (round 5, m-7): cseh2019 for the single paraphrase "the number of raters needed for adequate reliability has to be established for each domain"**;
  - the kempe2018 / zahno2023 / joode2023 characterisation;
  - primi2019 and forthmann2025 as support for product-level precision (P4);
  - pellegrino2025 "retained a GRM";
  - primi2019 "left rater-by-scale interactions / response styles to future research"; myszkowski2021 on central vs extreme responding; the looney2004 / anderlucci2021 / heiniger2021 characterisation; wind2018 / wind2019 "rater estimates depend on the linking set"; reise1990 on GRM parameter recovery;
  - eckes2015 as the source for the partial-credit MFRM.
- **FI-18** Notebook display fixes before render (analyst; display only, no new analyses). **Fixed at 04aefc5:** model labels in table cells ("M1 (rating-scale MFRM)", "M2 (partial-credit MFRM)", "M3 (GPCM)"); "Ratings (n)" headers replaced; Q3 computable-pair note; per-rater response-style table labelled. **Still open:**
  - old model names outside the cells: `tbl-reliability-overview` row labels "M1 (RSM)" / "M2 (PCM)"; `tbl-threshold-order` caption "M2 (PCM) and M3 (GPCM)"; `tbl-model-fit` and `tbl-rater-fit-m1` captions "rating scale model / MFRM";
  - Quantity labels that still show code names ("min_ratings_per_rater (exclusion cut-off)", "empirical_marginal_reliability (primary; actual scores)", "model_based_marginal_reliability_mirt (hypothetical full panel)", "marginal_rxx (mirt)");
  - the "Overlap" column of `tbl-grm-q3-flagged` is "–" in every row (drop or fill);
  - integer display: the diagonal "1" vs "1.000" in `tbl-theta-correlations`; R08's mean "3" and the "0" shares in `tbl-overview-rater-response-styles`;
  - *p* values in scientific notation in tables (APA: *p* < .001);
  - separators missing in N2 text notes ("639 of 1000", "3668 common products");
  - figure fixes from round 2, to be verified: `fig-grm-panel-information`, `fig-grm-rel-consistency`, `fig-grm-rel-post-by-theta`;
  - optional: APA leading zeros in `tidy()`, so that tables match the text.
- **FI-19** Data status (internal; **never mentioned in the prose**). If more ratings are added before submission, re-run N0–N2, the embedder and the interpreter, and recopy every Results number. Otherwise the current data are final for this paper.
- **FI-21** Rater-pool description: number at start, football playing/coaching experience, instruction or practice, sessions per rater, demographics; if not recorded, say so.
- **FI-22** Rate of "action not recognised" ratings by rater, and if possible by product. Descriptive only.
- **FI-23** Source or rationale for the 15-rating exclusion criterion.

**Closed or retired:**
- **FI-30 closed (round 5):** the notebook now defines a computable Q3 pair (F1.9); the definition is stated in Method 2.9.
- **FI-11 and FI-12** (optional CIs for agreement statistics and per-n means) stay retired under the author priority. The absence of CIs is stated in L3.
- **FI-20** resolved in round 3; **FI-24 to FI-29** dropped in round 3.
- **Closed earlier:** FI-5, FI-7, FI-8, FI-10, FI-13, FI-14.

## AUTHOR TO CONFIRM claims (23 open)

Markers render in the body text only; the abstract carries none (its claims are covered by ATC-2, -5, -14, -15 and listed in the hidden comment block).

- **ATC-1** The central contribution: three empirical parts (obtained reliability and by-n; rater differences with uncertainty; score dependence on modelling rater differences).
- **ATC-2** The novelty claim: "to our knowledge, rater differences have not been modelled with IRT/JRT for creativity ratings in sport". It also covers the abstract's "little is known" sentence (no rendered marker there). The search was not systematic.
- **ATC-3** Conventional indices describe a panel mean, not the precision of the scores used. The empirical marginal reliability is the relevant figure.
- **ATC-4** Product precision depends on the number of ratings, on which raters gave them, and on the product's location on θ, all read from the observed spread. No "mainly".
- **ATC-5** Practical reading of the observed by-n values: one or two ratings per action give limited precision for individual action scores in these data, so plan ratings per action accordingly. It also covers the optional half-sentence on the projection side note.
- **ATC-6** Raters differ substantially; for raters with many ratings the differences exceed the SEs; spacing is partly discrimination. Also covers "higher thresholds indicate a stricter rater" and "threshold location (severity)" in RQ2, used only if the author confirms.
- **ATC-7** Raw means are confounded with severity in incomplete designs (primi2019). The shared category structure is rejected only for M1 (rating-scale MFRM); M2 (partial-credit MFRM) relaxes it. Equal discrimination, the constraint common to the Rasch family, is rejected by LR/AIC but not by BIC, and the spread is partly uncertain. Severity on its own is not tested.
- **ATC-8** The GRM is preferred by information criteria; a cumulative link suits the unipolar scale.
- **ATC-9** The M1 misfit pattern (R17, R12) is consistent with discrimination differences surfacing as misfit. Step order is not evidence for either family.
- **ATC-10** (round 5 wording) Model choice: high correlations, yet ranking shifts that matter for selection, read together with the mean percentile shifts (.042 for M1, .017 for M3). The M1–GRM contrast mixes constraints and link.
- **ATC-11** Fit evidence is limited by the design. The pairwise α CI may be biased. Absence of misfit is not evidence of fit.
- **ATC-12** (round 5 wording) Information shares are not a ranking of rater quality. The largest standard errors belong to R18 (thresholds) and to R19 and R16 (discriminations); the widest information intervals belong to R19 and R16, not R18.
- **ATC-13** The Krippendorff vs Cronbach contrast illustrates kaufman2008a (pending the FI-17 "mask" check). The crossed-block α lies near the empirical reliability.
- **ATC-14** (round 5 wording) Recommendation, conditional: because parameters of raters with few ratings were imprecise, consider a calibration set rated by all raters, distinct from training. It links raters more strongly and estimates parameters more precisely only if the raters with few ratings rate it and it is large enough. The study did not use such a set. Applies to the abstract, contribution implication, box item 3 and Conclusion.
- **ATC-15** (C-M1) Scoring recommendation: because raters differed in thresholds and discrimination and raw means ordered actions partly differently from model-based scores, *consider* a model that adjusts for rater differences (under its assumptions) and report how far its ordering departs from raw means. No claim that model-based scores are more accurate. Also covers: report the empirical reliability and product SEs.
- **ATC-16** Recommendation: enough ratings per rater for stable parameters (about 50 were not enough here); no claim that 15 suffices.
- **ATC-18** The realised design departs from the planned benchmark-set design (if so).
- **ATC-19** Showing raters a creativity definition departs from the CAT "no criteria" rule.
- **ATC-20** The exploratory framing and the RQ wording.
- **ATC-21** The θ̂ range at equal raw mean reflects differences in both severity and discrimination between raters. With 1 rating, it reflects only the rater's parameters; with 2+ ratings, it also reflects the rating combinations. As a range, it is set by the most extreme raters, some imprecisely estimated.
- **ATC-22** The interpretation of F2.9: within each number of ratings, raw means order products partly differently from GRM scores, which matters for selecting actions. With 2 ratings, part of the reversals reflects the rating pattern, not rater differences. Only within-n values are used; no comparison with F2.7. "Non-trivial share" is used only with this marker.
- **ATC-23** The boxed recommendations: selection and wording of all five items (item 3 made conditional in round 5).
- **ATC-26** Sensitivity claim: "excluding them changed the product scores only slightly", with a visible [AUTHOR TO CONFIRM] at the claim and the largest change (0.16246) in the same sentence.

**Closed:** ATC-24, ATC-25, ATC-27 (round 3); ATC-17 (earlier).

---

## Evidence gaps

- **Aim 1.**
  - Supported by the empirical reliability with CIs (F1.12), the observed by-n values (F1.14) and the conventional indices (F1.18).
  - Gaps:
    - the by-n values are observational, without CIs;
    - they do not separate the number of ratings from which raters gave the ratings; whether rater composition differs by number of ratings is not printed and depends on FI-4;
    - no "ratings needed" figure exists, so none is stated;
    - the projection is a side note with parameters treated as known.
- **Aim 2.**
  - Well supported for raters with many ratings (SEs, information intervals, response styles, now all in embedded objects).
  - Gaps:
    - there is no single comparable severity metric (thresholds only), so RQ2 does not promise "severity";
    - raters with about 50 ratings have imprecise parameters;
    - the draw intervals are conditional on valid draws;
    - the response styles are unadjusted and have no uncertainty.
- **Aim 3.**
  - Supported by the LR tests (F1.2), the score agreement (F2.7) and the within-n raw-mean comparison (F2.9, F2.10).
  - Gaps:
    - the shared-category-structure result concerns only M1 (rating-scale MFRM); the case against the Rasch family rests on equal discrimination, where BIC disagrees with LR/AIC;
    - severity is not tested on its own;
    - the M1–M2 LR test is cross-software;
    - there is no accuracy criterion for GRM vs raw means, so the scoring recommendation is worded as "consider";
    - no CIs exist;
    - the number of equal-raw-mean groups and pairs is not printed.
- **Calibration-set recommendation.** Not tested in these data (no such set was used); it rests on the imprecision of raters with few ratings and is therefore worded conditionally (ATC-14).
- **Absolute fit.** Not established: C2 is not computable, and S-X², Q3 and infit/outfit are limited by the design. The Q3 computable-pair definition is now in the notebook (FI-30 closed); the number of non-computable pairs is not printed.
- **Methods.** FI-1–FI-4, FI-6, FI-15, FI-21, FI-22 and FI-23 remain open. The paper cannot be submitted until they are filled.
- **Out of scope.** Rater expertise and the rating scale; MFRM fair averages (EAP only).

---

## Revision plan vs 05_review.md (round 4)

The round-3 plan was applied; the round-4 review rated it 17 resolved, 3 partial, 0 not resolved, 8 deferred, 5 declined, with 0 critical, 0 major and 11 minor new points. "Text" = the writer fixes it as planned above. "Author" = cannot be fixed in the text. "Analyst" = display only in the notebook.

| Point | Round-5 action | Where | Type |
|---|---|---|---|
| m-1 Abstract (length, calibration, markers, "student raters") | ≤ 250 words; calibration set conditional ("because … imprecise, consider"); no rendered markers (claims tracked as ATC-2/5/14/15, FI-1 in the hidden comment block) | Abstract; ATC-14; FI-1 | Text + author |
| m-2 kaufman2008a "mask" not on FI-17 | Added to FI-17 | P4, 4.2; FI-17 | Author |
| m-3 "Q3" as quartile | "first and third quartiles .596 and .769" | 3.2 (3); Terminology | Text |
| m-4 Table labels vs MFRM framing | Cells now print "M1 (rating-scale MFRM)", "M2 (partial-credit MFRM)", "M3 (GPCM)"; prose aligned; remaining captions/rows on FI-18 | Terminology; 2.7; 3.4; FI-18 | Text + analyst |
| m-5 Projection pointer in Methods | One description-only sentence at the end of 2.10 | 2.10 | Text |
| m-6 Response-style values not shown | `tbl-overview-rater-response-styles` embedded in SUPP and cited in 2.11 and 3.3 | 2.11; 3.3; object plan | Text |
| m-7 cseh2019 paraphrase | One wording in P4, P7 and 4.2; added to FI-17 | P4; P7; 4.2 | Text + author |
| m-8 R18 "largest SEs" | "R18 for its thresholds, R19 and R16 for their discriminations" | 4.3; ATC-12 | Text |
| m-9 Quintile shares without shift size | Mean percentile shifts (.042 / .017) in the same sentence | 3.4; 4.4 (iii); contribution 3; ATC-10 | Text |
| m-10 "which" referent; hove2024 placement | "training, unlike a calibration set, conflicts with …"; hove2024 moved to the lead sentence of the conventional-indices paragraph, or dropped | 4.5; 2.10 | Text |
| m-11 Heading numbering; "equivalent to" | `number-sections: false`; M1 "corresponds to" the rating-scale MFRM, estimated by MML | YAML; 2.7 | Text |
| m19 `tbl-marginal-reliability-models` | Still an open author option | — | Author |
| M12 Display problems | FI-18 updated to the remaining items | FI-18 | Analyst |
| C2, M7, M8, m10, m18, m20, m22 | Deferred to author (FI-1–4, 6, 15, 16, 18, 21, 22) | — | Author |
| N-M2, M3, M5, M6, held-out check | Declined under author priority; one future-research list | 4.6 | Declined |

---

## Changes in this update (round 5; notebooks at 04aefc5)

- **Inputs:** 43 labels (new `tbl-overview-rater-response-styles`); values unchanged; R09 mean 3.643 in the new table; model labels and Ratings headers changed in the tables; Q3 computable pair defined in the notebook.
- **New table:** `tbl-overview-rater-response-styles` → SUPP, mapped to F0.8, cited in 2.11, 3.3 and 4.3 and wherever lowest/highest/middle shares are quoted.
- **Q3:** definition stated in Method 2.9; FI-30 closed; markers removed in 2.9 and 3.1.
- **Naming:** prose model names follow the table cells; column references follow the new Ratings headers; "first and third quartiles"; response-style shares named as in the table.
- **Wording pass:** abstract (conditional calibration, no rendered markers, ≤ 250 words); Methods projection pointer; one cseh2019 paraphrase; R18 threshold SEs; mean percentile shifts next to quintile shares; "which" fixed and hove2024 moved; M1 "corresponds to" (MML); `number-sections: false`; name particles; "many-facet".
- **Bibliography:** not edited; keys unchanged.
- **Object plan:** MAIN 10, SUPP 27 → **28**, not embedded 5; total 43.
- **FILL IN:** 15 → **14 open** (FI-30 closed; FI-17 extended by kaufman2008a "mask" and cseh2019; FI-18 updated). **ATC:** **23 open** (unchanged count; ATC-2, -10, -12, -13, -14, -23 reworded).

## Decisions (applied; condensed record)

- **Checkpoint 1:** OD1 title kept; OD2 main-text objects; OD3 raw-mean comparison integrated; OD4 exclusion wording; OD5 3-decimal response styles; OD6 boxed recommendations; OD7 draft now. Exploratory framing; no sparse-design framing; "product" as the analytic term.
- **Checkpoint 2 (2026-10-26):** revision against the round-1 review; compact 2-decimal rater-parameter table; no "15 is enough"; Methods FILL INs kept; APA number format; ATC-26 with 0.16246.
- **Checkpoint 2, round 3 (2026-10-27):** empirical findings first; projection as a side note; no analyses added only to project or extrapolate; within-n raw-mean statistics; all-rater parameter ranges; the cause of the unrecognised ratings is author-supplied, with no marker.
- **Checkpoint 2, round 4 (2026-10-27, relayed):** apply the round-3 review fixes; re-ground "model rather than average"; rating-scale MFRM wording and BIC in the abstract; neutral Q3 wording; FI-11 and FI-12 retired; phd_library.bib as the single bibliography.
- **Checkpoint 2, round 5 (2026-10-27, relayed):** final wording pass; embed the response-style table; Q3 definition; model labels and Ratings headers aligned; writer wording items m-1 to m-11; bib not edited, name particles and "many-facet" in prose.

**Open for the author:**
- whether to promote `fig-grm-rel-post-by-n` or `fig-grm-information-shares` to MAIN, or swap `tbl-overview-rater-response-styles` for its figure in the main text;
- whether to embed `tbl-marginal-reliability-models` in the supplement (m19);
- whether to keep the box (FI-16);
- whether to use "stricter rater" / "threshold location (severity)" (ATC-6);
- whether to keep the abstract's mean-range clause (m21) and the hove2024 citation (m-10).
