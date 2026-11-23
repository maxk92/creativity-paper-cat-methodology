# Candidate journals: JRT analysis of creativity ratings of football actions

Compiled 2026-10-27. Author guidelines were read on the publishers' pages on that date. Impact factors are
**JIF 2025 (JCR release June 2026)** as reported by bioxbio.com, with the 2024 value in brackets.
Quartiles are JCR quartiles as reported by third-party aggregators (journalmetrics.org,
wos-journal.info). They could not be checked in Clarivate JCR directly, so **verify them in JCR
(university login) before citing them anywhere.**

Manuscript as of draft 4 (for the compliance checks below): abstract 252 words; main text about 6,400 words
excluding references; 10 tables and figures in the main text and 27 in the supplement; written in first person
plural ("we"); exploratory secondary analysis, not preregistered; Quarto source rendering to .docx and .pdf.


## Daniel:
1) Journal of Creative Behavior
2) Behaviour Research Methods
3) Psychological Assessment

## Summary

| # | Journal | Publisher | JIF 2025 [2024] | JCR quartile (category) | Fit | Submission files |
|---|---|---|---|---|---|---|
| 1 | **Creativity Research Journal** (current target) | T&F/Routledge | 4.8 [3.1] | Q1 (Psychology, Educational; Psychology, Multidisciplinary) | ★★★★★ | Word, or LaTeX (PDF + zipped source) |
| 2 | **Journal of Creative Behavior** | Wiley | 4.1 [3.0] | Q1 (Psychology, Educational) | ★★★★★ | **Free format** (any editable file, any reference style) |
| 3 | **Psychology of Aesthetics, Creativity, and the Arts** | APA | 3.0 [2.7] | Q2 | ★★★★☆ | **Word (.doc) only** |
| 4 | **Psychology of Sport and Exercise** | Elsevier | 3.9 [3.3] | Q1 (Psychology, Applied; Sport Sciences) | ★★★☆☆ | Word (.docx) or LaTeX (.tex); PDF not accepted as source |
| 5 | *Journal of Intelligence* (own pick) | MDPI, gold OA | 3.8 [3.4] | Q1 (Psychology, Multidisciplinary) | ★★★☆☆ | **Free format**; Word or LaTeX (zip) |
| 6 | *Behavior Research Methods* (own pick) | Springer / Psychonomic Society | 5.0 [3.9] | Q1 (Psychology, Experimental / Mathematical; verify) | ★★★☆☆ (needs reframing) | Word or LaTeX (Springer standard; not restricted on the journal page) |
| 7 | *Journal of Sports Sciences* (own pick) | T&F | 3.1 [2.5] | Q2 (Sport Sciences; verify) | ★★★☆☆ | **Format-free**: Word, RTF, ODT **or PDF** |
| 8 | *Measurement in Physical Education and Exercise Science* (own pick) | T&F | 1.6 [1.9] | Q2 (Education & Educational Research), Q3 (Sport Sciences) | ★★★★☆ (scope) / lower prestige | Word only |
| 9 | *Thinking Skills and Creativity* (own pick) | Elsevier | 5.3 [4.5] | Q1 (Education & Educational Research) | ★★☆☆☆ | Word (.docx) or LaTeX (.tex) |
| 10 | Journal of Creativity ("Creativity Journal")¹ | Elsevier, gold OA | none (not in JCR) | n/a (Scopus-indexed only) | ★★★☆☆ | Converted to PDF for review; Word or LaTeX for production |
| 11 | Intelligence | Elsevier | 3.1 [2.8] | Q1 (Psychology, Multidisciplinary; verify) | ★☆☆☆☆ | Word (.docx) or LaTeX (.tex) |
| 12 | Psychological Bulletin | APA | 19.9 [19.8] | Q1 (Psychology, Multidisciplinary; 2nd in category) | ✗ (not eligible) | Word (.docx) preferred; LaTeX zip + PDF |

¹ No journal titled exactly "Creativity Journal" exists. I assumed you meant Elsevier's *Journal of Creativity*
(ISSN 2713-3745). The other candidate is *Creativity. Theories – Research – Applications* (Sciendo), which
ranks lower. Tell me if you meant a different journal.

Quarto: none of these journals takes .qmd source. All of them work from Quarto output. Render to .docx for
Word-only journals (PACA, MPEES), and to PDF plus the generated .tex for T&F or Elsevier LaTeX routes.
JCB, J. Intell. and J. Sports Sci. accept a rendered file in any layout and any consistent reference style.

## Recommendation

