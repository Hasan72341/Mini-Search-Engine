# command line search interface

from utils.io import load_pickle, load_json
from core.query import process_query
from core.snippet import get_snippet
from core.tokenizer import tokenize
import sys


def run_query(query, index, doc_info):
    # run single search query

    print(f"\nSearching for: \"{query}\"")
    print("-" * 60)

    results = process_query(query, index, doc_info)

    if not results:
        print("No results found.")
        return

    query_terms = [w for _, w in tokenize(query)]

    # show top 10
    for rank, (doc_id, score) in enumerate(results[:10], start=1):
        doc = doc_info[str(doc_id)]
        title = doc["title"]
        url = doc.get("url", "")
        text = doc.get("text", "")

        # gather all positions for query terms
        positions = []
        for term in query_terms:
            if term in index and doc_id in index[term]:
                positions.extend(index[term][doc_id])

        snippet = get_snippet(text, sorted(positions))

        print(f"{rank}. {title}")
        print(f"   score  : {score:.4f}")
        if url:
            print(f"   link   : {url}")
        if snippet:
            print(f"   snippet: {snippet}")
        print()


def search():
    # single query mode
    if len(sys.argv) >= 2:
        index = load_pickle("index/postings.pkl")
        doc_info = load_json("index/doc_map.json")
        run_query(sys.argv[1], index, doc_info)
        return

    # interactive mode
    print("Mini Search Engine")
    print("Type 'quit' or 'exit' to stop\n")

    print("Loading index...")
    index = load_pickle("index/postings.pkl")
    doc_info = load_json("index/doc_map.json")
    print(f"Loaded {len(doc_info)} documents, {len(index)} terms\n")

    while True:
        try:
            query = input("search> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not query:
            continue

        if query.lower() in ("quit", "exit", "q"):
            print("Bye!")
            break

        run_query(query, index, doc_info)


if __name__ == "__main__":
    search()
