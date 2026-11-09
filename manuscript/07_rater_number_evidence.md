# Rater-number evidence across domains (restructured from `cat_rater_number_findings.json`)

Mechanical restructuring of the external research report (created 2026-11-09) for the outline-architect, manuscript-writer and reviewer-critic. No content was added; wording is the report's paraphrase, not quotations. **Cite only the library keys in the key map** (`~/drive/phd_library.bib`); the report's own keys do not exist in the manuscript bibliography.

## Binding instructions from the report

- Cite via the bibkey fields, which match entries in the companion .bib file.
- Check verification_level before citing a number. Values 'abstract_or_secondary' and 'excerpts' require checking against the original paper.
- All text is paraphrased. No wording here should be presented as a direct quotation; retrieve quotes from the originals.
- Do not compare required rater numbers across studies without stating the reliability target and object of measurement.
- Fields under author_synthesis and planning_recommendations are interpretations from this review, not published findings. Do not attribute them to the cited authors.
- Do not state that Cseh and Jeffries (2019) explicitly require domain-by-domain determination of rater numbers. See cseh_jeffries_2019.framing_caveat.

Verification levels: **full_text** = Checked against full text or an accepted manuscript.; **excerpts** = Checked against partial full-text excerpts; some values were not retrieved.; **abstract_or_secondary** = Known only from an abstract or from citation in another paper.

Evidence classes: **a** = Directly and empirically tested required rater number or rater load.; **b** = Reports reliability for a given panel only.; **c** = Recommendation without a dedicated empirical basis.

## Key map (report key → library key)

| Report key | Library key |
|---|---|
| Amabile1982 | `amabile1982` |
| Barth2021 | `barth2021` |
| Cseh2019 | `cseh2019` |
| Forthmann2025 | `forthmann2025` |
| Forthmann2017 | `forthmann2017` |
| Goecke2024 | `goecke2024` |
| Haller2011 | `haller2011` |
| Hass2018 | `hass2018` |
| Hickey2001 | `hickey2001` |
| Kaufman2009 | `kaufman2009` |
| Kaufman2008 | `kaufman2008a` |
| Kaufman2013 | `kaufman2013` |
| KaufmanGentile2005 | `kaufman2005` |
| Kaufman2007 | `kaufman2007` |
| KaufmanPlucker2008 | `kaufman2008` |
| Long2015 | `long2015` |
| Long2022 | `long2022` |
| Myszkowski2021 | `myszkowski2021` |
| Myszkowski2019 | `myszkowski2019` |
| Primi2019 | `primi2019` |
| Roca2018 | `roca2018` |
| Silvia2008 | `silvia2008` |
| Stefanic2015 | `stefanic2015` |
| Terai2026 | `terai2026` |
| vanHooijdonk2022 | `vanhooijdonk2022` |

Notes: `kaufman2008a` = Kaufman, Baer, Cole & Sexton (2008, CRJ, experts vs nonexperts); `kaufman2008` = Kaufman, Plucker & Baer (2008, *Essentials of creativity assessment*). `terai2026` is the issue year (online 2024). `goecke2024` was updated to the published JCB version on 2026-11-09. Ten entries were added to the library on 2026-11-09 with Crossref metadata (haller2011, hass2018, hickey2001, kaufman2005, kaufman2007, long2022, silvia2008, stefanic2015, terai2026, vanhooijdonk2022).

## Bottom line (report)

No domain has a validated, general required number of raters. Published figures are conditional on reliability target, rater expertise and training, scale design, product heterogeneity, number of products and scoring format.

| Condition | Finding |
|---|---|
| Trained or expert raters scoring short, homogeneous responses (divergent thinking, captions) | About 2-5 raters reach relative reliability near .80. |
| Novices judging expert-domain products (poems, stories, engineering designs) | Random panels of 10 novices average alpha of about .53-.66. Very large panels can reach high alpha yet converge poorly with experts (poetry: r = .22). |
| Open-ended products rated by non-experts (fashion, design) | About 7-15 raters for stable aggregate scores; 15-20 for composite indices. |
| Person-level measurement with high person-by-task variance | Adding raters stops helping. With 2 divergent-thinking items, no panel of 1-10 lay raters reached .80 (Hass et al., 2018). More tasks are needed. |
| Sport/tactical creativity, music, mathematics, advertising, programming | No empirical rater-number study located; reliability reports or conventions only. |

