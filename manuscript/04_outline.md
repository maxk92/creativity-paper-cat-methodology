# Outline — Creativity Assessment in Sports: A CAT/JRT Methodology Study

Profile: `imrad-apa` (Creativity Research Journal, APA 7th).
Status: concept/proposal stage — no notebook exists (`notebook: None`). Methods is
outlined as a fully reproducible proposed design; Results is a structural skeleton
only; Discussion/Conclusion flag every interpretive claim as pending data.

Revision note (post author-approval, checkpoint 1): three of the five originally
flagged open items have been resolved by the author and are incorporated below
(ethics/preregistration statement, MFRM software choice, sample-size target +
sample-size-calculation guidance). Two items remain deliberately unresolved and
still flagged/hedged exactly as before: the fatigue/session-length artifact gap,
and the unverified "5–10 judges" heuristic figure.

Revision note (post reviewer-critic pass, checkpoint 2): the reviewer-critic
identified a reliability-threshold gap, an unspecified rater-panel size, a
missing-hypotheses gap, a CI/effect-size reporting gap, a confusing
six-vs-five-analyses framing, an unspecified rater-assignment mechanism, a
missing blinding statement, and an under-specified frame-of-reference (FOR)
training procedure. All eight are now resolved and incorporated below (see
"Aim and research questions" and Methods). A ninth reviewer item — the rating
platform being left unnamed — is newly flagged as an open item rather than
resolved; the author has chosen to leave the specific platform open for now.
Two items remain deliberately unresolved from checkpoint 1: the
fatigue/session-length artifact gap, and the unverified "5–10 judges"
heuristic figure. See "Evidence gaps" at the foot of this document for the
full changelog. (Purely textual manuscript-level fixes — the citation-bracket
syntax error, the YAML docx reference-doc mismatch, the title rewording, and
the Discussion "clearest applied payoff" editorializing line — are out of
scope for this outline revision and will be applied directly by
manuscript-writer against this updated outline.)

Revision note (post writing-models integration): outline-architect and
manuscript-writer now consult `/home/max/drive/utils/writing-models/` for
per-section move structures and phrase banks (Glasman-Deal). Checked every
section against its matching move model; almost all sections already
implement their model reasonably well, so this pass is a targeted diff, not a
rewrite. Two real gaps were found and are incorporated below: (1) Results
Move 1 (revisit aim before detail) was missing — the Results section opened
directly with the "no data" disclaimer without first echoing the RQs; (2)
Discussion/Conclusion Move 4's "pair each limitation with a nearby positive"
technique was applied inconsistently — 4 of 8 Limitations bullets lacked the
pairing that 2 others already had. The Title model's sentence-case guidance
was considered and rejected: it conflicts with this profile's APA 7th
title-case convention (see `paper.config.yml` review criteria), so the title
is left unchanged.

Scoping decision (per `manuscript/01_dossier.md`, themes 1 and section D): this is
**paper 1 of a planned 3-paper sequence** — (1) this method paper, (2) an
application paper correlating creativity with VAEP/market value, (3) an automated
(ML/transformer) detection paper. VAEP-correlation and automated-scoring material
are **out of scope** here and appear only as a brief pointer to future work in the
Conclusion.

---

## Central contribution

CAT is a mature but domain-underspecified method: Cseh & Jeffries (2019) show that
the number of judges and their required expertise cannot be determined in general —
each domain needs its own empirical evidence, and current sport-creativity research
(essentially just Kempe & Memmert, 2018) has never supplied it. This paper's
contribution is to generate the first large-scale, systematically varied multi-rater
creativity-rating dataset for a sports domain (football actions) and use it to give
the field an empirically grounded, reproducible answer to four linked psychometric
questions — number of judges needed for convergence, effect of rater expertise,
whether modern rater-effects models (JRT/MFRM) improve on naive averaging, and
whether creativity is discriminable from adjacent constructs (aesthetic appeal,
technical correctness) — plus a practical answer on session-length reliability. The
paper is framed as a general-purpose methodological template for CAT-based
creative-product research, with football/sport as the concrete, ecologically valid
testbed, not as an end in itself.

Evidence chain: Introduction establishes the psychometric gap (general
creativity-assessment literature) → Methods proposes a design capable of closing it
→ Results (once populated) will report the six planned analyses → Discussion
interprets them back into general CAT/measurement-theory recommendations, with
sport-specific application as a secondary, practical payoff.

---

## Abstract

Purpose: single paragraph (structured or unstructured per CRJ house style — author
to confirm), written so it can stand once Results are populated.

- Background: CAT is a widely used but domain-general method whose validity
  depends on domain-specific choices (number/expertise of judges) that have not
  been empirically resolved for many applied domains, including sport
  [`cseh2019`, `amabile1982`].
- Objective/RQs: state the four core RQs (judges needed, expertise effect,
  JRT/MFRM vs. averaging, construct/factor validity) plus the fatigue/session
  question, using football action-rating as the test domain.
- Method (one sentence): large-scale multi-rater benchmark + pairwise rating
  design on a purposively selected set of ~1,000–2,000 football actions, 7-point
  unipolar novelty × appropriateness scale [cross-ref Methods].
