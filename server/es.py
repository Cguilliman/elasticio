from elasticsearch_dsl import Document, Keyword, Text, connections, Q


class WordEs(Document):
    word = Text(fields={"keyword": Keyword()}, required=True)

    class Index:
        name = "words-01"
        settings = {
            "number_of_shards": 2,
            "analysis": {
                "analyzer": {
                    "autocomplete_analyzer": {
                        "tokenizer": "autocomplete_tokenizer"
                    }
                },
                "tokenizer": {
                    "autocomplete_tokenizer": {
                        "type": "ngram",
                        "token_chars": [
                            "letter",
                            "digit"
                        ]
                    }
                }
            }
        }
        mappings = {
            "properties": {
                "word": {
                    "type": "text",
                    "analyzer": "autocomplete_analyzer",
                    "search_analyzer": "standard"
                }
            }
        }


def init_connection():
    connections.create_connection(hosts=["http://localhost:9200"])
    es = connections.get_connection()
    if not es.indices.exists(index=WordEs.Index.name):
        WordEs.init()
