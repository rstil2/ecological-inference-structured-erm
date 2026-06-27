#!/usr/bin/env python3
"""Generate MEE ScholarOne-ready LaTeX from the main manuscript source."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "stillwell2026b_ecological_inference_structured_erm.tex"
OUT = ROOT / "submission" / "tex" / "stillwell2026b_mee_main.tex"

MEE_ABSTRACT = r"""Geographic models often fit latitude or climate strongly in sample, then
fail at withheld sites---a pattern now routine in continental mapping
\citep{ploton2020}.
\item Geographic surveys are nested empirical risk minimization problems; certifying
within-site interpolation as across-site transfer optimizes the wrong functional.
We unify ecological inference and domain-generalization learning under one geometry
and prove failure-mode theorems for estimand--CV mismatch, proxy rank reversal,
niche support, hidden context, and plasticity (proofs in Supporting Information).
\item Semi-synthetic simulation (500 replicates) yields 84\% disagreement between
strongest in-sample $|r|$ and leave-one-population-out ranking under a stated
generating process; a published beetle cline ($n=93$) shows the same qualitative
split (multivariate ecology LOPO RMSE 0.104 vs.\ temperature 0.112).
\item Claims about \emph{new sites} require population-level holdout
($\mathcal{E}_2$), not individual $k$-fold cross-validation.  Code and data for
peer review: \repoUrl{} (see REPRODUCE.md); Supporting Information contains full
proofs and supplementary tables."""

DATA_CODE_STATEMENT = r"""
\section*{Data and code for peer review}
Analysis code, simulation scripts, and reproduction instructions:
\repoUrl{} (\texttt{REPRODUCE.md}).  \emph{Stator limbatus} population-level
data are from Stillwell et al.\ \citep{stillwell2007}.  Full proofs and
supplementary tables are in the Supporting Information PDF.
"""


def strip_comments(text: str) -> str:
    return re.sub(r"(?m)^%.*$", "", text)


def extract_body(text: str) -> str:
    m = re.search(r"\\begin\{document\}(.*)\\end\{document\}", text, re.S)
    if not m:
        raise SystemExit("Could not find document body")
    return m.group(1)


def remove_block(text: str, pattern: str) -> str:
    return re.sub(pattern, "", text, flags=re.S)


def rename_section(text: str, old: str, new: str) -> str:
    return text.replace(old, new, 1)


def move_methods_before_results(body: str) -> str:
    methods = re.search(
        r"(\\section\{Methods\}.*?)(?=\\section\{Discussion\}|\\acks\{)",
        body,
        re.S,
    )
    if not methods:
        raise SystemExit("Methods section not found")
    methods_block = methods.group(1)
    body = body.replace(methods_block, "", 1)
    intro_end = re.search(r"(\\section\{Introduction.*?\n)(?=\\section\{Results\})", body, re.S)
    if not intro_end:
        raise SystemExit("Introduction/Results boundary not found")
    insert_at = intro_end.end(1)
    return body[:insert_at] + methods_block + body[insert_at:]


def anonymize_captions(body: str) -> str:
    body = body.replace("author reanalysis of the published survey", "reanalysis of the published survey")
    body = body.replace("Stillwell et al.\\ \\citep{stillwell2007}", "the published survey \\citep{stillwell2007}")
    return body


def build() -> None:
    raw = SRC.read_text()
    body = extract_body(raw)

    body = remove_block(body, r"\\editor\{.*?\}\s*")
    body = remove_block(body, r"\\author\{.*?\}\s*")
    body = remove_block(body, r"\\begin\{keywords\}.*?\\end\{keywords\}\s*")
    body = remove_block(body, r"\\section\*\{Media summary\}.*?(?=\\section\{Introduction)")
    body = remove_block(body, r"\\acks\{.*?\}\s*")

    body = re.sub(
        r"\\begin\{abstract\}%.*?\\end\{abstract\}",
        (
            "\\begin{abstract}\n"
            "\\begin{enumerate}\n"
            + MEE_ABSTRACT
            + "\n\\end{enumerate}\n\\end{abstract}\n"
            + DATA_CODE_STATEMENT
            + "\n\\begin{keywords}\n"
            "  Bergmann's rule, cross-validation, domain generalization, empirical risk minimization,\n"
            "  macroecology, niche theory, species distribution models\n"
            "\\end{keywords}\n"
        ),
        body,
        flags=re.S,
    )

    body = rename_section(body, "\\section{Methods}", "\\section{Materials and Methods}")
    body = move_methods_before_results(body)
    body = anonymize_captions(body)

    preamble = r"""\documentclass[11pt]{article}

\usepackage[nolinenumbers]{interface_submission}

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
