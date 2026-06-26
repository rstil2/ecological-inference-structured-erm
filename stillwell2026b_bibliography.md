# Volume II — Literature bibliography guide

**BibTeX file:** [`stillwell2026b.bib`](stillwell2026b.bib)  
**Volume I shared entries:** [`../Project 42 - AI:ML/stillwell2026.bib`](../Project%2042%20-%20AI:ML/stillwell2026.bib) (Fisher, Vapnik, Mohri, Lande & Arnold, etc.)

---

## Outline checklist (required)

| Author(s) | BibTeX key | Primary use |
|-----------|------------|-------------|
| Grinnell | `grinnell1917`, `grinnell1924` | §4 Grinnellian niche / support |
| Hutchinson | `hutchinson1957` | §4 *n*-dimensional hypervolume |
| Araújo & Guisan | `araujo2006` | §2, §4 SDM pitfalls, transfer |
| Jetz | `jetzrahbek2002`, `jetz2007` | §2 macroecological prediction |
| Blackburn | `blackburn1999`, `blackburn2002` | §3 Bergmann / proxy program |
| Kingsolver & Huey | `kingsolver2008` | §3 cline reviews; §6 mechanism |
| Gelman & Hill | `gelman2007` | §2 hierarchical / nested units |
| Arjovsky (IRM) | `arjovsky2019` | §2, §4 invariant prediction |
| Koh et al. (WILDS) | `koh2021` | §2 OOD / distribution shift benchmark |

---

## Proposition → citation map

| Prop | Section | Core citations | Vignette / extension |
|------|---------|----------------|----------------------|
| **P1** Estimand–CV mismatch | §2 | `gelman2007`, `roberts2017`, `varoquaux2018`, `bengio2004` | `stillwell2026methods`, `stillwell2007` |
| **P2** Three estimands (E₁–E₃) | §2 | `roberts2017`, `koh2021`, `quinonero2009`, `shimodaira2000` | `jetz2007`, `araujo2006` |
| **P3** Gradient confounding | §3 | `dormann2013`, `blackburn1999`, `kingsolver2008` | `stillwell2007`, `stillwell2026methods` |
| **P4** Proxy rank reversal | §3 | `blackburn1999`, `shelomi2012`, `burnham2002`, `geirhos2020` | `stillwell2007` |
| **P5** Grinnellian support bound | §4 | `grinnell1917`, `hutchinson1957`, `hastie2009`, `ploton2020` | `araujo2006`, `muscarella2016` |
| **P6** Realized niche = hidden context | §4 | `elton1927`, `soberon2007`, `araujo2019`, `bendavid2010` | `stillwell2007`, `guisan2000` |
| **P7** Plasticity as label noise | §5 | `via1985`, `stillwell2010`, `gienapp2008`, `scheiner2002` | `lande2009`, `price2003` |
| **P8** Mechanism ⇒ interaction | §6 | `lande1983`, `kingsolver1991`, `kingsolver2012` | `stillwell2008`, `wade2014` |
| **P9** Two-test logic | §6 | `pearl2009`, `rubin1974`, `carroll2007` | `stillwell2007`, `stillwell2008` |
| **§7 Bridge** | §7 | `stillwell2026a` | `stillwell2016` (allometry modularity) |

---

## By paper section

### §1 Introduction
- `stillwell2026a` — Volume I backbone
- `stillwell2026b` — this manuscript
- `mohri2018`, `vapnik1998` — ERM / generalization (shared with Vol I)

### §2 Structured ERM
- **Hierarchy:** `gelman2007`, `legendre1993`
- **Spatial / group CV:** `roberts2017`, `ploton2020`, `muscarella2016`, `varoquaux2018`
- **Macroecology:** `jetzrahbek2002`, `jetz2007`, `guisan2000`, `araujo2006`
- **ML shift:** `koh2021`, `quinonero2009`, `shimodaira2000`, `bendavid2010`, `arjovsky2019`
- **Vignette:** `stillwell2007`, `stillwell2026methods`

### §3 Confounded gradients
- **Collinearity / proxies:** `dormann2013`, `blackburn1999`, `blackburn2002`, `shelomi2012`
- **Clines / thermal size:** `kingsolver2008`, `kingsolver2001`
- **Causal framing:** `pearl2009`, `rubin1974`
- **ML spurious features:** `geirhos2020`
- **Model selection:** `burnham2002`

### §4 Niche as support
- **Canon:** `grinnell1917`, `grinnell1924`, `hutchinson1957`, `elton1927`, `soberon2007`
- **SDM practice:** `guisan2000`, `peterson2011`, `araujo2006`, `araujo2019`, `synes2018`
- **Extrapolation:** `hastie2009`, `ploton2020`
- **Domain shift:** `scholkopf2021`, `muandet2013`, `gretton2009`

### §5 Plasticity
- `via1985`, `stillwell2010`, `gienapp2008`, `scheiner2002`, `lande2009`, `price2003`

### §6 Mechanism & interaction
- `lande1983`, `kingsolver1991`, `kingsolver2012`, `stillwell2008`, `carroll2007`, `wade2014`

### §8 Discussion (open problems)
- `roberts2017` — optimal block size
- `arjovsky2019`, `scholkopf2021` — invariant prediction under confounding
- `legendre1993` — connecting spatial GP to Fisher geometry (future work pointer)

### Optional (MTE / invariance box — not required)
- `brown2004`, `damuth1991`, `stillwell2016`

---

## Entry count

| Category | Keys |
|----------|------|
| Author vignettes | 6 |
| Ecology / macroecology | 28 |
| ML / statistics | 18 |
| Optional MTE | 2 |
| **Total in `stillwell2026b.bib`** | **~54** |

---

## LaTeX usage

```latex
\bibliographystyle{plainnat}  % or jmlr2e.bst when scaffold exists
\bibliography{stillwell2026b,stillwell2026}  % merge Vol I + II
```

Cross-reference Volume I without duplicating entries: `\citep{stillwell2026a}` from either bib file.

---

## Keys to verify before submission

Most entries are standard; double-check page ranges if your target venue’s copy-editor is strict:

- `kingsolver2008` — *Evolutionary Ecology Research* (no DOI in many indexes)
- `peterson2011` — Princeton Monographs (book entry)
- `stillwell2026methods` — update with JAE volume/pages when accepted

---

## Not included (cite from Vol I bib or add later)

| Topic | Suggested add |
|-------|----------------|
| Kawecki negative transfer | Project 48 bib when published |
| Fisher / PAC backbone | `stillwell2026.bib` |
| Phylogenetic comparative methods | `harmon2019` etc. if P1 extended to tree CV |
| Block spatial CV original | `roberts2017` sufficient; `blockCV` R package paper if needed |