1. **Creativity Research Journal** remains the best first choice. It has the strongest fit, is Q1, has no word
   limit and charges no fees. It requires these changes: a **200-word** abstract (draft has 252), **no keywords**,
   and **no first person** (the draft uses "we" throughout, which is a substantial rewrite).
2. **Journal of Creative Behavior** is the best fallback, or an equal first choice if you can share data and code.
   Its free-format submission suits Quarto output. Since 1 January 2026 it **requires open data and analysis
   scripts** (or stated reasons why they cannot be shared) before review.
3. **PACA** is the venue where the JRT framework was introduced (Myszkowski & Storme, 2019; the `jrt` package
   paper, Myszkowski, 2021), so the method fits it closely. It is Q2, requires Word, caps length at 40 pages
   including references, tables and figures, and requires a sample-size justification.
4. **Psychology of Sport and Exercise** gives a sport-psychology audience in a Q1 journal. It sets a limit of about
   8,000 words including references, tables and figures, expects an a-priori power justification, and requires
   a "substantive methodological contribution".

I would not submit to Psychological Bulletin, Intelligence or Thinking Skills and Creativity, because they fall
outside their scopes (see below).

---

## Per-journal details

### 1. Creativity Research Journal (CRJ)
- **Metrics:** JIF 2025 4.8 (2024: 3.1); JCR Q1 in Psychology, Educational and in Psychology, Multidisciplinary.
- **Fit:** Very high. It is the home of CAT methodology papers and the target in `paper.config.yml`. It
  welcomes empirical papers on creativity assessment, and an applied domain (sport) is not a problem.
- **Specific demands:**
  - Unstructured abstract of **200 words** (draft: 252).
  - **Do not include keywords** (the draft YAML has 7).
  - APA 7; American spelling; report exact *p* values and effect sizes; discuss results and previous research in the **past tense**; "data" is plural.
  - **No first person, and no "the authors"** (draft uses "we"/"our"). This is the main rewrite.
  - Double-spaced, 1-inch margins, 12-pt font, page numbers, **submission date on the title page**; tables on separate pages after the references, figures separate, figure captions as a list.
  - Masked review is the default (authors may request single-anonymous review in the cover letter); a **cover letter is required**.
  - Required statements: funding, disclosure of interest, **declaration of generative-AI use**, data availability statement; CRediT roles.
  - No word limit, but a word count must be stated.
- **Submission files:** Word or LaTeX. For LaTeX, upload a PDF as the manuscript file and the LaTeX sources as one zip file. Word and LaTeX templates are available.
- **Costs:** no submission or page charges; hybrid OA optional.

### 2. The Journal of Creative Behavior (JCB)
- **Metrics:** JIF 2025 4.1 (2024: 3.0); JCR Q1 in Psychology, Educational.
- **Fit:** Very high. It invites "methodological and empirical articles" on creativity across contexts.
- **Specific demands:**
  - Original article: **6,000–12,000 words including references**, with a soft cap of 10,000. Brief report: 2,000–5,000 words. The draft fits as an article.
  - **Open-science requirement (from 1 January 2026):** empirical papers must give open access to the **data and analysis scripts** under a reuse licence on a reliable platform, or state legal or ethical reasons why they cannot be shared. Papers without this go back to the authors before review. The rating data and the R pipeline would need a repository (for example OSF), or the manuscript would need an explanation of why the data cannot be shared.
  - Cover letter stating the article type; the paper must be "adequately situated in the creativity studies literature".
  - Statements: data availability, funding, ethics approval, conflict of interest; **detailed AI-use disclosure** (tool, version, dates, purpose, sections, how outputs were checked).
- **Submission files:** **Free Format**. Any editable file (text, figures and tables in one file or separately) and references in any consistent style.

### 3. Psychology of Aesthetics, Creativity, and the Arts (PACA)
- **Metrics:** JIF 2025 3.0 (2024: 2.7); JCR **Q2**.
- **Fit:** High. JRT was introduced and published here, so reviewers know the method. Lower IF than CRJ and JCB.
- **Specific demands:**
  - **Under 40 double-spaced pages including references, tables and figures** (online-only supplements excluded). With 10 main-text displays this will be tight.
  - Abstract of at most **250 words** (draft: 252); up to **5 keywords** (draft: 7).
  - **Justification of sample size** required for quantitative analyses (number of raters, ratings and actions).
  - APA 7; author note must state prior dissemination (conference talks, preprints); APA data-sharing expectation (data available on request for 5 years); AI use disclosed in the Method section and cited.
  - Code goes in supplemental files, not in the text; tables built with Word's table function; equations in MathType or Equation Editor 3.0 preferred.
- **Submission files:** **Word (.doc) only**, via Editorial Manager. Render Quarto to .docx.

