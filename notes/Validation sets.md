---
title: "Validation sets"
date: 2026-09-02
updated: 2026-09-02
---

Idea: assemble externally labeled "landmark" works across domains (science, patents, law, people) to validate disruption/consolidation measures ([[Disruption index]], [[Embedding disruptiveness measure]], and relatives). Status: promising starting point; needs more investigation before committing to a specific list.

## Science

- **Nobel-prize-winning papers.** Li, Yin, Fortunato, Wang (2019), *Sci Data*, "A dataset of publication records for Nobel laureates." Flags the prize-winning papers. Standard CD-index validation set ([[Paper/Wu2019largeteams|Wu, Wang, Evans 2019]]; [[Paper/Park2023papers|Park, Leahey, Funk 2023]]). [[Paper/Kim2026uncovering|Kim et al. (2026)]] use 302 Nobel papers (1900–2016, physics/chemistry/medicine).
- **APS PRL Milestones.** 50th-anniversary editor-picked letters, 1958–2001. Also PRL 25 Milestones and Physical Review Focus landmarks. [[Paper/Kim2026uncovering|Kim et al. (2026)]] use 278 APS editor-selected milestone papers.
- **Nature Milestones series.** Per-field timelines, curated by editors.
- **Wikipedia "List of important publications in …"** (physics, mathematics, CS, biology, …). Broad, crowd-curated; weaker but cheap.
- **Garfield's Citation Classics.** Author commentaries; consolidating vs. disruptive not labeled.

## Patents

- **National Inventors Hall of Fame.** Each inductee tied to specific patent numbers. Starting point: <https://en.wikipedia.org/wiki/List_of_National_Inventors_Hall_of_Fame_inductees>
- **Kelly, Papanikolaou, Seru, Taddy (2021), *AER: Insights*.** Breakthrough-patent validation, drawn from Wikipedia/Britannica invention timelines. Their list is public with the paper.
- [[Paper/Funk2016dynamic|Funk & Owen-Smith (2017)]] used similar "great inventions" lists for CD-index validation.

## Law

- **Wikipedia "List of landmark court decisions in the United States."** Largest, categorized.
- **LII (Cornell) "Historic Supreme Court Decisions"; Oxford Guide to US Supreme Court Decisions.** Fowler et al. (2007, 2008) used such lists to validate citation-network authority measures.
- **Decisions overruled.** <https://constitution.congress.gov/resources/decisions-overruled/> — Supreme Court decisions overruled by later decisions. A natural "disruption" signal: the overruling case displaces its predecessor.
- **Full text / metadata.** Oyez, Justia for case pages; CourtListener or Caselaw Access Project for full text.

## People

- Same Nobel dataset for people-level validation. Control group: matched high-productivity non-laureates.

## First student task

Consolidate these into one labeled sheet (work, domain, identifier, source list), paired with a **consolidating control set** (e.g., review articles, textbook-standard methods papers) so the validation is not disruptive-only.
