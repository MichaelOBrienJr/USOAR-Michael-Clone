---
title: "Embedding disruptiveness measure"
date: 2026-09-02
updated: 2026-09-02
---

A continuous, embedding-based alternative to the [[Disruption index]], proposed in [[Paper/Kim2026uncovering]]. This project extends it to new domains (patents, law) and scales (people).

Each paper $i$ gets two vectors learned from the citation network: a past vector $\mathbf{p}_i$ representing the papers it cites, and a future vector $\mathbf{f}_i$ representing the papers that cite it. The vectors come from directional random walks on the citation network trained with a skip-gram objective (see [[Word2vec]]). Disruptiveness is the cosine distance between the two: $$\Delta_i = 1 - \frac{\mathbf{f}_i \cdot \mathbf{p}_i}{\|\mathbf{f}_i\| \, \|\mathbf{p}_i\|}.$$ A large distance means the paper's descendants depend little on its antecedents, i.e., the paper redirected the field.

Because future vectors summarize how a paper is used later, two contemporaneous papers with very similar future vectors and high disruptiveness are candidate simultaneous discoveries, which the CD index cannot see.

- Code: https://github.com/yy/embedding-disruptiveness
- PyPI: https://pypi.org/project/embedding-disruptiveness/
- Blog walkthrough by Munjung Kim: https://munjungkim.github.io/embedding-disruptiveness-blog/
