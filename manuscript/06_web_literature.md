# Web Literature Search — CAT Methodology in Sport Creativity Paper

Source dossier: `manuscript/01_dossier.md`
Brief: `/home/max/drive/KNOWLEDGE/Paper_CreativityAssessmentInSportsCAT.md`
Bibliography checked for duplicates: `/home/max/drive/phd_library.bib` (23,457 lines; read in full across the
"Creativity" cluster, roughly lines 5300–7100, plus targeted spot-checks elsewhere).

**Note on venue framing:** per instructions, this search prioritized general creativity-assessment /
psychometrics literature (the audience of *Creativity Research Journal*) over additional sports-science
papers. All new candidates below are mainstream creativity-psychometrics papers except the two sport-CAT
studies in Gap 3, which are included because the dossier explicitly asked for sport-CAT precedents.

## Pre-existing coverage confirmed in `phd_library.bib` (not duplicated below)

While checking for duplicates I confirmed the following are **already in the user's library** with full
metadata (no action needed, but flagged here because they are directly relevant to the gaps and the
manuscript-writer should know they don't need sourcing):

- `myszkowski2019`, `cseh2019`, `batey2012`, `barbot2019`, `barbot2019b`, `castel2007`, `baer2015`,
  `runco2012` — all already present (matches dossier section A).
- **`primi2019`** — Primi, R., Silvia, P. J., Jauk, E., & Benedek, M. (2019). Applying many-facet Rasch
  modeling in the assessment of creativity. *Psychology of Aesthetics, Creativity, and the Arts, 13*(2),
  176–186. **This is already in the library and is exactly the MFRM-in-creativity citation the dossier
  said was missing** (dossier gap: "No note on Many-Facet Rasch Models... as standalone concepts"). The
  manuscript can cite this directly for MFRM without needing a new source.
- `furley2015`, `santos2016`, `santos2017`, `fink2018`, `hristovski2007`, `hristovski2012` — existing
  sport-creativity papers in the library, but none use a CAT-style panel-of-judges rating design on
  discrete in-game actions the way Kempe & Memmert (2018) did (they study working memory, developmental
  frameworks, training programs, fMRI, or ecological-dynamics theory instead). See Gap 3 below for two new
  papers that are closer methodological analogues.

---

## Gap: "5–10 judges is adequate" and related judge-count/reliability citations (unlinked prose in `CreativityRatingStudy.md`)

**[kaufman2008]** Kaufman, J. C., Plucker, J. A., & Baer, J. (2008). *Essentials of Creativity Assessment.*
Wiley (Essentials of Psychological Assessment series).
- **DOI:** none (book; ISBN 978-0-470-13742-0)
- **Abstract summary:** A practitioner/researcher handbook covering divergent-thinking tests, the
  Consensual Assessment Technique, and other-rated/self-rated approaches to creativity assessment,
  including practical guidance on number and selection of judges.
- **Suggested citation context:** This is almost certainly the source the author's notes paraphrase as
  "Kaufman, Plucker, et al. (2008): for most purposes 5–10 judges is adequate" (author order matches
  exactly: Kaufman, Plucker, Baer). I could not access the exact page/quote to verify the "5–10" figure
  verbatim (no preview access), so flag this for the author to confirm the specific page reference before
  citing the number directly. Cite in Introduction/Method when justifying the number of judges chosen for
  the benchmark/pairwise rating design.

**[kaufman2008b]** Kaufman, J. C., Baer, J., Cole, J. C., & Sexton, J. D. (2008). A comparison of expert
and nonexpert raters using the Consensual Assessment Technique. *Creativity Research Journal, 20*(2),
171–178.
- **DOI:** `10.1080/10400410802059929`
- **Abstract summary:** Compares CAT ratings from expert and non-expert (novice) judges across creative
  writing tasks; expertise affected some aspects of judgment but non-experts were still meaningfully
  discerning, foreshadowing the domain-general vs. domain-specific expertise debate central to this paper.
- **Suggested citation context:** Found while searching for the "5–10 judges" source; not explicitly
  requested in the dossier but a strong direct fit for the "effect of expertise" research question
  (alongside Kaufman et al. 2008 book, Plucker et al. 2009, and Baer 2015 already in the library). Cite in
  Introduction/Discussion alongside Plucker et al. (2009) when discussing whether expert judges are
  necessary.

**[baer2004]** Baer, J., Kaufman, J. C., & Gentile, C. A. (2004). Extension of the Consensual Assessment
Technique to Nonparallel Creative Products. *Creativity Research Journal, 16*(1), 113–117.
- **DOI:** `10.1207/s15326934crj1601_11`
- **Abstract summary:** Shows CAT can produce high inter-rater reliability even when judges compare
  creative products that were *not* produced under identical, tightly controlled experimental prompts (13
  expert judges rated 8th-grade writing produced under a variety of assignments).
- **Suggested citation context:** Directly matches the dossier's paraphrase ("CAT inter-rater reliability
  could remain high even when creative outputs were not generated under experimental conditions"). Cite
  in Introduction/Discussion to support using CAT on naturalistic, "in the wild" football actions rather
  than standardized experimental stimuli.

**[christiaans2005]** Christiaans, H., & Venselaar, K. (2005). Creativity in design engineering and the
role of knowledge: Modelling the expert. *International Journal of Technology and Design Education,
15*(3), 217–236.
- **DOI:** `10.1007/s10798-004-1904-4`
- **Abstract summary:** Studies novice vs. expert design engineering students, relating process/domain
  knowledge to creative-outcome quality; often cited alongside Baer et al. (2004) as evidence that CAT
  reliability held up outside strictly parallel experimental conditions.
- **Suggested citation context:** Cite alongside `baer2004` in Introduction when justifying non-parallel,
  real-world (match) stimuli for CAT rating rather than standardized lab-generated stimuli.

**[plucker2009]** Plucker, J. A., Kaufman, J. C., Temple, J. S., & Qian, M. (2009). Do experts and novices
evaluate movies the same way? *Psychology & Marketing, 26*(5), 470–478.
- **DOI:** `10.1002/mar.20283`
- **Abstract summary:** Compares college-student, self-described-novice, and professional-critic movie
  ratings; novice ratings correlated with critic/expert ratings, and *raters who had seen more movies
  correlated more highly with critics* — domain expertise did not straightforwardly increase agreement,
  and high exposure/experience partially substituted for formal expert status.
- **Suggested citation context:** Exact match for the dossier's paraphrase, including the "heavy viewership
  might substitute for formal expertise" football analogy. Cite in Introduction/Discussion when framing the
  expertise research question and motivating the "heavy viewers as raters" design choice.

---

## Gap: JRT follow-ups, IRT-based rater models, and Many-Facet Rasch Model (MFRM) as competing approach

**[myszkowski2021]** Myszkowski, N. (2021). Development of the R library "jrt": Automated item response
theory procedures for judgment data and their application with the consensual assessment technique.
*Psychology of Aesthetics, Creativity, and the Arts, 15*(3), 426–438.
- **DOI:** `10.1037/aca0000287`
- **Abstract summary:** Introduces the open-source `jrt` R package that operationalizes Judge Response
  Theory (Myszkowski & Storme, 2019) for CAT data, providing ready-to-use tools for fitting IRT-style
  judge models and producing latent-trait creativity scores.
- **Suggested citation context:** Cite in Methods/Analysis-plan section when describing how JRT will
  actually be implemented computationally — this closes the gap between the purely theoretical
  `myszkowski2019` citation already in the vault and an applied analysis pipeline.

**[myszkowski2024]** Myszkowski, N. (2024). *Item Response Theory for Creativity Measurement.* Cambridge
University Press (Elements in Creativity and Imagination).
- **DOI:** `10.1017/9781009239035`
- **Abstract summary:** A book-length treatment extending the JRT argument into a full IRT framework for
  creativity measurement generally (not just CAT judge modeling), consolidating five years of follow-up
  work since Myszkowski & Storme (2019).
- **Suggested citation context:** Cite in Introduction/Discussion as the state-of-the-art theoretical
  reference for IRT approaches to creativity judgment, complementing (not just repeating) the single 2019
  citation currently in the vault. Directly addresses the dossier's flag that "JRT itself is
  undertheorized in the vault."

**[myszkowski2025]** Myszkowski, N., & Storme, M. (2025). One score, two components: Disentangling
appropriateness and originality in PISA creative thinking judgments using generalized item response tree
models. *The Journal of Creative Behavior, 59*(2), e70033.
- **DOI:** unconfirmed (article-number-only Wiley publication; CrossRef confirms metadata but page/DOI
  string could not be independently verified beyond the CrossRef record — treat as high-confidence but
  double-check before submission)
- **Abstract summary:** A 2025 empirical follow-up applying generalized IRT-tree models to large-scale
  (PISA) creativity judgment data, separating novelty and appropriateness as distinct latent components
  scored from judge ratings.
- **Suggested citation context:** Cite in Discussion as evidence that JRT/IRT-for-judges is an active,
  maturing research line beyond the original 2019 proposal, and as a possible analytic template for
  separately modeling this paper's planned novelty/appropriateness sub-dimensions.

**[eckes2015]** Eckes, T. (2015). *Introduction to Many-Facet Rasch Measurement: Analyzing and Evaluating
Rater-Mediated Assessments* (2nd rev. and updated ed.). Peter Lang (Language Testing and Evaluation,
Vol. 22).
- **DOI:** `10.3726/978-3-653-04844-5`
- **Abstract summary:** The standard textbook-length introduction to Many-Facet Rasch Measurement (MFRM):
  modeling rater severity/leniency, correcting proficiency estimates for rater differences, and diagnosing
  rating-scale and rater-consistency problems in rater-mediated assessments generally (not creativity-
  specific, but the foundational methodological reference).
- **Suggested citation context:** Cite in Methods when introducing MFRM as an alternative/competing
  aggregation approach to JRT, as flagged in `RatingScaleCreativityInSports.md`. This fills the dossier's
  explicit gap: "MFRM appears only within the prose of `RatingScaleCreativityInSports.md`... no dedicated
  concept note or citation."

**[hung2012]** Hung, S.-P., Chen, P.-H., & Chen, H.-C. (2012). Improving creativity performance assessment:
A rater effect examination with many facet Rasch model. *Creativity Research Journal, 24*(4), 345–357.
- **DOI:** `10.1080/10400419.2012.730331`
- **Abstract_summary:** Applies MFRM to creativity-task ratings to detect leniency/severity, central
  tendency, halo, and randomness rater effects; finds raters could be diagnosed and examinees reliably
  differentiated despite individual rater idiosyncrasies, and suggests MFRM output can support rater
  training.
- **Suggested citation context:** Cite alongside `primi2019` (already in library) in Methods/Discussion as
  a second, independent demonstration of MFRM applied specifically to creativity ratings — gives the
  manuscript two applied precedents rather than one when justifying MFRM as a JRT alternative.

**[myford2003]** Myford, C. M., & Wolfe, E. W. (2003). Detecting and measuring rater effects using
many-facet Rasch measurement: Part I. *Journal of Applied Measurement, 4*(4), 386–422.
- **DOI:** none found; **PMID:** 14523257 (used as the stable identifier in place of a DOI)
- **Abstract summary:** Foundational methodological paper introducing how MFRM detects five distinct rater
  effects (leniency/severity, central tendency, halo, randomness, differential leniency).
- **Suggested citation context:** Cite jointly with `eckes2015` in Methods as the canonical rater-effects
  MFRM reference; Part II (below) covers the applied Facets-software workflow.

**[myford2004]** Myford, C. M., & Wolfe, E. W. (2004). Detecting and measuring rater effects using
many-facet Rasch measurement: Part II. *Journal of Applied Measurement, 5*(2), 189–227.
- **DOI:** none found; **PMID:** 15064538 (used as the stable identifier in place of a DOI)
- **Abstract summary:** Companion paper to Part I; walks through using the Facets software to quantify the
  five rater effects identified in Part I.
- **Suggested citation context:** Cite alongside `myford2003` in Methods if the manuscript specifies
  software/estimation details for an MFRM analysis.

---

## Gap: Prior CAT-in-sport studies beyond Kempe & Memmert (2018)

No other study was found that replicates Kempe & Memmert's exact design (panel of several expert judges
rating discrete football actions on a numeric creativity scale, validated against an external outcome).
That specific combination does appear to be a genuine gap in the literature — worth stating in the
manuscript as motivation, rather than forcing a citation. However, two closer analogues than what is
already in the library were found:

