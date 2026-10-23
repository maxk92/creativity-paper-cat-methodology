# 04_outline.md: Argument architecture (Phase 5), GRM/JRT version

Profile: `imrad-apa`. Venue: *Creativity Research Journal*. Style: APA 7th.
Structure: Abstract, Introduction, Method, Results, Discussion, Conclusion, References.
Sources:
- Brief: `~/drive/KNOWLEDGE/Paper_CreativityAssessmentInSportsCAT.md`
- Dossier: `01_dossier.md`
- Labels: `02_artifacts.md`
- Numbers: `03_findings.md` (F-IDs). This is the ONLY source of numbers.
- Citekeys: `06_web_literature.md`

This outline replaces the obsolete Bayesian outline completely.

Conventions in this file:
- **F…** is a finding ID in `03_findings.md`. Every number below is copied from there exactly.
- `tbl-…` and `fig-…` are labels from `02_artifacts.md`. **[MAIN]** means embedded in the main text. **[SUPP]** means embedded in the online supplement.
- **[ATC-n]** marks an interpretive or contribution claim that the author must confirm.
- **[FI-n]** marks a FILL IN item: information or an output that is missing and must come from the author or analyst. A FILL IN that needs a number is only usable after it has been added to a notebook and passed through results-interpreter.
- Values marked NOT IN NOTEBOOK in `03_findings.md` are never used.

---

## Working title

**Judge response theory for creativity ratings of football actions: Rater differences, model choice, and score reliability in a sparse consensual assessment design**

Alternatives (decision D1):
- (b) *How reliable are crowd-sourced creativity scores of football actions? A judge response theory analysis of a sparse rating design*. This uses a question form, which the title model discourages.
- (c) *Scoring consensual creativity ratings of football actions with judge response theory*

## Terminology (decision D2)

The proposal is to use **"product"** as the single analytic term, introduced once as "each rated product was a single football action".
- Reason: it matches the CAT literature (creative *products*), the main notebook N2 and every main-text label.
- "Action" stays only in the title and in the description of the stimulus material in Method ("football actions", "video clips of actions").
- Use **"rater"** throughout. Use "judge" only in the fixed term *judge response theory* (JRT) and in quotations.
- The supplement caption of `tbl-cleaning-log` (N0) says "actions". Harmonise it to "products" in the caption text (the label stays unchanged).

---

## Central contribution [ATC-1]

To our knowledge [ATC-2], this is the first IRT/JRT analysis of Consensual Assessment Technique (CAT) creativity ratings in sport. The data are 7,820 ratings of 3,668 football actions by 19 raters (F2.1).

