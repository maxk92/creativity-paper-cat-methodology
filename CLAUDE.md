# Paper Orchestra — project conventions

This project writes scientific papers from vault notes + a results notebook using
a pipeline of specialised agents. Read `paper.config.yml` first; it is the single
source of truth for paper type, paths, venue and review criteria.

`.claude/agents/` and `.claude/skills/paper-config/` are symlinks to
`~/drive/utils/paper-orchestra/.claude/` — the shared agent source. Don't edit
agent files from inside this project; that edits the shared source for every
project. See `~/drive/utils/paper-orchestra/NEW_PROJECT.md` for the general
setup convention this project follows.

## How to run
Invoke the **orchestrator** agent to start or continue a manuscript run. It
delegates to subagents and manages phase artifacts in `manuscript/` (this
project's `build_dir`). Do not run the writer or interpreter directly unless
re-running a single phase on purpose. Data/analysis notebooks live in
`data-analysis/`.

## Pipeline & artifacts (in order)
0. orchestrator reads the concept note at `brief` (author's intent) ← entry point
1. vault-researcher    → manuscript/01_dossier.md
2. web-searcher        → manuscript/06_web_literature.md + manuscript/web_references.bib
3. results-embedder    → manuscript/02_artifacts.md   (objects/labels only)  ┐ parallel
4. results-interpreter → manuscript/03_findings.md    (numbers only)         ┘
5. outline-architect   → manuscript/04_outline.md     ← human checkpoint
6. manuscript-writer   → manuscript/manuscript.qmd
7. reviewer-critic     → manuscript/05_review.md       ← human checkpoint

## Non-negotiable rules
- Numbers come ONLY from the notebook via results-interpreter. Never invent,
  round, or reconstruct values anywhere in the pipeline.
- results-embedder handles objects; results-interpreter handles meaning. Keep
  them separate.
- Results sections are descriptive; interpretation lives in Discussion and is the
  author's responsibility. Interpretive claims are marked for author confirmation.
- Cross-references and citations are mechanical (see the paper-config skill);
  never hand-edit citation formatting — switch the CSL instead.
- Honour the two human checkpoints. Do not auto-proceed past them.

## Paper type
Defined in `paper.config.yml`, profile `imrad-apa` (target venue: Creativity
Research Journal). Add other profiles there rather than editing agents.
