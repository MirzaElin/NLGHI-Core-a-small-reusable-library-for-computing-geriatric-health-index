---
title: "NLGHI Core: a small, reusable library for computing geriatric health index"
tags:
  - public health
  - geriatrics
  - Python
authors:
  - name: Mirza Niaz Zaman Elin
    ORCID ID: https://orcid.org/0000-0001-9577-7821
    affiliation: 1
affiliations:
  - name: AMAL Youth & Family Centre, St. John's, NL, Canada
    index: 1
date: 2025-09-05
bibliography: paper.bib
---

# Summary

The Newfoundland & Labrador Geriatric Health Index (NLGHI) converts the traditionally narrative Comprehensive Geriatric Assessment (CGA) into a quantitative, longitudinal measure aligned with the World Health Organization’s (WHO) holistic definition of health. The software provides a PyQt5 desktop interface for entering per-domain impairment ratings (fixed 0–5 scale), automatically computing domain-specific aggregate values (DSAVs = rating × domain weight) and an overall Geriatric Health Index (GHI = ΣDSAV/27). Built-in charts visualize GHI trajectories and DSAV heatmaps across visits; a patient workspace supports clinical notes, history, symptom snapshots, follow-ups, attachments, and reports. The design preserves clinical nuance while enabling early signal detection, standardized comparison across services, and reproducible analytics for clinical and public health research [@palmer2018cga; @um2022cga].


Geriatric and community clinics and research centres that focus on geriatric health often capture structured impairment severity across multiple domains and need a transparent, "scriptable" tool—rather than a GUI‑only app—to compute a consistent composite index and integrate it into automated workflows. NLGHI Core provides a small, dependency‑light library with tests and examples to meet this need. By shipping as a Python library that depends on the scientific Python ecosystem [@Harris2020; @McKinney2010], the index can be embedded into notebooks and pipelines.

# Functionality

Given a unlimited‑length vector of impairment scores (0–5) and a N‑length vector of domain weights, the library computes:

- DSAV per domain = impairment × weight
- NLGHI (GHI) = sum(DSAV) ÷ N

The default domain list and weights mirror the original app configuration. This design follows common practice for composite indicators [@Nardo2005] and is conceptually aligned with simple burden‑style accounting (years × weights) seen in public‑health summaries [@MurrayLopez1996].

# Quality control

The package includes unit tests that verify the formula (including edge cases) and a small CLI test that reads/writes a JSON store for time‑series summaries. Continuous integration runs tests on push/PR. Examples are provided for quick CLI trials.

# State of the field

NLGHI Core aims for pragmatic reuse and transparency rather than novel methodology. It complements broader epidemiological toolkits by packaging a concrete composite‑index computation with a uniform API and CLI.

# Acknowledgements

We thank the maintainers of NumPy and pandas for the scientific Python ecosystem that enables this work.

# Conflict of interest

The author declares no competing interests.
