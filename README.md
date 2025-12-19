# Mini Search Engine (DSA-Focused)

A mini search engine built from scratch using core Data Structures and Algorithms.
The system indexes real Wikipedia articles and supports efficient keyword search
using a positional inverted index, sorted list intersection, TF-IDF ranking,
and proximity-based relevance scoring.

This project demonstrates algorithmic thinking, offline index construction,
and query-time efficiency — not web frameworks or libraries.

---

## Quick Start (Docker)

```bash
docker compose run --rm search-engine
```

This builds the image and starts interactive search. Requires pre-built index (see Data Setup).

---

## Core Ideas

The engine follows a classic two-phase search engine design:

1. **Offline Index Construction**
   - Stream documents from disk
   - Tokenize, normalize, and stem words
   - Build a positional inverted index

2. **Online Query Processing**
   - Tokenize query
   - Intersect posting lists using two pointers
   - Rank candidate documents using TF-IDF and proximity
   - Display ranked results with snippets and source links

---

## DSA Concepts Used

| Concept | File | Description |
|---------|------|-------------|
| Hash Map | `inverted_index.py` | Term → document postings lookup |
| Positional Inverted Index | `inverted_index.py` | Store word positions per document |
| Sorted List Intersection | `intersection.py` | Two-pointer AND query evaluation |
| Two-Pointer Technique | `proximity.py` | Minimum distance between term positions |
| TF-IDF Scoring | `ranking.py` | Term importance and rarity |
| Stemming | `tokenizer.py` | Porter stemmer for normalization |
| Sliding Window | `snippet.py` | Snippet extraction around matches |

---

## Features

- Indexes ~50,000 real Wikipedia articles
- Positional inverted index with word offsets
- Efficient AND queries using sorted list intersection
- TF-IDF ranking with proximity-based boost
- Snippet generation for result explanation
- Interactive CLI search
- Offline index persistence (pickle + JSON)

---

## Quick Start

```bash
# install
uv pip install -e .

# search (requires index)
python -m cli.search
```

---

## Example Query

```bash
python -m cli.search "linear algebra"
```

Sample output:

```
1. Lie algebra
   score  : 639.17
   link   : https://en.wikipedia.org/wiki/Lie_algebra
   snippet: In mathematics, a Lie algebra is a vector space together with a bilinear operation ...

2. Linear algebra
   score  : 434.09
   link   : https://en.wikipedia.org/wiki/Linear_algebra
   snippet: Linear algebra is the branch of mathematics concerning vector spaces and linear maps ...
```

Results are ranked by relevance, not exact title matching.

---

## Project Structure

```
core/                   # DSA algorithms
  tokenizer.py          # text normalization + stemming
  inverted_index.py     # positional index builder
  intersection.py       # sorted list intersection (two-pointer)
  proximity.py          # term distance scoring (two-pointer)
  ranking.py            # TF-IDF ranking
  snippet.py            # result snippets
  query.py              # query processing

cli/                    # command-line interface
  build_index.py        # offline index construction
  search.py             # interactive search

utils/
  io.py                 # disk I/O helpers

data/
  raw/                  # Wikipedia dump (not tracked)
  processed/            # extracted JSON articles

index/                  # serialized index files
  postings.pkl
  doc_map.json
  meta.json

tests/                  # unit tests
scripts/setup.sh        # data setup script
```

---

## Data Setup

Wikipedia data is not included due to size (~23GB compressed).

### Automatic setup

```bash
./scripts/setup.sh
```

This script:
1. Downloads the Wikipedia dump
2. Extracts 50,000 articles using WikiExtractor
3. Builds the inverted index

### Manual setup

```bash
# download dump
curl -L -o data/raw/enwiki-latest-pages-articles.xml.bz2 \
  https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2

# extract articles
python3 -m wikiextractor.wikiextractor.WikiExtractor \
  data/raw/enwiki-latest-pages-articles.xml.bz2 \
  -o data/processed \
  --processes 4 \
  --max-articles 50000 \
  --json

# build index
python -m cli.build_index
```

---

## Design Choices

- **CLI-first design** to emphasize algorithms over frameworks
- **Streaming document ingestion** to keep memory usage bounded
- **Pickle for posting lists** (fast, exact reconstruction)
- **JSON for metadata** (readable and debuggable)
- No databases, no search libraries, no ML frameworks

---

## Time Complexity Summary

| Operation | Complexity |
|-----------|------------|
| Index construction | O(total_tokens) |
| Query intersection | O(n1 + n2 + ...) |
| Proximity scoring | O(positions per term) |
| Ranking | O(k × q) for k docs, q terms |

---

## Tests

```bash
pytest
```

---

## Notes

This project intentionally avoids web frameworks and search libraries to
highlight fundamental data structures, algorithms, and information retrieval
principles.