- Results: placeholder sentence — "Results are reported for [ICC across judge
  counts / expertise comparison / JRT-MFRM rater diagnostics / factor structure]"
  — to be filled once data exist; do not draft specific outcome language now.
- Conclusion: methodological guidance for CAT-based creative-product research in
  sport and, by extension, other domains with naturalistic, non-parallel stimuli.

---

## Introduction

Purpose: carry the paper's intellectual weight. Written for a mainstream
creativity/psychometrics readership; football is the motivating applied context,
not the primary audience concern.

1. **Opening hook — creativity measurement is a live, unresolved methodological
   problem in the field generally**, not just in sport.
   - Creativity assessment is described as a fundamental challenge/point of
     debate; taxonomy of person/process/product/press clarifies that each facet
     needs its own measurement approach.
   - Citations: `batey2012`, `barbot2019`, `barbot2019b`, `long2022` (recent
     broad review situating CAT among assessment families for a CRJ audience).

2. **CAT as the dominant subjective-consensus method for the "product" facet.**
   - Introduce Amabile's CAT: expert/quasi-expert judges independently rate
     products' creativity without a predefined rubric; established validity,
     reasonable inter-rater agreement, improves when averaged across raters.
   - Citations: `amabile1982`, `kaufman2008` (textbook treatment), `long2015`
     (generalizability-theory treatment of rater effects as a facet of error).

3. **The central gap: CAT's validity is domain-contingent, and this
   domain-specificity has rarely been operationalized.**
   - Cseh & Jeffries' critique: appropriate judge number and expertise level
     depend on the nature of the product/domain and cannot be determined
     generally; each domain needs its own empirical evidence.
   - Citation: `cseh2019` (already the brief's own framing — carry forward
     verbatim logic).

4. **Sub-debate A — how many judges are "enough"?**
   - Existing heuristic guidance (e.g., "5–10 judges is adequate" for most
     purposes) is a general rule of thumb, not empirically derived per domain;
     flag that the specific figure/page needs author verification before being
     stated as settled (unresolved — see Evidence gaps).
   - Contrast with generalizability-theory approaches that derive judge/item
     numbers empirically and find requirements vary by task and design.
   - Citations: `kaufman2008` (heuristic — flag uncertainty), `hass2018`
     (G-theory-derived judge/item numbers, direct template for this paper's
     RQ1).

5. **Sub-debate B — does rater expertise matter, and how much?**
   - Present the tension explicitly, not as settled: Amabile suggests judges'
     level of experience need not be uniform; CAT reliability holds up even for
     non-parallel, naturalistically produced products (not just standardized lab
     stimuli); expert-vs-novice comparisons show novices can be meaningfully
     discerning; domain expertise does not straightforwardly increase agreement,
     and high exposure/experience can partly substitute for formal expert status
     (the "heavy viewer" analogy directly motivating this paper's design);
     domain-specific expertise is nonetheless argued to matter in other work;
     "dark side of expertise" cautions that expertise can introduce its own
     biases; individual-difference work asks what predicts discernment in
     novice raters specifically.
   - Citations: `amabile1982`, `baer2004`, `christiaans2005`, `kaufman2008b`,
     `plucker2009`, `baer2015`, `castel2007`, `ceh2021`.

6. **Sub-debate C — how should ratings from multiple, non-interchangeable judges
   be aggregated?**
   - Naive mean-averaging implicitly assumes judges are exchangeable random
     effects; this ignores systematic rater severity/leniency, which
     IRT-for-judges (Judge Response Theory, JRT) and Many-Facet Rasch Modeling
     (MFRM) are designed to detect and correct for. Present JRT and MFRM as two
     related but historically separate psychometric traditions the field has
     not yet compared head-to-head in a creativity-rating context at this
     scale.
   - Citations: `myszkowski2019` (JRT foundational proposal), `myszkowski2021`
     (applied `jrt` R package), `myszkowski2024` (book-length JRT synthesis),
     `myszkowski2025` (novelty/appropriateness decomposition via IRT-tree
     models — directly relevant since this paper's scale is novelty ×
     appropriateness), `eckes2015`, `myford2003`, `myford2004` (MFRM
     foundational), `primi2019`, `hung2012` (MFRM applied specifically to
     creativity ratings).

7. **Construct-validity concern: is "creativity" discriminable from adjacent
   rated constructs?**
   - When applying CAT to a new domain, judges should also rate secondary
     constructs (e.g., technical execution, aesthetic appeal) to establish
     discriminant/construct validity of the creativity rating itself; frame
     creativity as novelty × appropriateness/functionality, following standard
     definitional consensus.
   - Citations: `amabile1982` (construct-validity rationale), `runco2012`
     (novelty × functionality definition — vault note `CreativityDefinition.md`
     applies this specifically to football actions).

8. **Practical measurement concern: how long can raters reliably perform the
   task?**
   - Rater fatigue/reliability decline over long rating sessions is an
     under-addressed practical design question for any large-scale CAT study.
   - Citation: `barth2020` (direct precedent studying CAT reliability over
     time/session length).

9. **Narrowing to the applied domain — why football, and why now.**
   - Creativity is a key quality to develop/evaluate in players; process-level
     creativity (divergent thinking) is comparatively well studied in sport, but
     creative *product* has received far less attention.
   - One prior product-level study exists and demonstrates face validity
     (temporal proximity of creative actions to goals) using a 0–10 expert
     scale, but does not address number-of-judges, expertise, or aggregation
     methodology. Two closer but smaller-scale analogues exist (two-judge design
     with r > .90; functional-skills-vs-divergent-thinking-training comparison
     using expert on-field creativity ratings) — neither systematically varies
     judge number/expertise or applies JRT/MFRM.
   - Citations: `safardilha2019`, `memmert2011`, `kempe2018`, `oboeuf2020`,
     `zahno2022`.
   - State the gap explicitly and literature-supported: no CAT-in-sport study to
     date has systematically varied judge number or expertise, or modeled rater
     severity via JRT/MFRM, in this domain.

10. **Aim and research questions** (mirrors the brief and the vault's internal
    project charter — `StudentThesisProjects.md`, `1___ResearchPlan.md`; these
    are structural/internal sources, not citable literature, and are not cited
    in the manuscript itself).
    - RQ1 (judges): How many raters are needed for stable/convergent creativity
      ratings of football actions?
      - **H1**: Inter-rater reliability (ICC) increases with the number of
        judges averaged, with asymptotically diminishing returns, consistent
        with generalizability-theory/Spearman-Brown logic — the empirical
        template being `hass2018`, which derived comparable judge/item-count
        curves in a different domain.
      - **Pre-specified target/stopping rule** (design decision, stated in
        advance — not a result): ICC(2,k) >= .80 is the target reliability for
        declaring ratings "stable/convergent" for the purposes of RQ1, with
        .70 noted as a minimum acceptable floor — a standard convention in the
        reliability/psychometrics literature, cited generically as convention
        rather than to a single specific new source. See Methods, Analysis
        Plan (a), for how this threshold is applied to the ICC-by-judge-count
        curve.
    - RQ2 (expertise): Does rater expertise/exposure affect inter-rater
      agreement or severity? Framed as **competing, directional hypotheses**
      given the Amabile-vs-Plucker/Kaufman tension already laid out in
      Sub-debate B above — the RQ2 analyses test which position this dataset
      supports, not a single predicted winner.
      - **H2a** (Amabile-consistent): rater expertise level does not
        systematically affect agreement or severity.
      - **H2b** (Plucker/Kaufman-consistent): non-expert but high-exposure
        raters show agreement/severity comparable to, or exceeding, that of
        formally credentialed experts.
    - RQ3 (aggregation/psychometrics): Do JRT and/or MFRM rater-severity models
      improve on simple mean aggregation, and what do they reveal about
      individual raters? **Stated explicitly as open/exploratory, with no
      directional hypothesis**: JRT, MFRM, and naive averaging have not been
      compared head-to-head at this scale in a creativity-rating context
      before, so there is no established prior result from which to derive a
      directional prediction.
    - RQ4 (construct validity): What is the factor structure relating
      creativity, aesthetic appeal, and technical-correctness ratings?
      **Stated explicitly as open/exploratory, with no directional
      hypothesis**: the factor structure among these three constructs is not
      yet established in this domain.
    - RQ5 (reliability over time): How long can raters perform the task
      reliably before agreement/quality declines? **Stated explicitly as
      open/exploratory, with no directional hypothesis**: no prior
      football-specific (or, more broadly, sport-specific) fatigue/
      session-length data exist to ground a directional prediction.
    - Close with the explicit scope statement: this paper addresses these five
      measurement questions only; correlating creativity with performance
      outcomes (VAEP/market value) and automated/ML scoring are explicitly
      deferred to companion papers.

---

## Methods

Purpose: the strongest section available at this stage — write as a maximally
concrete, reproducible proposed design. Everything here is planned, not yet
executed; use future tense ("will be") throughout, per the profile's
"reproducible sample/design/procedures" review criterion.

1. **Design overview**
   - Cross-sectional, multi-rater creativity-rating study of discrete football
     actions, using a benchmark + pairwise rating structure to enable both
     full-overlap reliability analysis and larger-scale coverage.
   - **Benchmark panel size (resolved):** a fixed panel of **10 raters** will
     rate the full benchmark subset of actions, enabling ICC/agreement
     trajectories to be computed at every candidate judge count from 1 through
     10 (see Analysis Plan (a) and "Judges/raters" below).

2. **Stimuli / sample of football actions**
   - Source video/event data: StatsBomb (preferred, pending video-access
     confirmation), WyScout 17/18 as fallback.
   - **Sample target (resolved):** purposive sampling of approximately
     **1,000–2,000 football actions**, pre-selected as plausible creative-moment
     candidates (e.g., via event-data heuristics or expert pre-screening
     flagging actions likely to vary in creativity), rather than exhaustive or
     random sampling of every action per match. Matches sampled across multiple
     competitions (men's and women's FIFA tournaments, AFCON, UEFA tournaments,
     Copa America). This supersedes the earlier, larger vault figure
     (`CreativityRatingStudy.md`'s ~9,500-action planning note) — the author has
     set the ~1,000–2,000 purposive target as the operative plan for this
     manuscript.
   - **Sample-size justification (guidance only, not yet formally calculated):**
     add a short subsection explaining that the ~1,000–2,000 target is
     currently a plausibility-based design choice, and outlining how a formal a
     priori sample-size/power calculation could be performed if the author
     chooses to run one before data collection — e.g., precision-based
     planning for ICC estimation at each candidate judge count (targeting a
     minimum acceptable width for the ICC confidence interval), following a
     generalizability-theory (G-theory) logic in the spirit of `hass2018`
     (which empirically derived the number of raters/items needed for
     acceptable reliability). Present this as a decision point for the author —
     either (a) proceed with the plausible 1,000–2,000 target as currently
     planned, or (b) run a formal precision/power analysis first — and state
     clearly that no such calculation has been performed yet.
   - Citation for the sample-size-guidance subsection: `hass2018`.
   - Flag to author that the exact operational criteria for "plausible
     creative-moment candidate" pre-selection (rule-based vs. expert
     pre-screening) still need to be specified in full before data collection.

3. **Judges/raters**
   - **Rater-panel size (resolved):** the benchmark panel is set at **10
     raters** — every judge in this fixed panel rates the full benchmark
     subset of actions. In addition, a separate pool of pairwise-only raters
     will be recruited to cover the larger pairwise action subset (2–3 judges
     per action); the exact size of this additional pool is still open and
     will be finalized based on recruitment logistics — flagged explicitly as
     an open item, not invented here.
   - **Narrative rationale (a genuine strength of this design):** a 10-rater
     benchmark panel is large enough to let this study directly test the
     "5–10 judges is enough" heuristic (`kaufman2008`, already flagged
     elsewhere as unverified at the page/quote level — see Evidence gaps)
     against its own benchmark data, rather than merely citing the heuristic
     secondhand. The ICC-by-judge-count curve (Analysis Plan (a)) spans
     exactly the range the heuristic claims is sufficient.
   - Recruitment plan: raters spanning an expertise gradient (e.g.,
     coaches/domain experts vs. non-expert but high-exposure viewers), directly
     operationalizing the Amabile-vs-Plucker/Kaufman expertise debate.
   - Design: a benchmark subset of actions rated by all 10 judges in the fixed
     panel (enables full pairwise ICC/agreement comparisons at every candidate
     judge count from 1 through 10); a larger pairwise/rotating subset rated
     by 2–3 judges per action, drawn from the fixed panel and/or the
     additional pairwise-only pool (enables scale-up beyond the benchmark
     set).
   - **Rater-to-action assignment mechanism (resolved):** pairwise-subset
     raters will be assigned to actions via random assignment constrained to
     preserve a connected rater-by-action network — i.e., randomization is not
     fully unconstrained; it is constrained so that the resulting
     rater-by-action bipartite graph remains connected, which is a standard
     requirement for MFRM/JRT parameter identifiability. This partially
     de-risks, but does not eliminate, the rater-by-action matrix sparsity
     concern flagged in Limitations below — connectivity is guaranteed by
     design, but the realized *degree* of overlap/sparsity is still not known
     until data collection occurs.
   - Citations for expertise operationalization: `kaufman2008`, `kaufman2008b`,
     `plucker2009`, `baer2015`, `castel2007`, `ceh2021`.

4. **Rating instrument**
   - 7-point unipolar novelty × appropriateness rating scale, behaviorally
     anchored (verbal anchors at each scale point), following psychometric
     guidance on optimal category counts.
   - Secondary dimensions also rated for construct-validity purposes: aesthetic
     appeal, technical correctness.
   - Frame-of-reference (FOR) rater training procedure prior to rating.
     **Operational detail (resolved):** raters will review a set of
     worked/anchor examples at each of the 7 scale points, followed by a short
     calibration rating set with feedback, before live rating begins. (Kept
     generic/plausible — exact numbers of worked examples and calibration
     items are not yet fixed and are not invented here.)
   - **Blinding / ecological-validity statement (resolved):** raters will view
     full match footage/context, including player and team identity, rather
     than blinded/anonymized clips — this prioritizes ecological validity
     (creativity judgments are made on naturalistic match footage, not
     standardized lab stimuli) over experimental blinding. See the
     corresponding Limitations item on halo-effect risk.
   - Explicit conversion/compatibility bridge to Kempe & Memmert's 0–10 scale
     for cross-study comparability.
   - Citations: `amabile1982` (secondary-construct rationale), `runco2012`
     (novelty × functionality definition), `kempe2018` (0–10 scale precedent
     and conversion).

5. **Procedure**
   - Rating platform/app (randomized action order, structured data export) —
     described procedurally, no citation. **Specific platform: open item, not
     yet decided.** Flagged the same way as other open design items (e.g.,
     the additional pairwise-only rater-pool size in "Judges/raters," and the
     precise "plausible creative-moment candidate" pre-selection criteria in
     Methods §2) — the author will finalize the specific tool before data
     collection.
   - Pilot phase to establish per-session rating capacity by monitoring
     agreement/consistency decline across session position (directly informs
     RQ5), following the design logic of a prior CAT-reliability-over-time
     study.
   - Citation: `barth2020`.

6. **Analysis plan** (six analyses, each mapped to a `03_findings.md` finding
   and, where applicable, `02_artifacts.md` placeholder objects). **All six
   analyses (a)-(f) commit to reporting confidence intervals and effect sizes
   alongside, or instead of, significance/p-value tests**, per the venue's
   review criterion that "effect sizes and CIs reported, not just p-values" be
   satisfied — this is a design commitment stated in advance, not a result;
   no actual CI or effect-size values are stated anywhere in this outline.
   - **(a) Judge-count convergence** — ICC (e.g., ICC(2,k)/ICC(3,k)) computed
     on the benchmark subset (10-rater panel), examined as a function of
     number of raters averaged (k = 1…10); possibly a Spearman-Brown-type
     reliability projection. **Pre-specified target/stopping rule (resolved,
     design decision):** ICC(2,k) >= .80 is the target for declaring ratings
     "stable/convergent" for RQ1; .70 is noted as a minimum acceptable floor,
     following standard convention in the reliability literature (cited
     generically as convention, not to a single new source). The number of
     judges "needed" is read off the ICC-by-judge-count curve against this
     pre-specified target, not chosen post hoc.
     → Finding 1; `fig-icc-by-judge-count`, `tbl-agreement-by-judge-count`.
     Citations: `cseh2019` (motivating RQ), `hass2018` (G-theory template),
     `kaufman2008` (heuristic comparator).
   - **(b) Variance-source mixed model** — `rating ~ covariates + (1|rater) +
     (1|player) + (1|match)`. **Framing (resolved):** this model is an
     auxiliary/supporting analysis for RQ2 (expertise), not an independent
     sixth research question — it decomposes rating variance into
     rater/player/match sources and allows expertise to be entered as a
     covariate/moderator, directly informing the RQ2 hypotheses (H2a/H2b)
     above. It does not pose an unlisted RQ6.
     → Finding 2 (no dedicated artifact currently listed; author to confirm
     whether this produces its own table).
   - **(c) Rater-severity diagnostics via JRT and/or MFRM**, compared against
     naive mean aggregation.
     → Finding 3; `fig-rater-severity-jrt`, `tbl-rater-fit-diagnostics`.
     Citations: `myszkowski2019`, `myszkowski2021`, `myszkowski2024`,
     `myszkowski2025`, `eckes2015`, `myford2003`, `myford2004`, `primi2019`,
     `hung2012`.
   - **(d) Expertise-group comparison** on ICC and/or rater-severity parameters;
     expertise also entered as a covariate/moderator in the mixed model.
     → Finding 4; `fig-expertise-agreement`, `tbl-expertise-effects`.
     Citations: as in point 3 above.
   - **(e) Factor analysis** across creativity, aesthetic-appeal, and
     technical-correctness ratings (exploratory and/or confirmatory).
     → Finding 5; `fig-factor-structure`, `tbl-factor-loadings`.
     Citation: `amabile1982`.
   - **(f) Fatigue/session-duration reliability** — agreement/consistency
     trend across session position or time-on-task.
     → Finding 6 (no matching artifact currently in `02_artifacts.md` — this
     remains unresolved; see Evidence gaps).
     Citation: `barth2020`.
   - **Software/estimation (resolved):** the full analysis pipeline will be
     kept within a single open-source, reproducible R environment. JRT will be
     fit using the `jrt` R package (`myszkowski2021`); MFRM will be fit using an
     R-based implementation — the Test Analysis Modules package (**TAM**) for a
     standard many-facet Rasch model, or a Bayesian many-facet Rasch model fit
     via **brms** (with rater, player/examinee, and item as crossed random
     facets) as an alternative — rather than commercial Facets software. This
     keeps JRT and MFRM estimation, the mixed models, and the factor analysis
     all reproducible from a single R codebase.
     Citations: `eckes2015`, `myford2003`, `myford2004` (MFRM foundations,
     software-agnostic), `myszkowski2021` (`jrt` package).

7. **Ethics statement (resolved)**
   - Ethics approval for this project was obtained from the Ethics Committee of
     the German Sport University Cologne (approval no. 248/2025). State this
     verbatim as a standard APA/psychology-journal ethics statement in Methods,
     citing the approval number directly (no citation key needed — this is a
     factual institutional statement, not a literature citation).
   - Preregistration: this study has not been preregistered. Standard
     psychology-journal practice (and the profile's honesty/transparency
     review criterion) favors stating this explicitly and briefly rather than
     omitting it — a one-sentence disclosure ("This study was not
     preregistered.") is recommended, placed directly after the ethics-approval
     statement, so the manuscript-writer does not need to guess whether silence
     implies preregistration occurred.

---

## Results

Purpose: structural skeleton only. No numbers are planned or invented here —
every bullet below is a pointer to an artifact placeholder in `02_artifacts.md`
and a finding placeholder in `03_findings.md`. Order mirrors the RQ order
established in Introduction/Methods for narrative coherence.

Per the Results writing model (Move 1: revisit the research aim and give a
general overview before the detail), open the section with a sentence
recapping the five RQs — echoing the Introduction's own wording — before the
"no data collected yet" structural framing below.

1. **Sample description** — achieved number of actions, matches, competitions,
   judges recruited, ratings per action (benchmark vs. pairwise subset), to be
   reported against the ~1,000–2,000-action purposive target stated in Methods.
   → `tbl-sample-description`.
2. **RQ1 — judge-count convergence.** ICC trajectory across candidate judge
   counts (k = 1…10) on the 10-rater benchmark subset, read against the
   pre-specified ICC(2,k) >= .80 target (.70 minimum floor) stated in Methods,
   Analysis Plan (a), to identify the minimum number of judges needed for
   stable/convergent ratings.
   → `fig-icc-by-judge-count`, `tbl-agreement-by-judge-count`; Finding 1.
3. **RQ2 — expertise effects.** Agreement/severity compared across
   expertise groups; mixed-model expertise coefficient.
   → `fig-expertise-agreement`, `tbl-expertise-effects`; Finding 4 (and Finding
   2 for the general variance-decomposition mixed model, if reported as its own
   table).
4. **RQ3 — rater-severity/aggregation (JRT/MFRM).** Rater severity/leniency
   estimates and fit diagnostics (fit via `jrt` and TAM/brms per the resolved
   software plan), compared against naive averaging.
   → `fig-rater-severity-jrt`, `tbl-rater-fit-diagnostics`; Finding 3.
5. **RQ4 — construct/factor validity.** Factor structure and loadings across
   creativity, aesthetic-appeal, and technical-correctness dimensions.
   → `fig-factor-structure`, `tbl-factor-loadings`; Finding 5.
6. **RQ5 — reliability over session duration.** Agreement/consistency trend
   across session position/time.
   → Finding 6; **no artifact placeholder currently exists for this — remains
   unresolved, see Evidence gaps.**

Do not add any additional Results content beyond what these six blocks
describe; do not draft example numbers, directions, or outcomes anywhere in
this section pre-data.

---

## Discussion

Purpose: interpret each RQ's (eventual) findings back into general
measurement-theory/psychometrics terms for the CRJ audience, with sport as the
applied payoff. Every interpretive bullet below is explicitly conditional on
data not yet collected and is flagged **[TBC]** (to be confirmed once data are
collected) — author-responsibility items, not settled claims.

1. Restate the paper's contribution and its place in the CAT/JRT literature
   (`cseh2019`, `myszkowski2019`) — not flagged, this is argumentative framing
   carried from the Introduction.
2. **[TBC]** Judge-count finding → implication for a recommended minimum number
   of judges for football (and by extension, similarly naturalistic/product-
   based) creativity-rating studies, read against the pre-specified ICC(2,k)
   >= .80 target (.70 minimum floor; Methods, Analysis Plan (a)); explicit
   comparison against the generic "5–10 judges" heuristic (`kaufman2008`,
   unverified — see Evidence gaps), which the 10-rater benchmark panel design
   was built to test directly, and the G-theory-derived numbers found in
   other domains (`hass2018`).
3. **[TBC]** Expertise finding → resolves which of the two competing
   hypotheses (H2a, Amabile-consistent: expertise does not systematically
   affect agreement/severity; H2b, Plucker/Kaufman-consistent: non-expert but
   high-exposure raters match or exceed formal experts) the data support,
   i.e., whether this domain resolves toward Amabile's "expertise need not be
   uniform" position or the "domain expertise doesn't straightforwardly help"
   position (`plucker2009`, `kaufman2008b`); practical implication for who
   should be recruited as a rater (e.g., heavy viewers vs. coaches) — this is
   the section's clearest "applied/practical relevance for sport science"
   payoff required by the review criteria.
4. **[TBC]** JRT/MFRM vs. naive-averaging finding → methodological
   recommendation on whether rater-effects modeling is worth the added
   complexity for this kind of data; position this study as an applied test of
   the JRT research program (`myszkowski2021`, `myszkowski2024`,
   `myszkowski2025`) and of MFRM as an established alternative
   (`primi2019`, `hung2012`, `eckes2015`), estimated throughout in R (`jrt`,
   TAM/brms) for full reproducibility.
5. **[TBC]** Factor-structure finding → whether creativity is empirically
   discriminable from aesthetic appeal and technical correctness in this
   domain, connecting back to the taxonomy/facet-clarity argument
   (`barbot2019b`) and Amabile's construct-validity rationale.
6. **[TBC]** Fatigue/session-length finding → practical guidance for designing
   CAT rating protocols generally, not just in sport (`barth2020`).
7. **Generalizability statement** — position the (eventual) findings as
   informing CAT practice broadly, directly answering Cseh & Jeffries' call for
   domain-specific empirical evidence, while being explicit that a single
   domain (football) cannot fully resolve a domain-general question.
8. **Limitations** (explicit, honest, required by review criteria):
   - Single applied domain (football); generalization to other creative
     domains is an open question — though football's naturalistic,
     non-parallel-stimulus character (Methods, "Design overview") makes it a
     demanding test case, so findings that hold here are plausible
     candidates for transfer to other applied domains.
   - Convenience/plan-dependent rater recruitment; exact expertise
     operationalization still to be finalized — though recruiting explicitly
     along an expertise gradient (Methods, "Judges/raters") is the design
     feature that makes RQ2 testable at all, not an incidental shortcoming.
   - The "5–10 judges" heuristic's exact source page remains unverified (see
     Evidence gaps) — do not overstate certainty when citing it.
   - MFRM/JRT model identifiability depends on the realized sparsity of the
     rater-by-action matrix, which is not yet known; the constrained
     random-assignment rule (Methods, "Judges/raters") guarantees a connected
     rater-by-action network by design, which partially de-risks but does not
     eliminate this concern — the realized degree of overlap is still unknown
     until data collection occurs.
   - Raters will view full match footage/context, including player and team
     identity, rather than blinded clips (Methods, "Rating instrument"),
     prioritizing ecological validity over blinding; this introduces a
     plausible halo-effect risk (recognizable players/teams influencing
     creativity judgments independently of the action itself). MFRM
     (Sub-debate C; Analysis Plan (c)) is explicitly intended to help diagnose
     such rater idiosyncrasies, including halo effects, but cannot fully
     substitute for blinding.
   - Rater fatigue/motivation effects in a large-scale, possibly
     online/remote rating task — no dedicated Results artifact currently
     planned for this finding (see Evidence gaps), though the planned pilot
     phase (Methods, "Procedure") is designed explicitly to surface this
     before full-scale data collection begins.
   - Purposive (non-random) sampling of "plausible creative-moment" actions
     means prevalence/base-rate claims about creativity in football cannot be
     made from this sample; only relative/psychometric comparisons
     (judge-count, expertise, aggregation-method) are licensed by the design.
   - No formal a priori sample-size/power calculation was performed for the
     ~1,000–2,000-action target; it reflects a plausibility-based design
     decision rather than a precision-targeted calculation (see Methods §2) —
     though Methods §2 already sets out how such a calculation could be
     performed (Sample-size justification), leaving a clear path to
     strengthen this before data collection if the author chooses.
   - Not preregistered.

---

## Conclusion

- Restate contribution: an empirically grounded, reproducible methodological
  template for CAT-based creative-product rating in sport, addressing a
  domain-specificity gap the broader creativity-assessment literature has
  flagged but rarely operationalized (`cseh2019`).
- **[TBC]** Practical recommendations for future sport-creativity CAT studies
  (number of judges, expertise mix, aggregation method) — contingent on
  Results/Discussion; do not state specific numbers now.
- Explicit forward pointer, kept brief: this is paper 1 of a 3-paper sequence;
  a companion application paper will examine the relationship between rated
  creativity and performance outcomes (e.g., VAEP, market value), and a further
  companion paper will explore automated/ML-based creativity scoring using the
  human ratings generated here as ground truth. Both are named only as future
  work, not elaborated.

---

## References

- APA 7th, managed via CSL per project convention (never hand-edit citation
  formatting).
- Citekeys anticipated for use, drawn only from the dossier's "Existing
  references" list and `manuscript/web_references.bib`:
  `batey2012`, `barbot2019`, `barbot2019b`, `amabile1982`, `cseh2019`,
  `safardilha2019`, `memmert2011`, `kempe2018`, `myszkowski2019`, `castel2007`,
  `baer2015`, `runco2012`, `kaufman2008`, `kaufman2008b`, `baer2004`,
  `christiaans2005`, `plucker2009`, `myszkowski2021`, `myszkowski2024`,
  `myszkowski2025`, `eckes2015`, `hung2012`, `myford2003`, `myford2004`,
  `oboeuf2020`, `zahno2022`, `long2015`, `barth2020`, `ceh2021`, `hass2018`,
  `long2022`, `primi2019`.
- Not used in this outline but confirmed available if needed later:
  `distefano2024`, `organisciak2023` (automated/LLM scoring — belongs to the
  sibling automated-detection paper, out of scope here except as a one-line
  "why getting human CAT right matters first" aside, optional).
- No citation needed for the ethics-approval statement (institutional
  approval number, not literature).
- No new citekeys have been introduced during the checkpoint-2 revision;
  hypotheses H1/H2a/H2b and the ICC threshold/panel-size/assignment-mechanism
  resolutions above cite only keys already in this list (`hass2018`,
  `kaufman2008`, `plucker2009`, `kaufman2008b`).

---

## Evidence gaps (updated post reviewer-critic pass, checkpoint 2 — eight
## additional items from that review are now resolved, reflected directly in
## the sections above, and appended to the changelog below as items 8-15;
## items 1 and 2 remain open by deliberate author choice and are kept at
## their original numbers, since `02_artifacts.md` and `03_findings.md`
## cross-reference them by number; item 16 is newly flagged open at
## checkpoint 2)

**Remaining open (not resolved — kept exactly as flagged/hedged; numbered 1-2
for cross-reference stability with `02_artifacts.md` and `03_findings.md`):**

1. **No artifact/finding pairing exists for RQ5 (fatigue/session-duration)** —
   `03_findings.md` Finding 6 has no corresponding `fig-`/`tbl-` placeholder
   in `02_artifacts.md`. Either add one during the results-embedder re-pass
   once real data exist, or fold the fatigue result into the sample-description
   table/prose only.
2. **The "5–10 judges is adequate" figure** (`kaufman2008`) has not been
   verified at the page/quote level — web-searcher flagged this explicitly.
   Do not state it as a settled number in the Introduction/Discussion; phrase
   as a general heuristic pending confirmation. Note (added at checkpoint 2):
   the 10-rater benchmark panel design (Methods, "Judges/raters") is built to
   let this study test the heuristic's substance directly against its own
   data, independent of resolving this citation-verification issue.

**Resolved by author at checkpoint 1 (reflected in Methods §2, §6, §7 above;
kept here only as a changelog):**

3. ~~Exact achieved/target sample sizes not finalized~~ — RESOLVED: target is
   purposive sampling of ~1,000–2,000 actions (Methods §2); sample-size
   calculation guidance added as a subsection for the author to optionally
   follow before data collection (not yet performed).
4. ~~No ethics/IRB or preregistration statement exists~~ — RESOLVED: ethics
   approval from German Sport University Cologne, no. 248/2025, stated in
   Methods §7; explicit "not preregistered" disclosure added.
5. ~~Software/estimation choice for MFRM undecided~~ — RESOLVED: R-based
   pipeline throughout (`jrt` for JRT; TAM or brms for MFRM), stated in
   Methods §6.

**Unrelated, still open:**

6. **`myszkowski2025`'s DOI is unconfirmed** beyond a CrossRef record (per
   `06_web_literature.md`) — verify before submission if cited.
