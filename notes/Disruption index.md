---
title: "Disruption index (CD index)"
date: 2026-09-02
updated: 2026-09-02
---

A citation-based measure of whether a work consolidates or disrupts what came before, introduced for patents by [[Paper/Funk2016dynamic]] and popularized for science by [[Paper/Wu2019largeteams]] and [[Paper/Park2023papers]].

For a focal document $f$, $$CD(f) = \frac{n_i(f) - n_j(f)}{n_i(f) + n_j(f) + n_k(f)},$$ where $n_i(f)$ is the number of documents that cite $f$ but none of $f$'s references, $n_j(f)$ is the number that cite $f$ *and* some of $f$'s references, and $n_k(f)$ is the number that cite some of $f$'s references but not $f$. The index ranges from $-1$ (maximally consolidating) to $+1$ (maximally destabilizing/disruptive). Funk and Owen-Smith call it $CD_t$, with $t$ the citation window (commonly five years, $CD_5$), and also define a magnitude-weighted $mCD_t$.

[[Paper/Kim2026uncovering]] argues the index is fragile: it is discrete and sensitive to single citations, degenerate (different topologies give the same value), local (sees only the immediate citation neighborhood), and breaks on simultaneous discoveries, where twin papers citing each other flip from maximally to minimally disruptive. Their [[Embedding disruptiveness measure]] is the continuous replacement this project builds on.

## Implementations

- https://gist.github.com/skojaku/cee26755645b133a69d6630c79307cde
- https://github.com/yy/embedding-disruptiveness/blob/main/workflow/embedding_computation/scripts/Distance_disruption.py
