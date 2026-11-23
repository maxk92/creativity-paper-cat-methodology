## For me to do:
- improve title (align with title from colloq plan?)
- improve Outline/Roadmap
- improve wording on slide 5
- style boxes on slide 7 (remove arrow, make facet bold etc); reorganize the lower box
- section 6: "Preliminary study results"

## For Claude to do:
- make sure all citations are created properly, so that hovering over the citation shows the full reference (compare the mlsa-talk @/home/max/drive/projects/4_forecasting-poisson-binomial/papers/01-mlsa2026-poisson-binomial/talk/mlsa-oral/mlsa-oral.qmd if you don't know what I mean)
- in the two examples, the Dribble is assigned to Gareth Bale; for the cross, no player is specified (only Angola is sometimes mentioned, but that's actually the team); please fix that. also, it would be ideal if the second action would also be a dribbling

- slide 4:
	* put the blue box below the bullet points instead of the 2-column layout
	* stein1953 is now added to the librarry, so cite it directly (also cite Runco/Jaeger)
	* place the last bullet point ("creative" is used loosely) below the blue box, so it's framed as the issue leading to the next step of the presentation
	
- slide 5:
	*  print the following direct quote from barbot2019 to the slide: "Over the last few years, however, evolving research questions and needs, advances in methodology and technology, and efforts to address recurrent measurement issues in our field have led to important developments regarding creativity assessment. That notwithstanding, enduring conceptual and methodological issues and the lack of established assessment standards still challenge the validity of creativity studies, limit meta-analytical work, and make the creativity literature at times elusive to the novice eye."
	* place this quote below the paper header screenshot from barbot2019; instead, move the paper header screenshot of barbot2019b to a new slide, as well as the "say which facet..." statement; place the screenshot on the right and add some bullet points on the main conclusions of the SI on the left; for this, you may read directly from the PDF in @/home/max/drive/KNOWLEDGE/phd_lit/barbot2019b.pdf
	
- slide 6: introduce Rhodes' four P model more prominently, then show Batey's heuristic framework as a downstream application of it; also mention the "creative potential, performance, and achievement" taxonomy mentioned in barbot2019b with the respective primary reference; this can all be on one slide and shall just show that there is more than one solution and not a universal standard, but that all the approaches can correspond to each other in a way

- slide 9: move the right-hand subsection to the bottom of the first in a one-col layout; let it appear as an animation; the blue box goes below that and appears as a second animation

- slide 11: place the arrow below the boxes and make it solid

- slide 12:
	* remove the no. of actions and the type distribution;
	* remove the raters bullet point; remove the "per action, per player, per team" in the Creativity Score;
	* illustrate somehow that the plan for this is to compare different models, specifically LSA, Outlier Detection ML models (Isolation Forest, One-Class SVM), and transformer architectures and they are validated against human-based ratings through CAT (the current gold standard); state that the plan was to get two ratings per action and average them, as was done in previous studies
	* include the following three points into the justification of the 7-point unipolar scale (currently it sounds as 7 is as good as 8-10, which is not really the case):
		1) Large comparative experiments show that **reliability, validity, and discrimination generally improve as categories increase up to about 7–10**, with **diminishing returns beyond 7** and potential increases in response error when you go too high. A classic multi-study paper by **Preston & Colman (2000)** found **7–10** points to balance reliability, validity, discrimination, and respondent preference, with **7 often optimal** across outcomes. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/10769936/?utm_source=chatgpt.com "Optimal number of response categories in rating scales"))
		2) A simulation plus empirical review by **Lozano, García-Cueto & Muñiz (2008)** concluded the **optimum is between 4 and 7**, with little psychometric gain above 7. For <4, both reliability and validity drop. ([econtent.hogrefe.com](https://econtent.hogrefe.com/doi/abs/10.1027/1614-2241.4.2.73?utm_source=chatgpt.com "Effect of the Number of Response Categories on ..."))
		3) Reviews on response-scale design reach similar conclusions: too few categories under-discriminate; too many increase cognitive load and noise. ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5993837/?utm_source=chatgpt.com "A classification of response scale characteristics that affect ..."))



