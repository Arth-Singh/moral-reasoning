# Reference Verification

Checked `custom.bib` against the Semantic Scholar Graph API by title search.

- Date checked: 2026-05-03
- Scope: all 36 BibTeX entries in `custom.bib`
- Fields checked: title, author list/order where available, venue, and year
- Result: all titles matched exactly after normalization; no missing BibTeX entries were found.

Corrections applied:

- `wen2025dija`: corrected author list to match Semantic Scholar.
- `zhang2025pad`: corrected `Chen, Hao` to `Chen, Haopeng`.
- `li2025diffuguard`: corrected author order.
- `he2026fragileguardrail`: corrected `He, Zeyuan` to `He, Zeyu`.
- `llada15_2025`: corrected `Wang, Rongzhen` to `Wang, Rongzheng`.
- `meta2024llama3`: corrected first authors and order.
- `li2025earlycommit`: added missing `Liang, Yi`.
- `mercury2026`: removed non-paper organization author from the author list.
- `cardei2025cdd`: corrected author order.
- `shah2024decoupled`: corrected `Yan, Mingyuan` to `Yan, Ming`.

Year notes:

Some Semantic Scholar records use the initial arXiv year while the BibTeX uses the venue year. Those were left unchanged when the entry cites a venue publication, e.g. ICML/ICLR/SaTML/TMLR/EMNLP records.
