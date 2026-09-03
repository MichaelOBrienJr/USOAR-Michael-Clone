---
title: "USOAR contract: Geoffrey"
date: 2026-09-02
updated: 2026-09-02
---

Text filled into the USOAR Mentor-Mentee Contract (Google Drive, `2627_USOAR Mentor-Mentee Contract ... Geoffrey Lin.pdf`) on 2026-09-02. Geoffrey's slice: computing the [[Embedding disruptiveness measure]] on multiple datasets and comparing domains. Michael's slice (data collection, [[Validation sets]]) is in [[USOAR contract Michael]]. Set on the form: weekly 1:1 (day and time still blank), 3c Verbal, 4 Zoom or face-to-face.

## 1. Our major goals

**a. Proposed research project goals.** Compute an embedding-based disruption measure (EDM) on several datasets and compare what disruption looks like across domains. Start by reproducing the published measure on scientific papers, then run it on U.S. patents and case law as those datasets become available, validate it against curated lists of landmark works, and produce reproducible code, figures, and a written comparison across domains.

**b. USOAR Mentee's expectations.** Left blank for the student to write.

**c. Faculty Mentor's expectations.** Take ownership of the project: be a voracious reader and learner, come up with your own ideas, question the plan and the data rather than just following instructions. Prepare either written updates or slides for each meeting. Ask for help when stuck. Attend the weekly lab meeting if possible.

## 3. Meeting preparation

**a. Mentee will:** send a short written update the day before (what was done, what is blocked, questions), with links to the relevant notebook, figures, or results.

**b. Mentor will:** read the update, review any code or results shared, and bring suggestions and next steps.

## 6. Methods the mentor will train the mentee to use

1. Python data wrangling with pandas and DuckDB on large citation datasets (hands-on, first month).
2. Git and the lab's reproducible project workflow, including Snakemake pipelines (hands-on at onboarding, then through code review).
3. Text and network embeddings: word2vec/skip-gram and the embedding-disruptiveness package (readings, then a guided walkthrough of the code).
4. Evaluating a measure against ground-truth lists (ranking metrics, null models, and plots), taught as the first results come in.
5. Presenting research results at lab meeting (practice runs before each talk).

## 7. Procedural notes on collecting and organizing data

Raw data go under `data/raw/` untouched and cleaned tables under `data/derived/`, produced by scripts, never by hand edits. Computed measures and figures go under `results/` with the script that made them. Notebooks are timestamped (`YYYYMMDD_description`); reusable code moves into `src/`.

## 8. If the mentee gets stuck

Try for an hour, then write down what was tried. Message the mentor on the lab chat or by email; if unresolved within two days, bring it to the next meeting or ask for an extra one. Lab members at the weekly meeting are a second resource.

## 9. Other

A companion USOAR project (Michael O'Brien) collects the validation and domain datasets this analysis runs on, so the two students will coordinate on data formats. Authorship on any resulting paper follows standard norms based on contribution.