## Cseh and Jeffries (2019) (`cseh2019`; verification: full_text)

- **Expertise.** Expertise is undefined and domain-dependent. Evidence on experts versus novices is equivocal: expertise increases consensus only sometimes, and when or why it is vital is unclear. Quasi-experts substituted for experts in writing but not engineering (Kaufman et al., 2013). Sufficient type and length of experience remain open.
- **Number of judges.** Amabile (1982) tied the number to achieving acceptable agreement rather than fixing one. Silvia et al. (2008) and Kaufman, Plucker and Baer (2008; 5-10 judges) offer rough guidance. Practice ranges from 2 judges (Daly et al., 2016; 439 engineering designs; agreement .70) to 134 lay judges; Amabile's own studies used 3-21. The authors list the number needed for reliable consensus as an open research question.
- **Type I / Type II analogy.** More than 10 judges is argued to raise Type I error risk for inter-rater reliability; fewer than 5 is argued to raise both error types. This is conceptual, not empirical.
  - *Author synthesis (report, not Cseh & Jeffries):* The analogy arguably conflates a genuine reliability gain from a larger panel mean with a false positive, and does not address whether larger-panel consensus is valid.
- **Reliability reporting.** Cronbach's alpha is the default largely by convention. Consistency and absolute agreement are seldom distinguished (citing Stefanic and Randles, 2015), ICC forms are seldom declared, and designs where raters score different subsets are rarely addressed. JRT (Myszkowski and Storme) is noted as a model-based alternative.
- **Procedural issues.** Rater fatigue and items per judge (about 3,564 ratings per judge in one reused dataset), scale granularity (3-10 points), training and calibration versus the CAT's theoretical neutrality, and whether some tasks have any appropriate expert.

**Framing caveat (binding):** Cseh and Jeffries do not explicitly state that rater numbers must be determined separately per domain. That follows from their evidence on domain-by-expertise interactions and from G-theory authors such as van Hooijdonk et al. (2022), who argue that each assessment procedure needs its own G- and D-study.

## Studies