**[oboeuf2020]** Oboeuf, A., Hanneton, S., Buffet, J., Fantoni, C., & Labiadh, L. (2020). Influence of
traditional sporting games on the development of creative skills in team sports. The case of football.
*Frontiers in Psychology, 11*, 611803.
- **DOI:** `10.3389/fpsyg.2020.611803`
- **Abstract summary:** Two independent expert judges (experienced coaches, blind to study aims) rated
  individual players' in-game creativity on a 1–10 scale ("near 1" = predictable, "near 10" = surprising
  and helpful to teammates); inter-judge correlation exceeded .90.
- **Suggested citation context:** Cite in Introduction as a second, independent example of expert-judge
  rating of football creativity (albeit with only two judges, unlike this paper's larger panel design) —
  strengthens the claim that expert-rated creativity in football is feasible and reliable at small N of
  judges, while motivating why a systematic number-of-judges study is still needed.

**[zahno2022]** Zahno, S., & Hossner, E.-J. (2022). Creative actions in team sports are rooted in motor
skills rather than in a divergent thinking ability. *German Journal of Exercise and Sport Research,
53*(2), 206–216.
- **DOI:** `10.1007/s12662-022-00847-6`
- **Abstract summary:** Uses expert ratings of on-field functionality and creativity of youth football
  players' actions to test whether creativity training transfers from divergent-thinking tasks or
  functional-skills training; functional-skills training produced greater gains in rated on-field
  creativity than divergent-thinking training.
- **Suggested citation context:** Cite in Introduction/Discussion as another recent (2022) precedent for
  expert-rated in-game football creativity, and to connect this paper's psychometric focus to the broader
  "creative process vs. creative product in sport" literature already summarized in the vault.

---

## Gap: General CAT validity/reliability/history literature, generalizability theory, and rater-training/frame-of-reference effects (psychology-audience framing)

**[long2015]** Long, H., & Pang, W. (2015). Rater effects in creativity assessment: A mixed methods
investigation. *Thinking Skills and Creativity, 15*, 13–25.
- **DOI:** `10.1016/j.tsc.2014.10.004`
- **Abstract summary:** Analyzes 2,160 ratings from 45 raters using generalizability theory combined with
  qualitative rater-cognition interviews; finds rating inconsistencies relate to rater cognition (e.g.,
  more-expert raters sometimes used rating scales *less* consistently than novices).
- **Suggested citation context:** Cite in Introduction/Discussion as the core generalizability-theory
  precedent for treating "rater" as a facet of measurement error, complementing the MFRM citations above,
  and as a caution against assuming expertise straightforwardly improves consistency.

**[barth2020]** Barth, P., & Stadtmann, G. (2020). Creativity assessment over time: Examining the
reliability of CAT ratings. *The Journal of Creative Behavior, 55*(2), 396–409.
- **DOI:** `10.1002/jocb.462`
- **Abstract summary:** Directly investigates whether CAT ratings remain reliable when judges rate large
  batches of items over extended sessions/time — i.e., a rater-fatigue/reliability-over-duration study.
- **Suggested citation context:** Directly answers the dossier's flagged sub-question "how long can the
  task be done reliably?" (from `1___ResearchIdeas.md`/`StudentThesisProjects.md`). Cite in
  Introduction/Method when justifying session-length and fatigue-monitoring design choices, and in
  Discussion when interpreting any fatigue/session-length findings from the planned pilot.

**[ceh2021]** Ceh, S. M., Edelmann, C., Hofer, G., & Benedek, M. (2021). Assessing raters: What factors
predict discernment in novice creativity raters? *The Journal of Creative Behavior, 56*(1), 41–54.
- **DOI:** `10.1002/jocb.515`
- **Abstract summary:** Identifies individual-difference predictors (e.g., raters' own creative
  self-concept, cognitive style) of how discerning novice CAT raters are, moving the expertise question
  from "expert vs. novice" toward "what makes any given novice rater more or less useful."
- **Suggested citation context:** Cite in Discussion when discussing the expertise research question,
  as a more fine-grained companion to Baer (2015) / Plucker et al. (2009) / Kaufman et al. (2008) already
  identified — useful if the manuscript wants to characterize *which* non-expert raters (e.g., heavy
  viewers) are most reliable rather than treating "non-expert" as a monolithic category.

**[hass2018]** Hass, R. W., Rivera, M., & Silvia, P. J. (2018). On the dependability and feasibility of
layperson ratings of divergent thinking. *Frontiers in Psychology, 9*, 1343.
- **DOI:** `10.3389/fpsyg.2018.01343`
- **Abstract summary:** Uses generalizability theory to determine the number of untrained (MTurk) raters
  and items needed for adequate reliability of divergent-thinking ratings; found ~3 raters with 4 items
  sufficed for one task type but requirements varied by task and rating design (whole-set vs. item-by-item
  rating).
- **Suggested citation context:** Strong direct precedent for this paper's central "how many judges are
  needed for convergence" question — cite in Introduction/Method alongside the "5–10 judges" (Kaufman et
  al., 2008) heuristic as a G-theory-based, quantitatively derived alternative approach to answering the
  same question, and as a template for how this paper might formally estimate the number of raters needed
  for football-action ratings.