The paper makes three contributions:
1. **Rater assumptions.** It shows that the Rasch-family assumptions about raters do not hold for these ratings. These are the assumptions behind the many-facet Rasch model (MFRM): a shared category structure and equal discrimination. The study tests them as a model ladder (RSM/MFRM → PCM → GPCM) and compares the result with a cumulative JRT graded response model (GRM), which information criteria prefer.
2. **Two kinds of reliability.** It separates two quantities that the CAT literature usually treats as one:
   - the reliability a *hypothetical full panel* or an *unweighted rater mean* would reach (model-based marginal reliability 0.960; pairwise Cronbach's α 0.928);
   - the reliability of the scores *actually obtained* from a sparse design in which a median product received 2 ratings (empirical marginal reliability 0.672).

   Single-rating agreement is low (Krippendorff's α 0.392, 95% CI [0.362, 0.417]). The precision of an individual product's score rises steadily with the number of ratings it received.
3. **Design over model.** Product scores correlate highly across all four scoring models. The main lever for better CAT scores in sport is therefore the rating *design*: ratings per product and rater linkage. The choice of scoring model matters much less. This yields concrete design recommendations for sport-science rating studies [ATC-12 to ATC-15].

## Core argument (3–5 sentences)

1. CAT reliability is conventionally reported as the consistency of a panel mean (Cronbach's α / Spearman–Brown). Such a coefficient can be high even when single raters agree poorly, and it says little about the precision of scores in the large, sparse designs that sport applications need (amabile1982; kaufman2008; cseh2019).
2. JRT treats raters as items with their own severity, scale use and discrimination (myszkowski2019; myszkowski2021). The assumptions that classical scoring and the MFRM impose (linacre1989; primi2019) thereby become testable. The football ratings reject a shared threshold structure and equal discrimination (F2.5), and a cumulative GRM fits best by information criteria (F2.4).
3. The fitted GRM makes the contrast between hypothetical and actual reliability explicit:
   - the full-panel reliability is 0.960;
   - the actual scores have an empirical marginal reliability of 0.672;
   - product-level reliability increases with ratings per product, from a mean of 0.520 at one rating to 0.698 at two (F2.14, F2.15).
4. Product scores are nearly interchangeable across models (Spearman 0.978–0.996 between the GRM and each ladder model; F2.20). For sport science, this argues for investing in design: an anchor set rated by all raters, and at least two ratings per product. Reliability should be reported for the scores actually used [ATC-3, ATC-4, ATC-6, ATC-12, ATC-13].

## Research questions and hypotheses

Decision D3: Were H1a, H1b and H2 formulated before the analysis (preregistration or analysis plan)? If not, the writer labels them as theory-derived expectations tested in an exploratory analysis, to avoid HARKing.

**RQ1: Rater assumptions and model choice.** Do the Rasch-family constraints on raters hold for CAT ratings of football actions? Which scoring model describes the ratings best?
- **H1a.** A model with rater-specific thresholds (PCM, M2) fits better than a model with a shared category structure (RSM/MFRM, M1).
  - Test: LR test. Result: X² = 737.457, df = 84, p < .001 (F2.5). Supported.
- **H1b.** A model with rater-specific discriminations (GPCM, M3) fits better than the PCM (M2).
  - Test: LR test. Result: X² = 121.958, df = 18, p < .001 (F2.5). Supported by the LR test. **However, BIC ranks M2 (24529.585) below M3 (24555.360) (F2.4).** The writer must report this disagreement.
- **RQ1c (exploratory, no directional hypothesis).** Does the cumulative GRM fit better than the best adjacent-category model? The two families are not nested, so the comparison uses AIC/BIC/SABIC only. Result: the GRM has the lowest AIC, BIC and SABIC of all four models (F2.4).

**RQ2: Rater behaviour (descriptive).** How do the raters differ in discrimination, threshold location and spacing, category use, and their contribution to test information? What is the uncertainty of these rater parameters?
- No hypothesis. Evidence: F2.3, F2.18, F2.19.

**RQ3: Score reliability in a sparse design.** How precise are the product scores actually obtained? How does their reliability compare with (a) the model-based full-panel reliability and (b) classical agreement and consistency indices?
- **H2.** The empirical marginal reliability of the actual GRM scores is lower than both the model-based full-panel reliability and the pairwise Cronbach's α of the rater mean.
  - Result: 0.672 vs 0.960 vs 0.928 (F2.14, F2.17). Supported. The writer must note that the full-panel value is an upper bound by construction (NB02 caveat), so H2 is partly definitional. Its value lies in the size of the gap.
- **H3.** Product-level reliability increases, and the posterior SD decreases, with the number of ratings per product.
  - Result: monotonic across n = 1…10 (F2.15). Supported descriptively. This is an observational comparison: products were not randomly assigned to a number of ratings [FI-4].

**RQ4: Model dependence of product scores.** How strongly do product scores (EAP estimates) depend on the scoring model?
- Expectation, not a formal test: high rank-order agreement. Evidence: F2.20 (correlations only; no rank-change statistics exist, see FI-13).

---

## Section outline

### Abstract (≈ 200–250 words, single paragraph, unstructured; check the CRJ limit [FI-18])

Purpose: a standalone summary that persuades CRJ and sport-science readers that the paper is useful. It follows abstract Model 2: background/aim → method → results with naked numbers → implications. It contains no citations.

- **Background/gap (1–2 sentences).** CAT ratings are the standard way to assess creative products. They are increasingly used for sport actions. Yet their psychometric properties, and the precision of scores from large sparse designs, have not been examined in sport.
- **Aim/method (1–2 sentences).** 19 raters gave 7,820 ratings of 3,668 football actions on a 7-point scale (F2.1). Judge response theory models were fitted by marginal maximum likelihood:
  - an adjacent-category ladder (RSM/MFRM, PCM, GPCM);
  - a graded response model.
- **Results (3–4 sentences, naked numbers):**
  - LR tests rejected shared thresholds and equal discrimination (both p < .001; F2.5).
  - The GRM had the lowest AIC/BIC/SABIC (F2.4).
  - Rater discrimination ranged from 0.631 to 3.709 (F2.18).
  - Empirical marginal reliability of the actual scores was 0.672, against 0.960 for a hypothetical full panel and Cronbach's α of 0.928. Krippendorff's α was 0.392 (F2.14, F2.17).
  - Product-level reliability rose from 0.520 (one rating) to 0.698 (two ratings) (F2.15).
  - Scores correlated ≥ 0.975 across models (Pearson range, F2.20).
- **Implications (1–2 sentences, hedged) [ATC-3, ATC-12, ATC-13].** Design choices, not model choice, govern score precision. Sport studies should use an anchor set and at least two ratings per product, and should report the reliability of the scores actually used.

### 1 Introduction

Purpose: narrow from the importance of creativity, to the CAT and its scoring, to the gap in sport, to the present study. Four moves (writing-models/introduction.md). Moves 1–3 have several paragraphs; move 4 is short.

**Move 1: Background and importance (1–2 paragraphs)**
- P1. Creativity is a core competence:
  - ranked among core workforce skills (worldeconomicforum2025; check the wording against the PDF [FI-20]);
  - assessed in PISA 2022 (oecd2024).
  - In sport, creativity is a developmental target for players (safardilha2019; santos2016).
- P2. The 4P taxonomy distinguishes person, process, product and press (batey2012). Each facet needs its own measurement approach (barbot2019b; barbot2019). This paper concerns the *product* facet: individual football actions rated by others.

**Move 2: Previous research (3–4 paragraphs, ordered from CAT, to its scoring, to rater models)**
- P3. **CAT procedure and reliability.**
  - The CAT is the established product measure (amabile1982; hennessey2011; kaufman2024).
  - Independent raters usually reach α > .70 (baer2004; kaufman2008; hennessey2011), but some studies report much lower agreement. This has been attributed to differences in procedure, scale use and beliefs about creativity (long2015; cseh2019).
- P4. **Reliability rests on panel size.**
  - Spearman–Brown reliability depends on both the mean inter-rater correlation and the number of raters (amabile1982). A large panel can therefore mask low single-rater agreement (kaufman2008).
  - The appropriate number of raters is domain-specific and cannot be set in general (cseh2019); compare the "5–10 judges" rule of thumb (kaufman2008a).
  - Set up the key distinction here, worded neutrally: such coefficients describe a full panel's mean. Large-scale studies, where each product is rated by only a few raters, need the precision of each product's score. This is the seed for RQ3.
- P5. **Creativity in sport.**
  - Research has focused on the creative process, such as divergent thinking (memmert2011).
  - Product ratings of actions exist: kempe2018 (trained experts, ICC; face validity via proximity to goals); memmert2007 (expert-rating scale for tactical creativity); zahno2023; dejoode2023. These studies report ICCs or agreement only.
  - In judged sports, Rasch/MFRM has been used to monitor judges of performance quality, not creativity (looney2004; anderlucci2021). A Rasch validation of a coach-completed creativity questionnaire exists (shin2025).
- P6. **From classical scores to JRT: successive relaxation of rater assumptions.** Condense the brief's paragraph, keeping its logic.
  - Means and α treat raters as (essentially) τ-equivalent (myszkowski2019). They are confounded with rater severity in incomplete designs (primi2019).
  - IRT basics: lord1980; embretson2013; deayala2022.
  - Rasch models and their polytomous extensions: rasch1960; bond2020; RSM andrich1978; PCM masters1982.
  - MFRM: linacre1989; eckes2015; rater effects engelhard1994, myford2003, myford2004; creativity application primi2019. The MFRM adds additive severity but keeps equal discrimination; unequal discrimination appears only as misfit (myford2004; myszkowski2021).
  - JRT treats raters as items with their own discrimination and thresholds: GPCM (muraki1992) or GRM (samejima1969) (myszkowski2019; myszkowski2021). Applications: barbot2023; pellegrino2025, which also retained a GRM; forthmann2023 on planned-missing rating designs.
  - Adjacent-category vs cumulative link, taken from the brief's "Methodological choices":
    - RSM/PCM/GPCM are nested, so their assumptions can be tested by LR.
    - The GRM is cumulative and arguably matches a cumulative rating scale [ATC-5]. It is not nested in the ladder, so the comparison uses information criteria.

**Move 3: Gap (1 paragraph, opened with "However")**
- P7. Three points:
  - (i) To our knowledge, no study has applied IRT/JRT to CAT creativity ratings of sport actions [ATC-2]. The search was not systematic, so the claim is phrased cautiously.
  - (ii) Sport studies therefore have no empirical basis for choosing a scoring model or for planning the rating design (cseh2019).
  - (iii) The reliability reported for CAT scores usually refers to a full panel's mean. The precision of scores from sparse, large-scale designs, which are needed for example to label thousands of actions, is rarely reported [ATC-3].

**Move 4: Present study (1 short paragraph)**
- P8.
  - Data: a large sparse CAT rating set of football actions (19 raters, 3,668 products, 7,820 ratings; F2.1).
  - State RQ1–RQ4 and H1a, H1b, H2, H3 (as above; wording depends on D3).
  - One sentence on the analytic route: model ladder plus GRM, MML in mirt; reliability contrast; model dependence.
  - Scope note: rater expertise and an experimental variation of panel size are *not* addressed (see Evidence gaps). The brief's aims should be narrowed to match [decision D10].

### 2 Method

Purpose: allow replication and justify the analytic choices. The section runs top-down (writing-models/methods.md): overview → precise details → relation to prior methods → problems encountered (move 4 used; the sparse design is the main one).

**2.1 Overview and study context (move 1)**
- One paragraph:
  - Ratings were collected as a CAT-style study: independent raters, relative judgements, randomised order (amabile1982; hennessey2011).
  - The products are football actions.
  - Data were collected as part of a larger project [FI-1, FI-2].
  - Ethics approval and consent [FI-1].
  - Preregistration status [FI-17].

**2.2 Raters (move 2)**
- Recruitment: Bachelor's and Master's students rating as part of thesis projects (vault background; the author must confirm and give the actual numbers) [FI-1].
- Demographics, football playing or coaching experience, compensation [FI-1]. If none were recorded, say so explicitly. This links to limitation L4.
- Final number of raters: 19 (F2.1). Ratings per rater ranged from 50 to 1174 (F2.1).
- Pseudonyms R01–R19.

**2.3 Products and stimulus material (move 2)**
- Source of matches and competitions, how actions were selected (event data), clip length, number of matches [FI-2]. The vault describes FIFA, AFCON, UEFA and Copa América matches with StatsBomb events; the author must confirm.

**2.4 Rating procedure (move 2 and move 3)**
- Rating software [FI-3].
- Instruction and definition of creativity shown to raters (originality × functionality in game context; runco2012) [FI-3].
- Note the departure from the "no criteria" CAT rule, citing hennessey2011, and relate it to trained-rater sport studies (kempe2018; memmert2007) [ATC-19].
- 7-point unipolar scale: 1 = not at all creative, 4 = somewhat creative, 7 = very/extremely creative [FI-3 confirm anchors]. Plus an off-scale "action not recognised" option.
- Randomised order; session length and breaks; data-collection period [FI-3].
- Whether other dimensions (technical correctness, aesthetic appeal) were rated, and that they are not analysed here [FI-3].

**2.5 Rating design and allocation (move 2 and move 4)**
- How products were allocated to raters: planned overlap, benchmark set, randomisation [FI-4]. This is needed to argue that missingness is ignorable for MML.
- The vault plan mentions a benchmark set rated by all raters. The realised design has no fully crossed block beyond 3 raters × 139 products (F2.17). State whether the plan was changed [ATC-18].

**2.6 Data preparation and final data set (move 2 and move 4)**
- Cleaning (F0.2; `tbl-cleaning-log` [SUPP]):
  - 9148 raw rows;
  - 1290 "not recognised" ratings removed;
  - 1 out-of-range value removed (rating 0.0 by R04; F0.3);
  - 13 rows removed when resolving duplicate rater–product pairs (12 pairs, 1 with conflicting values; "keep last"; F0.4);
  - result: 7844 rows.
  - Give the exact wording of the cleaning rule for "not recognised" (off-scale option, treated as missing).
- **Bridge sentence (required, because `tbl-cleaning-log` ends before the exclusion):**
  - Bridge text: "After cleaning (7844 ratings; @tbl-cleaning-log), raters who had given fewer than 15 ratings were excluded (R20: 13, R21: 9, R22: 2; 24 ratings; @tbl-excluded-raters). One product rated only by them was dropped as well."
  - Source: F2.1, F2.2.
  - The rationale must be confirmed: their rater parameters are not identifiable with so few ratings [ATC-16]. The diagnostic values from the 22-rater run are NOT IN NOTEBOOK and must not be quoted [FI-6].
  - Exclusion sensitivity: [FI-7 / ATC-17] placeholder, see the FILL IN list. Include it only if added to a notebook. Otherwise state that a sensitivity analysis was not reported, or omit it.
- **Final data (F2.1; `tbl-design-summary` [MAIN]):**
  - 7820 ratings of 3668 products by 19 raters; scale 1–7, coded 0–6 internally.
  - Ratings per product: mean 2.1319520174482, median 2, min 1, max 10, harmonic mean 1.72615922960609; 897 products had a single rating. The writer should report the long decimals as printed or use the table's display; no rounding by the writer unless the table displays it rounded.
  - Matrix fill 0.112208000918326.
  - One connected component.
  - 17 of 171 rater pairs share no product; median pairwise overlap 13.
  - 5 raters did not use all categories (no internal gaps) (F2.3; `tbl-category-usage` [SUPP]): category 7 unused by R01, R03, R06 and R18; categories 6–7 unused by R17. Consequence: these raters have fewer thresholds.
- Post-exclusion descriptives (overall category distribution, rater response styles) are **not available** [FI-15]. Do not embed the NB01 objects (pre-exclusion, 22 raters).

**2.7 Measurement models (move 2 and move 3)**
- Common frame (JRT):
  - raters are items, products are persons, with a unidimensional latent creativity θ ~ N(0, 1) (myszkowski2019; myszkowski2021).
  - Severity is the threshold location; scale use is the threshold spacing; discrimination is a.
- Adjacent-category ladder:
  - M1: RSM (andrich1978), equivalent to a two-facet MFRM (linacre1989; eckes2015; primi2019). Estimated with sirt::rm.facets (robitzsch2025).
  - M2: PCM, rater-specific thresholds (masters1982).
  - M3: GPCM, rater-specific thresholds and discriminations (muraki1992).
  - M2 and M3 are estimated in mirt (chalmers2012).
- Central model: a GRM with rater-specific discriminations and thresholds (samejima1969), in mirt. Its thresholds are ordered by construction (F2.6 note).
- Estimation of the GRM (F2.9):
  - MML via EM, 61 fixed quadrature points;
  - standard errors from Oakes' identity (chalmers2018);
  - converged after 165 iterations, information matrix positive definite (F2.9; `tbl-grm-convergence` [SUPP]).
  - Convergence tolerance [FI-9]. It prints as 0.000; do not quote it.
- Problem statement (move 4): raters with unused end categories have fewer thresholds (F2.3, F2.18). The writer explains how this was handled. The df consequence is covered in 2.8.

**2.8 Model comparison (move 2)**
- LR tests within the nested ladder: M1 vs M2 (rater-specific thresholds) and M2 vs M3 (rater-specific discriminations).
- AIC, BIC and SABIC for all four models. GRM vs ladder by information criteria only, because the families are not nested (F2.4 caveat).
- Problems to state:
  - M1 vs M2 is a cross-software comparison (sirt vs mirt).
  - Its df (84) differ from the formula value (90) [FI-8: explanation and software cross-check must be added to the notebook or stated as a method description without numbers].
- Report p-values as p < .001 (exact values not available).

**2.9 Model fit (move 2 and move 4)**
- Rater infit/outfit mean squares (wright1982), for M1 and the GRM.
- S-X² rater fit (orlando2000; kang2008). It needs complete data, so missing ratings were multiply imputed (20 imputations; F2.11). Problem: about 90% of cells are imputed (matrix fill 0.112; F2.1), which makes the test conservative (NB02 caveat).
- Local dependence: Yen's Q3 (yen1984). Q3 is negatively biased with few raters per product (christensen2017), so pairs are ranked by deviation from the mean Q3, among pairs with ≥ 30 common products (F2.12).
- Limited-information global fit C2 (cai2014) was attempted. State in the text that it could not be computed for this design. Do not embed `tbl-grm-global-fit`, because it contains an R error string. The cause is not documented in the notebook [FI-19].

**2.10 Scores, reliability and information (move 2)**
- Product scores: EAP estimates θ̂ with posterior SD (PSD) as the conditional standard error.
- **Empirical marginal reliability** (primary): Var(θ̂) / (Var(θ̂) + mean PSD²). It refers to the actual scores.
- **Model-based marginal reliability** (green1984; mirt marginal_rxx): reliability for a hypothetical product rated by all raters (upper bound). A grid computation serves as a check.
- **Product-level reliability:**
  - rel_post = 1 − PSD²;
  - rel_info = the information of the product's own raters at θ̂, I/(I + 1). Consistency check between the two.
- Rater information functions, integrated over N(0, 1). Each rater's share of full-panel information, weighted and at selected θ.
- **Classical comparison indices:**
  - Cronbach's α (cronbach1951), computed (a) from pairwise covariances with all usable raters and (b) on the largest fully crossed block. State why 5 raters were removed for the pairwise version [FI-16].
  - Krippendorff's ordinal α (hayes2007) with a 95% bootstrap CI over products (1000 replications).
  - State what each index refers to (tbl-reliability-overview's "refers_to" column): consensus of single ratings vs consistency of the unweighted rater mean.
  - Optionally cite tenhove2024 on reliability indices in incomplete designs.

**2.11 Model dependence and sensitivity (move 2)**
- Pearson and Spearman correlations of EAP estimates between all model pairs.
- Integration-grid check for M1 (fine grid vs sirt default grid).

**2.12 Software and availability (move 2)**
- R version; versions of mirt, sirt, psych and the Krippendorff package; Python for display [FI-9].
- Data/code availability statement, with pseudonymised rater IDs only [FI-17; see privacy item D11].

### 3 Results

Purpose: describe, not interpret. The section uses the four moves of writing-models/results.md: (1) revisit the aim and give an overview, (2) invite the reader to the objects and give key results, (3) state problems openly, (4) one hedged pointer to implications at the end of each subsection at most. Statistics follow APA style: p < .001, values as displayed. The subsection order follows RQ1 → fit check → RQ2 → RQ3 → RQ4.

**3.0 Overview (1 short paragraph, move 1)**
- Echo the aim. All analyses use the final data in @tbl-design-summary (F2.1).
- Give the overall picture in one sentence. The writer must keep it descriptive:
  - constraints rejected;
  - the GRM lowest on information criteria;
  - a large gap between full-panel and empirical reliability;
  - high agreement of scores across models.

**3.1 Model comparison (RQ1, H1a, H1b, RQ1c)**
- Findings: F2.4, F2.5, F2.6, F2.7, F2.8.
- Embed:
  - `tbl-model-fit` [MAIN]
  - `tbl-lr-tests` [MAIN]
- Cross-reference only:
  - `tbl-threshold-order` [SUPP]
  - `tbl-discrimination-m3` [SUPP]
  - `tbl-rater-fit-m1` [SUPP]
- Bullets:
  - Invite the reader to @tbl-model-fit. Report logLik, npar, AIC, BIC and SABIC for M1, M2, M3 and the GRM (F2.4).
  - H1a: M1 vs M2: X² = 737.457, df = 84, p < .001. H1b: M2 vs M3: X² = 121.958, df = 18, p < .001 (F2.5; @tbl-lr-tests).
  - RQ1c:
    - The GRM has the lowest AIC (23720.455), BIC (24508.795) and SABIC (24105.251).
    - The GRM and M3 have the same number of parameters (127), so the comparison reduces to logLik: −11733.227 vs −11756.510 (F2.4).
  - Move 3 (problem):
    - Within the ladder, BIC ranks M2 (24529.585) below M3 (24555.360). BIC thus does not support H1b, whereas AIC and the LR test do (F2.4).
    - No ΔIC or Akaike weights are available [FI-11].
  - Supporting detail, in one sentence each, pointing to [SUPP]:
    - Unordered step parameters in 9 raters under M2 and 9 under M3 (F2.6; @tbl-threshold-order). GRM thresholds are ordered for all 19 raters (F2.6, F2.18).
    - M3 discriminations range from 0.283 (R09, SE 0.055) to 2.606 (R16, SE 1.419) (F2.7).
    - Under M1, rater infit ranges from 0.238 (R12) to 1.328 (R17) (F2.8).
  - Do **not** state in Results that unordered steps "show" the PCM/GPCM is wrong [ATC-7].

**3.2 Estimation and fit of the GRM (adequacy check before the RQ2–RQ4 results)**
- Findings: F2.9, F2.10, F2.11, F2.12, F2.13.
- Cross-reference:
  - `tbl-grm-convergence` [SUPP]
  - `tbl-grm-rater-fit` [SUPP]
  - `tbl-grm-q3-flagged` [SUPP]
- Not embedded: `tbl-grm-global-fit`.
- Bullets:
  - Converged after 165 EM iterations; information matrix positive definite (F2.9).
  - S-X²: no rater significant. p ranges from 0.294 (R12) to 0.671 (R02), with 20 imputations (F2.11).
  - GRM infit 0.334 (R19) to 0.971 (R18); outfit 0.322 (R19) to 0.961 (R18). All 19 values are below 1 (F2.10).
  - Q3: the 10 pairs with the largest deviation from the mean Q3 (|q3 − mean| from 0.322 to 0.524). All but one are negative deviations. Largest: R08–R19 (n_common 46, q3 −0.761) and R08–R12 (51, −0.743). The only positive deviation is R10–R11 (32, 0.105; deviation 0.343) (F2.12).
  - C2 could not be computed (F2.13); state this in the text.
  - Move 3 (problems, stated descriptively here and interpreted in the Discussion):
    - about 90% of cells imputed for S-X²;
    - Q3 bias with few raters per product;
    - infit/outfit below 1 expected with about 2 ratings per product;
    - C2 not available.
    - Do not quote the mean Q3, "20 pairs > 0.2", RMSEA, or the 0.7–1.3 flag count (all NOT IN NOTEBOOK) [FI-21].

**3.3 Rater parameters and information (RQ2)**
- Findings: F2.3, F2.18, F2.19.
- Embed:
  - `tbl-grm-rater-parameters` [MAIN]
  - `fig-grm-category-response-functions` [MAIN] (D4: could move to SUPP)
  - `fig-grm-information-shares` [MAIN]
- Cross-reference:
  - `tbl-grm-information-summary` [SUPP]
  - `fig-grm-rater-information` [SUPP]
  - `tbl-category-usage` [SUPP]
- Bullets:
  - **Discrimination**:
    - a ranges from 0.631 (R18, SE 0.263) to 3.709 (R19, SE 2.220). Second highest: R16, 3.701 (SE 1.359).
    - Low values: R09 0.863 (SE 0.151), R17 1.446 (0.465), R13 1.504 (0.223) (F2.18).
    - Use the SEs as the precision statement (effect-size/uncertainty criterion).
  - **Thresholds**:
    - All ordered.
    - Number of thresholds: 4 for R17, 5 for R01, R03, R06 and R18, 6 for the rest.
    - Most extreme spreads: R18 (b1 = −6.565, b5 = 4.440) and R13 (b1 = −3.384, b6 = 4.435) (F2.18).
    - Threshold SEs are not displayed [FI-10].
  - **Information**:
    - Weighted information area ranges from 0.123 (R18) to 3.539 (R19).
    - Largest weighted shares of full-panel information: R19 0.135 and R16 0.126, raters with 50 and 52 ratings.
    - Smallest: R18 0.005 and R09 0.009.
    - R01, who gave the most ratings (1174), has share 0.037.
    - Location of maximum information: R01 at 2.700, R06 at 2.400, down to R13 at −0.550 (F2.19).
    - The shares differ by θ, for example R06: 0.001 at θ = −2 and 0.083 at θ = +2 (F2.19).
  - Move 3 (problem):
    - Information values are computed at point estimates; no SE or CI exists for information or shares (F2.19).
    - The two highest-share raters have the largest a SEs (F2.18) [FI-14].
    - State this in Results; interpret it in the Discussion [ATC-10].

**3.4 Reliability of the product scores (RQ3, H2, H3)**
- Findings: F2.14, F2.15, F2.16, F2.17, F2.21.
- Embed:
  - `tbl-reliability-overview` [MAIN]
  - `fig-grm-rel-post-by-n` [MAIN]
- Cross-reference:
  - `tbl-grm-reliability-by-n` [SUPP], the source of the quoted means
  - `tbl-grm-reliability-summary` [SUPP]
  - `tbl-naive-indices` [SUPP]
  - `tbl-marginal-reliability-models` [SUPP] (decision D5)
  - `fig-grm-panel-information` [SUPP]
  - `fig-grm-rel-post-histogram` [SUPP]
  - `fig-grm-rel-post-by-theta` [SUPP]
  - `fig-grm-rel-consistency` [SUPP]
- Bullets:
  - Invite the reader to @tbl-reliability-overview, which lists each index together with what it refers to.
  - **H2:**
    - GRM empirical marginal reliability (actual scores) 0.672.
    - Model-based marginal reliability (hypothetical full panel) 0.960 (grid check 0.960).
    - Cronbach's α, pairwise covariances: 0.928 (14 raters, 1900 products; removed: R19, R14, R02, R16, R12).
    - Cronbach's α, fully crossed block: 0.658 (3 raters, 139 products).
    - Krippendorff's ordinal α: 0.392, 95% bootstrap CI [0.362, 0.417] (19 raters, 2771 products; 1000 replications) (F2.14, F2.17).
  - **Distribution of product-level reliability** (rel_post): median 0.698, IQR 0.173 (Q1 0.596, Q3 0.769); p10 0.485, p90 0.813; range 0.057–0.929 (F2.14).
  - **H3** (@fig-grm-rel-post-by-n; values from @tbl-grm-reliability-by-n):
    - Mean rel_post: 0.520 (n = 1, 897 products), 0.698 (n = 2, 2080), 0.757 (n = 3, 357), 0.810 (n = 4, 125), up to 0.919 (n = 10, 3 products).
    - Mean PSD falls from 0.686 to 0.285 (F2.15).
    - Move 3: the cells for n = 9 and n = 10 contain 3 products each.
  - Consistency of the two product-level routes (F2.21, F2.14): rel_post and rel_info correlate 0.935; mean difference 0.016; max |diff| 0.413; 320 products differ by > 0.1.
  - Across models (only if D5 = include): empirical reliability 0.626 (M1), 0.637 (M2), 0.657 (M3), 0.672 (GRM); model-based 0.943, 0.944, 0.955, 0.960 (F2.16). The full-panel/empirical gap appears under every model.
  - Effect-size/CI note for the writer:
    - Only Krippendorff's α has a CI.
    - The empirical marginal reliability and the Cronbach's α values have none [FI-12]. Do not imply precision they lack.

**3.5 Model dependence of product scores (RQ4)**
- Findings: F2.20, F2.21.
- Embed: `tbl-theta-correlations` [MAIN].
- Bullets:
  - Pearson / Spearman between the GRM and each ladder model:
    - M3 0.996 / 0.996;
    - M2 0.985 / 0.983;
    - M1 0.975 / 0.978.
  - Among the ladder models: 0.980–0.993 (Pearson) and 0.983–0.996 (Spearman) (F2.20).
  - Integration-grid check: M1 fine grid vs sirt default grid 1.000 / 1.000 (F2.20, F2.21). Explain the extra `rm_facets_default_grid` row in the table note.
  - Move 3: no rank-change statistics (e.g., top-k overlap, maximum rank shift) and no CIs for the correlations are available [FI-13]. The text therefore reports correlations only and makes no claim about individual products' ranks.
  - Move 4 (one hedged sentence that closes Results): "Taken together, the choice among the four models affected fit more than it affected product scores" [ATC-6].

### 4 Discussion

Purpose: interpret, map to the literature, state the contribution, and draw the sport-science implications and limitations. Four moves (writing-models/discussion-conclusion.md), mirroring the Introduction. **Every interpretive claim below is [ATC].**

**4.1 Summary of the answers (move 1, 1 paragraph)**
- Echo RQ1–RQ4 in the Introduction's wording:
  - constraints rejected (with the BIC caveat);
  - the GRM preferred by information criteria;
  - heterogeneous raters;
  - empirical vs full-panel reliability;
  - product reliability rising with ratings per product;
  - scores robust to model choice.

**4.2 Two kinds of reliability (moves 2–3) [ATC-3, ATC-4, ATC-11]**
- The full-panel marginal reliability (0.960) and the pairwise Cronbach's α (0.928) describe the consistency of a mean over many raters. Each product in this design, however, was rated by about two raters (median 2). The scores actually used have an empirical reliability of 0.672 [ATC-3].
- Map to the literature:
  - Amabile's Spearman–Brown logic (amabile1982);
  - kaufman2008: a high α can hide low single-rater agreement. Krippendorff's α of 0.392 vs α of 0.928 illustrates exactly this [ATC-11];
  - cseh2019 on panel size.
  - The crossed-block α of 0.658 (3 raters) lies close to the empirical reliability. Keep this as a cautious observation and do not claim equivalence [ATC-11].
- Product-level precision depends mainly on how many ratings a product received (F2.15) [ATC-4]. Qualify with:
  - the observational allocation [FI-4];
  - rel_post also varies with θ (`fig-grm-rel-post-by-theta` [SUPP]) and with which raters rated the product (rater information differs; F2.19).
- Implication for CAT reporting: report the reliability of the scores actually used (empirical marginal reliability and product-level SEs), not only α or full-panel values [ATC-14].

**4.3 Rater assumptions and model choice (moves 2–3) [ATC-5, ATC-6, ATC-7, ATC-8]**
- Raters differ in scale use (thresholds) and discrimination. The LR tests reject the Rasch/MFRM constraints (F2.5). This is consistent with myszkowski2019, myszkowski2021 and long2015, and extends primi2019, who left response styles to future work, to football [ATC-8].
- Consequence: unweighted means treat raters as interchangeable, which these data do not support. This matters especially in sparse designs, where severity is confounded with rater assignment (primi2019) [ATC-8].
- BIC caveat: the evidence for unequal discrimination is weaker under BIC. Large SEs for the low-n raters (F2.7, F2.18) suggest that part of the discrimination heterogeneity is estimation noise [ATC-8].
- The GRM is preferred by information criteria. A cumulative link is plausible for a unipolar "amount of creativity" scale (brief's rationale), and pellegrino2025 also retained a GRM [ATC-5].
  - Unordered PCM/GPCM step parameters (F2.6) are not by themselves evidence of misfit in adjacent-category models (andrich1978; bond2020).
  - The ordered GRM thresholds hold by construction, so they are not evidence either [ATC-7].
- Product scores, however, barely depend on the model (correlations ≥ 0.975, F2.20) [ATC-6]. For applied users, model choice is secondary to design; the model matters more for diagnosing raters. Ground this only in the correlations and do not claim rank stability for individual products.

**4.4 What the rater parameters can and cannot tell (moves 2–3) [ATC-10]**
- Raters with about 50 ratings (R16, R19) have the largest discriminations, and therefore the largest information shares, but also the largest SEs (a_se 1.359 and 2.220). Their information shares are point estimates without uncertainty (F2.18, F2.19). They should not be read as evidence that these raters are the best raters [ATC-10].
- Raters with many ratings can still contribute little information at some θ regions (R01 share 0.037; R06 peaks at high θ) (F2.19). This motivates combining rater-specific information when assigning raters [ATC-15].
- Map to the literature:
  - sparse-design rater estimates depend on linking-set size (wind2018; wind2019a);
  - GRM recovery requires adequate sample size (reise1990);
  - rater characteristics predicting discernment (ceh2022) are a route to explain a_j.

**4.5 What the fit evidence can and cannot tell (move 3) [ATC-9]**
- No S-X² misfit was found, but the test is conservative with about 90% imputed cells.
- C2 could not be computed.
- Q3 is negatively biased with few raters per product (christensen2017). Interpret the flagged pairs as candidates, not as established local dependence.
- Infit/outfit values below 1 are an expected artefact of estimating θ from the same ≈ 2 ratings (wright1982 metric).
- Conclusion: the design permits *relative* model comparison but only weak *absolute* fit evidence. Absence of detected misfit is not evidence of fit [ATC-9].

**4.6 Practical implications for sport science (move 4: applications) [ATC-12 to ATC-15]**
- **Anchor/calibration set** [ATC-12]. Have all raters rate a common set of products. The vault's original plan had a benchmark set. This would:
  - strengthen rater linkage (17 of 171 pairs currently share no product; F2.1);
  - make C2/Q3 and crossed reliability estimable;
  - stabilise a_j for raters with few ratings (wind2019a; forthmann2023).
  - Distinguish this from rater *training*, which conflicts with the CAT's no-criteria rule (storme2014; dollinger2005; hennessey2011).
- **At least two ratings per product** [ATC-13]. 897 products have a single rating, with mean rel_post 0.520 vs 0.698 at two ratings (F2.15). Planned-missing designs (forthmann2023; primi2019) can target this within a fixed rater workload.
- **Minimum workload per rater** [ATC-15]: the author decided that raters with fewer than 15 ratings cannot be calibrated. Raters with about 50 ratings still yield very uncertain discriminations (F2.18). Plan more ratings per rater, or pool raters through the anchor set.
- **Report and propagate precision** [ATC-14]:
  - use EAP scores with PSDs rather than raw means;
  - report empirical marginal reliability;
  - for downstream uses (e.g., labels for automated creativity rating, selection of creative actions for training), carry the product-level SEs or weight by them.
- Optionally, a short boxed list of 4–5 design recommendations (CRJ readers and sport scientists). Decision D4.

**4.7 Limitations and future research (move 4)**
- L1. **Sparse, observational design.** Allocation of products to raters [FI-4]; ignorable missingness assumed. The by-n reliability comparison is not experimental.
- L2. **Weak absolute fit evidence** (see 4.5). C2 not computable.
- L3. **Uncertain rater parameters for low-n raters.** No uncertainty for information shares [FI-14].
- L4. **Raters.** One pool of student raters [FI-1]. No expertise or demographic covariates, so the brief's question on required expertise is not answered. Future work: expertise comparison (kaufman2008; kaufman2009; kaufman2013; plucker2009; zamparo2017).
- L5. **Rater exclusion.** Three raters with fewer than 15 ratings were excluded. Sensitivity: [FI-7/ATC-17] placeholder, else state it as not reported.
- L6. **Model comparison caveats:**
  - cross-software LR test with df deviation [FI-8];
  - BIC vs LR disagreement for discrimination;
  - no ΔIC or Akaike weights [FI-11].
- L7. **Model dependence** assessed by correlations only. No rank-change statistics [FI-13].
- L8. **Two-facet model only.**
  - No time, session or fatigue facet: drift (barth2020; leckie2011; myford2009); workload (forthmann2017).
  - No product subgroups or differential rater functioning (wind2019b).
  - Extensions: hierarchical rater model (patz2002); generalised MFRM (uto2020).
- L9. **Only one dimension** (creativity) analysed. Unidimensionality assumed. The number of scale categories was not varied: the brief's "rating scale" aim is only partly addressed via category use (F2.3).
- L10. **"Not recognised" ratings** (1290 rows removed; F0.2) may reflect clip quality or rater uncertainty. Whether to discuss: decision D12.
- Future work:
  - a D-study or simulation for panel size using the fitted GRM (forthmann2023);
  - a prospective anchor-set design;
  - rater covariates;
  - replication in other sports.

### 5 Conclusion (1 paragraph)

- Restate the contribution in 3–4 sentences [ATC-1]:
  - JRT is feasible for large sparse CAT data in sport;
  - the Rasch constraints on raters do not hold;
  - the GRM fits best, but scores are robust across models;
  - the reliability of actual scores (0.672) is far below conventional indices.
- End with the main design message: invest in ratings per product and rater linkage, and report score-level precision [ATC-12, ATC-13, ATC-14].

### References

APA 7th via CSL; citekeys only (see the list below). Mechanical; no hand formatting.

---

## Figure/table plan

There are 9 main-text objects (6 tables, 3 figures) and 19 supplement objects (14 tables, 5 figures). 6 objects are not embedded.

### Main text (9)

| # | Label | Section | Role |
|---|---|---|---|
| 1 | `tbl-design-summary` | 2.6 | Final data and design (reproducibility) |
| 2 | `tbl-model-fit` | 3.1 | RQ1: information criteria |
| 3 | `tbl-lr-tests` | 3.1 | H1a/H1b |
| 4 | `tbl-grm-rater-parameters` | 3.3 | RQ2: a, thresholds, SEs (wide: landscape or reduced columns) |
| 5 | `fig-grm-category-response-functions` | 3.3 | RQ2: rater scale use (D4: could be SUPP) |
| 6 | `fig-grm-information-shares` | 3.3 | RQ2: information contributions across θ |
| 7 | `tbl-reliability-overview` | 3.4 | RQ3/H2: core reliability contrast, all indices with "refers to" and the Krippendorff CI |
| 8 | `fig-grm-rel-post-by-n` | 3.4 | H3: reliability by ratings per product |
| 9 | `tbl-theta-correlations` | 3.5 | RQ4 |

### Duplicate-pair decisions (02_artifacts.md C6)

1. `fig-grm-rel-post-by-n` vs `tbl-grm-reliability-by-n`:
   - **Figure → MAIN**: it shows the distribution as well as the means.
   - Table → SUPP: it is the citable source of the exact means quoted in the text.
2. `tbl-reliability-overview` vs `tbl-naive-indices`:
   - **Overview → MAIN**: it carries the naive indices *and* the GRM empirical/full-panel values in one table with a "refers_to" column. That is exactly the core contrast.
   - `tbl-naive-indices` → SUPP: it holds the n_products of each index (1900, 139, 2771).
3. `tbl-marginal-reliability-models` vs `tbl-grm-reliability-summary`:
   - **Neither in MAIN.** `tbl-reliability-overview` already shows the GRM's empirical and full-panel values and the ladder's marginal reliabilities.
   - `tbl-grm-reliability-summary` → SUPP: the full rel_post distribution and the consistency check.
   - `tbl-marginal-reliability-models` → SUPP only if D5 = include: it is the sole source of the per-model *empirical* reliabilities (0.626/0.637/0.657).

### Supplement (19)

- **Tables (14):**
  - `tbl-cleaning-log` (with the bridge sentence in 2.6; caption: "actions" → "products")
  - `tbl-excluded-raters`
  - `tbl-category-usage`
  - `tbl-grm-convergence`
  - `tbl-grm-rater-fit`
  - `tbl-grm-q3-flagged`
  - `tbl-discrimination-m3`
  - `tbl-threshold-order`
  - `tbl-rater-fit-m1`
  - `tbl-grm-information-summary`
  - `tbl-grm-reliability-by-n`
  - `tbl-naive-indices`
  - `tbl-grm-reliability-summary`
  - `tbl-marginal-reliability-models` (D5)
- **Figures (5):**
  - `fig-grm-rater-information`
  - `fig-grm-panel-information` (its caption must keep "hypothetical")
  - `fig-grm-rel-post-histogram`
  - `fig-grm-rel-post-by-theta`
  - `fig-grm-rel-consistency`

### Not embedded (6)

- `tbl-grm-global-fit`: contains an R error string. C2 is reported in the text as not computable.
- NB01 (pre-exclusion, 22 raters):
  - `tbl-overview-ratings-per-action`
  - `fig-overview-rater-overlap`
  - `fig-overview-rating-distribution`
  - `fig-overview-rater-response-styles`
  - `fig-overview-degree-distributions`

  These may come back only after a post-exclusion re-run [FI-15].

### Formatting notes for the writer and embedder (from 02_artifacts.md C4/C5)

- Literal `nan` cells and float-formatted integers (e.g., "897.000", npar "25.000") must be fixed in the notebook before rendering.
- APA tables need display column names, not snake_case.
- R figures carry in-figure titles, which are non-APA.
- `02_artifacts.md` says N2 has 33 labels, but its table lists 28 N2 rows. All 28 listed rows are planned above. Check for missing labels.

---

## Effect sizes and CIs (APA review criterion): inventory

| Quantity | Uncertainty available? | Where |
|---|---|---|
| Krippendorff's α | Yes: 95% bootstrap CI [0.362, 0.417] | F2.17, tbl-reliability-overview |
| GRM discriminations a | Yes: SEs (Oakes) | F2.18 |
| M3 discriminations | Yes: SEs | F2.7 |
| Product scores | Yes: PSD per product; mean PSD by n | F2.14, F2.15 |
| Product-level reliability | Distribution (quantiles, IQR) | F2.14 |
| Model comparison | logLik, AIC/BIC/SABIC, LR X² with df. **No ΔIC, Akaike weights or effect size** | F2.4, F2.5 → FI-11 |
| LR p-values | Only p < .001 | F2.5 |
| GRM thresholds | **SEs not displayed** | FI-10 |
| Empirical / model-based marginal reliability | **No CI** | FI-12 |
| Cronbach's α (both versions) | **No CI** | FI-12 |
| θ correlations between models | **No CI; no rank-change statistics** | FI-13 |
| Rater information and shares | **No SE/CI** | FI-14 |

---

## FILL IN items (21)

Items marked "notebook" must be added to a notebook and passed through results-interpreter before any number is quoted.

- **FI-1** Raters: recruitment, number at start, demographics, football playing/coaching experience, compensation, informed consent, ethics approval.
- **FI-2** Products: competitions and matches, selection rule for actions (event data), clip length and video source, number of matches.
- **FI-3** Procedure:
  - rating software;
  - verbatim instruction and creativity definition;
  - scale anchors;
  - the "not recognised" option;
  - randomisation, session length and breaks, data-collection period;
  - other dimensions rated.
- **FI-4** Allocation of products to raters (planned design, benchmark set, randomisation). Needed for the missing-at-random argument and to qualify H3.
- **FI-5** The 23 → 22 rater step (former R23), if it is to be reported (notebook).
- **FI-6** Evidence that the parameters of R20–R22 are not identified (notebook) and the rationale for the cut-off of 15.
- **FI-7** Exclusion sensitivity (agreement of scores with and without R20–R22). Plan only as a conditional placeholder: "[FILL IN / AUTHOR TO CONFIRM: sensitivity statistic, if added to a notebook]". The value r = 0.99997 must NOT be quoted.
- **FI-8** Explanation of LR df 84 vs 90 (end-category gaps) and the sirt–mirt cross-check (notebook if numbers are quoted).
- **FI-9** Software versions (R, mirt, sirt, psych, Krippendorff package) and the GRM convergence tolerance.
- **FI-10** Threshold SEs in `tbl-grm-rater-parameters`: the caption announces them but they are not displayed (notebook).
- **FI-11** ΔAIC/ΔBIC/ΔSABIC or Akaike weights for `tbl-model-fit` (notebook).
- **FI-12** Bootstrap CIs for the empirical marginal reliability and both Cronbach's α (notebook).
- **FI-13** CIs for the θ correlations and rank-change statistics (top-k overlap, maximum rank shift) (notebook). These are needed for any claim beyond "correlations are high".
- **FI-14** Uncertainty of the rater information shares, e.g., parametric bootstrap (notebook).
- **FI-15** Post-exclusion descriptives (19 raters):
  - overall category distribution;
  - rater response styles (mean, SD, floor/ceiling, categories used);
  - overlap heatmap;
  - degree distributions.

  Options: re-run NB01 on the final data, or drop these descriptives.
- **FI-16** Reason why R19, R14, R02, R16 and R12 were removed for the pairwise Cronbach's α. Optionally, the identity of the 3 raters in the crossed block (notebook).
- **FI-17** Preregistration status; data and code availability statement.
- **FI-18** CRJ requirements: abstract word limit, keywords, word count, supplement policy.
- **FI-19** Cause of the C2 failure (notebook), or a neutral wording ("could not be computed for this design").
- **FI-20** Verify the Introduction framing claims against the PDFs: worldeconomicforum2025 wording; safardilha2019; memmert2011; batey2012; barbot2019b.
- **FI-21** Mean Q3 and the number of pairs above a deviation threshold, if they are wanted (notebook).

## AUTHOR TO CONFIRM claims (19)

- **ATC-1** The central contribution statement.
- **ATC-2** The novelty claim: "to our knowledge, first IRT/JRT analysis of CAT creativity ratings in sport". The search was not systematic.
- **ATC-3** Two kinds of reliability: conventional CAT indices (α, full-panel marginal reliability) describe a hypothetical full panel or the rater mean, not the precision of the sparse-design scores actually used.
- **ATC-4** Product-level reliability depends mainly on the number of ratings per product (observational; also depends on θ and rater mix).
- **ATC-5** The GRM is preferred by information criteria, and a cumulative link suits the unipolar creativity scale.
- **ATC-6** Product rankings barely depend on the model, grounded only in `tbl-theta-correlations`.
- **ATC-7** Unordered PCM/GPCM steps and ordered GRM thresholds are not used as evidence for or against either family.
- **ATC-8** Rater heterogeneity in discrimination and scale use makes τ-equivalent raters and unweighted means questionable, with the BIC and SE caveats.
- **ATC-9** The fit evidence is limited by the design: S-X² conservative (≈ 90% imputed), C2 not computable, Q3 negatively biased, infit/outfit overfit an artefact. Absence of misfit ≠ fit.
- **ATC-10** The information estimates for R16 and R19 (about 50 ratings) are uncertain. Shares are not a ranking of rater quality.
- **ATC-11** The Krippendorff vs Cronbach contrast illustrates kaufman2008. The crossed-block α lies near the empirical reliability (cautious).
- **ATC-12** Recommendation: an anchor/calibration set rated by all raters, distinct from rater training.
- **ATC-13** Recommendation: raise single-rated products to ≥ 2 ratings.
- **ATC-14** Recommendation: report empirical marginal reliability and product SEs; propagate PSDs downstream.
- **ATC-15** Recommendation: a minimum number of ratings per rater, and rater assignment informed by information functions.
- **ATC-16** Rationale for excluding R20–R22 (parameters not identified with < 15 ratings).
- **ATC-17** Exclusion sensitivity is negligible. Only valid if FI-7 is added to a notebook.
- **ATC-18** The realised design departs from the planned benchmark-set design.
- **ATC-19** Showing raters a creativity definition is a (minor) departure from the classical CAT "no criteria" procedure.

---

## Evidence gaps (brief vs findings)

- **"Agreement among various numbers of raters"** (brief aim). This is only addressed observationally via reliability by ratings per product (F2.15). There is no subsampling, D-study or simulation. Either narrow the aim or add an analysis (D10).
- **"Required level of expertise"** (brief, cseh2019 framing). There are no rater covariates in any notebook, so this cannot be answered. Move it to Limitations/Future work.
- **"Rating scale" choices** (brief: e.g., combining levels). Only category use (F2.3) and threshold order (F2.6) are available. No collapsing analysis exists.
- **MFRM "fair averages" / fair scores** (brief Introduction). There is no fair-average output. Fair scores are represented only by EAP estimates.
- **Rater tendencies (response styles).** The only response-style table is pre-exclusion (F1.6) and may not be quoted for the final data [FI-15]. The GRM thresholds (F2.18) are the usable post-exclusion evidence.
- **Rank stability across models.** Correlations only (F2.20) [FI-13].
- **Absolute model fit.** Not established: C2 is missing, and S-X² and Q3 are compromised by the design (F2.11–F2.13).
- **Exclusion sensitivity.** NOT IN NOTEBOOK (F2.22) [FI-7].
- **Effect sizes and CIs** for model comparison and reliability are largely missing (see the inventory).
- **Bibliography.**
  - The keys `memmert2007` and `santos2016` are in `phd_library.bib`, not in web_references.bib. That is fine.
  - All web keys used above exist in `web_references.bib`.
  - None of the methods keys (robitzsch2025, chalmers2018, orlando2000, kang2008, yen1984, christensen2017, cai2014, wright1982, cronbach1951, hayes2007, green1984) clash with `phd_library.bib`. I checked this with grep.
  - No Bayesian keys are used.

---

## Open decisions for the author (checkpoint 1)

- **D1 Title.** Choose the working title (a), alternative (b) or (c), or your own.
- **D2 Terminology.** Is "product" (with "football action" introduced once) the single analytic term, and "rater" rather than "judge"?
- **D3 Hypothesis status.** Were H1a, H1b, H2 and H3 specified a priori (preregistered or planned)? If not, frame them as exploratory expectations. RQ1c and RQ4 stay exploratory in either case.
- **D4 Main/supplement split.**
  - Accept 9 main / 19 supplement?
  - Move `fig-grm-category-response-functions` (19 panels) to the supplement?
  - Include a boxed "design recommendations" list in the Discussion?
- **D5** Include `tbl-marginal-reliability-models` in the supplement and report the per-model empirical reliabilities, or drop it?
- **D6 Rater exclusion in the data flow.** Keep `tbl-cleaning-log` plus the bridge sentence, or add a rater-exclusion row to the cleaning log in the notebook?
- **D7 Exclusion sensitivity.** Add it to a notebook (then FI-7 becomes quotable), or omit it and list it as a limitation?
- **D8 Effect sizes and CIs.** Commission the notebook additions FI-10 to FI-14 before the writer runs? They are the main gap against the APA "effect sizes and CIs" criterion.
- **D9 Post-exclusion descriptives.** Re-run NB01 on 19 raters (FI-15), or report no overall descriptives beyond `tbl-design-summary` and `tbl-category-usage`?
- **D10 Scope of aims.** Narrow the brief's aims (number of raters, expertise, rating-scale choices) to what the findings support, or add analyses such as a D-study or simulation?
- **D11 Privacy.** Clear the cells that leak original rater IDs (NB01 b1510393, NB02 ad422588) and remove the Google Sheet URL in NB00 before any render or publication.
- **D12 "Not recognised" ratings.** Discuss the 1290 removed "not recognised" ratings as a limitation or design issue?
- **D13 Hypothesis H1b and BIC.** Accept the framing "supported by LR/AIC, not by BIC", or treat discrimination heterogeneity as tentative throughout?