| Library key | Domain | Task | Object | Raters | Criterion | Method | Required raters | Class | Verification |
|---|---|---|---|---|---|---|---|---|---|
| `silvia2008` | Divergent thinking | Unusual uses, instances, consequences | persons | Trained student raters (3 per response) | Relative G >= .80 | G-study and D-study | {"average_scoring": {"uses": {"raters": 2, "G": 0.82}, "instances": {"raters": 2, "G": 0.84}, "consequences": {"raters": 3, "G": 0.83}}, "top2_scoring": {"uses": {"raters": 3, "G": 0.81}, "instances": {"raters": 4, "G": 0.83}, "consequences": {"raters": 5, "G": 0.83}}} | a | excerpts |
| `hass2018` | Divergent thinking | Alternate uses (AUT), consequences | persons | 3 MTurk laypeople per scoring system; about 2,091 unique responses from 80 participants | E rho-squared >= .80 | G-study and D-study, fully crossed p x i x r | With 2 items, no number of raters from 1 to 10 reached .80. With 3 raters: at least 4 AUT items or at least 8 consequences items. Phi stayed below .80 for every design considered. Snapshot scoring never reached .80. | a | full_text |
| `primi2019` | Divergent thinking and metaphors | Metaphors (Study 1); AUT and instances (Study 2) | persons | Study 1: N = 132, 3 raters. Study 2: N = 298, 4 raters, 88,256 ratings | Correlation with full-data scores; Rasch reliability | Many-facet Rasch model with simulated missingness | No headcount. Rater workload could be cut by about one third with similar scores. | a (rater load and design) | full_text |
| `forthmann2017` | Divergent thinking | Subjective divergent-thinking scoring | persons | Not extracted | Rater agreement | Cognitive workload effects on rater disagreement | No headcount. | b | abstract_or_secondary |
| `kaufman2007` | Creative writing | Captions (12 from each of 81 undergraduates) | persons | 4 psychology graduate students | g and phi >= .80 | G-study and D-study | 5 raters with 15 captions | a | excerpts |
| `kaufman2008a` | Creative writing | Poetry | products | 10 expert poets; 106 novices | Cronbach's alpha | Spearman-Brown or resampling to smaller panels | No threshold established. 10 novices are insufficient, and even 106 novices converged poorly with experts. | a | abstract_or_secondary |
| `kaufman2013` | Creative writing | 205 short stories (Study 1) | products | 10 expert writers; quasi-expert subgroups of 9-12; 106 novices | Cronbach's alpha | Resampling: 100 random panels of 10 novices | 9-12 quasi-experts or 10 experts perform well; 10 novices do not. | a | full_text |
| `kaufman2013` | Engineering design | 5 mousetrap designs (Study 2) | products | 15 professional engineers; 31 first-year engineering students; 274 novices | Cronbach's alpha | Resampling: 100 random panels of 10 novices | No threshold established. Quasi-experts were not adequate substitutes for experts. | a | full_text |
| `kaufman2005` | Creative writing | Poems and stories | products | Gifted novice writers | Cronbach's alpha | Reliability and correlation with experts | Not tested. | b | abstract_or_secondary |
| `terai2026` | Design products | Creativity-related indices of design products | products | 84 undergraduates | Test-retest ICC >= .70 | Random subsampling of raters | 10-15 for creativity ratings; about 15-20 for composite originality-practicality indices (product or Euclidean distance) | a | abstract_or_secondary; Abstract and excerpts only. |
| `haller2011` | Product design | Design products rated with CSDS | products | 5 experts; 5 novices | Cronbach's alpha | Reliability report | Not tested. | b | abstract_or_secondary |
| `barth2021` | Fashion / visual products | 90 Instagram fashion outfits, rated twice 2 or 4 weeks apart | products | 61 non-experts | ICC >= .70 (inter-rater and test-retest) | ICCs for the full panel and random panels of 3, 5, 7 and 10 raters | 7 or more for consistently exceeding .70, inter-rater and test-retest. 3-rater samples already exceeded .70 for test-retest, but not consistently. | a | excerpts |
| `amabile1982` | Visual art | Children's collages | products | Psychologists, art teachers, artists; panels of 3-21 | Alpha > .70 | Reliability report | Not tested. | b | abstract_or_secondary |
| `long2015` | Scientific creativity | 2 science tasks; 48 sixth-graders | persons | 45 raters (students, teachers, researchers); 2,160 ratings | Dependability | G-theory, mixed methods | Exact D-study numbers not verified. Dependability was low for all rater groups; van Hooijdonk et al. (2022) summarize that too many raters would be required for relative and absolute decisions. | a | abstract_or_secondary |
| `vanhooijdonk2022` | Creative problem solving | 1 science and 1 social task; 137 primary pupils | persons | 2 trained raters | Generalizability >= .70 | G-study and D-study | {"relative": {"originality": {"tasks": 5, "raters": 2}, "completeness": {"tasks": 5, "raters": 2}, "practicality": {"tasks": 3, "raters": 2}}, "absolute": {"originality": [{"tasks": 10, "raters": 4}, {"tasks": ">=30", "raters": 2}], "completeness": {"tasks": 4, "raters": 4}, "practicality": {"tasks": 8, "raters": 2}}} | a | full_text |
| `goecke2024` | Scientific creativity (German) | Scientific creativity responses | persons | 40 raters (Prolific) | Expected reliability >= .80, framed through factor determinacy | Simulation-based planned-missing design with GPCM, following Forthmann, Goecke and Beaty (2023) | 40 raters, 4 ratings per response for 50% of responses | a (applied design) | excerpts |
| `stefanic2015` | Music | Individual compositions and group performances by pre-service teachers | products | 5 music-education judges | Alpha and absolute agreement | Reliability analysis with partial G-theory decomposition | No optimal number. Number of raters mattered far more than number of occasions. | b | excerpts |
| `hickey2001` | Music | Children's compositions | products | Composers, music teachers, music theorists, seventh-graders, second-graders | Inter-judge reliability | Reliability comparison by rater type | Not tested. | b | abstract_or_secondary |
| `roca2018` | Sport / soccer tactical creativity | Originality of creative decision making in soccer | persons | 3 UEFA-qualified coaches; 1-5 scale | ICC | Reliability report | Not tested. Part of a convention of about 3 raters. | b | excerpts |
| `long2022` | Cross-domain review | Review of 84 empirical studies of subjective creativity assessment | not applicable | Most reviewed studies had fewer than 10 raters; mean and median about 5 | Not applicable | Literature review | No optimal number established. | b | excerpts |
| `kaufman2008` | General | General recommendation | not applicable | Not applicable | None | Expert recommendation | 5-10 judges for most purposes | c | abstract_or_secondary; As cited in Cseh and Jeffries (2019). |