- slide 13:
	* stitch the current screenshot from the app together with @rating-app-screenshot.png from this directory (make sure the images are compressed or stretched as needed, so that they look like one image without margin)
	* cite the gh repo of the streamlit-rating-app, not the creativity-rating-app and update the box text accordingly (I know the early ratings were done using the kivy app, but that's not relevant for the upcoming talk)
	* remove all bullet points except the mention of the gh repo; put that below the screenshot and center the screenshot on the slide
	
slide 15:
- remove the quotation marks from the title
- include a bullet point stating that the number of raters for CAT is not fixed in the literature; plucker2008 suggested 5-10, previous research in soccer used 2
- move the text from the blue box behind slide 21; remove the blue box and just show the text; make this slide the main "aim" slide of the study

slide 17:
- remove the matrix fill row and the "Actions with a single rating" row
- remove the "(one component)" from the Design row

slide 18: when first showing the slide, make the GIFs/videos span the full height of the slide (showing the action details written below); when the additional info about the ratings and the rater behavior enters, shrink the videos to the size they currently have; remove the blue box and put its content into presenter notes

slide 20: remove the grey box with the comment, and instead include the percentiles into the table below the plot (percentile of respective action relative to that rater's ratings)

slide 22: reframe the slide more as a "how reliability looks like right now" slide, prompting the exploration of additional methods; show the poor Krippendorff's alpha and the Cronbach's, but mention Cronbach's limitations on this study design and how it might be misleading; mention that we have a sparse, unbalanced design which prevents us from just using averages per action in a crowd wisdom fashion

slides 24-28: spend some more effort on designing these slides and their transitions w.r.t. content:
- for the latent variable problem, use less text and bullet points, but make clear that the difficulty in modeling arises from the fact that the latent variable is a predictor, so we cannot just use normal modeling and estimation; in the grey box, arrange the first two elements side-by-side to make their additive effect more clear instead of printing them below each other
- for both IRT and JRT, include some animations so the audience is not hit with those slides full of text immediately
- please verify this point on the slide: "Solving an easy item says less about θ than solving a hard one, so the same number of solved items can mean different θ. IRT estimates θ from the whole response pattern, with a standard error." Is that not mixing up difficulty and discrimination?
- make the plot on slide 25 slightly smaller so that the list of parameters doesn't experience line breaks; move the "Solving an easy..." text to below the two-col panel
- remove the content about Rasch; make slide 26 instead exclusively on estimation with MML and EM
- slide 27: stretch the table to full width: move the four bullet points from the right below the table and summarize them into two concise bullet points
- slide 28: make theta, bjk and aj appear one by one; then show the bullet points; remove the second bullet point; mention Myszkowski references and the jrt package here; in the grey boxes, include line breaks after the parameters and their names
- slide 30: make the first column only as wide as necessary to avoid as much line break in the last column as possible

- slide 31: change the color coding of the ratings: make all the circles corresponding to the Dribble blue, where the actual rating is larger and has a darker blue than the others; make all the Cross ratings orange, and make the actual ratings given red; remove the blue box from the bottom

slide 33: trim the table: start with Krippendorff's, then show Cronbach's, then GRM empirical, bold-face; rephrase and trim the bullet points on the right, remove reliability per action, rephrase "CAT paper would report..." - not all papers would

- slide 34: remove the blue box around the text and make it two bullet points, appearing together

- slide 35: make the two plots the same height so that captions are aligned, increase space between text and plots slightly
- same as for 35 for slide 37

- slide 38: make the tables appear one by one: first top left, then bottom left, then top right, then bottom right

- slide 39: let contributions appear one by one; rephrase all points - I know the contents are complex, but the sentences are way to long and incomprehensible for audience; make them shorter and more readable; split into two sentences if necessary

- move slide 40 to an unnumbered backlog slide after the reference list

- slide 41: title "Outlook"; create two boxes for the two columns; make the font size smaller 

