# To do: fix entries in `~/drive/phd_library.bib`

These entries render wrongly in the manuscript's reference list (APA 7 CSL, Quarto/pandoc). The checks
are against the pdf render of draft 4 (2026-10-27). Fix them at the source (Zotero/JabRef, whatever
writes the file) so a re-export keeps the fixes. Then re-render the manuscript and check the
reference list again.

The citekeys used by the paper stay unchanged.

## Wrong content

- [ ] **memmert2011: cited as "Memmert, 2010".**
  - Cause: the entry has `date = {2010-09-27}` (online-first date). It overrides `year = {2011}`.
  - Fix: delete the `date` and `day` fields, or set `date = {2011-01}`. The issue is *Journal of
    Sports Sciences* 29(1), 2011.
- [ ] **cai2014: renders as "National Center for Research on Evaluation, Standards,; Student Testing
  (CRESST)".**
  - Cause: the institution sits in `school` (thesis field), and its "and" is read as a list separator.
  - Fix: rename `school` to `institution`, and wrap the name in double braces so "and" is not split:
    `institution = {{National Center for Research on Evaluation, Standards, and Student Testing (CRESST), University of California, Los Angeles}}`
- [ ] **engelhard1994: renders as "Engelhard, Jr., George."**
  - Cause: `author = {Engelhard, George, Jr.}` is in the wrong order for BibTeX.
  - Fix: `author = {Engelhard, Jr., George}` (BibTeX order: Last, Jr, First). The result should be
    "Engelhard, G., Jr. (1994)".

## Name particles (sorting and display)

- [ ] **Particles are moved behind the given name and sorted under the main surname.** The list shows
  "Ayala, R. J. de", "Hove, D. ten", "Joode, T. de", "Sa Fardilha, F. de" and "Kamp, J. van der".
  - Proposed fix: protect the whole surname with braces, so it displays and sorts as written.
    - ayala2022: `author = {{de Ayala}, R. J.}`, which gives "de Ayala, R. J. (2022)", sorted under D.
    - hove2024: `author = {{ten Hove}, Debby and Jorgensen, Terrence D. and {van der Ark}, L. Andries}`
    - joode2023: `author = {{de Joode}, Tom and {van der Kamp}, John and Savelsbergh, Geert J. P.}`
    - safardilha2019: `author = {{de Sa Fardilha}, Francisco and Allen, Justine B.}`
      (check the author's own spelling first: "de Sá Fardilha"?)
  - **Your decision:** APA follows the author's own usage for particles, and Dutch names are often
    listed under the main name ("Hove, D. ten"). Choose per author and keep it consistent.

## Titles lowercased by the APA sentence case

APA sentence case lowercases every unprotected word except the first. Protect proper nouns and
numerals with braces.

- [ ] **primi2019:** "many-facet rasch". Use `{Rasch}` and remove the trailing full stop:
  `title = {Applying many-facet {Rasch} modeling in the assessment of creativity}`
- [ ] **myford2003:** "Part i". Use `... measurement: {Part I}`; check myford2004 the same way
  (`{Part II}`).
- [ ] **myszkowski2021:** "the r library 'jrt'". Use `{R}` and `{jrt}` and remove the trailing
  full stop:
  `title = {Development of the {R} library "{jrt}": Automated item response theory procedures for judgment data and their application with the consensual assessment technique}`
- [ ] **Quick scan:** check other cited titles for unprotected proper nouns (Rasch, Bayesian, R,
  person and place names). A quick check: search the rendered reference list for lowercase "rasch",
  "bayes", " r " and "mfrm".

## Type-specific details

- [ ] **linacre1989: shows "[PhD thesis]"; APA uses "[Doctoral dissertation]".**
  - Option A (dissertation): add `type = {Doctoral dissertation}`, giving "[Doctoral dissertation,
    The University of Chicago]".
  - Option B (the more commonly cited book form):
    `@book{linacre1989, author = {Linacre, John Michael}, title = {Many-facet {Rasch} measurement}, publisher = {MESA Press}, address = {Chicago}, year = {1989}}`
  - The note in the entry already says you need to choose. Note the title spelling: "faceted"
    (dissertation) vs "facet" (book).
- [ ] **robitzsch2025: the version and software type are missing**
  ("Robitzsch, A. (2025). sirt: Supplementary item response theory models. https://doi…").
  - Fix: change the type to `@software`, add `version = {4.2-133}`, and shorten the note:
    `@software{robitzsch2025, author = {Robitzsch, Alexander}, title = {{sirt}: Supplementary item response theory models}, version = {4.2-133}, year = {2025}, doi = {10.32614/CRAN.package.sirt}, url = {https://CRAN.R-project.org/package=sirt}}`
  - APA target: "Robitzsch, A. (2025). *sirt: Supplementary item response theory models* (Version
    4.2-133) [Computer software]."
  - Check the other R packages the paper cites (mirt, psych, irr) the same way, if they are cited.
- [ ] **eckes2015: shows "Vol. 22" without the series name.**
  - Fix: delete `volume = {22}`. APA does not require the series. Alternatively keep both and
    accept the CSL output.

## Library hygiene (not used by the paper, but break exports)

- [ ] **Duplicate keys:** each of these is defined twice. pandoc uses the first entry, and other tools
  may warn or fail. Merge each pair and keep one entry:
  - **bransen2019**, lines ≈5921 (`@InProceedings`, with booktitle) and ≈21526 (`@misc`). Keep
    `@InProceedings`.
  - **brinkschulte2023**, lines ≈15368 and ≈21534. Keep the one with the full journal data, and
    protect `{The}` after the dash.
  - **vanhaaren2021**, lines ≈249 (`@Article`) and ≈22291 (`@Misc`). Keep the one with the correct
    venue (check whether it was a workshop paper or arXiv).
- [ ] **Optional:** many entries imported from the web search carry `note = {Found via web search for
  paper...}`. APA does not print `note`, but remove these notes before sharing the library.

## After fixing

- [ ] Re-render: `quarto render manuscript/manuscript.qmd`
- [ ] Check the reference list in the pdf for:
  - Memmert (2011);
  - the CRESST institution;
  - Engelhard, G., Jr.;
  - the particles;
  - Rasch / Part I / R;
  - Linacre;
  - the sirt version;
  - Eckes.