### Study details (results and notes)

**`silvia2008` — Divergent thinking**
- required_raters:
  - average_scoring: 
    - uses: 
      - raters: 2
      - G: 0.82
    - instances: 
      - raters: 2
      - G: 0.84
    - consequences: 
      - raters: 3
      - G: 0.83
  - top2_scoring: 
    - uses: 
      - raters: 3
      - G: 0.81
    - instances: 
      - raters: 4
      - G: 0.83
    - consequences: 
      - raters: 5
      - G: 0.83
- notes: Gain in dependability diminishes after 3-4 raters. Authors' summary: 2 raters for Average scoring, 3 for Top-2.

**`hass2018` — Divergent thinking**
- results:
  - three_raters_two_items: 
    - AUT: 
      - E_rho2: 0.65
      - phi: 0.47
    - consequences: 
      - E_rho2: 0.52
      - phi: 0.27
  - rater_variance_percent: 
    - AUT: 26.6
    - consequences: 56.9
  - person_by_rater_variance_percent: 
    - AUT: 1.2
    - consequences: 2.5
- notes: Too few items cannot be compensated by more raters when person-by-item variance is large. Large rater main effects indicate severity differences.

**`primi2019` — Divergent thinking and metaphors**
- results:
  - severity_range_logits: 
    - study1: -1.18 to .64
    - study2_range: 0.9
  - severity_adjusted_score_correlation_with_full_data: 
    - 67_percent_of_data: 0.93
    - 43_percent_of_data: 0.74
  - rasch_separation_reliability_metaphor_data: 0.46
- notes: Severity differences were significant in Study 2.

**`forthmann2017` — Divergent thinking**
- notes: Disagreement increases with workload (be-creative instructions; snapshot or complex response sets), implying that rater needs depend on scoring format.

**`kaufman2007` — Creative writing**
- results:
  - single_rater_reliability_across_captions: .50-.83
- notes: Exact D-study coefficients were not retrieved.

**`kaufman2008a` — Creative writing**
- results:
  - alpha_10_experts: 0.83
  - alpha_106_novices: 0.94
  - alpha_10_novices_approx: .53-.58
  - expert_novice_r: 0.22
- notes: Secondary sources disagree: Cseh and Jeffries give .53 for poetry; Kaufman et al. (2013) give .58 for poetry and .53 for stories.

**`kaufman2013` — Creative writing** (related: `kaufman2009`)
- results:
  - alpha_experts: 0.93
  - alpha_quasi_experts: .86-.92
  - alpha_106_novices: 0.99
  - alpha_10_novices_mean: 0.53
  - alpha_10_novices_range: .35-.75
  - expert_novice_r_full_panel: 0.72
  - expert_novice_r_10_novice_panels_mean: 0.56
  - expert_quasi_expert_r: 0.89

**`kaufman2013` — Engineering design**
- results:
  - alpha_experts: 0.86
  - alpha_quasi_experts: 0.93
  - alpha_274_novices: 0.98
  - alpha_10_novices_mean: 0.66
  - alpha_10_novices_min_approx: 0.06
  - expert_novice_r: 0.29
  - expert_quasi_expert_r: 0.52
- notes: Only 5 products, so alpha rests on a very small sample of objects.

**`kaufman2005` — Creative writing**
- results:
  - alpha: 
    - poems: 0.82
    - stories: 0.74
  - correlation_with_experts: 
    - poems: 0.78
    - stories: 0.77

**`terai2026` — Design products**
- notes: Individual raters were unstable over time.

**`haller2011` — Product design**
- results:
  - median_alpha_CSDS_total_approx: 0.87
  - novice_total_alpha_range: .74-.92

