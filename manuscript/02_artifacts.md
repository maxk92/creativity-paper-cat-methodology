# Object/Artifact Inventory — PLACEHOLDER (no data collected yet)

> STATUS: No analysis notebook exists for this manuscript (`paper.config.yml`
> field `notebook: None`). This paper is at concept/proposal stage. The table
> below is a STRUCTURAL PLACEHOLDER only, derived from the planned study design
> described in `manuscript/01_dossier.md` (section B: `CreativityRatingStudy.md`,
> `RatingScaleCreativityInSports.md`) and updated per the author-approved
> outline (`manuscript/04_outline.md`). It contains NO invented numbers, effect
> sizes, sample sizes, or example values. Every row must be revisited by
> results-embedder once `analysis/results.ipynb` (or equivalent) exists and is
> populated with real figures/tables carrying the labels below.

| label | type (fig/tbl) | source cell id | caption draft | embed snippet |
|---|---|---|---|---|
| tbl-sample-description | tbl | N/A — no notebook | [TO BE POPULATED once data collection is complete] Description of the collected sample: number of distinct football actions rated, number of matches and competitions sampled, number of judges/raters recruited (against the 10-rater benchmark-panel target plus the additional pairwise-only rater pool, size still to be finalized), ratings per action (benchmark vs. pairwise subset), reported against the planned purposive target of ~1,000–2,000 actions (see Methods). | `{{< embed analysis/results.ipynb#tbl-sample-description >}}` <!-- TODO: notebook does not exist yet --> |
| fig-icc-by-judge-count | fig | N/A — no notebook | [TO BE POPULATED once data collection is complete] Inter-rater reliability (ICC) as a function of the number of judges included in the aggregate rating (k = 1…10), computed on the 10-rater benchmark subset. The plot will include reference lines at the pre-specified ICC(2,k) >= .80 target and the .70 minimum acceptable floor (per `04_outline.md` Methods, Analysis Plan (a)), so the number of judges needed for stable/convergent ratings can be read directly off the curve against these pre-specified thresholds. | `{{< embed analysis/results.ipynb#fig-icc-by-judge-count >}}` <!-- TODO: notebook does not exist yet --> |
| tbl-agreement-by-judge-count | tbl | N/A — no notebook | [TO BE POPULATED once data collection is complete] Summary agreement/reliability statistics (e.g., ICC with 95% CIs and category-usage checks) tabulated across candidate numbers of judges (2, 3, 5, and 10 — all achievable from the 10-rater benchmark panel), with the pre-specified ICC(2,k) >= .80 target / .70 floor noted alongside the achieved values. | `{{< embed analysis/results.ipynb#tbl-agreement-by-judge-count >}}` <!-- TODO: notebook does not exist yet --> |
| fig-expertise-agreement | fig | N/A — no notebook | [TO BE POPULATED once data collection is complete] Rater agreement/validity metrics compared across rater-expertise groups (e.g., expert vs. novice/high-viewership judges), framed against the competing H2a/H2b hypotheses stated in `04_outline.md` RQ2. | `{{< embed analysis/results.ipynb#fig-expertise-agreement >}}` <!-- TODO: notebook does not exist yet --> |
| tbl-expertise-effects | tbl | N/A — no notebook | [TO BE POPULATED once data collection is complete] Mixed-model estimates of rater expertise as a predictor of rating level/variance, with rater/player/match random effects, as planned in `RatingScaleCreativityInSports.md` (auxiliary analysis supporting RQ2, per `04_outline.md` Methods, Analysis Plan (b)). | `{{< embed analysis/results.ipynb#tbl-expertise-effects >}}` <!-- TODO: notebook does not exist yet --> |
| fig-factor-structure | fig | N/A — no notebook | [TO BE POPULATED once data collection is complete] Factor structure / correlation structure among creativity (novelty x appropriateness), aesthetic, and technical-correctness ratings (e.g., loadings plot or path diagram). | `{{< embed analysis/results.ipynb#fig-factor-structure >}}` <!-- TODO: notebook does not exist yet --> |
| tbl-factor-loadings | tbl | N/A — no notebook | [TO BE POPULATED once data collection is complete] Factor loadings and fit indices for the proposed factor model relating creativity, aesthetic appeal, and technical correctness dimensions. | `{{< embed analysis/results.ipynb#tbl-factor-loadings >}}` <!-- TODO: notebook does not exist yet --> |
| fig-rater-severity-jrt | fig | N/A — no notebook | [TO BE POPULATED once data collection is complete] Judge Response Theory (JRT, via the R `jrt` package) / Many-Facet Rasch Model (MFRM, via TAM or brms)-based rater severity estimates, ordered by rater, with uncertainty intervals. | `{{< embed analysis/results.ipynb#fig-rater-severity-jrt >}}` <!-- TODO: notebook does not exist yet --> |
| tbl-rater-fit-diagnostics | tbl | N/A — no notebook | [TO BE POPULATED once data collection is complete] Rater fit diagnostics (e.g., infit/outfit statistics or JRT-equivalent) flagging raters with atypical response patterns. | `{{< embed analysis/results.ipynb#tbl-rater-fit-diagnostics >}}` <!-- TODO: notebook does not exist yet --> |

## Problems / notes for the user

1. **No notebook exists.** `paper.config.yml` sets `notebook: None`. All source
   cell ids above are marked "N/A — no notebook" because there is nothing to
   inventory yet. This entire file must be re-run through the normal
   results-embedder process (reading real `#| label:`/`#| fig-cap:`/`#| tbl-cap:`
   tags from cell metadata) once `analysis/results.ipynb` (or whatever path is
   set) is created and populated with actual analysis outputs.
2. **Embed paths are placeholders.** The embed snippets above reference a
   notional `analysis/results.ipynb` path since no real notebook path is
   configured. Update `paper.config.yml`'s `notebook` field and regenerate this
   file before the embed snippets are used in the manuscript.
3. **Coverage is provisional and may not match final analysis.** The eight
   anticipated objects above map to the five result areas named in the task
   (sample description; reliability by judge count; expertise effects; factor
   structure; JRT/MFRM rater diagnostics) plus natural table/figure splits
   within each. The actual analysis may produce more, fewer, or differently
   structured objects (e.g., JRT and MFRM might end up as competing analyses
   each needing their own figure — the outline resolves the estimation
   software for both to an all-R pipeline, but whether they are reported as
   one combined figure or two remains an open editorial choice).
4. **No numeric values, axis ranges, or example figures are included anywhere
   in this file**, per instructions — only structural/label placeholders. The
   ICC(2,k) >= .80 target / .70 floor referenced in `fig-icc-by-judge-count`
   and `tbl-agreement-by-judge-count` above is a pre-specified design decision
   (stated in `04_outline.md` Methods, Analysis Plan (a)), not an invented or
   achieved result.
5. **Bibliography path**: resolved. `paper.config.yml` points to
   `~/drive/phd_library.bib`, confirmed to exist on disk. No longer a blocker.
6. **Sample-size target (resolved post outline-checkpoint)**: the planned
   purposive sample is ~1,000–2,000 football actions (see `04_outline.md`
   Methods §2), superseding the earlier ~9,500-action vault planning figure.
   `tbl-sample-description`'s caption above has been updated to reference this
   target; achieved N remains unknown and unstated until data collection
   completes.
7. **No dedicated artifact exists for the fatigue/session-duration finding**
   (Finding 6 in `03_findings.md`) — this gap was explicitly NOT selected for
   resolution by the author and remains open; see `04_outline.md` Evidence
   gaps item 1. Do not add a placeholder object for it without author
   direction, to avoid pre-judging whether it warrants its own figure/table or
   should be folded into `tbl-sample-description` prose.
8. **Rater-panel size (resolved post reviewer-critic pass, checkpoint 2)**:
   the benchmark panel is now specified as **10 raters** (not 5), enabling the
   ICC-by-judge-count trajectory to run k = 1…10 and making the "2, 3, 5, and
   10 judges" candidate counts in `tbl-agreement-by-judge-count`'s caption
   fully achievable and internally consistent — see `04_outline.md` Methods,
   "Design overview" and "Judges/raters," and Evidence gaps item 9. No row in
   this file now states or implies a 5-rater benchmark panel.
9. **Reliability target/floor reference lines (resolved post reviewer-critic
   pass, checkpoint 2)**: `fig-icc-by-judge-count`'s caption above now notes
   the pre-specified ICC(2,k) >= .80 target and .70 minimum floor as reference
   lines to be plotted alongside the achieved ICC trajectory, per
   `04_outline.md` Methods, Analysis Plan (a). This is a stated design
   decision only — no achieved ICC value is included here or anywhere in this
   file.
10. **Rating platform left unnamed (newly flagged open at checkpoint 2)**:
    per `04_outline.md` Methods, "Procedure," and Evidence gaps item 16, the
    specific rating platform/app has not been decided and is not named in any
    caption above; this is an open item for the author to finalize, not an
    artifact gap.