**[long2022]** Long, H., Kerr, B. A., Emler, T. E., & Birdnow, M. (2022). A critical review of assessments
of creativity in education. *Review of Research in Education, 46*(1), 288–323.
- **DOI:** `10.3102/0091732X221084326`
- **Abstract summary:** Systematic review (2010–2021) of creativity-assessment methods across psychology
  and education journals, covering divergent-thinking tests, self-report, and product/CAT-style
  subjective techniques, with attention to demographic fairness.
- **Suggested citation context:** Cite in Introduction as a recent, broad review situating CAT among other
  creativity-assessment families for a *Creativity Research Journal* (general psychology) audience — useful
  as a one-stop "state of the field" citation alongside Barbot et al. (2019) and Barbot & Reiter-Palmon
  (2019) already in the vault.

---

## Papers not found / could not confirm

- **Exact page/quote confirming "5–10 judges is adequate"** inside Kaufman, Plucker, & Baer (2008)
  *Essentials of Creativity Assessment* — the book is confirmed real and is almost certainly the source,
  but I could not access its internal text to verify the exact figure or page. Recommend the author verify
  directly from a copy of the book before citing the specific number.
- **A direct CAT-in-sport study matching Kempe & Memmert's exact design** (panel of ≥3 expert judges rating
  discrete football actions on a numeric scale, validated against an external performance metric) —
  none found beyond Kempe & Memmert (2018) itself. Oboeuf et al. (2020) and Zahno & Hossner (2022) are the
  closest analogues but use only 1–2 judges and/or a different validation strategy. This gap is real and
  can be stated as such in the manuscript (i.e., "no CAT-in-sport study to date has systematically varied
  judge number or expertise" is a defensible, literature-supported claim).
- **A published meta-analysis specifically aggregating CAT inter-rater reliability coefficients across
  domains** (as opposed to narrative reviews like Cseh & Jeffries, 2019, and Long et al., 2022) — searches
  did not surface a quantitative meta-analysis of this kind; it may not exist yet, which is itself worth
  noting if the manuscript claims CAT reliability lacks a meta-analytic summary.
- **"Wisdom of crowds" as an aggregation theory specifically applied to creativity judgment** — the
  dossier flagged this as gestured at but undeveloped in the vault. General wisdom-of-crowds literature
  (Galton 1907, Davis-Stober et al. 2014) already exists in `phd_library.bib` but tagged under "Match
  Analysis," not creativity; no creativity-specific wisdom-of-crowds paper was found and confirmed within
  the scope of this search. Flagged for a possible follow-up search if the manuscript wants to develop this
  angle further.
