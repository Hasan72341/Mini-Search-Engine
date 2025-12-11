# build positional inverted index from documents

from collections import defaultdict
from core.tokenizer import tokenize


def build_index(read_documents_func, processed_path):
    # build positional inverted index

    index = defaultdict(lambda: defaultdict(list))
    doc_info = {}

    doc_id = 0

    for title, url, text in read_documents_func(processed_path):
        tokens = tokenize(title + " " + text)

        # store document metadata
        doc_info[doc_id] = {
            "title": title,
            "url": url,
            "text": text,
            "length": len(tokens)
        }

        # fill inverted index
        for position, word in tokens:
            index[word][doc_id].append(position)

        doc_id += 1

    return index, doc_info