**`barth2021` — Fashion / visual products**
- results:
  - full_panel_test_retest_ICC: above .90
  - mean_single_rater_ICC_C1_2_week: 0.714
  - share_of_raters_above_.70_2_week: 0.61
- notes: Panel-specific ICC values were not retrieved.

**`amabile1982` — Visual art**
- results:
  - reliability_range: .73 (psychologists) to .88 (art teachers)

**`long2015` — Scientific creativity**
- notes: Low dependability attributed to inconsistent rating procedure, scale use and beliefs about creativity. Rater inconsistency differed across tasks.

**`vanhooijdonk2022` — Creative problem solving**
- results:
  - current_design_2_tasks_2_raters: 
    - relative_g: 
      - originality: 0.49
      - completeness: 0.49
      - practicality: 0.61
    - absolute_D: 
      - originality: 0.4
      - completeness: 0.45
      - practicality: 0.46
- required_raters:
  - relative: 
    - originality: 
      - tasks: 5
      - raters: 2
    - completeness: 
      - tasks: 5
      - raters: 2
    - practicality: 
      - tasks: 3
      - raters: 2
  - absolute: 
    - originality: 
      - 
        - tasks: 10
        - raters: 4
      - 
        - tasks: >=30
        - raters: 2
    - completeness: 
      - tasks: 4
      - raters: 4
    - practicality: 
      - tasks: 8
      - raters: 2

**`goecke2024` — Scientific creativity (German)**
- results:
  - expected_average_reliability: 0.822
- notes: A design solution for a specific rater budget and response pool, not a minimum for the domain.

**`stefanic2015` — Music**
- results:
  - consistency_alpha: 
    - individual: 0.9
    - group: 0.86
  - absolute_agreement: 
    - individual: 0.79
    - group: 0.87
  - aesthetic_sensitivity_range: .57-.71
  - test_retest_creativity: 0.89

**`hickey2001` — Music**
- results:
  - reliability: 
    - composers: 0.04
    - music_teachers: 0.64
    - music_theorists: 0.73
    - seventh_graders: 0.61
    - second_graders: 0.5
- notes: Expert status alone did not guarantee consensus.

**`roca2018` — Sport / soccer tactical creativity**
- results:
  - ICC: 0.85
- notes: Other Memmert-group game-test work reportedly used 3 trained experts on 1-10 scales (one consistency coefficient of .74). A goal-sequence study reportedly obtained .89-.92 with 3 UEFA A/Pro raters, known only from a practitioner summary. Neither has a confirmed citation here; locate the originals before citing.

**`long2022` — Cross-domain review**
- notes: Alpha differed through an interaction of domain and judge expertise.

**`kaufman2008` — General**

## Analytic approaches (report)

**Spearman-Brown or alpha projection** (`kaufman2008a`). Project single-rater reliability to k raters.
- strengths: Simple; Needs little data
- weaknesses: Assumes parallel raters; Alpha ignores rater severity; Does not separate rater-by-product interaction; Rises with panel size alone

**Resampling raters from a large pool** (`kaufman2013`, `barth2021`, `terai2026`). Draw repeated panels of size k; examine the distribution of reliability and convergence with full-panel or expert scores.
- strengths: Shows risk across panels, not only the mean; Allows validity-relevant convergence checks
- weaknesses: Requires a very large pool; Results are pool-specific

**Generalizability theory with D-studies** (`silvia2008`, `kaufman2007`, `hass2018`, `long2015`, `vanhooijdonk2022`). Decompose variance into person, rater, item and interaction components; project relative and absolute coefficients across rater and task numbers.
- strengths: Separates relative and absolute decisions; Trades raters against tasks; Phi reflects rater severity
- weaknesses: Does not scale or correct individual raters; Needs balanced or near-balanced designs; Assumes interchangeable raters

**Many-facet Rasch modeling** (`primi2019`). Estimate rater severity and fit; compute severity-adjusted scores; link raters through incomplete designs.
- strengths: Corrects severity rather than only quantifying it; Supports incomplete linked designs
- weaknesses: Assumes equal rater discrimination; Requires design connectedness