7. **The mixed-model finding (Finding 2)** is now clearly framed in Methods §6
   as an auxiliary/supporting analysis for RQ2 rather than posing its own
   unlisted research question (see item 12 below), but it still has no
   dedicated Results artifact listed in `02_artifacts.md`; confirm whether it
   warrants its own table or should be folded into the expertise-effects and
   factor-structure tables.

**Resolved at checkpoint 2 (reviewer-critic pass; reflected in the sections
above, kept here only as a changelog):**

8. ~~No pre-specified reliability threshold for RQ1~~ — RESOLVED: ICC(2,k) >=
   .80 target, .70 minimum floor, stated as a pre-specified design decision in
   "Aim and research questions" (RQ1) and Methods, Analysis Plan (a); reflected
   in Results and Discussion RQ1 framing.
9. ~~Total rater-panel size never specified~~ — RESOLVED: a 10-rater benchmark
   panel is now stated in Methods, "Design overview" and "Judges/raters"; the
   additional pairwise-only pool size remains open (logistics-dependent,
   explicitly flagged as such in Methods, not invented).
10. ~~No explicit hypotheses, only research questions~~ — RESOLVED: directional
    hypothesis H1 (RQ1) and competing hypotheses H2a/H2b (RQ2) added under
    "Aim and research questions"; RQ3-RQ5 explicitly stated as open/
    exploratory with reasons given, rather than left hypothesis-free by
    omission.
