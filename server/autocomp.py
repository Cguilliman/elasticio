from elasticsearch_dsl import Q
from es import WordEs, init_connection


def autocomplete(search_term: str):
    query = WordEs.search()
    query = query.extra(
        track_scores=True,
        _source={"include": ["word"]}
    )
    if len(search_term) > 7:
        # {
        #   "query": {
        #     "match": {
        #       "word": {
        #         "query": search_term,
        #         "fuzziness": "AUTO",
        #         "max_expansions": 10
        #       }
        #     }
        #   }
        # }
        query = query.query(Q(
            name_or_query="match",
            word={"query": search_term, "fuzziness": "AUTO", "max_expansions": 10}
        ))
    else:
        # {
        #   "query": {
        #     "match": {
        #       "word": {
        #         "query": search_term,
        #         "fuzziness": 0,
        #         "prefix_length": 1,
        #         "max_expansions": 10
        #       }
        #     }
        #   }
        # }
        query = query.query(Q(
            name_or_query="match",
            word={"query": search_term, "fuzziness": 0, "prefix_length": 1, "max_expansions": 10}
        ))

    res = query.execute()
    for i in res.hits:
        print(i.word)


if __name__ == "__main__":
    init_connection()
    autocomplete("advirtisimint")
