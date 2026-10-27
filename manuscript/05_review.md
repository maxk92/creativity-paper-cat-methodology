# 05_review.md: Peer review, SIXTH ROUND (reviewer-critic, Phase 7)

Manuscript reviewed: `manuscript/manuscript.qmd` (working tree after commit 27c9c63, last minor pass; 345 lines).

Checked against:
- the round-5 review (previous version of this file);
- `03_findings.md`, including the never-quote list;
- the labelled cells of `02_jrt_results.ipynb`, for captions and stored outputs;
- `/home/max/drive/phd_library.bib`;
- `/home/max/drive/utils/csl/apa-7th-edition.csl`.

Line numbers refer to the current `manuscript.qmd`.

I respected these author positions and do not re-raise them:
- the empirical focus, with the projection as a side note;
- no new analyses;
- the sparse design is not foregrounded;
- the Methods FILL INs are the author's;
- the latent variances are not quoted, and `tbl-marginal-reliability-models` stays unembedded.

---

## 1. Recommendation

**Minor revision. From the reviewer's side, the paper is ready for submission once the author items are done.**

The pass applied all seven round-5 points. Six are fully resolved. The seventh is resolved in the Methods, but one Limitations sentence still says "standard normal" (N6-1). The coordinator's notebook fixes removed the old model names from every caption and every table row.

This pass introduced no new substantive problem. One genuine text point remains (N6-1, one sentence). Two housekeeping points concern the hidden comment block and the abstract word count.

**Counts:**
- **Round-5 points (7):** 6 resolved, 1 partially resolved (m5-1, through N6-1), 0 not resolved. The APA manuscript-format part of m5-7 stays with the author (FI-16).
- **Round-5 display list (FI-18):** the model names are resolved. The "Q1 0.596, Q3 0.769" note in the main-text `tbl-reliability-overview` is still open.
- **New issues:** 0 critical, 0 major, 3 minor (one text point and two housekeeping points).
- **Numeric mismatches:** 0. **Never-quote violations:** 0. **Unresolved cited keys:** 0.

---

## 2. Response check of the round-5 points

| # | Status | Evidence | Location |
|---|---|---|---|
| m5-1 θ "standard normal" in all models | **P** | The Methods now say "a normal distribution and a mean of 0. Its variance was fixed at 1 in M3 and the GRM and estimated in M1 and M2, whose discriminations are fixed." This agrees with "a normal product distribution" for M1 (111). Lines 127 ("unit prior variance"), 135 ("standard normal distribution of θ") and 318 (θ ~ N(0, 1)) refer to the GRM only and are correct. **Residual:** the Limitations still say "A standard normal latent distribution was assumed" (255). See N6-1. | 109, 111; residual 255 |
| m5-2 Abstract opening | **R** | "…is the established method for rating creative products, and similar ratings are used for actions in sport." This now matches the Introduction (53, 63) and the "CAT-style" framing (79, 91). | 9 |
| m5-3 Box item 3 size condition | **R** | "…let all raters rate a sufficiently large common calibration set of actions…". This matches the Discussion's "only if these raters rate it and it is large enough" (237). | 242 |
| m5-4 Circular model definitions | **R** | "M1 (rating-scale MFRM) was the rating scale model …, which corresponds to a two-facet MFRM with a shared rating scale…". "M2 (partial-credit MFRM) was the partial credit model …, which corresponds to an MFRM with a rater-specific category structure". Each model is now defined once. | 111 |
| m5-5 Categorical gap statements | **R** | The gaps now read "we found a Rasch analysis only for…" and "we are not aware of evidence on how raters differ…". The third keeps "to our knowledge". ATC-2 still applies. | 63 |
| m5-6 "describes the mean" | **R** | "A panel coefficient refers to the reliability of the mean over all raters of a panel" (55). "The conventional figures refer to the reliability of the mean over a large or complete panel" (213). | 55, 213 |
| m5-7 Format, bib notes, "three" | **R** (text) / **D** (format) | The text reads "at least three jointly rated products" (121). The bib `note` fields ("Found via web search…", "Citekey year …") are still in `phd_library.bib`, but the APA CSL never calls `variable="note"`, so they do not render. The APA manuscript format (title page, running head, double spacing) is still FI-16 (author). | 121; YAML 14–16 |

**FI-18 display items, after the coordinator's notebook fixes:**
- **Model names: resolved.**
  - The row labels of `tbl-reliability-overview`, `tbl-model-fit`, `tbl-score-agreement`, `tbl-theta-correlations` and `tbl-threshold-order` print "M1 (rating-scale MFRM)" and "M2 (partial-credit MFRM)".
  - The captions of `tbl-model-fit`, `tbl-threshold-order` and `tbl-rater-fit-m1` use the new names.
  - A search of `02_jrt_results.ipynb` finds no "M1 (RSM)", "M2 (PCM)" or "rating scale model / MFRM".
- **Still open (main text):** `tbl-reliability-overview`, row "GRM: median rel_post", note column "Q1 0.596, Q3 0.769". This comes from `summary/reliability_overview.csv`. It still clashes with Yen's Q3 in the same paper. Change it to "quartiles 0.596, 0.769" or similar in the CSV or the display function.
- **Now moot:** the "marginal_rxx (mirt)" header. It appears only in `tbl-marginal-reliability-models`, which stays unembedded by author decision.
- The other FI-18 items (code-name Quantity labels, the empty "Overlap" column, integer display, scientific-notation *p*, thousands separators in notes, figure legends) are unchanged and still listed in comment line 42.

**No regressions.** Every point marked resolved in rounds 3–5 is still resolved.

---

## 3. New issues

### Critical
None.

### Major
None.

### Minor

- **N6-1 (text; the remaining internal inconsistency). The Limitations sentence still says "standard normal" (line 255).**
  - **Problem.** "A standard normal latent distribution was assumed, although the ratings concentrated at the low end of the scale." Line 109 now states that the variance was estimated in M1 and M2.
  - **Why it matters.** The two sentences contradict each other within the paper. The limitation is really about normality, not about unit variance.
  - **Fix.** For example: "A normal latent distribution (standard normal in the GRM) was assumed, although the ratings concentrated at the low end of the scale." No number is needed.
- **N6-2 (housekeeping). The abstract word count in the comment is out of date (comment line 39 and FI-16).**
  - **Problem.** The new opening sentence adds one token. By the comment's own counting rule (whitespace-separated tokens, with "=" and "<" counted), the abstract now has **250** tokens, not 249.
  - **Fix.** Update the comment. Re-check the count against the CRJ limit under FI-16. If the limit is 250 words, the abstract is exactly at it.
- **N6-3 (housekeeping). The hidden comment block is stale (lines 42, 44).**
  - **Problem.** FI-18 (line 42) still lists the old model names as open, although they are fixed. Line 44 still offers "embed tbl-marginal-reliability-models in the supplement (recommended…)" as an open option, although the author has decided against it.
  - **Fix.** Remove the model-name item and "marginal_rxx (mirt)" from FI-18. Record the decision not to embed `tbl-marginal-reliability-models` and not to quote the latent variances. The whole block must be removed before submission anyway.

---

## 4. Number and citation check

### Numbers

**No mismatches.**
- **Changed text.** The edited sentences (9, 55, 63, 109, 111, 121, 213, 242) introduce no new values. "137 of 171" (121) matches `03_findings.md`.
- **Latent variances.** 0.962 and 1.087 appear nowhere, as decided by the author.
- **Unchanged text.** All other values are as verified in round 5 (Section 4 of that review). A re-scan of the abstract, Results, Discussion and Conclusion found no change to any number.
- **Never-quote list.** None quoted. The only "(PCM)"/"(RSM)" strings are the abbreviation definitions in the Introduction (61) and the stale FI-18 comment (42).

### Embedded objects

There are still 38 embedded labels. Every embedded object is cross-referenced, and every `@tbl-`/`@fig-` reference resolves. The five unembedded labels are unchanged and need no reference. `tbl-marginal-reliability-models` is unembedded by author decision.

### Citations

- **Resolution.** No citation was added or removed in this pass. A spot check confirmed that keys such as shin2025, runco2012, hove2024, forthmann2025, kaufman2008a, cseh2019, eckes2015, robitzsch2025, chalmers2018 and christensen2017 are present.
- **Narrative citations.** `narrative-and.lua` now runs citeproc after Quarto's filters, with `citeproc: false` in the YAML. Check in the rendered docx and pdf that every narrative citation prints "and" (e.g., "Myszkowski and Storme (2019)") and that the reference list is complete.
- **Bib `note` fields.** They are not printed by the APA CSL (see m5-7).
- **FI-17 PDF verification.** Unchanged and still open (author).

---

## 5. Remaining before submission

### A. Author items (preconditions, not review issues)

1. **Methods FILL INs:**
   - FI-1: project context, ethics and consent, the rater pool, "19 student raters";
   - FI-2: stimulus material;
   - FI-3: software, instruction, anchors, the "not recognised" wording, randomisation and the data-collection period, and the other dimensions;
   - FI-4: allocation of products to raters;
   - FI-6: software versions;
   - FI-9: pairwise alpha raters and the crossed block;
   - FI-15: preregistration and data and code availability;
   - FI-21: rater-pool description;
   - FI-22: non-recognition rate by rater;
   - FI-23: rationale for the cut-off of 15 ratings.
2. **FI-16 (CRJ requirements):** abstract limit (now 250 tokens), APA manuscript format (title page, running head, double spacing) through the format or template, figure and table limits, supplement policy and S-numbering, and whether boxes are accepted.
3. **FI-17:** PDF verification of all marked attributions.
4. **ATC confirmations:** all inline markers, plus the abstract claims tracked in the comment block (ATC-2, 5, 14, 15).
5. **YAML:** the author list and affiliations.
6. **Final clean-up:**
   - remove all inline markers, the YAML affiliation marker and the hidden comment block;
   - remove `mark-highlight.lua` and the `soul`/`xcolor` header if they serve only the markers;
   - keep `narrative-and.lua`.

### B. Genuinely open text and display points

1. **N6-1:** Limitations line 255, change "standard normal" to "normal (standard normal in the GRM)".
2. **FI-18:**
   - the "Q1 0.596, Q3 0.769" note in the main-text `tbl-reliability-overview`;
   - the remaining display items: code-name Quantity labels, the empty "Overlap" column, integer display, scientific-notation *p*, thousands separators in notes, and three figure legends.
3. **Housekeeping:**
   - update the abstract word count in the comment (N6-2) and the stale comment entries (N6-3);
   - re-run the results-embedder so that `02_artifacts.md` shows 38 embedded labels;
   - check the rendered narrative "and" and the reference list.
