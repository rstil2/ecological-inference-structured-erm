#!/usr/bin/env python3
"""Generate pandoc-friendly LaTeX for Interface ScholarOne (.docx upload)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "stillwell2026b_ecological_inference_structured_erm.tex"
OUT = ROOT / "submission" / "interface" / "tex" / "stillwell2026b_interface_main.tex"
REPO = r"https://github.com/rstil2/ecological-inference-structured-erm"

INTERFACE_ABSTRACT = r"""Geographic models often fit latitude or climate strongly in sample, then
fail at withheld sites---a pattern now routine in continental mapping studies.
We show that the failure is estimand mismatch, not model pathology: nested
surveys are empirical risk minimization on \emph{structured} data, and
certifying within-site interpolation as across-site transfer optimizes the
wrong functional.  Ecological inference and domain-generalization learning are
therefore one geometry---ERM under nested units, confounded gradients, and
niche support---the spatial counterpart to temporal learning in a companion
preprint on selection as ERM across generations.  Semi-synthetic simulation
(500 replicates; electronic supplementary material) yields 84\% disagreement
between strongest in-sample $|r|$ and leave-one-population-out ranking under
a stated generating process---a design-specific rate, not an ecological law.
A published beetle cline (\emph{Stator limbatus}; $n=93$) exhibits the same
qualitative split: multivariate ecology wins on holdout (LOPO RMSE 0.104
vs.\ 0.112) while proxy correlates dominate in sample.  The practical rule is
explicit: claims about \emph{new sites} require population-level holdout
($\mathcal{E}_2$), not individual $k$-fold CV.  Proofs and supplementary
tables are in the electronic supplementary material."""

ACKS_SECTION = rf"""
\section*{{Acknowledgments and disclosure}}

\textbf{{Funding:}} No external funding was received.

\textbf{{Competing Interests:}} None declared.

\textbf{{Use of AI:}} During manuscript preparation (2026), the author used
Cursor with large-language-model assistance to edit prose for readability,
format \\LaTeX{{}}, and draft reproducible analysis scripts.  No AI tool was
listed as an author.  The author reviewed and verified all scientific
statements, formal results, empirical analyses, figures, tables, and
references.

\textbf{{Data and code:}} \emph{{Stator}} data from Stillwell et al.\ (2007).
Analysis code and simulation scripts: \url{{{REPO}}} (REPRODUCE.md).
Supplementary tables and full proofs: electronic supplementary material (ESM).
"""


def extract_body(text: str) -> str:
    m = re.search(r"\\begin\{document\}(.*)\\end\{document\}", text, re.S)
    if not m:
        raise SystemExit("Could not find document body")
    return m.group(1)


def remove_braced_command(body: str, command: str) -> str:
    needle = f"\\{command}" + "{"
    idx = body.find(needle)
    if idx == -1:
        return body
    start = idx + len(needle)
    depth = 1
    i = start
    while i < len(body) and depth:
        ch = body[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        i += 1
    return body[:idx] + body[i:]


def apply_macros(body: str) -> str:
    reps = [
        (r"\\Rkfold\(([^)]*)\)", r"$\\hat{R}^{\\mathrm{kfold}}(\1)$"),
        (r"\\RLOPO\(([^)]*)\)", r"$\\hat{R}^{\\mathrm{LOPO}}(\1)$"),
        (r"\\Eone\b", r"$\\mathcal{E}_1$"),
        (r"\\Etwo\b", r"$\\mathcal{E}_2$"),
        (r"\\Ethree\b", r"$\\mathcal{E}_3$"),
        (r"\\repoUrl\{\}", rf"\\url{{{REPO}}}"),
        (r"\\supp\b", r"\\operatorname{supp}"),
    ]
    for pat, repl in reps:
        body = re.sub(pat, repl, body)
    return body


def build() -> None:
    raw = SRC.read_text()
    body = extract_body(raw)

    new_abstract = "\\begin{abstract}\n" + INTERFACE_ABSTRACT + "\n\\end{abstract}\n"
    body = re.sub(
        r"\\begin\{abstract\}%.*?\\end\{abstract\}",
        lambda _m: new_abstract,
        body,
        flags=re.S,
    )

    body = remove_braced_command(body, "acks")
    body = apply_macros(body)
    body = remove_braced_command(body, "bibliography")
    body = body.rstrip() + "\n" + ACKS_SECTION + "\n"

    preamble = r"""\documentclass[11pt]{article}
\usepackage[nolinenumbers]{interface_submission}
\usepackage{url}

\begin{document}

"""
    footer = r"""
\bibliography{stillwell2026b}

\end{document}
"""

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(preamble + body + footer)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