**Judge response theory / IRT** (`myszkowski2019`, `myszkowski2021`). Treat judges as items in GRM or GPCM models, yielding judge-specific discrimination and thresholds and reliability conditional on creativity level.
- strengths: Conditional reliability; Judge-level diagnostics; Supports selecting complementary judges
- weaknesses: Needs adequate data for judge parameters
- notes: Estimates of creativity levels are reported to be especially affected when judges are few.

**Simulation-based planned-missing designs** (`forthmann2025`, `goecke2024`). Estimate parameters from prior or pilot data; simulate designs varying raters, ratings per response and share of doubly rated responses; evaluate against reliability and cost.
- strengths: Explicit planning under budget constraints; Accommodates sparse designs
- weaknesses: Depends on how representative pilot parameters are

## Limits of reliability evidence (report)

- **Validity.** High consensus need not reflect domain creativity: 106 novices reached alpha = .94 on poetry yet correlated .22 with experts. (`kaufman2008a`)
- **Severity and leniency.** Do not affect alpha or relative G in fully crossed designs, but confound scores when raters score different subsets, and matter for phi. (`primi2019`, `hass2018`)
- **Rater-by-product interaction.** Treated as error in classical and G-theory indices; JRT can partly model it as information. (`myszkowski2019`)
- **Consistency versus absolute agreement.** In the same music data, individual creativity had alpha .90 but agreement .79. (`stefanic2015`)
- **Temporal stability.** Individual raters drift even when aggregates remain stable. (`barth2021`, `terai2026`)

## Gaps and inconsistencies (report)

- Domains without located rater-number studies: Sport/tactical creativity, Dance/movement, Music (headcount), Mathematics, Advertising, Business-idea evaluation, Humor/cartoon captions, Programming
- Inconsistent targets: Alpha > .70, G or phi >= .80, generalizability >= .70, test-retest ICC >= .70, and factor determinacy >= .80 are not directly comparable.
- Inconsistent object of measurement: Person-level studies across tasks have tasks competing with raters; product-level studies have raters as the only facet.
- Generalization limits: Small product samples (5 mousetraps); Results from single rater pools
- Secondary-source discrepancies: Ten-novice poetry alpha is given as .53 or .58 depending on the citing paper.

## Planning recommendations — status: author_synthesis (NOT published findings; do not attribute to cited authors)

Derived from this review; these are not published standards. The numeric fallback is a judgment call without direct empirical support.

1. Define the object of measurement and decision type. Use relative G for correlational research; use phi or ICC(A) for absolute standards or rater-subset designs.
2. Run a pilot G-study with more raters than planned (e.g., 8-10 domain-matched raters, such as UEFA-licensed coaches for soccer, plus a quasi-expert group). Run D-studies over raters and situations, targeting >= .80 relative and reporting phi. Expect tasks or situations to be the bottleneck.
3. Resample the pilot panel (all k-subsets or about 1,000 draws) and report the distribution of reliability and full-panel correlation for k = 2 to 10.
4. Fit an MFRM or JRT model to quantify severity and judge discrimination and to flag misfitting raters. If rater load is high, simulate a linked planned-missing design.
5. Test rater-type validity by correlating quasi-expert or novice panels with experts, and collect discriminant ratings such as technical execution or effectiveness.

Fallback without pilot (author synthesis): At least 5-7 domain experts for product ratings. Three raters only for short, homogeneous responses with trained raters and a clear rubric. Avoid fewer than about 10 lay raters for expert-domain products.

## Open verification items (report)

- Long and Pang (2015): exact D-study rater numbers.
- Terai et al.: confirm values in Table 3 and final publication year, volume and pages.
- Haller et al. (2011): reliability values.
- Barth and Stadtmann (2021): panel-specific ICCs in Table 2.
- Kaufman et al. (2008): resolve .53 versus .58.
- Kaufman et al. (2007): exact D-study coefficients.
- Soccer: locate original sources for the Memmert-group reliabilities.
- Goecke et al. (2024): full author list and confirm the title against the DOI.
- Daly et al. (2016), cited in Cseh and Jeffries: reference not available here and not in the .bib file.

---
Source metadata: created 2026-11-09; scope note: Based on a time-limited literature search. Absence of a study here does not establish absence from the literature.
