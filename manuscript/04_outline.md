# 04_outline.md: Argument outline (Phase 5, outline-architect)

Regenerated from scratch on 2026-10-21. The previous outline is obsolete: no numbers, RQs, F-IDs or labels were carried over. Some argumentative ideas were reused where they still fit.

- **Profile:** `imrad-apa`. Venue: *Creativity Research Journal* (APA 7).
- **Structure:** Abstract, Introduction, Methods, Results, Discussion, Conclusion, References, plus an Appendix inside the same manuscript.
- **Inputs:**
  - brief `~/drive/KNOWLEDGE/Paper_CreativityAssessmentInSportsCAT.md`
  - `01_dossier.md`, `02_artifacts.md` (18 labels), `03_findings.md` (regenerated 2026-10-21), `06_web_literature.md` (including "Targeted additions (2026-10-21)")
  - `web_references.bib` and `~/drive/phd_library.bib`
- **Move order:** follows `~/drive/utils/writing-models/` (introduction, methods, results, discussion-conclusion, abstract, title).

## Conventions in this outline

- **F-IDs:** `F…` and `X…` are finding and flag IDs in `03_findings.md`.
- **Labels:** `fig-…` and `tbl-…` are the 18 labels in `02_artifacts.md`. No other labels exist. The interpreter's remark (X1) that 02_artifacts is outdated is obsolete, because the labels now match.
- **Citekeys:** every key below was checked against the two bibs. Methods software and algorithm keys: `abrilpla2023` for PyMC (**not** salvatier2016), `kumar2019a` for ArviZ (**not** kumar2019), `hoffman2014`, `vehtari2017`, `vehtari2021`, `green1984`.
- **`[AUTHOR TO CONFIRM]`:** an interpretive claim or framing decision that the author must approve. Every interpretive claim in the Discussion carries this tag.
- **`[**FILL IN:** …]{.mark}`:** a Methods fact that no in-scope source provides. The writer must insert the placeholder **verbatim** at the stated spot and must never supply a value.
- **Numbers:** quote them exactly as in `03_findings.md`. Display rounding to APA precision is a writer decision (see "Number display" at the end). Rounding may not change a value beyond conventional display rounding, and no new values may be computed. Values marked NOT QUOTABLE in 03 (trace plots, the pool-sum information curve, secondary-dimension PairGrid, stale outputs X6/X7) must never appear.
- **Scope:**
  - JRT is the only analysis.
  - Mean scores, MFRM and G-theory appear only as literature background (Introduction, Discussion), never as results.
  - The PSIS-LOO comparison is JRT's own nested constraint test (rater-specific a_j vs. all a_j equal). It is not a rival approach.
- **Terminology:**
  - Use **leniency** λ_j (higher = more lenient, relative to the average rater; F1.0a, F2.3).
  - "Severity" is used only when describing the MFRM literature.

---

## Central contribution

**[AUTHOR TO CONFIRM]** To our knowledge, this is the first Judge Response Theory (JRT) analysis of Consensual Assessment Technique (CAT) creativity ratings of sport actions. It is based on a large, sparse but fully connected design: 22 raters, 3669 football actions and 7844 ratings (F0.3).

It provides domain-specific evidence of two kinds:

1. **Judge behaviour (RQ1).**
   - Raters differ in leniency and in discrimination (F2.1–F2.3).
   - Constraining all raters to equal discrimination, as Rasch-family and mean-score approaches implicitly do, gives worse out-of-sample prediction than rater-specific discrimination (F2.6).
2. **Precision and panel size (RQ2).**
   - At the realised panel size (harmonic mean of 1.726320341325184 ratings per action), JRT scores reach an empirical reliability of 0.6603541094329908 (F3.1).
   - A model-based IRT D-study quantifies how marginal reliability grows with the number of judges per action (F3.4). This answers the call of cseh2019 for domain-specific evidence on panel size.

For sport-science researchers, the paper offers a reproducible template: collect CAT ratings in a connected sparse design, score them with JRT, check whether judges are equally discriminating, and plan panel size from a D-study. **[AUTHOR TO CONFIRM]**

**Evidence chain (narrative order):**
1. Creativity matters in society and in sport (literature).
2. The CAT is the product-level standard. Its reliability rests on aggregating judges, and the required number of judges is domain-specific (amabile1982; cseh2019).
3. Sport has no psychometric evidence on CAT ratings of actions (gap; 06_web_literature novelty check).
4. Scoring models can be ordered as a successive relaxation of assumptions about judges. JRT frees discrimination per judge and makes equal discrimination testable (literature).
5. The design is connected, so all raters and actions sit on one scale. A crude agreement index is reported only as a descriptor (F0.3–F0.7).
6. RQ1: category use, leniency, discrimination and the equal-discrimination test (F0.6, F1.3, F2.1–F2.6).
7. RQ2: reliability at the realised panel size, precision by number of ratings, and the D-study (F3.1–F3.4).
8. Discussion (all [AUTHOR TO CONFIRM]): judges are not interchangeable; current panels give modest precision; design recommendations follow.

---

## Research questions (binding author decision 1)

The stated aim is narrowed to these two RQs. The brief's broader aims become future work and limitations (rater expertise, rating-scale choices, comparison of rating-processing techniques such as means, MFRM and G-theory).

- **RQ1. Judge behaviour.** How do judges differ in leniency and discrimination, and is the equal-discrimination constraint tenable?
  - Sub-parts reported within RQ1:
    - category use: observed category frequencies and the spacing of the shared thresholds;
    - leniency λ_j;
    - discrimination a_j;
    - nested comparison of the rater-specific model against the equal-discrimination model via PSIS-LOO;
    - rater information.
  - Status: an exploratory nested-model comparison. **[AUTHOR TO CONFIRM: was the equal-discrimination comparison planned a priori or exploratory? Was anything preregistered?]** Default wording until confirmed: "exploratory". Do not phrase it as a hypothesis test with a prediction.
  - Evidence: F0.6, F0.8, F1.3, F2.1–F2.6.
- **RQ2. Reliability and panel size.**
  - How reliable are the JRT scores at the realised panel size?
  - How does reliability depend on the number of judges per action (IRT D-study)?
  - Descriptive. Evidence: F3.1–F3.4.

No directional hypotheses are stated. The review criterion asks for "clear RQ/hypotheses". The writer states the RQs explicitly in the last Introduction paragraph and echoes them as Results subheadings.

---

## Title (proposals; sentence case, neutral, no question mark)

1. "Judge response theory for the consensual assessment of creativity in football: Judge leniency, discrimination, and the number of judges"
2. "Modelling judges in consensual creativity ratings of football actions with judge response theory"
3. "Rater leniency, rater discrimination, and score reliability in consensual assessments of creative football actions"

**[AUTHOR TO CONFIRM choice]**

---

## Abstract

- **Purpose:** a standalone summary that persuades creativity and sport-science researchers to read on.
- **Model:** abstract.md Model 1 (Background → Aim → Method → Results → Implications), one paragraph with each component in its own sentence. **[AUTHOR TO CONFIRM: CRJ abstract word limit and format; check the CRJ Instructions for Authors]**
- No citations. Define CAT and JRT at first use. Write last. Introduce nothing new.

Sentence plan:

1. **Background.** The CAT is the standard for rating creative products. Its reliability depends on how many judges are aggregated and how they differ, and the evidence on this is domain-specific. No such evidence exists for sport actions.
2. **Aim.** To model judge leniency and discrimination and to quantify score reliability as a function of the number of judges, using JRT on CAT ratings of football actions.
3. **Method.**
   - 22 raters gave 7844 ratings of 3669 football actions on a 7-point scale in a sparse, connected design (F0.3).
   - Bayesian graded-response JRT model with rater-specific leniency and discrimination and shared thresholds (F1.0a).
   - Nested comparison with an equal-discrimination model via PSIS-LOO (F2.6).
   - IRT D-study (F3.4).
4. **Results (naked numbers):**
   - posterior-mean discrimination range 0.9569497104368692–3.2408227509685186 (F2.1);
   - elpd difference 163.25478584290235 (SE 19.684919284549657) in favour of rater-specific discrimination (F2.6);
   - empirical reliability 0.6603541094329908 (F3.1);
   - marginal reliability 0.514110299035415 at k = 1, 0.6462162523422212 at the realised k (1.726320341325184), 0.8088802281726432 at k = 4 and 0.91365019867287 at k = 10 (F3.4).
   - All are displayed with APA rounding by the writer.
