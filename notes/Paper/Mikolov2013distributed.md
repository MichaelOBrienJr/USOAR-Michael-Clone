---
title: 'Mikolov et al., Distributed Representations of Words and Phrases and their Compositionality'
date: 2026-09-02
updated: 2026-09-02
---

- Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S. Corrado, Jeff Dean. *Advances in Neural Information Processing Systems* 26 (NIPS 2013).
- https://proceedings.neurips.cc/paper_files/paper/2013/file/9aa42b31882ec039965f3c4923ce901b-Paper.pdf

[[Word2vec]]

The follow-up to [[Paper/Mikolov2013efficient]] that made skip-gram practical. Three contributions: subsampling frequent words (faster training, better vectors), negative sampling (a simplified variant of noise-contrastive estimation that replaces the hierarchical softmax and needs few negative examples per step), and a simple method for finding phrases such as "Air Canada" so that they get their own vectors. Negative sampling is the training objective behind the [[Embedding disruptiveness measure]]'s paper vectors.