### 4. Psychology of Sport and Exercise (PSE)
- **Metrics:** JIF 2025 3.9 (2024: 3.3); JCR Q1 (Psychology; Sport Sciences).
- **Fit:** Medium. Football actions and sport-creativity readers fit, but the journal requires a
  "substantive theoretical or methodological contribution" to sport and exercise psychology. The framing would need to
  emphasise what the findings mean for measuring creativity in sport.
- **Specific demands:**
  - About **30 pages / 8,000 words including references, tables and figures**. Move material to the supplement.
  - Quantitative studies must be "theoretically informed" and give **a-priori power estimates**. For an exploratory secondary analysis, explain why this does not apply and give a precision or sensitivity argument instead.
  - Abstract of at most 250 words; 1–7 keywords; **Highlights** (3–5 bullets of at most 85 characters each); double-anonymised review (separate title page); declaration of competing interests; generative-AI statement; ethics statement with committee name and approval number.
  - Research-data Option B (data sharing encouraged); preregistration welcome but not required; adhere to reporting guidelines.
- **Submission files:** Word (.docx) or LaTeX (.tex); PDF is not accepted as the source file.

### 5. Journal of Intelligence (MDPI): own pick
- **Metrics:** JIF 2025 3.8 (2024: 3.4); JCR Q1 in Psychology, Multidisciplinary.
- **Fit:** Medium to high. It regularly publishes creativity-assessment and psychometric (IRT/JRT) papers and
  special issues on creativity measurement. It is gold OA.
- **Specific demands:** abstract of about **200 words**, single paragraph, structured without headings
  (background, methods, results, conclusions); **3–10 keywords**; back matter with Author Contributions, Funding,
  **Data Availability Statement**, Conflicts of Interest; preregistration links if any; full datasets "where possible".
  **APC CHF 2,600.**
- **Submission files:** **Free format accepted** (any layout, any consistent reference style). Otherwise Word
  template, or LaTeX as a zip of all sources.

### 6. Behavior Research Methods (BRM): own pick
- **Metrics:** JIF 2025 5.0 (2024: 3.9); JCR Q1 (verify the category).
- **Fit:** Only with reframing. BRM publishes *methods* papers and tutorials. The paper would need to become a
  methods contribution, for example a reusable JRT workflow for incomplete multi-rater designs with
  documented code, and the football data would serve as the worked example.
- **Specific demands:** **TOP Level 2**: data, materials and code in a trusted repository; an **Open Practices
  Statement** just before the references; **data availability statement** under a type-4 data policy; Psychonomic
  Society statistical guidelines (report all exclusions and analyses, CIs, flag exploratory analyses);
  APA 7; abstract of at most 250 words; figures and tables may be embedded in the text.
- **Submission files:** Word or LaTeX (Springer standard; the journal page does not restrict the format).

### 7. Journal of Sports Sciences (JSS): own pick
- **Metrics:** JIF 2025 3.1 (2024: 2.5); JCR Q2 in Sport Sciences (verify).
- **Fit:** Medium. It reaches a broad sport-science audience and accepts measurement and methods work.
- **Specific demands:**
  - A typical paper is about **4,000 words** excluding tables, references and figure captions. This is guidance, not a hard limit, but the draft would need to shrink by about 35%.
  - Unstructured abstract of **200 words**; 1–6 keywords.
  - A Method section titled **"Sample size estimation and justification"** is required. For exploratory studies, report a sensitivity analysis or minimum detectable effect, following Ditroilo et al. (2025).
  - Double-anonymous review; continuous line numbers in the anonymised version; generative-AI declaration; data availability statement; Open Science Badges available.
- **Submission files:** **Format-free**: Word, RTF, ODT or **PDF**, any layout and any consistent reference style. An editable file is required at revision.

### 8. Measurement in Physical Education and Exercise Science (MPEES): own pick
- **Metrics:** JIF 2025 1.6 (2024: 1.9); JCR Q2 (Education & Educational Research), Q3 (Sport Sciences).
- **Fit:** Scope fit is very high: original measurement research, with sections for Psychology and for Research
  Methodology & Statistics. Prestige is clearly lower than the creativity journals.
- **Specific demands:** at most **30 pages including abstract, references, tables and figures**; abstract of **150 words**;
  **4–5 keywords**; double-spaced, 23–25 lines per page, line numbers, each element starting on a new page;
  APA style; single-anonymous review; generative-AI declaration; data availability statement; no APC.
- **Submission files:** **Word only**.

