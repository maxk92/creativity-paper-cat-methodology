# 05_review.md: Peer review, EIGHTH ROUND (reviewer-critic, Phase 7, revision run 2026-11-09)

Manuscript reviewed: `manuscript/manuscript.qmd` (draft 8, working tree, 370 lines, single file; one paragraph per line, so draft-7 line numbers still hold; frozen data 9,046 ratings / 3,669 products / 24 raters).

Checked against:
- `03_findings.md` including BOTH delta sections: "Delta 2026-11-09 (commit 164c146)" and "Delta 2026-11-09b (coordinator; notebook 02 note corrected after reading R/08_reliability_min_ratings.R)", the latter being the authoritative description of the top-up simulation (the only authority for numbers and simulation procedure);
- `02_artifacts.md` (53 labels incl. the Delta row; embed syntax);
- `04_outline.md` (conventions, APA number format, never-quote list at lines 28–38, simulation-assumption rule, object plan, decisions D1–D16 and the author's choices for D5, D7, D8);
- `07_rater_number_evidence.md` (binding instructions, key map, Studies table, Study details, Resolutions);
- `06_web_literature.md` §F4–F9 and `01_dossier.md` final section (literature support);
- `author_todo.md` (regenerated after round 7);
- `/home/max/drive/phd_library.bib` (citekeys);
- the round-7 review (previous version of this file) for the tracked points and author positions.

Author positions respected and not re-raised: empirical focus; the two simulations are part of RQ1 by author decision; the GRM is retained with the BIC disagreement stated; the Methods FILL INs are the author's; `tbl-marginal-reliability-models` stays unembedded; the latent variances are not quoted; the D7 title is the author's choice; the supplement note (335) is kept standalone pending FI-16.

---

## 1. Recommendation

**Minor revision. Ready for the author's FILL IN pass; one wording fix in the Discussion (M8-1) should be made before submission.** Every round-7 point is resolved or carried as an explicit author item; the top-up simulation is now described exactly as the corrected notebook note describes it, in all six places; every numeric claim matches the findings file; the closing argument no longer asserts domain specificity or non-transfer as facts; the sport literature is described study by study. What remains on the reviewer's side is one selective-metric sentence in the RQ3 Discussion (M8-1), a handful of attribution and wording items (m8-1 to m8-9), and the author's own FILL IN, ATC, render and CRJ-format work (Section 8).

**Counts:**
- **Critical:** 0.
- **Major:** 1 (M8-1).
- **Minor:** 9 (m8-1 to m8-9).
- **Numeric mismatches against `03_findings.md` (incl. both deltas):** 0 (Section 3; every numeric claim audited).
- **Never-quote violations:** 0. The estimation tolerance "0.0001" at line 111 is ruled acceptable (Section 3, ruling); no md5, no "2.25", no "7-fold", no "RS-MFRM"/"PC-MFRM", no report-qmd roundings, no claim that the notebook compares observed and simulated values, no min-4 seed, no statement about θ in the top-up beyond the corrected notebook note.
- **Unresolved citekeys:** 0 of 96 distinct keys (all resolve to `@…{key,` entries in `phd_library.bib`).
- **Banned keys present:** 0 (fardilha2020, johnson2003, brown1967, harrison2016, memmert2015, memmert2017, myszkowski2026, beaty2026 all absent).
- **Stale-string hits:** 1, legitimate (".928" at 163 is the projection value at 10 ratings). All other §8 strings and the additional strings ("has to be established", "no evidence", "side note", "by convention", "we show", "real ratings were kept", "2.25", "7-fold", "RS-MFRM", "md5", "regardless of how many", "earlier data set", "data update", "updated", "previous", "new data") return 0 hits.
- **Glyphs:** 0 hits for "⚑", "✕" and "†" in the manuscript; flags are referred to in plain words ("flagged", "with flags").
- **Embeds:** 48, each exactly once (14 main text at 101–209, 34 supplement at 291–369); the 5 unembedded labels (`tbl-cleaning-log`, `tbl-marginal-reliability-models`, `tbl-grm-global-fit`, `tbl-overview-ratings-per-action`, `fig-overview-rater-overlap`) appear nowhere, neither as embeds nor as `@`-references.
- **Abstract:** 246 words by my count (whitespace tokens; "*p*", "<" and ".001" counted; the writer counts 247; the difference is one hyphenated token), under 250; no citations, no markers, no "student raters"; all numbers match; BIC wording "constrained models in both cases" verbatim; headline formulation identical to 163, 219, 227, 251 and 278.
- **Title:** verbatim the D7 alternative (`04_outline.md` line 66); `shorttitle` unchanged.

---

## 2. Round-7 response table

| Point | Status | Evidence (line, quote) |
|---|---|---|
| M7-1 domain specificity / non-transfer stated as fact | **resolved** | 247 "First, the number of ratings needed could not have been read off the existing evidence: the published figures come from other material, targets and objects, and the figure found here … differs from them for reasons that these data cannot separate (domain, rater pool, scale, target and object). To our knowledge, this study supplies the first rating-design figures …"; 247 "Second, in these ratings of actions observed in competition, single ratings agreed weakly"; 255 "cannot be assumed to hold for other nonverbal, time-pressured products, rater pools or scales"; 278 "rating-design figures from verbal or static material cannot be assumed to hold; they have to be collected for the product class and rater pool at hand" |
| M7-2 top-up simulation under-specified | **resolved (and corrected to the Delta-b procedure)** | 129 "it kept the actual assignment of raters to products … but not the ratings themselves … additional raters, drawn at random with equal probability and without replacement from the panel raters who had not rated it, until it had four … every real product received a creativity value θ drawn from N(0, 1), all ratings in the design … were generated from the fitted GRM … scored by EAP with the parameters treated as known. The real ratings were not reused; the actual-design row is a validation"; same at 262 and 335; author_todo line 51 explains why no FI-33 exists |
| M7-3 roca2018 / memmert2010 misdescribed | **resolved**; one residual hedge needed (m8-2) | 51 "in competition footage [@kempe2018], in games of academy players [@joode2023], in game-test situations [@memmert2010] or in verbal responses to video scenes [@roca2018], relied on three or four coaches or trained experts"; 229 same four-way split; "licensed" dropped |
| M7-4 "ten or more lay raters" misread | **resolved** | 229 "the finding that 10 lay raters did not reach an adequate Cronbach's alpha for expert-domain products, where 10 experts did [@kaufman2008a; @kaufman2013]" |
| M7-5 box item 3 unconfirmed design fact | **resolved** | 252 "[FILL IN: confirm that no set of actions was rated by all raters; the largest fully crossed block comprised three raters and 261 actions (FI-4)]"; author_todo line 46 gives the replacement text |
| m7-1 APA numerals | **resolved** | 41 "10 novices", "100 random panels of 10 novices", "10–15", "one to 10"; 159 "at 12", "at 10 ratings", "at 13"; 163 "at 10"; 225 "10 and 13"; 262 "one to 10"; only spelled-out number ≥ 10 is sentence-initial "Twenty-one" (95), which APA requires |
| m7-2 "judges" | **resolved** | 43 "the number of raters needed"; 247 "the number of raters needed"; "judge" remains only in "judge response theory" (2, 9, 10, 53, 59), the terminology sentence (35) and "judgement" (247) |
| m7-3 target/object precision | **resolved** | 41 "inter-rater and test-retest intraclass correlations of .70 consistently [@barth2021]", "against a test-retest intraclass correlation of .70 [@terai2026]"; 229 "fashion and design products against inter-rater and test-retest intraclass correlations of .70" |
| m7-4 D-study wording | **resolved** | 41 "D-studies projected that two raters … would reach … and that five graduate-student raters with 15 captions would reach .80" |
| m7-5 severity gloss | **resolved** | 41 "rater main effects, which indicate severity differences" |
| m7-6 non-recognition cause unmarked; "non-visible" | **resolved** | 95 "leave the action not visible in the clip"; ATC-40 (author_todo line 73) |
| m7-7 ecological validity as fact | **resolved** | 49 "has been argued to be more ecologically valid than laboratory and game-test settings"; ATC-39 (author_todo line 61) |
| m7-8 Primi comparability | **resolved** | 233 "although their ratings used other scales, rating formats and raters, so that logit spans are only indicatively comparable" |
| m7-9 Krippendorff package unnamed | **partially (author item)** | 141 "an R package for Krippendorff's alpha" with the FILL IN "name and version of the package used for Krippendorff's alpha (FI-6)"; acceptable as a FILL IN |
| m7-10 "$10^{-4}$" notation | **resolved** | 111 "tolerance 0.0001"; see the ruling in Section 3 |
| m7-11 rendered marker vs author_todo | **resolved** | author_todo line 4 "the only one left is the YAML affiliation placeholder (manuscript.qmd:7), listed in section 1" |
| m7-12 .80 unjustified | **resolved** | 129 "the target used in the generalizability studies cited above [@silvia2008; @kaufman2007; @hass2018]"; ATC-42; see m8-7 for one clause |
| m7-13 closing order | **resolved** | 274 "Until such evidence exists, the design implications above, several ratings per action, a calibration set rated by all raters and the reliability of the scores actually used, are what these data support." |
| m7-14 R17 under M3 | **resolved, but introduces M8-1** | 239 "together with R17, whose M3 discrimination (0.797) was the third-lowest" |
| m7-15 runco2012 definition | **resolved** | 87 "functionality being its effectiveness in the game context (cf. the standard definition of creativity as originality and effectiveness by @runco2012)" |
| m7-16 supplement duplicates Method | **carried as author decision** | author_todo FI-16 note: "if CRJ does not publish the supplement as a separate file, shorten it to a pointer" |
| m7-17 headline wording | **resolved** | identical formulation at 9, 163, 219, 227, 251, 278: "the smallest number of ratings at which simulated reliability reached .80 was four" |
| m7-18 CRJ format | **open (author, FI-16)** | author_todo §3 FI-16 |
| Housekeeping: FI-18 Q1/Q3 entry | **removed** | author_todo §3 FI-18 no longer mentions Q1/Q3 |
| Housekeeping: three bib-repair items | **removed** | no bibliography item in author_todo §3 |
| Housekeeping: "flatten" item | **removed** | author_todo §4 has no such item; §1 header says single file |
| Housekeeping: §2 header vs YAML marker | **consistent** | author_todo line 4 |
| Housekeeping: FI-16 word count stated | **done** | author_todo line 139 "about 1,600 words excluding the FILL IN markers and headings; about 1,750 with them" |
| Housekeeping: interpretive claims to add (49, 95, 107, 115, 252, 247 extension) | **done** | ATC-39 (49), ATC-40 (95), ATC-6 now quotes the Methods sentence at 107, ATC-41 (115), FI-4/ATC-18 at 252, the 247 quote now runs to "cannot separate (domain, rater pool, scale, target and object)" |

---

## 3. Number audit (complete)

Every numeric claim in the abstract, body, box and supplement note, in line order. "F" = finding in `03_findings.md`; "Δ" = Delta 2026-11-09; "Δb" = Delta 2026-11-09b; "07" = `07_rater_number_evidence.md`.

| Line | Text value(s) | Source value(s) | Status |
|---|---|---|---|
| 9 | 24 raters; 9,046 ratings; 3,669 actions; 7-point | F0.3 | match |
| 9 | .689 vs .969 | F1.12 | match |
| 9 | .522 (one rating), .699 (two) | F1.14 | match |
| 9 | smallest number reaching .80 = four (simulated) | Δ2 "Smallest k … at least .80: 4" | match |
| 9 | .579 to .016 | F0.9 R06 0.579, R13 0.016 | match |
| 9 | about 50 ratings | F0.5 R26 46, R27 47, R19 50, R17 52, R18 55 | match (descriptive) |
| 9 | both *p* < .001 | F1.2 | match |
| 39 | α = .94 (106 novices), *r* = .22 | 07 kaufman2008a 0.94; 0.22 | match (07) |
| 41 | 2 raters uses/instances, 3 consequences, relative G ≥ .80, average scoring | 07 silvia2008 (2/.82, 2/.84, 3/.83) | match (07) |
| 41 | 5 graduate-student raters, 15 captions, .80 relative and absolute | 07 kaufman2007 (4 graduate students; 5 raters with 15 captions; g and phi ≥ .80) | match (07; see m8-3) |
| 41 | 10 novices .58 (own projection, poems) | 07 Resolutions .58 (.575) | match (07) |
| 41 | 100 panels of 10 novices .53 (.35–.75); designs .66; experts .93 and .86; *r* = .56 | 07 kaufman2013 details | match (07) |
| 41 | 7 or more raters, inter-rater and test-retest ICC .70 (fashion); 10–15 and 15–20 (design, test-retest ICC .70) | 07 barth2021; terai2026 | match (07) |
| 41 | no panel of 1–10 lay raters reached .80; 26.6% and 56.9% | 07 hass2018 | match (07) |
| 41 | 2 trained raters, 5 tasks, relative .70 | 07 vanhooijdonk2022 (originality/completeness 5 tasks, 2 raters) | match (07) |
| 41 | 84 studies; fewer than 10; about five; 5–10; 2 to 134 | 07 long2022; kaufman2008; cseh2019 | match (07) |
| 57 | workload cut by about a third | 07 primi2019 | match (07) |
| 63 | 24 raters | F0.3 | match |
| 69 | one to 10 ratings; at least four | F1.20; F1.21 | match |
| 79 | 24 raters; R01–R19, R23–R27; four excluded; 46 to 1,174 | F0.3; F0.5 | match |
| 91 | 832, 2,107, 68, 153, 198, 137, 95, 36, 22, 14, 4, 2, 1 | F0.4 | match (13 of 13) |
| 95 | 10,447; 1,347; 0.0 (R04); 21 pairs, one conflicting; 22 rows; 9,077 by 28 | F0.1 | match |
| 97 | fewer than 15; up to seven parameters; R20 13, R21 9, R22 2, R28 7; 31; one product; *r* = .99994; 0.00204; 0.35026 | F0.2; F2.12 | match |
| 99 | 9,046 / 3,669 / 24; 1–7 coded 0–6; 2.466; median 2; 1–13; 1.806; 832; .103; one component; 30 of 276; median overlap 19 | F0.3 | match |
| 99 | eight raters; category 7: R01, R03, R06, R18, R25, R26; 6 and 7: R17; 5 and 7: R27; thresholds 4/5/6 | F0.7 | match |
| 107 | variance fixed at 1 in M3 and GRM, estimated in M1 and M2 | F1.6 (values not quoted) | match |
| 111 | 61 quadrature points; **0.0001**; 436 iterations; positive definite | F1.3 "Tolerance 10⁻⁴"; 436; True | match (notation; see ruling) |
| 115 | df 105 vs (J−1)(K−2) = 115 | F1.2 | match |
| 119 | 0.7–1.3; 20 imputations; about 90%; 222 of 276; ≥ 3 shared; ≥ 30 shared; 0.2; 30 of 276 | Δ4c/4d; F1.7; F1.9; F1.10 | match |
| 123 | 200 accepted draws; 43 rejected | F1.12 | match |
| 127 | six raters (R26, R19, R14, R02, R12, R27); 1,000; 647; 353 | F1.18 | match |
| 129 | .80; k = 1–10; 50 × 2,000; seed 20260713; smallest k; until four; 50 replications | F1.20; Δ2; F1.21; Δb | match |
| 133 | ±1.96 *SE*; 95%; 1–7; (1), (7), (1, 7), (3–5); natural log | F2.3; F0.9 | match |
| 137 | with one rating only seven distinct raw means; four models | F2.13 note | match |
| 149 | AIC 27,258.550; SABIC 27,737.316; BIC M1 28,235.202; GRM 4.161 above (28,239.363); 158; −13,471.275 vs −13,495.966; 49.381 | F1.1 | match |
| 149 | 436 iterations; S-X² *p* .328 to .665 | F1.3; F1.8 | match |
| 149 | infit 0.429 (R02)–0.980 (R18); outfit 0.402–0.971; 15 flagged, all < 0.7, none > 1.3 | F1.7; Δ4d | match |
| 149 | mean Q3 −.202 (222); 28 flagged; 10 shown; eight negative, two positive (R09–R23, R10–R11) | F1.9 | match |
| 155 | .689 [.669, .703]; .969 [.965, .974]; grid .969 | F1.12 | match |
| 155 | α .949 [.926, .958] (18, 1,946); 647 of 1,000; .750 [.684, .800] (3, 261); .391 [.363, .417] (24, 2,837) | F1.18 | match |
| 159 | .522 (832); .699 (2,107); .756 (68); .948 at 12; .897 at 10 after .915 at 9; .947 at 13 after .948 at 12; PSD 0.684 to 0.228; 0.314 at 10; 0.230 at 13; 14, 4, 2, 1; .969 | F1.14; F1.12 | match |
| 163 | .530 [.513, .544]; .705 [.696, .713]; .787 [.778, .797]; .834 [.827, .841]; .928 [.925, .931]; four | F1.20; Δ2 | match |
| 163 | inside at 1, 2, 8; below at 3–7, 9, 10 | F1.22 direction (reader comparison, ATC-32) | match |
| 167 | .686 [.675, .695]; .687; observed .689; 6,778; 3,007; 15,824; .835 [.829, .840] | F1.21; F1.12 | match |
| 171 | .712; .191; .599, .789; .068 to .954; *r* = .947; 229 | F1.13; F1.16 | match |
| 175 | 1.760 (R06)–3.836 (R18); SD 1.022 (R01)–1.953 (R19); .579 (R06)–.016 (R13); R19 .080; eight raters listed; R27 no 5; R13 .799, R18 .764, R12 .735, R06 .192; entropy 1.191 (R06)–1.903 (R09; 3.643); 2,179; 2,355; 128 | F0.9; F0.6 | match |
| 179 | −0.878 (*SE* 0.066, R24) to 1.369 (*SE* 0.057, R06); 2.247; 13 below, 11 above; R18 3.84, −0.79 | Δ3; F2.8; F2.9 | match |
| 185 | *b*₁ −6.25 (R18, 55, *SE* 2.86) to 0.25 (R06, 0.05); −3.36 (R13, 0.47); R02 −0.67 to 1.99; R13 −3.36 to 4.31; thresholds 4/5/6 | F2.2; F0.7 | match |
| 189 | 0.66 (R18, 55, 0.27) to 3.19 (R26, 46, 1.72); R06 3.10 (520, 0.45); R27 3.04 (47, 0.91); R25 3.01 (138, 0.47); R24 2.89 (190, 0.37); R09 0.93 (400, 0.15); R16 2.47 (268, 0.26); R01 1.82 (0.13); R02 2.71 (0.35); R23 1.75 (0.13); SEs 1.72, 1.01, 0.91 | F2.1 | match |
| 193 | 0.13 [0.02, 0.39]; 2.52 [0.11, 6.75]; .004 [.000, .011]; .074 [.003, .178]; R09 0.28 [0.13, 0.48]; R01 0.86 [0.66, 1.05]; R02 1.96 [1.11, 2.97]; R19 2.03 [0.27, 5.31]; R27 2.01 [0.50, 4.12]; 200 draws | F2.5 | match |
| 193 | R01 2.800, R16 2.400, R06 2.300; R13 −0.600; R06 .001 at −2, .082 at 2; R12 .137, R24 .120 | F2.4 | match |
| 197 | χ²(105) = 840.447; AIC 27,418.524 vs 28,048.971; BIC 28,235.202 vs 28,256.560; χ²(23) = 156.593; AIC 27,307.931 vs 27,418.524; BIC 28,256.560 vs 28,288.744 | F1.2; F1.1 | match |
| 199 | 0.305 (R18, 0.141) to 2.221 (R27, 0.873); median 1.240; 7.277; SD 0.550; nine (M2), eight (M3); R09 1.083/1.060; R17 1.323/1.167; R18 1.170/1.231; R12 0.260/0.278 | F1.4; Δ1; F1.5; F1.11 | match |
| 201 | 832; .833; .041; 1.229; 1.430 — 2,107; .818; .066; 1.531; 2.170 — 730; .849; .071; 0.537; 1.317 | F2.13 | match |
| 207 | .977/.979/.206/.042; .985/.984/.155/.032; .996/.996/.081/.016; .981–.993; .984–.996; 1.000 | F2.11; F2.10 | match |
| 215 | 28, 9,077, 3,670; .68896 → .68837; .96893 → .97142; 3,669; .99994; 0.00204; 0.35026; .00273; 24; .99802; 0.19349 | F2.12 | match |
| 219 | four; about 50; 4.161 | Δ2; F0.5; F1.1 | match |
| 223 | .969; .949; .689 [.669, .703]; .391; .949 | F1.12; F1.18 | match |
| 225 | .522; .699; rows at 10 and 13 on 14 and 1 products | F1.14 | match |
| 227 | four (.834); .835 | F1.20; F1.21 | match |
| 229 | .80 (relative G); 10 lay / 10 experts; 7 to 15; .70; three or four raters | 07 | match (07; see m8-2) |
| 233 | 2.247; −1.18 to .64; about 0.9; R09 0.93 (0.15), R06 3.10 (0.45); 46–55; 520, 138, 190; 2.52 vs 0.13; 0.11 to 6.75 | Δ3; 07 primi2019; F2.1; F0.5; F2.5 | match |
| 239 | 158, 158, 135, 30; 0.305 to 2.221; 7.277; R18 0.66, R09 0.93 (GRM); R17 0.797 (M3); R12 2.72 (GRM) | F1.1; Δ1; F2.1; F1.4 | match (values); see M8-1 for the mixed metric |
| 241 | 1.229; 1.430; .066 vs .041 | F2.13 | match |
| 243 | .977; .206; .042; .081; .016 | F2.11 | match |
| 247 | four for .80; .391; about five raters (long2022); about 50 (R17, R18, R19, R26, R27) | Δ2; F1.18; 07 line 96; F0.5 | match |
| 250–255 (box) | .689, .949, .969, .391; .522, .699, four, .80; three raters, 261 actions; about 50 | as above; F1.18 | match |
| 262 | one to 10 | F1.20 | match |
| 264 | 0.7 | Δ4c | match |
| 266 | 105 vs 115 | F1.2 | match |
| 270 | fewer than 15; .99994; 0.35026 | F2.12 | match |
| 278 | .689; .949; .969; .522; .699; four; .80 | as above | match |
| 335 (supplement) | k = 1–10; 50 × 2,000; seed 20260713; at least four; 50 replications | F1.20; F1.21; Δb | match |

**APA number formatting:** unchanged from round 7 and correct (no leading zero for bounded quantities; leading zero for logits, *a*, PSD, infit; thousands separators on all ≥ 1,000 counts and criteria; seed without separator; *p* < .001; symbols italic). The one spelled-out number ≥ 10 ("Twenty-one", 95) opens a sentence and is therefore correct.

**Ruling on the estimation tolerance (line 111, "tolerance 0.0001"):**
- Premise check first: the outline's never-quote list (`04_outline.md` lines 28–38) does **not** name "0.0001"; the only mention of the tolerance in the outline is the object plan at line 199, "tolerance 10⁻⁴", which simply repeats the printed form of `tbl-grm-convergence` (F1.3). So there is no explicit never-quote entry to enforce here; the question is whether a notation change counts as a departure from "values as printed".
- Ruling: **acceptable; not a mismatch and not a never-quote violation.** Reasons: (1) 10⁻⁴ and 0.0001 are the same exact number; nothing is invented, rounded, reconstructed, or changed in precision, which is what the non-negotiable rule and the "no rounding, no added or removed decimals" convention forbid. (2) The outline already sanctions notation conversions that depart from the printed form when APA prose calls for them (thousands separators where the notebook prints none, leading zeros, the "1174 → 1,174" rule); writing a single tolerance as a decimal in Methods prose is the same kind of conversion. (3) The printed form remains visible in the embedded `tbl-grm-convergence` in the supplement, so a reader can match the two. 
- Condition: record the conversion in `author_todo.md` §3 (one line under the stale-string self-check or FI-18: "tolerance printed as 10⁻⁴ in `tbl-grm-convergence`, written 0.0001 in Methods; same value") so that the next audit does not re-open it. If the author prefers zero friction, reverting to "$10^{-4}$" is equally acceptable; either way the value is right.

---

## 4. Top-up simulation wording check (per location, against Delta 2026-11-09b)

Required substance: actual rater–product assignment kept, not the ratings; additional raters drawn at random with equal probability and without replacement from panel raters who had not rated the product, until 4; products with ≥ 4 unchanged; 50 replications; θ ~ N(0, 1) per real product; all ratings generated from the fitted GRM and scored by EAP with parameters treated as known; actual-design row = validation against the observed empirical reliability.

| Location | Wording | Verdict |
|---|---|---|
| 69 (Introduction) | "simulated the actual design topped up so that every action had at least four ratings" | consistent (neutral summary; no procedural claim) |
| 129 (Method) | "kept the actual assignment of raters to products, that is, which raters had rated which product, but not the ratings themselves … In the actual design, each product kept exactly the raters who had rated it. In the design with at least four ratings per product, each product kept its raters, and every product with fewer than four ratings was assigned additional raters, drawn at random with equal probability and without replacement from the panel raters who had not rated it, until it had four; products with four or more ratings were unchanged. In each of 50 replications, every real product received a creativity value θ drawn from N(0, 1), all ratings in the design, for the kept and the added rater–product pairs alike, were generated from the fitted GRM, and the products were scored by EAP with the parameters treated as known. The real ratings were not reused; the actual-design row is a validation of the simulation, which should reproduce the observed empirical reliability of the real scores." | **matches Δb in every element** |
| 167 (Results) | "The simulated actual design, in which each product kept the raters who had rated it, gave … .686 [.675, .695] (mean rel~post~ .687), against the observed .689 of the real scores. The design in which every product had at least four ratings, which added 6,778 ratings to 3,007 products (15,824 ratings in total), gave .835" | consistent; "added 6,778 ratings" follows the table header "Ratings added" but could be read as additions to the real data (m8-4) |
| 227 (Discussion) | "the actual design topped up so that every action had at least four ratings gave .835 … Under the stated assumptions, that raters are drawn at random with equal probability, that the parameters are known and that all ratings, including those of the actual rater–product pairs in the top-up simulation, follow the fitted GRM" | consistent ("all ratings, including those of the actual rater–product pairs" states that kept pairs are regenerated) |
| 262 (Limitations) | "in the top-up simulation, the added raters were drawn with equal probability and without replacement from the panel raters who had not rated the product … all ratings, including those of the kept rater–product pairs in the top-up simulation, were generated from the fitted GRM with θ ~ N(0, 1), so the simulations presuppose the model and the latent distribution and do not reuse the real ratings" | **matches Δb** |
| 335 (Supplement) | "kept the actual assignment of raters to products, not the ratings … drawn at random with equal probability and without replacement from the panel raters who had not rated it, until it had four, and products with four or more ratings were unchanged. In each of 50 replications, every real product received θ ~ N(0, 1), all ratings for the kept and the added rater–product pairs were generated from the fitted GRM, and the products were scored by EAP with the parameters treated as known; the real ratings were not reused, and the actual-design row is a validation against the observed empirical reliability" | **matches Δb** |

- No sentence anywhere says that the real ratings were kept or that ratings were added to the real data (grep "real ratings were kept": 0; "the real ratings are kept": 0).
- Projection vs top-up: not conflated. 129 and 335 introduce the two under their own names and settings (projection: θ ~ N(0, 1) simulated products, k random raters, 50 × 2,000, seed; top-up: actual design, 50 replications, no seed quoted). 163 attributes the curve and the "four" to the projection; 167 attributes .686/.835 to the top-up; 227 names "In the projection … four (.834)" and "the actual design topped up … .835" separately; `tbl-grm-reliability-observed-vs-simulated` is described as the projection at 163 and 335. The never-quote items (min-4 seed; whether a rater may rate twice; how θ enters) are now covered by the corrected notebook note itself (without replacement from raters who had not rated the product; θ ~ N(0, 1) per real product) and are stated only in that form.

---

## 5. Regression check (rounds 3–7 and the round-7 confirmations)

| Item | Status | Evidence |
|---|---|---|
| Stale strings (§8 list + additions) | 0 illegitimate hits | only ".928" at 163 (projection value) |
| 48 embeds each once; 5 unembedded labels absent | confirmed | lines 101–209 (14), 291–369 (34); no `@tbl-marginal-reliability-models`, `@tbl-cleaning-log`, `@tbl-grm-global-fit`, `@tbl-overview-ratings-per-action`, `@fig-overview-rater-overlap` |
| 96 citekeys resolve | confirmed | 96 `@…{key,` matches in `phd_library.bib`, none missing |
| Abstract ≤ 250 words, no citations/markers/"student raters" | confirmed | 246 words (my count) |
| Title verbatim D7 alternative | confirmed | line 2 = `04_outline.md` line 66 |
| D5 two rater groups | confirmed | 79 "The raters came from two groups … The second group, raters R23 to R27, joined later"; 270 "the raters came from two groups" |
| D8 swap | confirmed | `fig-category-usage-shares` at 177 (main); `fig-overview-rater-response-styles` at 301 (supplement) |
| C1 GRM not best on every criterion | confirmed | 149, 219, 264 |
| C2 shared category structure not rejected by BIC | confirmed | 9, 197, 219, 239, 266, 278 |
| C3 reliability not monotone in n | confirmed | 159, 225 |
| C4 crossed-block closeness deleted | confirmed | 155 |
| C5 extremes not only from ~50-rating raters; R16 not "few ratings" | confirmed | 189, 233 |
| C6 maximum-information locations | confirmed | 193 |
| C7 R27 internal gap; thresholds not compared | confirmed | 99, 115, 185, 268 |
| C8 non-consecutive rater IDs explained | confirmed | 79, 97 |
| C9 duplicate rule | confirmed | 95 |
| C10 M1 misfit examples | confirmed | 199, 239 |
| C11 local dependence counts | confirmed | 149 |
| C12 exclusion sensitivity wording (D4) | confirmed | 97, 215, 270 |
| C13 no allocation rule or timing claim | confirmed | FILL INs at 91, 159, 227, 260; timing note inside FI-3 marker at 87 |
| 07: targets and objects with every cross-study figure | confirmed | 41 (person level / relative G; product level / alpha; inter-rater and test-retest ICC .70; persons across tasks / relative .70); 229 (same) |
| 07: Cseh & Jeffries as open question, not requirement | confirmed | 43 "list the number of raters needed … among the open questions of the CAT"; 247 "remains an open question of the CAT" |
| 07: .53 / .58 attribution per Resolutions | confirmed | 41 ".58 [@kaufman2008a]" as "Kaufman et al.'s own Spearman–Brown projection"; ".53 (range .35–.75) [@kaufman2013]" |
| 07: author synthesis not attributed; no "by convention" | confirmed with one borderline clause (m8-1) | no "5–7 experts", no "avoid fewer than 10 lay raters", no "by convention" |
| 07: Memmert-group descriptions per confirmed sources | confirmed | 51, 229 (four-way split per 06 §F4) |
| APA numerals | confirmed | Section 3 |
| "raters" not "judges" outside the terminology sentence and the JRT term | confirmed | grep |
| Rounds 3–6 items (model names as printed; latent variances not quoted; narrative-and filter; N6-1 θ wording at 107/268; m5-x items) | no regressions | 107, 109, 123, 155, 223, 268; YAML 23–27 |
| Glyphs | confirmed | 0 hits for ⚑ ✕ † |

---

## 6. New issues (draft 8)

### Critical
None.

### Major

**M8-1 (selective metric in an interpretive sentence). Line 239 supports the "discrimination surfaces as misfit" account with GRM discriminations for R18 and R09 but with the M3 discrimination for R17.**
- Quote: "R18 (GRM $a$ = 0.66) and R09 (0.93), the two lowest discriminations, were the raters with values above 1 under M1, together with R17, whose M3 discrimination (0.797) was the third-lowest, whereas R12 ($a$ = 2.72) had the lowest values under M1; the account is illustrative."
- Problem: R17's GRM discrimination is 1.81 (F2.1), mid-range among the 24 raters; the sentence switches to the M3 metric for R17 only, where 0.797 is third-lowest (F1.4). A reviewer who opens `tbl-grm-rater-parameters` will see that the account does not hold for R17 under the model the sentence otherwise uses, and the mixed metric looks like selection. The misfit values being explained are M1 values, so the discrimination metric nearest to M1 is M3 (same adjacent-category family, same software, same latent variance), not the GRM.
- Fix: use one metric, preferably M3, for all four raters: "R18 (M3 discrimination 0.305), R09 (0.306) and R17 (0.797), the three lowest discriminations in the ladder (@tbl-discrimination-m3), were the raters with values above 1 under M1, whereas R12 (2.169, the second-highest) had the lowest values under M1; the GRM discriminations give the same picture for R18, R09 and R12 (0.66, 0.93, 2.72) but not for R17 (1.81); the account is illustrative." All values are printed (F1.4, F2.1). Update the ATC-9 quote in author_todo accordingly.

### Minor

- **m8-1 (attribution; 07 binding instruction 11). Line 247: "and practice has settled on about five raters without such evidence [@long2022]."** 07 (line 96) records from long2022 that most of 84 reviewed studies used fewer than 10 raters, mean and median about 5, and that "no optimal number [was] established"; 06 (line 337) adds that only the abstract was read. "Settled on" and "without such evidence" are the authors' reading of that review, placed under the long2022 citation. Rephrase so the citation carries only the descriptive finding: "and most published studies use about five raters [@long2022], a figure that does not rest on such evidence." Add this clause to the 247 ATC entry in author_todo (its quote currently stops before it).
- **m8-2 (literature precision, residual of M7-3). Lines 51 and 229 attribute averaging and an intraclass correlation to all four sport studies.** 51: "summarised the panel by averaging and reported its agreement, mostly as an intraclass correlation"; 229: "reported intraclass correlations of averaged ratings rather than the number of ratings needed". Per 06 §F4, averaging is confirmed only for roca2018 and joode2023 ("not stated" for kempe2018 and memmert2010), and kempe2018's index is an unspecified "inter-judge reliability" known from a secondary summary. 51 already hedges the index ("mostly"); 229 does not, and neither hedges the averaging. Suggested 229: "reported the agreement of the panel, mostly as an intraclass correlation, rather than the number of ratings needed for a target reliability"; 51: "summarised the panel by averaging where this is reported". The FI-17 marker at 51 covers verification; 229 should carry the same hedge until the PDFs are checked.
- **m8-3 (classification). Line 41 groups kaufman2007's captions under "trained student raters scoring short, homogeneous divergent-thinking responses".** 07 classifies kaufman2007 as creative writing (captions) rated by four psychology graduate students; training is not recorded. Suggested: "For student raters scoring short, homogeneous responses at the person level (divergent-thinking responses and captions), D-studies projected …". The silvia2008 raters were trained (07: "Trained student raters"), so "trained" can stay if attached to silvia2008 only.
- **m8-4 (wording that could be read as data augmentation). Line 167: "which added 6,778 ratings to 3,007 products (15,824 ratings in total)".** The numbers follow the table headers ("Ratings added", "Ratings (total)") and are correct, but after Method 129 has stressed that no real rating is reused, "added … ratings to … products" may be read as additions to the real data. Suggested: "in which 6,778 rater–product pairs were added to 3,007 products (15,824 simulated ratings in total)".
- **m8-5 (APA abbreviations). "BIC" appears in the abstract (9) undefined; "MFRM" is first used at 109 ("M1 (rating-scale MFRM)") without expansion, because the only expansion ("partial-credit MFRM") sits inside the FILL IN marker at 57, which will be removed; "EM" (111) and "AIC"/"BIC" (115) are never expanded (SABIC is).** Define at first use: "many-facet Rasch models (MFRM)" at 57, "expectation–maximization (EM)" at 111, "Akaike information criterion (AIC), Bayesian information criterion (BIC)" at 115; in the abstract either spell out "the Bayesian information criterion" or accept the abbreviation as journal-standard (author's call per CRJ practice).
- **m8-6 (implicit sampling claim, author to confirm from code). Line 129 and 335: "each received $k$ ratings … from $k$ raters of the panel drawn at random".** "k ratings from k raters" implies k distinct raters per simulated product (without replacement), which the never-quote list says the notebook does not state for the projection. The phrase is the notebook's own wording, so it is quotable, but the author should confirm from the R code that raters are drawn without replacement within a product and, if so, may write "from $k$ different raters"; if not, the wording must change. This is a code fact of the author's own analysis, like the former FI-33.
- **m8-7 (criterion comparability, one clause). Line 129: "The criterion was a reliability of .80, the target used in the generalizability studies cited above [@silvia2008; @kaufman2007; @hass2018]."** Those targets are relative G, Eρ² or g and phi for persons; the present criterion is the empirical marginal reliability of product scores. The paper itself insists (41, 43, 229) that targets and objects are not interchangeable. One clause keeps the paper consistent: "the conventional value used as the target in the generalizability studies cited above, applied here to the empirical marginal reliability of product scores". ATC-42 covers the attribution.
- **m8-8 (figure reference). Line 227: "gave .835, the reference line in @fig-grm-reliability-observed-vs-simulated".** The figure has two dashed reference lines (top-up .835 and full panel .969; F1.23). Write "the lower dashed reference line" or "one of the two dashed lines".
- **m8-9 (grammar). Line 9: "how many raters are needed and how raters differ has been studied mostly with verbal and static material."** Two coordinated subjects; "have been studied" (or recast: "the number of raters needed and the differences between raters have been studied mostly …").

---

## 7. `author_todo.md` check

**Quoted sentences and line numbers.** All FILL IN locations in §1 (7, 35, 39, 41, 47, 49, 51, 57, 59, 75, 79, 83, 87, 91, 95, 97, 127, 141, 159, 223, 227, 233, 235, 247, 252, 260, 270) and all ATC locations in §2 (9, 41, 47, 49, 51, 59, 63–67, 87, 91, 95, 97, 107, 115, 119, 127, 129, 163, 167, 201, 219, 223, 225, 227, 229, 233, 235, 239, 241, 243, 247, 249–256, 262, 264, 266, 270, 274, 278) match the current manuscript line by line; every quoted sentence is present verbatim at the stated line.

**Housekeeping from round 7:** the FI-18 Q1/Q3 note, the three bibliography-repair items and the "flatten" item are gone; the §2 header now agrees with the YAML marker; FI-16 states both Introduction counts. New ATC-39, ATC-40, ATC-41, ATC-42 are present with the right sentences (lines 61, 73, 79, 85); ATC-6 now also quotes the Methods sentence at 107; the 247 quote is extended; box item 3 carries FI-4/ATC-18 and the replacement text (line 46). The note on FI-33 (line 51) is correct and consistent with Delta b. "Open ATC items (36)" matches the list. The stale-string self-check (line 142) agrees with my grep, including the "has to be established anew" 0-hit claim.

**Interpretive claims still without an ATC item (add):**
- 247 "practice has settled on about five raters without such evidence [@long2022]" (m8-1): extend the 247 quote or add a line under ATC-31.
- 239: the ATC-9 quote should be updated once M8-1 is applied (metric change).
- 129/335 "from $k$ raters of the panel drawn at random" (m8-6): one author item "confirm from the R code that the projection draws k distinct raters per simulated product".

**Stale or inconsistent entries:** none found. Two small additions recommended: (a) the tolerance notation note (Section 3 ruling); (b) under §3 "Top-up simulation (M7-2)", add line 227 to the list of locations (129, 167, 262, 335), since 227 also carries the assumption statement.

---

## 8. Readiness statement

What remains before submission, in order:

1. **Reviewer-side text fixes (this round):** M8-1 (metric at 239); m8-1 to m8-9 as the author sees fit (all are single-sentence edits; none needs new analyses).
2. **Author FILL INs (39 in §1 of author_todo, incl. the YAML affiliation):** study context, ethics, preregistration, rater groups and pool description (FI-1, FI-21, FI-31), stimulus material (FI-2), rating procedure and instruction wording (FI-3, FI-32), allocation and common-set question (FI-4, incl. box item 3), non-recognition rates (FI-22), exclusion-criterion rationale (FI-23), crossed-block raters and pairwise-alpha removal rule (FI-9), software versions and Krippendorff package (FI-6), data/code availability (FI-15), and the FI-17 verifications of every literature figure and attribution used in the Introduction and Discussion (the 07/06 verification levels are "excerpts" or "abstract_or_secondary" for kaufman2007, kaufman2008a, terai2026, barth2021, long2022, kempe2018, zahno2023/2024, so the PDFs must be checked).
3. **ATC confirmations (36 open + the long2022 clause and the k-distinct-raters code fact):** especially ATC-35/ATC-32 (simulation assumptions and reader comparisons), ATC-30/31 (design argument), ATC-39 to ATC-42 (new in round 7), ATC-9 after M8-1.
4. **Render check:** 48 embeds must resolve against the rebuilt notebooks (the Delta-b rebuild changed the `tbl-rater-overview` glyph to † and the `fig-category-usage-shares` labels to "unused: …"; `tbl-discrimination-summary` must be present); 96 citekeys; narrative "and" via `narrative-and.lua`; the FILL IN highlight inside the callout at 252 renders in both docx and pdf; FI-18 display fixes in the notebooks (code-style headers and row labels, severity-figure colours, `tbl-rater-overview` separators, `tbl-lr-tests` caption) are the notebook's business but should be done before the final render.
5. **CRJ format (FI-16):** abstract limit, title page, running head, double spacing, table/figure placement, supplement S-numbering and standalone policy (then decide m7-16), acceptance of the callout box, heading levels, abbreviation policy (m8-5).
6. **Final steps (author_todo §4):** remove `mark-highlight.lua` and the `soul`/`xcolor` header once no FILL IN remains; keep `citeproc: false` and the filter order; retire or update the D6 stale files (`submission/3_PACA.md`, `preliminary_draft/manuscript.qmd`).

From the reviewer's side, no further round is needed after M8-1 and the minor items are addressed; the next checkpoint is the author's.

---

## 9. Positive points

- The top-up simulation is now described identically and correctly in Method, Results, Discussion, Limitations and the supplement, following the corrected notebook note word for word in substance, and the validation role of the actual-design row is stated without a "close" claim.
- All roughly 330 numeric claims match the findings file, including every value newly quotable through the two deltas; the never-quote discipline holds throughout.
- The Discussion's closing argument now says exactly what one rater pool can support: the figure could not have been read off the existing evidence and cannot be assumed to transfer; the five conditions of the Introduction are echoed rather than contradicted.
- The sport literature is described per study with its object and setting, which also removes the earlier tension with the ecological-validity sentence.
- The cross-domain comparison at 229 states target and object for every figure and treats the ten-novice result as the negative finding it is.
- author_todo is accurate against the manuscript and now carries every interpretive claim the round-7 review asked for.
