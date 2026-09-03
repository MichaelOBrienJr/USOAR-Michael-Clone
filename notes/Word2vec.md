---
title: "Word2vec"
date: 2026-09-02
updated: 2026-09-02
---

A family of shallow neural models that learn a vector for each word from its neighbors in text, so that words used in similar contexts land near each other. Introduced by [[Paper/Mikolov2013efficient]] (CBOW and skip-gram architectures) and made practical by [[Paper/Mikolov2013distributed]] (negative sampling, subsampling of frequent words, phrase vectors).

Why it matters here: the [[Embedding disruptiveness measure]] treats random walks on the citation network as "sentences" and trains skip-gram on them, so the same machinery produces a vector per paper. Understanding skip-gram and negative sampling is enough to read the methods of [[Paper/Kim2026uncovering]].

## Explainers

- [The Illustrated Word2vec](https://jalammar.github.io/illustrated-word2vec/) by Jay Alammar (2019). Covers embeddings and cosine similarity, analogies, language modeling, the skip-gram architecture, negative sampling, the training loop, and the window-size and negative-sample hyperparameters. Start here.