### 9. Thinking Skills and Creativity (TSC): own pick, not recommended
- **Metrics:** JIF 2025 5.3 (2024: 4.5); JCR Q1 in Education & Educational Research.
- **Fit:** Low. The scope is the *learning and teaching* of creativity and thinking skills, and papers "must connect
  to the learning and teaching, facilitation and/or practice" of creativity. It is listed here because of its high IF.
  A submission would need an educational framing, such as talent development or coaching, which the paper does not have.
- **Specific demands:** full-length articles of **at most 8,000 words including references**; abstract of at most 250 words;
  1–7 keywords; Highlights; double-anonymised review; research-data **Option C** (data **must be deposited** and cited, or reasons
  given).
- **Submission files:** Word (.docx) or LaTeX (.tex).

### 10. Journal of Creativity (Elsevier)
- **Metrics:** no JIF (not found in JCR or ESCI); Scopus-indexed. Aggregators report Scopus Q2, but this is unverified.
  Small journal (23 articles in 2025). Gold OA with an APC; check the amount on the journal's OA page.
- **Fit:** Medium to high on topic (interdisciplinary creativity research), but its prestige and indexing are well
  below CRJ, JCB and PACA.
- **Specific demands:** **at most 9,000 words including references** (excluding tables and figures); **at most 8 figures,
  tables or boxes**; **no standalone Conclusion section** (the draft has one); results and literature described in the
  past tense; at most 6 keywords; Highlights; double-anonymised review; CRediT.
- **Submission files:** Word or LaTeX. The system converts them to a single PDF for review.

### 11. Intelligence (Elsevier): not recommended
- **Metrics:** JIF 2025 3.1 (2024: 2.8); JCR Q1 in Psychology, Multidisciplinary per aggregator (verify).
- **Fit:** Low. The journal publishes research on *intelligence* (ISIR journal). Creativity ratings of
  football actions are outside its scope unless the paper is linked to cognitive ability, which it is not.
- **Specific demands (for completeness):** abstract of at most 250 words; 1–7 keywords; **Highlights required**; double-anonymised
  review (separate title page); research-data **Option C** (deposit, cite and link data, or explain why not);
  CRediT; generative-AI statement before the references; any consistent reference style at submission.
- **Submission files:** Word (.docx) or LaTeX (.tex); PDF is not accepted as the source file.

### 12. Psychological Bulletin: not eligible
- **Metrics:** JIF 2025 19.9 (2024: 19.8); JCR Q1, 2nd in Psychology, Multidisciplinary.
- **Fit:** None for this manuscript. The journal publishes **research syntheses** (meta-analyses, systematic and
  integrative reviews), not single primary studies. A future meta-analysis of CAT inter-rater reliability across
  domains could fit.
- **Specific demands (for reference):** masked review; **TOP Level 2** with a required "Transparency and openness" subsection
  in the Method; JARS/MARS or PRISMA 2020; preregistration status; data, code and coding scheme must be supplied.
- **Submission files:** Word (.docx) preferred; LaTeX as a zip with a PDF.

---

## Changes needed for the top candidates

| Requirement | CRJ | JCB | PACA | PSE |
|---|---|---|---|---|
| Abstract length | ≤200 (cut 52) | none stated | ≤250 (cut 2) | ≤250 (cut 2) |
| Keywords | **remove** | as usual | ≤5 (cut 2) | 1–7 |
| Length | no limit | 6–12k incl. refs | <40 pp. incl. refs/tables/figs | ~8,000 words incl. refs/tables/figs |
| Voice | **no first person** | free | APA (we is fine) | free |
| Open data/code | encouraged | **required or justified** | on request (APA) | encouraged |
| Sample-size justification | — | — | **required** | **a-priori power expected** |
| Highlights | — | — | — | **required** |
| AI-use statement | required | required (detailed) | required (in Method) | required |
| File | Word / LaTeX+PDF | free format | **Word only** | Word / LaTeX |

## Sources
- Impact factors: bioxbio.com journal pages (2025 values labelled "2026 update"); MDPI J. Intell. and MPEES from journalmetrics.org.
- Quartiles: journalmetrics.org JCR listings; wos-journal.info (TSC); APA impact-factor page (Psych. Bull. rank).
- Author guidelines (read 2026-10-27): tandfonline.com instructions for hcrj20, rjsp20, hmpe20; apa.org/pubs/journals/aca/submit and /bul/submit;
  onlinelibrary.wiley.com JCB "For authors"; sciencedirect.com guides for Intelligence, Psychology of Sport and Exercise,
  Thinking Skills and Creativity, Journal of Creativity; mdpi.com/journal/jintelligence/instructions and /apc;
  link.springer.com/journal/13428/submission-guidelines.
