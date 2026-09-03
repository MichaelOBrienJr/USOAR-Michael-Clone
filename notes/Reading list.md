---
title: "Reading list"
date: 2026-09-02
updated: 2026-09-02
---

Ordered reading for getting into the project. Start at the top; it is normal not to understand everything on the first pass. Each paper has its own page under `Paper/` with links and a short summary. Keep adding to this list.

## 1. The paper this project builds on

- [[Paper/Kim2026uncovering]] — the [[Embedding disruptiveness measure]] (EDM) paper. Read it first. Then follow some of the references, especially those in the introduction (listed below).

## 2. The measure it replaces

- [[Paper/Funk2016dynamic]] — the original CD index ([[Disruption index]]), defined on patent citation networks. Free PDF: https://www.russellfunk.org/cdindex/static/funk_ms_2016.pdf

## 3. The embedding method behind the EDM

The EDM learns paper vectors with a skip-gram model over random walks on the citation network, so the [[Word2vec]] papers are the technical foundation.

- [[Paper/Mikolov2013efficient]] — the first word2vec paper (CBOW and skip-gram architectures).
- [[Paper/Mikolov2013distributed]] — the follow-up with negative sampling and subsampling, which is the training recipe most implementations use.
- Explainer: [The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/) by Jay Alammar (2019). Read this before or alongside the two papers.

## 4. References from the Kim et al. introduction

Pulled from the introduction of [[Paper/Kim2026uncovering]]. Pick a few; the first group is closest to the project.

Disruption and its correlates:

- [[Paper/Wu2019largeteams]] — Wu, Wang, Evans, "Large teams develop and small teams disrupt science and technology," *Nature* 566, 378–382 (2019).
- [[Paper/Park2023papers]] — Park, Leahey, Funk, "Papers and patents are becoming less disruptive over time," *Nature* 613, 138–144 (2023).
- Uzzi et al., "Atypical Combinations and Scientific Impact," *Science* 342, 468–472 (2013).
- Kedrick et al., "Conceptual structure and the growth of scientific knowledge," *Nat. Hum. Behav.* 8, 1915–1923 (2024).
- Lin, Evans, Wu, "New directions in science emerge from disconnection and discord," *J. Informetr.* 16, 101234 (2022).
- Lin, Frey, Wu, "Remote collaboration fuses fewer breakthrough ideas," *Nature* 623, 987–991 (2023).
- Chu and Evans, "Slowed canonical progress in large fields of science," *PNAS* 118, e2021636118 (2021).
- Zeng et al., "Fresh teams are associated with original and multidisciplinary research," *Nat. Hum. Behav.* 5, 1314–1322 (2021).

Simultaneous discovery (the paper's motivating failure case):

- Merton, "Singletons and multiples in scientific discovery," *Proc. Am. Philos. Soc.* 105, 470–486 (1961).
- Bikard, "Idea twins: Simultaneous discoveries as a research tool," *Strateg. Manag. J.* 41, 1528–1543 (2020).
- Simonton, "Multiple discovery and invention: Zeitgeist, genius, or chance?" *J. Pers. Soc. Psychol.* 37, 1603–1616 (1979).

Background theory (skim or skip):

- Kuhn, *The Structure of Scientific Revolutions*.
- Schumpeter, *Capitalism, Socialism and Democracy*.
- Arthur, *The Nature of Technology: What It Is and How It Evolves*.

## 5. Validation data

- [[Validation sets]] — candidate lists of landmark works (Nobel papers, APS milestones, Hall of Fame patents, landmark court decisions) for testing the measure.

## To add

- Domain-specific data sources (USPTO, case law) once the slice is scoped.
