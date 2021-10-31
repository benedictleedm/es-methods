import json
from ssl import _create_unverified_context

from elasticsearch import Elasticsearch, helpers

from es_utils import prepare_search_request, prepare_delete_request

with open("config.json", "r") as f:
    config = json.load(f)

# ssl_context = _create_unverified_context(config["ssl_cert"])

# es = Elasticsearch(
#     hosts=[{"host": config["host"], "port": config["port"]}],
#     http_auth=(config["id"], config["key"]),
#     ssl_context=ssl_context,
# )

es = Elasticsearch(
    hosts=[{"host": config["host"], "port": config["port"]}],
)


def search(query, index_name=config["index_name"]):
    search_request = prepare_search_request(query)
    results = es.search(index=index_name, body=search_request, size=config["n_samples"])
    results["raw_query"], results["index"] = query, index_name
    return results


def delete(file_ids, index_name=config["index_name"]):
    delete_request = prepare_delete_request(file_ids)
    results = es.delete_by_query(index=index_name, body=delete_request)
    return results
