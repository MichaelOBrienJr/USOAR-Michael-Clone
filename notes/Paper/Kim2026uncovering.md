---
title: 'Kim, Kojaku, and Ahn, Uncovering simultaneous breakthroughs with a robust measure of disruptiveness'
date: 2026-09-02
updated: 2026-09-02
---

- Munjung Kim, Sadamori Kojaku, Yong-Yeol Ahn. *Science Advances* 12(14), eadx3420 (2026).
- https://doi.org/10.1126/sciadv.adx3420 | https://arxiv.org/abs/2502.16845 | https://github.com/yy/embedding-disruptiveness | https://munjungkim.github.io/embedding-disruptiveness-blog/

[[Disruption index]], [[Embedding disruptiveness measure]], [[Word2vec]], [[Validation sets]]

The paper this project builds on. It shows that the [[Disruption index]] is discrete, sensitive to single citations, degenerate, local, and, most importantly, gives conflicting scores to simultaneous discoveries (the Higgs mechanism papers of 1964 are the running example: one ranks near the top, the others near the bottom). It then proposes the [[Embedding disruptiveness measure]]: learn a past vector and a future vector per paper via directional random walks on the citation network with a skip-gram objective, and score disruptiveness as the cosine distance between them.

Data and validation: 23.7 million Web of Science papers (1960–2019), 327,021 APS physics papers, and 2.65 million U.S. patents (1976–2020). Ground truth for disruptive works: 302 Nobel Prize papers (1900–2016; physics, chemistry, medicine) and 278 APS editor-selected milestone papers; 56,243 government-funded patents on the patent side. A randomized null model preserves citation and reference counts but reshuffles links, to separate disruption from citation volume. The measure ranks Nobel and milestone papers consistently high, and pairs of contemporaneous papers with similar future vectors and high scores turn out to be simultaneous discoveries (Higgs mechanism, reverse transcriptase, charm quark, asymptotic freedom, and others).

Reading tips: the introduction is the best short review of the disruption literature; its references are listed in [[Reading list]]. The methods assume familiarity with [[Word2vec]].
