# query processing logic

from core.tokenizer import tokenize
from core.intersection import intersect_many_lists
from core.proximity import proximity_score
from core.ranking import rank_documents


def process_query(query, index, doc_info):
# Process search query and return ranked documents.

    # tokenize query
    query_tokens = tokenize(query)
    query_terms = [word for _, word in query_tokens]

    if not query_terms:
        return []

    # fetch posting lists
    posting_lists = []
    for term in query_terms:
        if term not in index:
            return []
        posting_lists.append(sorted(index[term].keys()))

    # intersect doc_ids
    candidate_docs = intersect_many_lists(posting_lists)

    if not candidate_docs:
        return []

    # compute proximity for each candidate doc
    proximity_scores = {}

    for doc_id in candidate_docs:
        position_lists = []
        for term in query_terms:
            position_lists.append(index[term][doc_id])

        proximity_scores[doc_id] = proximity_score(position_lists)

    # rank documents
    ranked = rank_documents(
        query_terms,
        candidate_docs,
        index,
        doc_info,
        proximity_scores
    )

    return ranked