5. **Implications [AUTHOR TO CONFIRM].** Judges are not interchangeable. Fair scores should model judges rather than average them, and panels of about two judges per action give modest precision for individual actions.
6. **Keywords (proposal):** consensual assessment technique; judge response theory; item response theory; rater effects; creativity; football.

---

## 1. Introduction

**Purpose:** follow the brief's line of reasoning, narrowing from why creativity matters → the CAT and its dependence on judges → sport as an under-studied domain → scoring models as a successive relaxation of assumptions about judges → JRT → aim and RQs.

**Model:** introduction.md, four moves in order. Moves 1–3 span several paragraphs; Move 4 is short.

**Deviation from the brief:**
- In the brief, the aim paragraph ("generate a large-scale set of ratings … reference for future creativity research") sits *before* the IRT/JRT paragraphs.
- Per the writing model, the formal aim and RQs move to the end (Move 4).
- The brief's aim paragraph is kept in its place as a short bridging statement of the domain need (a design reference for sport). Its broad aims (expertise, scales, processing techniques) are not promised.
- **[AUTHOR TO CONFIRM]**

**Competitor approaches** (mean scores, MFRM, G-theory) appear here only as literature background (author decision 4).

### Move 1: Importance and background

**P1.1 Creativity as a key competency.**
- Purpose: a general "meeting place" fact.
- Content:
  - Employers rank creative thinking among core skills, with growing importance (worldeconomicforum2025; **the author must check this wording against the report PDF**, see 06 §A).
  - PISA 2022 assessed creative thinking (oecd2024).
  - In sport, creativity is a key quality to develop and evaluate in players (safardilha2019; santos2016). **The author must check the safardilha2019 claim against the PDF**; the dossier rates it unverified.
- Findings/objects: none.

**P1.2 Taxonomy and measurement.**
- Purpose: locate the paper at the product facet, with products rated by others.
- Content:
  - The person/process/product/press taxonomy (batey2012).
  - Each facet needs its own measurement approach (barbot2019; barbot2019b).
  - This paper concerns products, namely creative actions in matches, judged by others.
- Findings/objects: none.

### Move 2: Previous research (grouped by approach, not listed study by study)

**P2.1 The CAT as a procedure and its agreement.**
- Purpose: establish the CAT and its reliability record.
- Content:
  - Origin and procedure of the CAT (amabile1982; hennessey2011; kaufman2024).
  - Expert panels typically reach coefficient alphas above .70 (baer2004; kaufman2008; hennessey2011).
  - Lower agreement has also been reported and attributed to differences in procedure, scale use and beliefs about creativity (long2015; cseh2019).
  - One sentence on what the CAT has yielded: the intrinsic-motivation principle (amabile1985; hennessey2010).
- Findings/objects: none.

**P2.2 Reliability rests on aggregation.**
- Purpose: set up RQ2.
- Content:
  - Spearman–Brown logic: the reliability of the aggregate depends on both the mean inter-judge correlation and the number of judges (amabile1982).
  - A large panel can mask low agreement among individual judges (kaufman2008).
  - Rule of thumb of 5–10 judges (kaufman2008a). cseh2019 argue that the appropriate number of judges depends on product and domain, cannot be set in general, and must be established empirically per domain, together with the required expertise.
- Findings/objects: none.

**P2.3 Creativity assessment in sport.**
- Purpose: show that sport research has focused on process and that product ratings use agreement indices only.
- Content:
  - Process and divergent-thinking focus (memmert2011).
  - Product (action) ratings:
    - expert ratings of competition actions, which predict temporal proximity to goals (kempe2018; trained experts, ICC);
    - on-field action ratings by experts (zahno2023; zahno2024; dejoode2023);
    - origin of trained expert scales (memmert2007).
  - None of these studies provides parameters for designing a CAT study of football actions, such as the number of judges or the required expertise.
- Findings/objects: none.

