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

NLGHI Core is a small, reusable Python library—with a companion command-line interface—for computing the Newfoundland & Labrador Geriatric Health Index (NLGHI) from structured clinical inputs. The package takes a 27-item vector of domain impairment scores (each in 
[
0
,
5
]
[0,5]) and a matching weight vector, computes domain contributions 
D
S
A
V
𝑖
=
𝑥
𝑖
𝑤
𝑖
DSAV
i
	​

=x
i
	​

w
i
	​

, and returns the overall index 
G
H
I
=
1
27
∑
𝑖
=
1
27
D
S
A
V
𝑖
GHI=
27
1
	​

∑
i=1
27
	​

DSAV
i
	​

. To support transparent, reproducible research, the computation is delivered as an importable library (no GUI), with a simple CLI for batch use, examples for quick trials, and lightweight utilities to write/read patient-level time series as JSON. The implementation is dependency-light (NumPy/pandas), packaged under an OSI-approved license, and includes unit tests and GitHub Actions CI to encourage reliability, sustainability, and reuse in notebooks and pipelines.

# Statement of need

Geriatric and community clinics often capture structured impairment severity across multiple domains and need a transparent, "scriptable" tool—rather than a GUI‑only app—to compute a consistent composite index and integrate it into automated workflows. NLGHI Core provides a small, dependency‑light library with tests and examples to meet this need. By shipping as a Python library that depends on the scientific Python ecosystem [@Harris2020; @McKinney2010], the index can be embedded into notebooks and pipelines.

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
