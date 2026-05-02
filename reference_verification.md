# Reference Verification

Checked `custom.bib` against the Semantic Scholar Graph API by title search, then
verified title, author list/order, venue, and year for each matched record.

- Date checked: 2026-05-03
- Scope: all 36 BibTeX entries in `custom.bib`
- Fields checked: title, author list/order, venue, and year
- Result: all titles matched exactly after normalization; no missing BibTeX entries were found.
- Author result: all entries match Semantic Scholar after allowing normal initial/full-name abbreviation, except `zou2023gcg`, where Semantic Scholar omits two arXiv authors; the fuller six-author BibTeX list was kept and verified against arXiv `2307.15043`.
- Year result: all arXiv-only entries match Semantic Scholar year. Venue entries keep the conference/journal publication year when Semantic Scholar reports the earlier arXiv upload year.

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

Semantic Scholar reports the initial arXiv year for several entries whose BibTeX
is intentionally citing the later venue publication. These venue-year entries
were left unchanged:

- `lou2024mdlm`: ICML 2024, Semantic Scholar year 2023 from arXiv.
- `liu2024autodan`: ICLR 2024, Semantic Scholar year 2023 from arXiv.
- `chao2025pair`: SaTML 2025, Semantic Scholar year 2023 from arXiv.
- `song2021scorebased`: ICLR 2021, Semantic Scholar year 2020 from arXiv.
- `jang2017gumbel`: ICLR 2017, Semantic Scholar year 2016 from arXiv.
- `maddison2017concrete`: ICLR 2017, Semantic Scholar year 2016 from arXiv.
- `robey2024smoothllm`: TMLR 2025, Semantic Scholar year 2023 from arXiv.
- `xie2026mosa`: AAAI 2026, Semantic Scholar year 2025 from arXiv.
- `wang2025diffusionattacker`: EMNLP 2025, Semantic Scholar year 2024 from arXiv.

Two entries cite announced 2026 conference versions while Semantic Scholar
currently indexes the arXiv record as 2025:

- `yamabe2026priming`: ICLR 2026 note, Semantic Scholar year 2025 from arXiv.
- `jeung2026a2d`: ICLR 2026 entry, Semantic Scholar year 2025 from arXiv.