**P2.4 Bridging statement (from the brief's aim paragraph).**
- Purpose: state the domain need.
- Content: sport research needs an empirical reference for designing CAT studies of actions. A key design aspect is how ratings from different judges are combined into "fair" scores that reflect rater tendencies.
- Keep it to 1–2 sentences, with no aims list.
- Findings/objects: none.

**P2.5 IRT as the framework.**
- Purpose: introduce the measurement-model view.
- Content:
  - IRT models the probability of each response as a function of a latent attribute and of item location and discrimination (lord1980; embretson2013; deayala2022; myszkowski2019).
  - Contrast with CTT: a falsifiable model, a common latent scale, and precision that is conditional on the latent level (myszkowski2019).
  - Polytomous models: the GRM (samejima1969) and the GPCM (muraki1992).
- Findings/objects: none.

**P2.6 Rasch family and MFRM.**
- Purpose: describe the equal-discrimination constraint and its use in creativity research.
- Content:
  - The Rasch model constrains discrimination to be equal, which gives sufficiency of the raw score and specific objectivity (rasch1960; bond2020).
  - The RSM and the PCM differ in whether thresholds are shared (andrich1978; masters1982).
  - The MFRM adds rater severity as a facet, and fair averages adjust for it (linacre1989; eckes2015).
  - Rater-effect diagnostics: severity, central tendency, range restriction, randomness and halo (engelhard1994; myford2003; myford2004).
  - In creativity research, primi2019 showed that:
    - raters differ in severity;
    - severity confounds scores when raters score different subsets;
    - MFRM-adjusted scores are robust under moderate planned missingness.
  - In judged sports, the MFRM has been used to monitor judges of performance quality, not creativity (looney2004; anderlucci2021).
- Findings/objects: none.

**P2.7 Successive relaxation of assumptions; JRT.**
- Purpose: build the core rationale for RQ1.
- Content:
  1. Mean or sum scores treat judges as interchangeable, (essentially) τ-equivalent measures (myszkowski2019). Their scores are comparable across products only when all products have the same or equally severe judges (primi2019).
  2. The MFRM models severity additively but keeps equal discrimination. Unequal discrimination surfaces only as misfit (myford2004; myszkowski2021). Response styles were left to future research (primi2019).
  3. Equal accuracy of judges is questionable in heterogeneous panels, which differ in expertise, training, attention, understanding of the instructions and category preferences (myszkowski2021).
  4. JRT treats judges as items with individual severity, discrimination and thresholds (myszkowski2019; myszkowski2021). Equal discrimination and a shared category structure become testable by comparing nested models, and fair scores come with product-specific standard errors.
  5. JRT applications in creativity research: barbot2023; pellegrino2025; forthmann2023 (planning missing-data rating designs).
- **Caution for the writer:** this study tests the equal-discrimination constraint only. Thresholds are shared and were not tested (F1.0a). Phrase the "testable" sentence generically. Do not imply that the shared category structure is tested here.
- G-theory is mentioned at most in one clause, as the classical route to D-studies (it is background only, and no citekey is planned). **[AUTHOR TO CONFIRM whether to mention it]**
- Findings/objects: none.

### Move 3: Gap

**P3.1 Gap.**
- Purpose: create the research space. Open with "However".
- Content:
  - To our knowledge, no study has modelled CAT ratings of sport actions with IRT or JRT. Closest precedents:
    - Rasch/MFRM applied to judges of performance quality (looney2004; anderlucci2021);
    - non-IRT evaluation of judge accuracy (heiniger2021);
    - a Rasch validation of a coach-completed creativity questionnaire, which rates players, not actions (shin2025);
    - CAT-like action ratings that report agreement indices only (kempe2018; zahno2023).
  - Consequently, for football actions it is unknown:
    - whether judges discriminate equally;
    - how much they differ in leniency;
    - how many judges per action are needed for reliable scores (cseh2019's call).
  - Hedge the claim ("to our knowledge"). The literature search was not systematic (06 §C). **[AUTHOR TO CONFIRM novelty claim; consider a SPORTDiscus/PsycINFO search]**
- Findings/objects: none.

### Move 4: Present paper

**P4.1 Aim and RQs.**
- Purpose: state the aim narrowly (author decision 1).
- Content:
  - Aim (Past Simple): to model judge leniency and discrimination in a large set of CAT ratings of football actions with JRT, and to quantify how reliable the resulting scores are as a function of the number of judges.
  - State RQ1 and RQ2 verbatim as above. RQ1 includes category use. RQ1's nested comparison is "exploratory" until confirmed.
  - One sentence on the approach: Bayesian graded-response JRT model; PSIS-LOO comparison with the nested equal-discrimination model; IRT D-study.
  - One sentence on intended use: a design reference for CAT studies in sport.
  - Rater expertise, rating-scale choices and comparisons of scoring approaches are explicitly beyond the scope of this paper (one clause).
- Findings/objects: none.

---

## 2. Methods

**Purpose:** reproducibility (review criterion) and trust.

**Model:** methods.md, top-down. Move 1 (overview) comes first. Then Move 2 (precise details with justification), Move 3 (relation to prior methods) where a method is borrowed, and Move 4 (problems) stated openly where they arose.

**Placeholders:** every `FILL IN` placeholder below goes at the exact spot named, verbatim.

### 2.1 Study overview and design (Move 1)

- **Purpose:** frame the study.
- **Content:**
  - A CAT-style rating study. Independent raters judged the creativity of football actions from real matches. All ratings were pooled into one sparse rater-by-action design and analysed with JRT.
  - Ethics and consent go here as the second sentence: `[**FILL IN:** ethics approval (committee, reference number) and informed-consent procedure for raters]{.mark}`
  - Preregistration goes after the ethics sentence: `[**FILL IN:** preregistration status (registry and ID, or statement that the study was not preregistered)]{.mark}`
  - Data-collection period goes at the end of the paragraph: `[**FILL IN:** data-collection period (start and end dates of rating)]{.mark}`
- **Findings/objects:** none.
- **Citekeys:** amabile1982; hennessey2011.

### 2.2 Raters (Move 2)

- **Purpose:** describe the judges.
- **Content:**
  - The analysed data contain 22 raters (F0.3), pseudonymised as R01–R22 and ordered by number of ratings (F0.5).
  - Recruitment goes immediately after the count: `[**FILL IN:** how raters were recruited (e.g., students rating as part of thesis projects), inclusion criteria, and compensation]{.mark}`
  - Background goes next: `[**FILL IN:** rater background and football expertise (e.g., number of raters holding a coaching licence, playing experience and level, years of involvement)]{.mark}`
  - Demographics go next: `[**FILL IN:** rater demographics (age, gender), if collected]{.mark}`
- **Author note (not for prose):** the vault indicates Bachelor's and Master's students rating for 5 or 10 h as part of their theses (dossier T8). This is unverified, so the writer must **not** write it. The author decides whether it goes into the placeholder.
- **Findings/objects:** F0.3, F0.5.

### 2.3 Stimuli: football actions (Move 2)

- **Purpose:** describe what was rated.
- **Content:**
  - Actions were identified via StatsBomb event data. The event lookup on the raw action IDs covered 4104 actions (F0.1), and 3669 actions remained after cleaning (F0.3).
  - Raters saw a mix of StatsBomb action types (e.g., passes, clearances, interceptions; F0.10). Name only the types that appear in F0.10. **[AUTHOR TO CONFIRM list of types to name]**
  - Video source and matches go after the StatsBomb sentence: `[**FILL IN:** video source of the clips and the competitions, seasons and matches sampled]{.mark}`
  - Selection goes next: `[**FILL IN:** how actions were selected from the event data (sampling frame, action types included or excluded)]{.mark}`
  - Clips go next: `[**FILL IN:** clip construction (clip length, pre-/post-action context, whether the target player or action was marked)]{.mark}`
  - Viewing conditions close the subsection: `[**FILL IN:** viewing conditions (device and screen, sound, whether replays or pausing were allowed, self-paced or fixed timing)]{.mark}`
- **Findings/objects:** F0.1, F0.3, F0.10.

### 2.4 Rating scale, instructions and procedure (Move 2 + Move 3)

- **Purpose:** make the rating task reproducible.
- **Content:**
  1. **Scale.** Creativity was rated on a 7-point scale with categories 1–7 (F0.2: values outside {1,…,7} were excluded; F0.6).
     - Labels go right after the scale sentence: `[**FILL IN:** verbatim verbal labels of the rating categories, including categories 2–6 (and the endpoint labels for 1 and 7)]{.mark}`
  2. **Off-scale option.** An off-scale "action not recognised" option existed. Its use led to the largest exclusion (F0.2).
     - Wording goes next: `[**FILL IN:** exact wording of the "action not recognised" option and the instruction on when to use it]{.mark}`
  3. **Additional dimensions.** Raters also rated technical correctness and aesthetic appeal ("Not found" list in 03: the columns exist), following amabile1982's separation of creativity from technical quality. These ratings are not analysed here.
     - Wording goes next: `[**FILL IN:** wording and scale of the technical-correctness and aesthetic-appeal items]{.mark}`
  4. **Instructions.**
     - Instructions go next: `[**FILL IN:** verbatim instructions given to raters, including the definition of creativity shown to them (original language and English translation)]{.mark}`
     - Training goes next: `[**FILL IN:** whether any training, practice clips or anchor examples were provided, or a statement that none were]{.mark}`
     - Move 3 (relation to prior methods): the CAT prescribes independent judgements without imposed criteria (amabile1982; hennessey2011). Showing a definition departs from this, which is a contrast with the trained raters in kempe2018, who used the memmert2007 scale. Phrase this only after the author has filled in the placeholder. **[AUTHOR TO CONFIRM]**
  5. **Procedure and allocation.**
     - Software goes first: `[**FILL IN:** rating software (name, version) and order of presentation (e.g., randomised per rater)]{.mark}`
     - Allocation goes next: `[**FILL IN:** how actions were assigned to raters (e.g., planned overlapping rater pairs, a benchmark set rated by all raters, or free selection)]{.mark}`
     - Sessions go last: `[**FILL IN:** session structure (session length, breaks, number of sessions per rater)]{.mark}`
- **Author note:** the vault describes a planned design (a benchmark set plus overlapping rater pairs; about 1 h sessions; dossier T8), but the plan figures differ from the realised design. The writer must not use vault plan figures.
- **Findings/objects:** F0.2, F0.6.
- **Citekeys:** amabile1982; hennessey2011; kempe2018; memmert2007.

### 2.5 Data preprocessing (Move 2 + Move 4)

- **Purpose:** trace the path from raw export to analysed sample.
- **Content:**
  1. **Raw export.** The raw export had 9150 rows and 23 pseudonymised rater IDs (F0.1).
  2. **Cleaning steps** (Appendix A, `@tbl-cleaning-log`; F0.2):
     - "action not recognised" (1292 rows removed);
     - missing IDs (0);
     - out-of-range value (1 row, a rating of 0);
     - missing ratings (0);
     - duplicate rater–action pairs resolved by keeping the last entry (13 rows removed; 25 duplicated rows formed 11 pairs and 1 triple; in one pair the ratings differed).
  3. **Final sample.** 7844 ratings, 3669 actions, 22 raters (F0.2, F0.3).
  4. **Move 4 (problems).**
     - The raw export had 23 rater IDs, but the cleaned data have 22 (X3). The placeholder goes immediately after the sentence that gives both counts: `[**FILL IN:** which of the 23 pseudonymised rater IDs was removed, at which cleaning step, and why]{.mark}`
     - The keep-last rule is an assumption. Rationale: `[**FILL IN:** rationale for keeping the last entry for duplicate rater–action pairs]{.mark}`
- **Writer cautions:**
  - Do not quote the printout "7858 -> 7844" as the overall cleaning (X8).
  - Never embed or reproduce 00 cell `520638b8`, which leaks original user IDs (X2).
- **Findings/objects:** F0.1, F0.2, F0.3; `@tbl-cleaning-log` (Appendix A).

### 2.6 Realised rating design and descriptive agreement (Move 2 + Move 4)

This subsection carries the descriptive design and Krippendorff's α (author decision 2).

- **P2.6a Design.**
  - Purpose: describe the sparse design the model must handle.
  - Content:
    - 7844 ratings, 3669 actions and 22 raters; 2.137912237666939 ratings per action on average and a harmonic mean of 1.726320341325184 (F0.3, F0.4).
    - Of the actions, 898 have 1 rating, 2080 have 2 and 691 have 3 or more, with a maximum of 12. Shares: 0.2447533387844099, 0.5669119651131098 and 0.18833469610248024 (F0.4).
    - Ratings per rater: median 316.5, range 2–1174 (F0.5).
    - Invite the reader to `@tbl-overview-ratings-per-action` (main text). Degree distributions are in Appendix B (`@fig-overview-degree-distributions`).
- **P2.6b Connectivity.**
  - Purpose: show that one common scale is identified.
  - Content:
    - The rater–action graph forms a single connected component containing all actions and raters, so no data were excluded for connectivity (F0.3).
    - Overlap with the best-connected partner ranges widely. Three raters share fewer than 15 actions with their best-connected partner (R22, R21, R20; F0.5). Pairwise overlap is in Appendix B (`@fig-overview-rater-overlap`).
    - Move 4: R22 (2 ratings), R21 (9) and R20 (13) contribute very little information (F0.5).
- **P2.6c Allocation check.**
  - Purpose: describe how action types were distributed across raters, which bears on the assumption of ignorable missingness.
  - Content:
    - χ² test of rater × action type: χ²(210) = 1260.2, p = 3.618e-149 (display as *p* < .001), Cramér's V = 0.127 (F0.10).
    - Row percentages differ between raters. Example: the share of passes ranges from 46.5% (R13) to 77.8% (R21) (F0.10).
    - Move 4: 49% of cells have expected counts below 5, so the approximation is rough (F0.10).
  - Placement: here, not in Results.
- **P2.6d Krippendorff's α (author decision 2; in-text only, no embed).**
  - Purpose: give one crude descriptor of raw agreement for comparability with CAT reporting habits.
  - Content:
    - Krippendorff's α (interval level), computed on the incomplete rater × action matrix, is 0.41813163607566517. It is based on the 2771 actions with at least 2 ratings (share 0.75524666121559) (F0.7).
    - Mandatory wording: describe α explicitly as a **crude agreement index that treats raters as interchangeable** (the notebook's own wording, F0.7). It is not a reliability of the JRT scores, and no confidence interval is available.
    - Move 4: the interval level treats the ordinal categories as equally spaced. **[AUTHOR TO CONFIRM whether to note this]**
    - `[**FILL IN:** version of the krippendorff Python package]{.mark}` goes in 2.10 (software), not here.
- **Findings/objects:** F0.3, F0.4, F0.5, F0.7, F0.10; `@tbl-overview-ratings-per-action` (main); `@fig-overview-degree-distributions` and `@fig-overview-rater-overlap` (Appendix B).

### 2.7 Judge response theory model (Move 2 + Move 3)

- **P2.7a Specification.**
  - Purpose: give the model exactly as coded (F1.0a).
  - Content:
    - η_ij = a_j·θ_i + λ_j and Pr(Y_ij ≤ k) = logit⁻¹(τ_k − η_ij), with six ordered cutpoints shared by all raters (ordered logistic).
    - θ_i is action creativity; a_j is rater discrimination; λ_j is rater leniency relative to the average rater (sum-to-zero; higher means more lenient).
    - Move 3: this is a graded-response formulation (samejima1969) within the JRT framework (myszkowski2019; myszkowski2021), constrained to shared thresholds plus a rater-specific location shift. Rater-specific thresholds b_jk were not estimated, so a common category structure is **assumed, not tested** (F1.0a). Move 4: say this plainly.
- **P2.7b Identification and priors.**
  - Purpose: reproducibility (F1.0a).
  - Content:
    - θ_i ~ N(0, 1), which fixes the scale.
    - λ_j ~ ZeroSumNormal(σ_λ), with σ_λ ~ Exp(1).
    - log a_j = mu_log_a + log_a_raw·sigma_log_a (non-centred), with log_a_raw ~ N(0, 1), mu_log_a ~ N(0, 1) and sigma_log_a ~ Exp(2).
    - τ ~ N(linspace(−2.5, 2.5, 6), 1.5) with an ordered transform.
  - Optional placeholder after the priors: `[**FILL IN:** rationale for the prior choices (e.g., weakly informative on the logit scale)]{.mark}` **[AUTHOR TO CONFIRM whether to include]**
- **P2.7c Equal-discrimination model.**
  - Purpose: define the nested comparison model.
  - Content:
    - Same model with log a_j = mu_log_a for all raters, so sigma_log_a is absent. Everything else is identical (F1.0a).
    - Framing: a constraint within JRT that corresponds to judges discriminating equally, as Rasch-family models assume. It is not a rival scoring approach.
- **P2.7d Scores.**
  - Purpose: define the action scores.
  - Content: the posterior mean of θ_i serves as the action's score, with its posterior SD as the standard error and a 95% credible interval (F3.2, F3.3).
- **Findings/objects:** F1.0a.
- **Citekeys:** samejima1969; myszkowski2019; myszkowski2021.

### 2.8 Estimation and model checking (Move 2 + Move 4)

- **Purpose:** make the estimation reproducible and state the criteria used.
- **Content:**
  - **Sampler.** PyMC (abrilpla2023), NUTS (hoffman2014), 4 chains × 2000 draws after 2000 tuning steps, target_accept = 0.95, jitter+adapt_diag initialisation, seed 20260713. The equal-discrimination model used the same settings (F1.0b).
  - **Convergence criteria** (as stated in the notebook; F1.1): rank-normalised split R-hat < 1.01, bulk and tail ESS > 400, no divergent transitions (vehtari2021). Diagnostics were computed with ArviZ (kumar2019a).
  - **Posterior predictive check.** Observed category shares and observed rater means were compared with 95% posterior predictive intervals. Replicates were drawn from every 10th posterior draw (F1.4).
    - Placeholder right after this sentence: `[**FILL IN:** number of posterior predictive replicate data sets (not printed by the notebook)]{.mark}`
  - **Interval conventions** (X9): 95% intervals (2.5th–97.5th percentiles) for rater parameters, PPC and scores; 89% equal-tailed intervals for thresholds and hyperparameters (the exported summary). State both conventions explicitly.
  - **Move 4.** No prior predictive checks or prior-sensitivity analyses were run ("Not found"). State this here in one sentence.
- **Findings/objects:** F1.0b, F1.1, F1.4.
- **Citekeys:** abrilpla2023; hoffman2014; vehtari2021; kumar2019a.

### 2.9 Model comparison, information and reliability (Move 2 + Move 3)

- **P2.9a PSIS-LOO.**
  - Purpose: define the RQ1 comparison.
  - Content:
    - Models are compared by the expected log pointwise predictive density estimated with Pareto-smoothed importance-sampling leave-one-out cross-validation (vehtari2017).
    - The SE of the difference is computed from the pointwise differences, sqrt(N·var(pointwise difference)) (F2.6).
    - Pareto-k > 0.7 flags observations for which the approximation is unreliable (vehtari2017). The notebook reports the share of such observations (F2.6).
    - Placeholder right after the SE sentence: `[**FILL IN:** decision criterion used to judge the elpd difference (e.g., difference relative to its SE) and whether it was specified before the analysis]{.mark}` The findings do not document any decision rule.
    - Status: exploratory comparison **[AUTHOR TO CONFIRM a priori vs. exploratory]**.
- **P2.9b Information.**
  - Purpose: define rater information.
  - Content:
    - Graded-response Fisher information per rater, computed by plugging in the posterior means of a_j, λ_j and τ_k on a θ grid from −4 to 4 in steps of 0.02 (F2.5).
    - The mean information per rating across the pool is defined in the same way.
    - Move 4: these are plug-in values with no posterior uncertainty.
- **P2.9c Reliability.**
  - Purpose: define the RQ2 quantities (F3.1).
  - Content:
    - **Empirical reliability:** Var(θ̂) / [Var(θ̂) + mean(PSD²)].
    - **Marginal reliability** for k judges per action: 1 / (1 + ∫φ(θ)[k·Ī(θ)]⁻¹dθ), where Ī is the mean plug-in information across the 22 raters (green1984).
    - **D-study:** evaluated for k = 1–10 and at the realised harmonic-mean k.
    - Move 3: the IRT analogue of Spearman–Brown or G-theory D-studies (amabile1982; background only).
    - Move 4: the D-study assumes judges drawn at random from the pool with equal weights. It does not weight raters by their actual rating volume and gives no uncertainty (F3.1, F3.4).
- **Findings/objects:** F2.5, F2.6, F3.1, F3.4.
- **Citekeys:** vehtari2017; green1984; amabile1982.

### 2.10 Software, reproducibility and data availability

- **Purpose:** reproducibility.
- **Content:**
  - Python "3.12.3"; numpy 2.4.6, pandas 3.0.3, scipy 1.18.0, matplotlib 3.11.0, networkx 3.6.1, pymc 6.1.0, arviz 1.2.0 (F1.0b). Wall clock and run log are optional.
  - Preprocessing and descriptives ran in a Python 3.12.9 kernel (F1.0b caveat, X10).
  - Package versions, placed after the version list: `[**FILL IN:** versions of packages used in the preprocessing and descriptive notebooks (including krippendorff) and the PyTensor version]{.mark}`
  - Code archive, next: `[**FILL IN:** code repository and commit hash or archived DOI (the JRT run reports git_commit "not available")]{.mark}`
  - Data availability, closing the subsection: `[**FILL IN:** data and code availability statement (repository/OSF link; licence constraints for StatsBomb-derived and video material)]{.mark}`
- **Findings/objects:** F1.0b, X10.

---

## 3. Results

- **Purpose:** describe what was found, ordered by RQ. This section is **descriptive only**; interpretation goes in the Discussion.
- **Model:** results.md.
  - Move 1 opens the section.
  - Move 2 repeats in each subsection: invite the reader to a figure or table, then present the key results.
  - Move 3 (problems) is integrated where it arises.
  - Move 4 is a single hedged closing sentence.
- **Writer rules:**
  - Prefer pointing to tables over restating every value.
  - Quote only F-ID values.
  - No plot-read values.

### 3.1 Overview and model estimation (Move 1 + Move 3)

- **P3.1a Opening.**
  - Purpose: echo the aim.
  - Content: restate the aim in the Introduction's wording, then give the order: estimation and fit → RQ1 (category use, leniency, discrimination, equal-discrimination comparison, information) → RQ2 (reliability, precision, D-study).
- **P3.1b Convergence and fit.**
  - Purpose: establish trust in the estimates.
  - Content:
    - Rater-specific model (F1.1): 0 divergences; largest split R-hat 1.004775; smallest bulk ESS 2014.040992; smallest tail ESS 3033.626914. Every parameter group met the stated criteria, and no warnings were logged. Details are in Appendix C (`@tbl-jrt-convergence`, `@fig-jrt-traceplots`).
    - Equal-discrimination model (F1.2): 0 divergences; largest R-hat 1.003762; smallest ESS 1552.024542. In-text in Appendix C.
    - Posterior predictive check (F1.4): all 7 of 7 observed category shares and all 22 of 22 observed rater means fell inside their 95% posterior predictive intervals (Appendix D, `@fig-jrt-ppc`).
    - Move 3: the check covers only pooled category shares and rater means, not per-rater category distributions or action-level checks (F1.4).
  - The trace plots are visual and NOT QUOTABLE.
- **Findings/objects:** F1.1, F1.2, F1.4; `@tbl-jrt-convergence`, `@fig-jrt-traceplots`, `@fig-jrt-ppc` (all Appendix).

### 3.2 RQ1: Judge behaviour

**P3.2a Category use.**
- Purpose: describe how the scale was used (RQ1, category use).
- Content:
  - Invite the reader to `@fig-overview-rating-distribution`.
  - Categories 1 and 2 account for 0.5290668026517084 of all ratings, and categories 6 and 7 for 0.05736868944416114.
  - Category 2 is the most frequent (2116) and category 7 the least (109). From category 2 upward, frequency falls with each higher category (F0.6).
- Findings/objects: F0.6; `@fig-overview-rating-distribution` (main).

**P3.2b Shared thresholds.**
- Purpose: describe the model's category structure.
- Content:
  - The six shared cutpoints rise from -2.25336 to 6.441121 (posterior means; 89% ETIs in Appendix E, `@tbl-jrt-model-summary`) (F1.3).
  - The gaps between consecutive cutpoints are 2.0531452144114093, 1.4309147172774972, 1.3486183730574282, 1.6737964330037762 and 2.188005717864627. The smallest gap is between cutpoints 3 and 4, and the largest between cutpoints 5 and 6 (F1.3; `@tbl-jrt-derived-counts`).
  - Caution: the gap labels index cutpoints, not rating categories (F1.3 caveat). Word them as "between the third and fourth cutpoints".
  - Move 3: these thresholds are shared by all raters, so individual scale use is captured only through leniency (cross-reference to 2.7).
- Findings/objects: F1.3; `@tbl-jrt-model-summary`, `@tbl-jrt-derived-counts` (Appendix E).

**P3.2c Descriptive rater response styles.**
- Purpose: show raw rater differences before modelling.
- Content:
  - Invite the reader to `@fig-overview-rater-response-styles`.
  - Raw rater means range from 1.7596153846153846 (R06) to 3.8363636363636364 (R18) (F0.8).
  - R06 has the highest floor rate (0.5788461538461539), and five raters have a ceiling rate of 0.0 (F0.8).
  - Move 3: R22, R21 and R20 rest on very few ratings (F0.8).
- Findings/objects: F0.8; `@fig-overview-rater-response-styles` (main).

**P3.2d Leniency.**
- Purpose: answer the first part of RQ1 (leniency).
- Content:
  - Invite the reader to `@fig-jrt-rater-parameters` (panel B). The full table is in Appendix E (`@tbl-jrt-rater-parameters`).
  - Posterior-mean leniency ranges from -2.9279955470625105 (R06) to 1.6348645170687754 (R18) (F2.1).
  - σ_λ = 1.232476 (89% ETI 0.956799 to 1.583755) (F1.3, F2.3).
  - For 16 of the 22 raters, the 95% interval excludes 0: 8 are more lenient and 8 less lenient than the average rater (F2.3).
  - Descriptive correspondence only: the raters with the lowest and highest leniency (R06, R18) are also the raters with the lowest and highest raw means (F0.8, F2.1).
  - Move 3: the intervals for R20, R21 and R22 include 0 (F2.1 caveat). λ_j is relative to the average rater, not to an absolute zero (F2.3).
- Findings/objects: F1.3, F2.1, F2.3, F0.8; `@fig-jrt-rater-parameters` (main), `@tbl-jrt-rater-parameters` (Appendix E).

**P3.2e Discrimination.**
- Purpose: answer the second part of RQ1 (discrimination).
- Content:
  - Invite the reader to `@fig-jrt-rater-parameters` (panel A).
  - Posterior-mean a_j has a median of 2.0844708365638205 and ranges from 0.9569497104368692 (R18) to 3.2408227509685186 (R02). The max/min ratio is 3.3866176201558282 (F2.1; `@tbl-jrt-derived-counts`).
  - No rater falls below 0.5 (F2.1).
  - Pool discrimination exp(mu_log_a) (posterior median) is 1.8680804941316524. mu_log_a = 0.622311 and sigma_log_a = 0.388639 (89% ETIs in F2.4) (F2.2, F2.4).
  - **Pool-discrimination count.** Use the notebook's definition (X4) and state it in the sentence. Mandatory wording, adapted: "For 11 of the 22 raters, the 95% credible interval of the deviation of their log discrimination from the pool mean (log a_j − mu_log_a) excluded zero: 6 above and 5 below the pool (F2.2)."
  - Add a figure note or sentence: the figure shows the marginal 95% intervals of a_j against the pool point value. A visual count can therefore differ from the reported count (R07, R08 and R14 have marginal lower bounds above the dashed line, but their deviation intervals include 0; X4).
  - Mention that R09's lower bound is close to 0 (F2.2 caveat). **[AUTHOR TO CONFIRM whether to mention]**
  - Move 3: posterior SDs of a_j are largest for the raters with the fewest ratings (R22 0.6786987089652162, n = 2; R20 0.5798476500178956; R21 0.49999548951006645) (F2.1 caveat).
  - **Caution:** do **not** present "the 89% interval of sigma_log_a excludes 0" as evidence of heterogeneity. sigma_log_a has an Exp(2) prior with positive support, so the interval cannot include 0. The evidence for heterogeneity is the LOO comparison (P3.2f) and the deviation counts.
- Findings/objects: F2.1, F2.2, F2.4, X4; `@fig-jrt-rater-parameters` (main), `@tbl-jrt-rater-parameters`, `@tbl-jrt-derived-counts` (Appendix E).

**P3.2f Equal-discrimination comparison.**
- Purpose: answer the third part of RQ1 (tenability of equal discrimination).
- Content:
  - Invite the reader to `@tbl-jrt-equal-discrimination-loo`.
  - The rater-specific model has the higher elpd_loo: -11537.930567469428 vs. -11701.18535331233 for the equal model. elpd_diff = 163.25478584290235 (SE 19.684919284549657), a ratio printed as 8.3 (F2.6).
  - Relate this to the criterion in the placeholder in 2.9 only once the author has filled it in. Until then, state the difference and its SE without a verdict word.
  - p_loo is 2573.6857918258565 (rater-specific) and 2375.8767147154235 (equal). State this neutrally.
  - Move 3 (Pareto-k):
    - ArviZ warned that k > 0.7 for some observations in both models (F2.6).
    - The shares with k > 0.7 were 0.02804691483936767 (rater-specific) and 0.0014023457419683834 (equal).
    - **Nothing beyond these shares is available**: no count, no maximum k, no share with k > 1 and no re-check (F2.6, X5). The writer must not imply that any re-check was done.
- Findings/objects: F2.6, X5; `@tbl-jrt-equal-discrimination-loo` (main).

**P3.2g Rater information.**
- Purpose: show where on the latent scale individual raters are informative.
- Content:
  - Invite the reader to `@fig-jrt-category-curves-information` (raters with the lowest, median and highest discrimination).
  - Peak information per rater ranges from 0.28630034428415285 (R18) to 3.2836317353059203 (R02) (F2.5).
  - The mean information per rating across the pool peaks at 1.3335752264232335, at θ = 0.7400000000000002 (display as 0.74) (F2.5).
  - Descriptive pairing only: raters with lower leniency tend to have their information peak at higher θ (e.g., R06 peaks at θ = 1.74 and R01 at 2.10) (F2.5).
  - Move 3: these are plug-in values without uncertainty, resolved on a grid of 0.02 (F2.5).
  - Never quote the pool-sum curve (NOT QUOTABLE).
- Findings/objects: F2.5; `@fig-jrt-category-curves-information` (main).

### 3.3 RQ2: Reliability and number of judges

**P3.3a Reliability at the realised panel size.**
- Purpose: give the realised reliability.
- Content:
  - Empirical reliability of the JRT scores is 0.6603541094329908.
  - Marginal reliability at the realised harmonic-mean k (1.726320341325184) is 0.6462162523422212. These are different quantities (F3.1).
  - The posterior-mean scores have an SD of 0.813 across actions and range from -2.08 to 3.08. These are printed values; no unrounded summary exists, so quote them as printed (F3.2).
  - Move 3: no interval is available for either reliability (F3.1).
- Findings/objects: F3.1, F3.2.

**P3.3b Precision by number of ratings.**
- Purpose: show how score precision varies across actions.
- Content:
  - Invite the reader to `@tbl-jrt-score-precision`.
  - The mean posterior SD of θ falls from 0.6506952848078058 (1 rating; 898 actions) to 0.39954470672839787 (5 or more ratings; 211 actions). Mean 95% interval width falls from 2.575876218002324 to 1.5694773558748427 (F3.3).
  - Both decrease monotonically with the number of ratings.
  - Move 3: the ranges overlap heavily between groups (F3.3 caveat).
- Findings/objects: F3.3; `@tbl-jrt-score-precision` (main).

**P3.3c D-study.**
- Purpose: answer the second part of RQ2.
- Content:
  - Invite the reader to `@fig-jrt-information-reliability` (panel B) and `@tbl-jrt-d-study`.
  - Marginal reliability rises from 0.514110299035415 at k = 1 to 0.91365019867287 at k = 10. The largest one-step increase is from k = 1 to k = 2 (0.6790922687243275) (F3.4).
  - Values at or above .80 start at k = 4 (0.8088802281726432), and values at or above .90 start at k = 9 (0.9049675576934999) (F3.4).
  - Optional reading straight from the table, with no new value: the tabled values first exceed .70 at k = 3 (0.7604354765814204). **[AUTHOR TO CONFIRM use of .70/.80/.90 benchmarks; .70 echoes the CAT convention in P2.1]**
  - Panel A of the figure is referenced for the mean information per rating only. The pool-sum curve is NOT QUOTABLE.
  - Move 3: these are model-based projections under the assumption of random judges, with no uncertainty bands (F3.4 caveat).
- Findings/objects: F3.4; `@fig-jrt-information-reliability` (main), `@tbl-jrt-d-study` (main).

### 3.4 Closing (Move 4)

- One hedged sentence, Past Simple: the results indicated that raters in this dataset differed in leniency and discrimination, and that action-level precision at the realised panel size was limited. **[AUTHOR TO CONFIRM]**

---

## 4. Discussion

- **Purpose:** say what the results mean for CAT methodology in sport, position them in the CAT, MFRM and JRT literatures, give practical recommendations, and state limitations honestly.
- **Model:** discussion-conclusion.md, four moves, widening out.
- **Every interpretive sentence is [AUTHOR TO CONFIRM].**
- Competitor approaches appear as literature only. No competitor scores were computed.

### Move 1: Revisit aim and key results

**D1.1 Summary.**
- Purpose: echo the aim and RQs.
- Content:
  - Raters differed in leniency and discrimination (F2.1–F2.3).
  - Rater-specific discrimination predicted better than equal discrimination (F2.6).
  - Reliability at about two judges per action was modest, and the D-study showed how it rises with k (F3.1, F3.4).
  - Use no new numbers beyond those already in Results.

### Move 2: Mapping to existing research

**D2.1 Judges are not interchangeable.** [AUTHOR TO CONFIRM]
- Content:
  - Consistent with JRT applications that report differing judge discrimination (myszkowski2021; barbot2023; pellegrino2025).
  - Consistent with long2015's attribution of low agreement to rater differences.
  - Extends primi2019's severity findings: discrimination differences have no parameter in the MFRM (myford2004).
  - Literature context only: judge monitoring in judged sports treats judge quality as an individual property (looney2004; anderlucci2021; heiniger2021).
- Findings: F2.1, F2.2, F2.6.

**D2.2 Consequences for mean and Rasch-family scoring.** [AUTHOR TO CONFIRM]
- Content:
  - Equal weighting of judges, as in mean scores and Rasch-family fair averages, rests on an assumption these data did not support (myszkowski2019; primi2019).
  - Explicitly an argument from the literature: no comparison of scoring methods was performed.
- Findings: F2.6.

**D2.3 Panel size.** [AUTHOR TO CONFIRM]
- Content:
  - Relate the D-study to the 5–10-judge rule of thumb (kaufman2008a) and to cseh2019's call for domain-specific evidence.
  - Relate the realised reliability to the ≥ .70 convention for expert panels (baer2004; kaufman2008), noting that coefficients from different frameworks are not directly comparable.
  - Compare with kempe2018 (three trained experts, ICC).
  - Mention Krippendorff's α only with its caveat: a crude index that treats raters as interchangeable, a different quantity from the model-based reliabilities. Do not compare its size with them.
- Findings: F0.7, F3.1, F3.4.

**D2.4 Scale use and where the panel is informative.** [AUTHOR TO CONFIRM; speculative]
- Content:
  - Ratings concentrate in the low categories (F0.6), and pool information peaks above the average θ (F2.5).
  - Possible reading: most match actions are routine, and the panel discriminates best among more creative actions. This could matter if the aim is to identify creative actions.
  - Less lenient raters' information peaks at higher θ (F2.5, descriptive pairing).
- Findings: F0.6, F2.5.

### Move 3: Contribution and refined implications (all [AUTHOR TO CONFIRM])

**D3.1 Contribution.**
- Content: Present Perfect ("We have shown…"), hedged with "to our knowledge" (see Central contribution).

**D3.2 Why raters might differ in discrimination.**
- Content: hypotheses only, since no rater covariates were collected or analysed:
  - expertise as a continuum (kaufman2009; kaufman2013; plucker2009);
  - rater characteristics and motivation (ceh2022);
  - workload and attention (forthmann2017; ling2014);
  - understanding of the instructions or the definition (myszkowski2021).
- Link to the FILL IN placeholders on rater background.

**D3.3 Practical recommendations for sport science.**
1. Use a connected design with sufficient overlap per rater; rater parameters depend on the linking set (wind2018; wind2019a). See F0.3 and F0.5 (raters with little overlap).
2. Score with JRT (or at least a model with rater leniency) rather than raw means when raters rate different subsets (primi2019; myszkowski2019).
3. Plan the number of judges per action from a D-study or pilot rather than a fixed rule (F3.4; forthmann2023). Use planned-missing designs to manage workload (primi2019; forthmann2023).
4. Use discrimination estimates for rater feedback, screening or calibration (storme2014; dollinger2005; weigle1998), weighing this against the CAT's principle of no imposed criteria.
5. Consider precision when action scores are used downstream, e.g., as outcomes or as labels for automated rating. No citable source exists, so mark it as the author's own argument. **[AUTHOR TO CONFIRM]**

### Move 4: Limitations and future work (pair each with a next step)

**D4.1 Scope versus the original aims.**
- Rater expertise, rating-scale choices (number of categories, labels) and comparisons of rating-processing techniques (means, MFRM, G-theory) were not examined.
- Future work: compare coaches, players and lay raters with JRT discrimination as the outcome (kaufman2013; zamparo2017); vary the scale; compare scoring approaches on the same data.

**D4.2 Shared thresholds.**
- Response styles beyond leniency were not modelled, and the shared category structure was not tested (F1.0a).
- Future work: JRT GRM or GPCM with rater-specific thresholds (myszkowski2021), which needs more ratings per rater.

**D4.3 Sparse design and weakly informed raters.**
- About two ratings per action (F0.4). R20–R22 have few ratings, wide intervals and little overlap (F0.5, F2.1).
- Future work: a benchmark set rated by all judges (wind2019a).

**D4.4 Non-random allocation.**
- Action types differed between raters (F0.10), which threatens ignorable missingness.
- Future work: randomised allocation.

**D4.5 Rater drift.**
- 3 of 20 raters had |ρ| > .2 between rating and rating order: R01 -0.3001559154879249, R09 -0.3677232235594994, R12 0.20248946268481147. This indicator is descriptive only, with no inference (F0.9). The drift values are not reported elsewhere; they appear here and in Appendix B text.
- Future work: a time facet; frameworks for monitoring rater drift (myford2009; leckie2011; barth2020); differential rater functioning (wind2019b); the hierarchical rater model (patz2002) or a generalised MFRM (uto2020) for multi-facet designs.

**D4.6 Computational.**
- Pareto-k warnings with limited detail (F2.6, X5); large p_loo (F2.6); plug-in information (F2.5); no uncertainty for the reliabilities or the D-study (F3.1, F3.4); no prior sensitivity; a limited PPC (F1.4).
- Future work: moment matching or k-fold CV; propagating posterior uncertainty into the reliability estimates.

**D4.7 Validity.**
- One dimension only, with no external criterion. Technical-correctness and aesthetic-appeal ratings were collected but not analysed.
- Future work: discriminant validity (amabile1982; zamparo2017) and criterion validity, such as proximity to goals (kempe2018).

**D4.8 Generalisability.**
- One sport, one action pool and one rater sample. Pair this with the reproducible template as the positive counterpart.

---

## 5. Conclusion

- **Purpose:** a standalone take-home of one short paragraph.
- **Content:**
  - Restate the contribution in one sentence each:
    - raters differ in leniency and discrimination;
    - equal discrimination predicted worse;
    - the realised panel size gives modest reliability, which the D-study shows rising with more judges.
  - Use no numbers beyond those in the Abstract.
  - Main recommendation **[AUTHOR TO CONFIRM]**: CAT studies in sport should model judges rather than average them, and should plan panel size empirically.
  - Close with one forward-looking sentence: rater expertise, rater-specific thresholds, scoring comparisons.
- **Findings:** F2.1, F2.6, F3.4.

---

## Appendix (inside the same manuscript; all labels must resolve)

- **Appendix A. Data processing.**
  - `@tbl-cleaning-log` (F0.2), with the 23→22 rater placeholder echoed from 2.5.
- **Appendix B. Rating design.**
  - `@fig-overview-degree-distributions` (F0.4, F0.5).
  - `@fig-overview-rater-overlap` (F0.5).
  - Text only: the drift indicator (F0.9) as a short paragraph.
- **Appendix C. Estimation diagnostics.**
  - `@tbl-jrt-convergence` (F1.1).
  - `@fig-jrt-traceplots` (visual only; NOT QUOTABLE).
  - Text: convergence of the equal-discrimination model (F1.2), including the note that its a_j group equals the hyperparameter group.
- **Appendix D. Posterior predictive check.**
  - `@fig-jrt-ppc` (F1.4), with the replicate-count placeholder echoed from 2.8.
- **Appendix E. Parameter summaries.**
  - `@tbl-jrt-model-summary` (89% ETIs; F1.3, F2.4).
  - `@tbl-jrt-rater-parameters` (95% intervals; F2.1).
  - `@tbl-jrt-derived-counts` (F1.3, F2.2, F2.3, F2.5, F0.6). Its caption says "used in the text", so cross-reference it from the Results sentences that use those values.

## Placement of all 18 objects

| # | Label | Placement | Section that references it |
|---|---|---|---|
| 1 | tbl-cleaning-log | Appendix A | 2.5 |
| 2 | tbl-overview-ratings-per-action | **Main** | 2.6 |
| 3 | fig-overview-rater-overlap | Appendix B | 2.6 |
| 4 | fig-overview-rating-distribution | **Main** | 3.2a |
| 5 | fig-overview-rater-response-styles | **Main** | 3.2c |
| 6 | fig-overview-degree-distributions | Appendix B | 2.6 |
| 7 | tbl-jrt-convergence | Appendix C | 3.1 |
| 8 | tbl-jrt-model-summary | Appendix E | 3.2b, 3.2e |
| 9 | tbl-jrt-rater-parameters | Appendix E | 3.2d, 3.2e |
| 10 | fig-jrt-rater-parameters | **Main** | 3.2d, 3.2e |
| 11 | fig-jrt-traceplots | Appendix C | 3.1 |
| 12 | fig-jrt-ppc | Appendix D | 3.1 |
| 13 | tbl-jrt-equal-discrimination-loo | **Main** | 3.2f |
| 14 | fig-jrt-category-curves-information | **Main** | 3.2g |
| 15 | fig-jrt-information-reliability | **Main** | 3.3c |
| 16 | tbl-jrt-d-study | **Main** | 3.3c |
| 17 | tbl-jrt-score-precision | **Main** | 3.3b |
| 18 | tbl-jrt-derived-counts | Appendix E | 3.2b, 3.2e |

**Main text: 5 figures and 4 tables.** If space is tight, `fig-overview-rater-response-styles` is the first candidate to move to Appendix B. **[AUTHOR TO CONFIRM]**

**Embedding hazards (02_artifacts §3; for the author):**
- Labelled cells also print stdout/stderr text into the embeds (P6). This includes the NUTS progress lines and the Pareto-k warning in `tbl-jrt-equal-discrimination-loo`, and "Sampling: [y_obs]" in `fig-jrt-ppc`.
- `fig-jrt-category-curves-information` also renders a 22-row information table (P5).
- Both need notebook cell options or a split display cell. Agents must not edit the notebooks.

---

## Number display (writer decisions; display rounding only, never new values)

- **APA conventions:**
  - no leading zero for quantities bounded by 1 (reliabilities, α, shares written as proportions, Cramér's V);
  - two decimals for reliabilities and α (e.g., 0.6603541094329908 → .66; 0.41813163607566517 → .42);
  - two decimals for parameters, e.g., a_j range 0.96–3.24. This matches the notebook's own printout "[0.96, 3.24]", median "2.08" and pool "1.87".
  - elpd values to one or two decimals (163.25478584290235 → 163.25 or 163.3; the notebook prints 163.3 and SE 19.7);
  - *p* = 3.618e-149 → *p* < .001.
  - Percentages from shares: 0.2447533387844099 → 24.5%. Note that the notebook prints "24%" (F0.4). The writer should be consistent with one convention.
- **Quote as printed (no unrounded value exists):** score SD 0.813 and range −2.08 to 3.08 (F3.2); χ² = 1260.2 and V = 0.127 (F0.10); the 8.3 ratio (F2.6).
- **Grid values:** θ = 0.7400000000000002 → 0.74. Grid values must not be shown with spurious precision.
- **Medians:** report the median ratings per rater as 316.5, not the printed "316" (X8).
- **Interval width:** always state 95% vs. 89% next to each interval (X9).

---

## Complete list of FILL IN placeholders (verbatim syntax and location)

| # | Location | Placeholder |
|---|---|---|
| 1 | 2.1, sentence 2 | `[**FILL IN:** ethics approval (committee, reference number) and informed-consent procedure for raters]{.mark}` |
| 2 | 2.1, after ethics | `[**FILL IN:** preregistration status (registry and ID, or statement that the study was not preregistered)]{.mark}` |
| 3 | 2.1, end | `[**FILL IN:** data-collection period (start and end dates of rating)]{.mark}` |
| 4 | 2.2, after rater count | `[**FILL IN:** how raters were recruited (e.g., students rating as part of thesis projects), inclusion criteria, and compensation]{.mark}` |
| 5 | 2.2 | `[**FILL IN:** rater background and football expertise (e.g., number of raters holding a coaching licence, playing experience and level, years of involvement)]{.mark}` |
| 6 | 2.2 | `[**FILL IN:** rater demographics (age, gender), if collected]{.mark}` |
| 7 | 2.3, after StatsBomb sentence | `[**FILL IN:** video source of the clips and the competitions, seasons and matches sampled]{.mark}` |
| 8 | 2.3 | `[**FILL IN:** how actions were selected from the event data (sampling frame, action types included or excluded)]{.mark}` |
| 9 | 2.3 | `[**FILL IN:** clip construction (clip length, pre-/post-action context, whether the target player or action was marked)]{.mark}` |
| 10 | 2.3, end | `[**FILL IN:** viewing conditions (device and screen, sound, whether replays or pausing were allowed, self-paced or fixed timing)]{.mark}` |
| 11 | 2.4, after scale sentence | `[**FILL IN:** verbatim verbal labels of the rating categories, including categories 2–6 (and the endpoint labels for 1 and 7)]{.mark}` |
| 12 | 2.4, off-scale option | `[**FILL IN:** exact wording of the "action not recognised" option and the instruction on when to use it]{.mark}` |
| 13 | 2.4, additional dimensions | `[**FILL IN:** wording and scale of the technical-correctness and aesthetic-appeal items]{.mark}` |
| 14 | 2.4, instructions | `[**FILL IN:** verbatim instructions given to raters, including the definition of creativity shown to them (original language and English translation)]{.mark}` |
| 15 | 2.4, instructions | `[**FILL IN:** whether any training, practice clips or anchor examples were provided, or a statement that none were]{.mark}` |
| 16 | 2.4, procedure | `[**FILL IN:** rating software (name, version) and order of presentation (e.g., randomised per rater)]{.mark}` |
| 17 | 2.4, procedure | `[**FILL IN:** how actions were assigned to raters (e.g., planned overlapping rater pairs, a benchmark set rated by all raters, or free selection)]{.mark}` |
| 18 | 2.4, procedure, end | `[**FILL IN:** session structure (session length, breaks, number of sessions per rater)]{.mark}` |
| 19 | 2.5, after 23 vs. 22 sentence (echoed in Appendix A) | `[**FILL IN:** which of the 23 pseudonymised rater IDs was removed, at which cleaning step, and why]{.mark}` |
| 20 | 2.5, keep-last rule | `[**FILL IN:** rationale for keeping the last entry for duplicate rater–action pairs]{.mark}` |
| 21 | 2.7b, after priors (optional) | `[**FILL IN:** rationale for the prior choices (e.g., weakly informative on the logit scale)]{.mark}` |
| 22 | 2.8, PPC sentence (echoed in Appendix D) | `[**FILL IN:** number of posterior predictive replicate data sets (not printed by the notebook)]{.mark}` |
| 23 | 2.9a, after SE sentence | `[**FILL IN:** decision criterion used to judge the elpd difference (e.g., difference relative to its SE) and whether it was specified before the analysis]{.mark}` |
| 24 | 2.10, after version list | `[**FILL IN:** versions of packages used in the preprocessing and descriptive notebooks (including krippendorff) and the PyTensor version]{.mark}` |
| 25 | 2.10 | `[**FILL IN:** code repository and commit hash or archived DOI (the JRT run reports git_commit "not available")]{.mark}` |
| 26 | 2.10, end | `[**FILL IN:** data and code availability statement (repository/OSF link; licence constraints for StatsBomb-derived and video material)]{.mark}` |

---

## Evidence gaps

Places where the intended argument (brief) or a planned claim lacks support in `03_findings.md`:

- **G1. Brief's broader aims.**
  - The brief promises to "systematically investigate agreement among various numbers of raters" and to "empirically evaluate the implications of various methodological choices" (raters, scales, processing techniques).
  - Only the model-based D-study (F3.4) and the equal-discrimination comparison (F2.6) are in scope. There is no subsampling of rater numbers and no comparison of processing techniques or scales.
  - These aims are narrowed (decision 1) and moved to limitations and future work (D4.1).
- **G2. Rater expertise.**
  - No rater background data exist ("Not found").
  - The brief's expertise question cannot be answered, so explanations of discrimination differences are hypotheses only (D3.2).
- **G3. Shared category structure.**
  - The brief's JRT paragraph says equal discrimination *and* a shared category structure become testable.
  - Only the former was tested. Thresholds are shared (F1.0a), so the Introduction must not imply otherwise.
- **G4. Uncertainty.**
  - There are no intervals for the reliabilities, the D-study, the information values or Krippendorff's α (F0.7, F2.5, F3.1, F3.4).
  - The review criterion "effect sizes and CIs reported" is met for model parameters (95% CrIs and 89% ETIs) and for the elpd difference (SE), but not for the reliabilities. State this openly.
- **G5. PSIS-LOO robustness.**
  - Only the k > 0.7 shares are available. There is no count, no maximum k, no share with k > 1 and no re-check (F2.6, X5).
  - No decision criterion is documented (placeholder 23).
- **G6. A priori status of RQ1's comparison.** Unknown. **[AUTHOR TO CONFIRM]**
- **G7. Methods details.** 26 FILL IN placeholders (above), including the unexplained 23→22 rater reduction (X3).
- **G8. Validity.**
  - There is no external criterion.
  - The secondary dimensions are NOT QUOTABLE, so they cannot support discriminant-validity claims.
- **G9. Provenance.** 02d ran on another host with no git commit. Package versions for 00 and 01 are missing (X10).
- **G10. Heterogeneity evidence.** sigma_log_a's interval cannot include 0 under its prior (P3.2e caution). Heterogeneity claims must rest on F2.6 and F2.2.
- **G11. Literature verification.**
  - The worldeconomicforum2025 wording and the linacre1989 imprint are only partly verified.
  - The claims attributed to safardilha2019, memmert2011, batey2012 and barbot2019b are unverified from the vault.
  - The novelty search was not systematic (06 §C).
- **G12. Bibliography.**
  - santos2016 and memmert2007 exist in **both** `phd_library.bib` and `web_references.bib` (same papers, same keys). Remove one copy before rendering to avoid duplicate-key warnings.
  - The six targeted-addition keys were not found in the main bib by DOI, so there is no collision.
  - Use abrilpla2023, not salvatier2016.

## Open questions for the author (checkpoint)

1. Was RQ1's equal-discrimination comparison planned a priori or exploratory? Was anything preregistered?
2. Do you accept that the Introduction moves the formal aim to the end and keeps the brief's aim paragraph as a short bridge?
3. Do you endorse the novelty claim ("to our knowledge"), or do you want a database search first?
4. Main-text set: 5 figures and 4 tables. Should response styles move to the Appendix?
5. Benchmarks .70/.80/.90 in the D-study description: keep or drop?
6. Should the Methods note that α is computed at the interval level for ordinal categories?
7. Fill in placeholders 1–26, including the 23→22 rater step.
8. Fix the embed hazards (stdout/stderr; the information table in the category-curves cell) in the notebooks.
9. Check the WEF and safardilha2019 wording, and deduplicate the santos2016 and memmert2007 entries.
10. What is the CRJ abstract word limit and format?
