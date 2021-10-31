import json

config = json.load(open("config.json", "r"))


def prepare_search_request(query):
    search_request_body = {
        "query": {
            "match": {
                config["snippet_index"]: {
                    "query": query,
                    # "analyzer": config["snippet_analyzer"],
                }
            }
        }
    }
    return search_request_body


def prepare_delete_request(file_ids):
    delete_request_body = {
        "query": {
            "terms": {
                config["file_id_field"]: file_ids,
            }
        }
    }
    return delete_request_body


def prepare_index_request():

    return index_request_body
