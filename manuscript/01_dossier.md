# 01_dossier.md — Vault research dossier (Phase 1)

Paper: Creativity assessment in sport via the CAT; Judge Response Theory (JRT) as core scoring/analysis model. Profile imrad-apa, target Creativity Research Journal.
Brief: `/home/max/drive/KNOWLEDGE/Paper_CreativityAssessmentInSportsCAT.md`
Vault: `/home/max/drive/KNOWLEDGE/`. All paths below are relative to the vault root unless absolute.

> Provenance rule: everything here is vault-sourced background. The vault notes contain some design figures (e.g., numbers of raters/actions, ratings per action). They are **not results** and must not enter the manuscript unless they come from the notebook via results-interpreter.

## Relevant notes

| Note path | Why relevant | Key passage (short) |
|---|---|---|
| `Paper_CreativityAssessmentInSportsCAT.md` | The brief: aims, argument chain, citekeys | "JRT … seems to be the most suitable choice to handle CAT ratings from multiple rater … and will be the core of analysis" |
| `JudgeResponseTheory.md` | Core model note: GRM/GPCM families, eight `jrt` models, nesting, judge parameters, outputs, estimation in sparse designs, limitations, applications | "Equal discrimination and a shared category structure are therefore not imposed. They become *testable constraints* through model comparison" |
| `ConsensualAssessmentTechnique.md` | CAT origin, procedure, reliability (Spearman–Brown, alpha), expertise, rater effects, criticisms, CAT in sport | "interjudge reliability in the CAT *is* construct validity"; "no sport study has examined the psychometrics of CAT ratings themselves" (novelty claim, author to confirm) |
| `ItemResponseTheory.md` | General IRT background: CTT vs IRT, polytomous models, information, EAP, relation to GLMMs | "judges are the 'items': product creativity is θ_p, judge severity is b_i …, judge consistency/expertise is a_i" |
| `RaschModel.md` | RSM/PCM, sufficiency, specific objectivity, prescriptive vs descriptive stance | "Fit statistics are how Rasch detects unequal discrimination; it does not model it." |
| `ManyFacetRaschModel.md` | MFRM equation, fair averages, rater-effect diagnostics, relation to LMM/G-theory, limitations leading to JRT (background only) | "differential discrimination … has no parameter: it appears only as misfit" |
| `GeneralizabilityTheory.md` | G/D-study, Spearman–Brown link, sparse/incomplete designs (harmonic mean, non-overlap term q), BLUP vs raw means (background; number-of-judges framing) | "With 22 raters and < 2 ratings per action … Severity differences then hurt rankings, not only levels." (design figure: not a result) |
| `IntraclassCorrelation.md` | ICC taxonomy, alpha = ICC(C,k), sparse-design problems, ordinal/latent ICCs, Koo & Li thresholds | "Cronbach's α … equals ICC(C,k) = ICC(3,k) … undefined for the sparse football design" |
| `C___BibliographicNotes/@myszkowski2019.md` | Summary of the JRT proposal | CTT critique; GRM simulation (4 judges, 30 products); "no need to 'brainwash' judges into parallel scale use" |
| `C___BibliographicNotes/@primi2019.md` | Summary of MFRM in creativity | Rater severity confounds scores in planned-missing designs; fair averages robust at moderate missingness; response styles left to future work |
| `C___BibliographicNotes/@cseh2019.md` | "A scattered CAT" | Amabile used 3–21 judges; "5–10" rule of thumb; panels from 2 to >100; "Large panels may inflate consensus"; number of judges must be established per domain |
| `C___BibliographicNotes/@amabile1982.md` | CAT origin | Spearman–Brown reliability depends on mean inter-judge r and number of judges; creativity vs technical goodness separate in factor analysis |
| `C___BibliographicNotes/@kempe2018.md` | Only CAT-like sport precedent in the vault | 3 UEFA A/Pro-licence experts, *trained* on the scale (Memmert & Roth, 2007), 1–10 scale, ICC reported, last 8 actions before open-play goals at WC 2010/2014 and Euro 2016 |
| `CreativityRatingStudy.md` | **Methods background**: design plan for the football rating study | Overlapping pairs plus a benchmark set rated by all; 7-point unipolar scale; randomised order; three dimensions (creativity, technical correctness, aesthetic appeal); "no formal training and no specific criteria"; analysis "JudgeResponseTheory TBD" |
| `RatingScaleCreativityInSports.md` | **Methods background**: rationale for the scale (AI-generated text, sources unverified) | 7-point unipolar; novelty × appropriateness; "Can't judge" option; suggests calibration training (which conflicts with the CAT) |
| `PsychologicalRatingScales.md` | **Methods background**: number of categories and polarity (AI-generated text, sources unverified) | 7 categories as optimum (Preston & Colman 2000; Lozano et al. 2008); unipolar for amount-type constructs |
| `CreativityDefinition.md` | **Methods background**: definition shown to raters (German) | Originality (rarity relative to peers) and functionality (intended effect, luck discounted), judged in game context, independent of success, appearance or technical quality; [[@runco2012]] |
| `CreativityRatingApp.md` | **Methods background**: rating software | Kivy vs Streamlit implementations; randomisation |
| `CreativityProject.md` | Project context; pilot plan on fatigue; this paper is publication 1 of 3 | Pilot: several raters rate the same series; "where the agreement starts to decline rapidly, cut the number of videos" per session |
| `DFGCreativity.md` | Grant context; planned questions on rater demographics and expertise | "consult [[@cseh2019]] to decide how many ratings per action"; "record ratings from people with potentially heterogeneous background, expertise, demographics" |
| `StudentThesisProjects.md`, `StudentThesisProjectsGerman.md`, `StudentProjects.md` | Origin of raters (students' theses; 5 h or 10 h of rating each); open methodological questions | "how many raters for convergence? … what effect does expertise play? [[@castel2007]]; [[@baer2015]] … how long can the task be done reliably?" |
| `1___ResearchPlan.md`, `1___ResearchIdeas.md` | Author's framing of the methods paper | "How many raters are needed for convergence? … How does IRT or JRT perform on the data?" |
| `Paper_AutomatedRatingCreativitySoccer.md` | Downstream use of the scores (labels for automated models); justification via labour cost | "enormous labour cost … increases exponentially if researchers aim to provide multiple ratings per product" |
| `CreativityAssessment.md` | Barbot special issue; taxonomies | "taxonomies needed in order to clarify which facet of creativity is being assessed" |
| `CreativityInSports.md` | Very thin | "assessing creativity in an ecologically valid environment is important for sports" |
| `CreativityResearch.md` | **Empty** (only an LSA link); nothing usable | — |

## Themes

### T1. The CAT as a procedure, separate from how it is scored (Introduction)
The vault consistently separates the CAT as a way of collecting data (independent, domain-familiar judges; relative judgements; random order; no criteria; extra dimensions such as technical goodness and aesthetic appeal) from the choice of scoring model. The psychometric criticism (myszkowski2019) is aimed at classical scoring (sums or means plus alpha), not at the procedure (`ConsensualAssessmentTechnique.md`). The consensual definition makes judge agreement, by definition, the construct-validity criterion (hennessey2011). Taxonomy framing: Batey's person/process/product/press, with the CAT located at individual level, product facet, other-rated (batey2012; `CreativityRatingStudy.md`).

### T2. Reliability rests on panel size and can hide weak single-judge agreement (Introduction/Discussion)
Spearman–Brown (amabile1982) and alpha = ICC(C,k) both grow with the number of judges, so a large panel can mask low single-judge agreement (kaufman2008; cseh2019 "large panels may inflate consensus"). The vault explains, mathematically, that a G-theory D-study is Spearman–Brown for a one-facet design (`GeneralizabilityTheory.md`, `IntraclassCorrelation.md`). The domain-specific "how many judges" question (cseh2019) is the stated gap.

### T3. Scoring models as successive relaxation of assumptions about judges (Introduction; competitors as background only)
The vault builds a single chain: means/alpha (τ-equivalent, equally severe judges) → crossed LMM/G-theory (additive severity, one slope, interval scale) → Rasch/MFRM (ordinal adjacent-category link, severity facet, equal discrimination, optional rater-specific thresholds) → JRT (free discrimination per judge and judge-specific thresholds). Recurring points:
- In sparse designs raw means are confounded with which judges rated a product (primi2019); a constant severity shift cancels out only in complete designs.
- The MFRM cannot represent differential discrimination except as misfit (myford2004; myszkowski2021).
- The vault itself qualifies primi2019's claim that G-theory "will not … correct a participant's estimated trait score": this holds for ANOVA-based G-studies, but crossed-LMM BLUPs do adjust for severity (`ManyFacetRaschModel.md`, `GeneralizabilityTheory.md`). Useful for a balanced account of the competitors.

### T4. JRT specifics for the Methods (core)
From `JudgeResponseTheory.md`:
- Judges as items, products as persons. Eight `jrt` models in two families that are not nested with each other: cumulative (GRM, constrained GRM, GRSM, constrained GRSM) and adjacent-category (GPCM, PCM, generalised RSM, RSM).
- Within a family, models are nested and can be compared by likelihood-ratio test. Across families, comparison uses information criteria (AICc is the `jrt` default) and Akaike weights.
- The RSM with judges as items equals a two-facet MFRM, which links JRT to the Rasch line.
- Judge parameters: a_j is discrimination (a factor loading; congeneric vs τ-equivalent judges). b_jk are thresholds: their mean is severity, their spacing is response style (central tendency, extreme responding, unused categories).
- Outputs: judge category curves, information functions, EAP scores with conditional standard errors, empirical vs marginal reliability, and non-IRT statistics for comparison.
- Estimation: MML in `mirt` (chalmers2012) or Bayesian (brms, Stan, PyMC).
- Identification in sparse designs: the design must be connected; a_j is informed mainly by co-rated products; shared-structure models fail if a judge leaves a category unused; missingness must be ignorable (non-random allocation of actions can confound severity with creativity).
- Limitations: only two facets in `jrt`; per-judge sample size; local independence (e.g., shared rater background, conferring); unidimensionality; information grows without bound as judges are added (motivation for the HRM, patz2002).
- Extensions: hierarchical rater model (patz2002) and generalised MFRM (uto2020; the many-facet version of the JRT GPCM).

### T5. JRT applications in creativity research (Introduction/Discussion)
myszkowski2021 (tutorial), barbot2023 (VR drawings, CRJ), forthmann2023 (planning planned-missing rating designs with JRT and simulation, CRJ), pellegrino2025 (divergent-thinking ratings; GRM retained; rater severity and discrimination examined; notes that `jrt` cannot model raters and tasks together). No sport application of JRT is recorded in the vault.

### T6. Who is an appropriate judge? (Discussion: expertise)
- Experts are more consistent than novices: kaufman2008 (poems), kaufman2009 (short stories).
- Quasi-experts are a possible compromise (kaufman2012a).
- Lenient view for everyday domains (hennessey2011).
- Plucker et al. (2009) on movie-watching students vs critics, summarised in `CreativityRatingStudy.md` (not in bib): expertise only sometimes increases consensus.
- "Dark side of expertise" (castel2007) and domain-specific expertise (baer2015) are listed as seeds in the student-thesis notes; their bibliographic notes have no summary.
- Domain specificity of creativity: baer1998, baer2012, baer2015.

### T7. Rater effects and their stability (Discussion: rater behaviour)
- long2015: low reliability attributed to differences in following the procedure, in using the scale, and in beliefs about creativity.
- barth2020: product means are stable over time but individual raters' tendencies drift (time-sampling error).
- Classic rater-effect taxonomy from MFRM: engelhard1994; myford2003; myford2004 (severity, central tendency, restriction of range, randomness, halo, differential severity).
- JRT turns severity, discrimination and scale use into parameters of each judge.

### T8. Football study design and rating scale (Methods background, vault-sourced, not results)
From `CreativityRatingStudy.md`, `RatingScaleCreativityInSports.md`, `CreativityDefinition.md`, `CreativityProject.md`, student-thesis notes:
- **Sample of actions.** Matches from several competitions (FIFA men/women, AFCON, UEFA men/women, Copa América), with matches from different teams. StatsBomb event data as the basis for cutting videos.
- **Raters.** Bachelor's and Master's students rating as part of their theses (5 h or 10 h).
- **Design plan.** A benchmark set rated by all raters (intended partly as a fatigue pilot) plus overlapping rater pairs (A/B, B/C, …) for linkage. "Aim for 5–10 judges, at least on a benchmark set …; after that, 5 maximum, maybe only 2–3." Plan figures differ from the realised design mentioned in the method notes; take actual numbers only from the notebook.
- **Sessions.** About 1 h per session with breaks; about 20–35 s per clip; 45–60 min seen as the maximum.
- **Scale.** 1–7 unipolar ("not at all creative", "somewhat creative", "very/extremely creative" at 1/4/7). Justified by number-of-categories literature (sources unverified). Off-scale "action not recognised / can't judge" option.
- **Extra dimensions.** Technical correctness and aesthetic appeal, following amabile1982.
- **Instructions.** Randomised order; independent judgement; "no formal training and no specific criteria", **but** a definition of creativity is shown (originality × functionality in game context; runco2012). `RatingScaleCreativityInSports.md` additionally recommends calibration training with anchors, which contradicts the CAT procedure. Discussion point (cf. kempe2018, who trained raters).
- **Planned analysis note.** Within-rater z-scores as a sensitivity check.

### T9. Practical implications for sport science (Discussion)
Seeds in the vault:
- Panel size via D-study or Spearman–Brown logic, or via JRT information and simulation (forthmann2023).
- Planned-missing designs to reduce workload (primi2019; forthmann2023).
- Selecting raters on discrimination a_j rather than only on expertise labels.
- Rater-specific scale use argues against relying on raw means.
- Precision of each action's score matters for downstream use, e.g., labels for automated models (`Paper_AutomatedRatingCreativitySoccer.md`); labour cost as a motivation.
- Fatigue and session length (`CreativityProject.md` pilot logic).
- Rater demographics (age, gender, nationality, coaching/playing expertise) as a planned follow-up (`DFGCreativity.md`).

## Existing references

### Brief citekeys present in `/home/max/drive/phd_library.bib`
amabile1982, cseh2019, myszkowski2019, myszkowski2021, primi2019, kempe2018, memmert2011, myford2003, myford2004, embretson2013, batey2012, barbot2019, barbot2019b, hennessey2010, safardilha2019.

### Brief citekeys MISSING from the bib (must be added or replaced)
kaufman2008, baer2004, hennessey2011, long2015, linacre1989, eckes2015, samejima1969, muraki1992, deayala2022, bond2020, andrich1978, masters1982, rasch1960, lord1980, worldeconomicforum2025, oecd2024, amabile1985, engelhard1994 (cited in the brief body).
Full reference strings with DOIs for most of these are in the vault's References sections: `ConsensualAssessmentTechnique.md`, `ItemResponseTheory.md`, `RaschModel.md`, `ManyFacetRaschModel.md`. worldeconomicforum2025 and oecd2024 have no vault reference text.

### Useful additional keys from vault notes
- **In bib:** bates2015, nakagawa2017, salvatier2016, baer1998, baer2012, baer2015, castel2007, runco2012, beaty2020, distefano2024.
- **Not in bib** (full references with DOIs in the vault notes):
  - Creativity/CAT and sport: kaufman2009, kaufman2012a, barth2020 (published 2021), zahno2024, dejoode2023.
  - JRT and applications: forthmann2023 (published 2025), pellegrino2025, barbot2023, chalmers2012, muraki1990, takane1987, burkner2021, burkner2017, patz2002, uto2020.
  - Reliability, G-theory, ICC: tenhove2022, tenhove2024, tenhove2025, shrout1979, mcgraw1996, koo2016, brennan2001, cronbach1972, silvia2008, hallgren2012.
  - Rasch/IRT: wright1982, deboeck2004.
- **Mentioned in plain text, no key, not in bib:** Kaufman, Plucker et al. (2008) "5–10 judges"; Plucker, Kaufman, Temple & Qian (2009); Christiaans & Venselaar (2005); Memmert & Roth (2007); Preston & Colman (2000); Lozano, García-Cueto & Muñiz (2008).

### Inconsistencies to resolve
- kempe2018 scale is described as "10-point" (`ConsensualAssessmentTechnique.md`), "1–10" (`@kempe2018.md`) and "0–10" (`RatingScaleCreativityInSports.md`). Verify against the PDF.
- forthmann2023 and barth2020: the citekey year differs from the publication year.

## Gaps & open questions
1. **No psychometric study of CAT ratings in sport** is recorded. The vault has only kempe2018 (trained raters, ICC), zahno2024 and dejoode2023, the last two only briefly summarised and not in the bib. The novelty claim needs author confirmation and a web search.
2. **No JRT or IRT application in sport** in the vault.
3. **Expertise in sport judging**: no vault evidence on coaches vs players vs students as raters of football actions. Expert vs novice evidence comes only from writing and poetry (kaufman2008, kaufman2009). castel2007 and baer2015 notes have no summaries.
4. **Rater training vs the CAT**: the vault holds conflicting guidance (CAT: no criteria; study: definition shown; scale note: calibration training). No peer-reviewed rater-training source is in the bib.
5. **Fatigue and drift within sessions**: only the pilot plan and barth2020 (drift over time). No literature on vigilance or fatigue in video rating.
6. **Discriminant validity of the creativity, technical-quality and aesthetic-appeal ratings**: only amabile1982 is noted. No literature on separating these for sport actions.
7. **Requirements of JRT in sparse designs** (co-ratings per judge needed to estimate a_j stably; recovery simulations): only forthmann2023 and general remarks. No sample-size guidance specific to judge discrimination.
8. **Local dependence and differential judge functioning** (e.g., rater background groups): mentioned conceptually only; no applied source.
9. **Introduction framing sources**: worldeconomicforum2025 and oecd2024 have no vault notes and no bib entries; safardilha2019, memmert2011, batey2012 and barbot2019b bibliographic notes are empty, so the claims attributed to them in the brief are unverified from the vault.
10. **`CreativityResearch.md` and `CreativityInSports.md`** contain almost nothing. Sport-creativity background (e.g., Memmert's tactical creativity work, Roca & Memmert, which are in the bib under Roca) is not summarised in the vault.
