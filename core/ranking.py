# rank documents using tf-idf and proximity
import math


def tf(term_freq):
    return term_freq


def idf(total_docs, doc_freq):
    # inverse document frequency
    return math.log((total_docs + 1) / (doc_freq + 1)) + 1


def tf_idf(term_freq, total_docs, doc_freq):
    return tf(term_freq) * idf(total_docs, doc_freq)


def rank_documents(
    query_terms,
    candidate_docs,
    index,
    doc_info,
    proximity_scores
):
    # rank docs by score

    scores = {}

    total_docs = len(doc_info)

    for doc_id in candidate_docs:
        score = 0.0

        for term in query_terms:
            postings = index.get(term, {})
            if doc_id not in postings:
                continue

            term_freq = len(postings[doc_id])
            doc_freq = len(postings)

            score += tf_idf(term_freq, total_docs, doc_freq)

        # proximity boost (smaller distance → higher boost)
        prox = proximity_scores.get(doc_id, 0)
        proximity_boost = 1 / (1 + prox)

        scores[doc_id] = score * proximity_boost

    # sort documents by score (descending)
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked
