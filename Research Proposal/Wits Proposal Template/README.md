# Wits Proposal Template

A Wits rebuild of the **BITM LaTeX Proposal Template v4** from
[eduankotze/BITM](https://github.com/eduankotze/BITM/tree/master/latex),
used here as the structural ground truth for the research proposal.

The source is a University of the Free State template, from the Department of
Computer Science & Informatics. Its structure and typography are kept; the
branding and one methodology subsection are not.

## Build

Requires XeLaTeX, because the template sets system fonts (Arial).

```
tectonic -X compile proposal.tex     # or: xelatex proposal.tex
```

## Files

| File | Purpose |
|---|---|
| `proposal.tex` | The proposal itself: section skeleton with page budgets, pre-filled candidate details |
| `cover_and_title_pages.cls` | Cover page and formal title page |
| `proposal_template_style.sty` | Fonts, spacing, caption and list formatting |
| `template_images/` | Wits logo assets |
| `library.bib` | Bibliography (currently the template's sample; swap for `../../References.bib`) |

## What was kept from the source template

- The eighteen-section proposal structure, in order, with the per-section page
  budgets preserved as comments.
- Front matter: table of contents, list of figures, list of tables, list of
  abbreviations, glossary.
- Typography: 12pt Arial, A4, 2.5 cm margins, one-and-a-half spacing, no
  paragraph indent, justified text, APA citations via `apacite`, italic
  captions separated by two spaces.
- The two-cover-page arrangement: a designed cover followed by a formal title
  page.
- The convention of highlighting fields that still need editing.

## What was changed

**Branding.** The UFS cover artwork (`csi_cover.jpg`) is not reused. The cover
is drawn in TikZ from the official Wits palette, taken from the university's own
stylesheet at `wits.ac.za/media/wits-university-style-assets/css/redesign.css`:

| Colour | Hex | Use |
|---|---|---|
| Wits navy | `#003B5C` | Cover field, headings, links |
| Wits gold | `#FFA300` | Wedge, rules, accents |
| Wits blue | `#407EC9` | Secondary wedge |
| Wits maroon | `#9B2242` | Citation links |
| Wits teal | `#007377` | Available |
| Wits green | `#359946` | Available |

The logo is the official full-colour lockup from
`wits.ac.za/media/wits-university-style-assets/images/wits-logo.svg`, converted
to vector PDF. It sits on a white band so it needs no reversed variant. A
black-and-white crest is included for greyscale printing.

**Institution.** Department of Computer Science & Informatics, Faculty of
Natural and Agricultural Sciences, University of the Free State, Bloemfontein →
School of Statistics and Actuarial Science, Faculty of Science, University of
the Witwatersrand, Johannesburg.

**Section 9.7.** The source frames methodology through Saunders' research onion
and CRISP-DM, whose phases — Business Understanding through Deployment — fit
applied information-systems and data-science work. This proposal proves results
and then tests them, so 9.7 is restructured around the actual work phases: model
and observation map, identification analysis, hedging and the loss process,
finite-sample guarantees, simulation study, empirical evaluation. The deviation
is flagged in the document. Sections 9.1–9.6 are left in place; keep or drop the
research-onion framing according to what the supervisor expects.

**Degree wording.** "Proposal submitted in partial fulfilment" → "in
fulfilment", since a PhD by thesis is not partially fulfilled by coursework.
Check this against the School's own wording before submitting.

## Still to confirm

- Whether the School of Statistics and Actuarial Science has its own proposal
  template, which would supersede this one.
- The School's proposal length requirement. `STANDARD.md` records a Faculty
  guideline of about 3000 words, sourced to Proposal Form V4 2025 and FSO §8,
  which is far shorter than this template's eighteen sections imply.
- Whether a module code applies, as the source template expects one.