11. ~~Analysis plan did not commit to CI/effect-size reporting~~ — RESOLVED:
    one-sentence commitment added to the Methods Analysis Plan preamble,
    applying to all six analyses (a)-(f).
12. ~~Confusing "six analyses map onto five RQs" framing~~ — RESOLVED: analysis
    (b), the variance-source mixed model, is now explicitly framed in Methods
    §6 as an auxiliary/supporting model for RQ2, not an independent sixth
    research question (see item 7 above for the still-open artifact
    question).
13. ~~Assignment/rotation mechanism for the pairwise subset unspecified~~ —
    RESOLVED: random assignment constrained to preserve a connected
    rater-by-action network, stated in Methods, "Judges/raters"; cross-
    referenced against the rater-by-action sparsity concern in Limitations
    (partially de-risked, not eliminated).
14. ~~No mention of blinding/player-identity control~~ — RESOLVED: raters will
    view full match footage/context including player/team identity,
    prioritizing ecological validity over blinding, stated in Methods,
    "Rating instrument"; corresponding halo-effect risk added to Limitations,
    tied to MFRM's diagnostic role.
15. ~~Frame-of-reference (FOR) rater training under-specified~~ — RESOLVED:
    brief operational detail added (worked/anchor examples at each of the 7
    scale points, followed by a calibration rating set with feedback), stated
    in Methods, "Rating instrument."

**Newly flagged open at checkpoint 2:**

16. **Rating platform is unnamed.** Left open deliberately — flagged in
    Methods, "Procedure," the same way other open items are flagged (e.g.,
    the additional pairwise-rater-pool size in item 9, and the exact
    "plausible creative-moment candidate" pre-selection criteria in Methods
    §2). Specific platform to be finalized by the author.
