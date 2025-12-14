# build index and save to disk (DSA style, simple)

from pathlib import Path


from utils.io import read_documents, save_pickle, save_json
from core.inverted_index import build_index


def build():
    processed_path = "data/processed"
    index_path = "index"

    print("Starting index build...")

    # build index in memory
    index, doc_info = build_index(read_documents, processed_path)

    print("Saving index to disk...")

    # convert defaultdict -> dict for safe serialization
    index_clean = {
        term: dict(doc_postings)
        for term, doc_postings in index.items()
    }

    save_pickle(index_clean, f"{index_path}/postings.pkl")
    save_json(doc_info, f"{index_path}/doc_map.json")
    save_json(
        {
            "total_docs": len(doc_info),
            "total_terms": len(index_clean)
        },
        f"{index_path}/meta.json"
    )

    print("Index build finished ✅")
    print("Total documents:", len(doc_info))
    print("Total terms:", len(index_clean))


if __name__ == "__main__":
    build()
