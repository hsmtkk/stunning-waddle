import json
import os

import requests


def lambda_handler(event, context):
    print(f"{event=}")
    print(f"{context=}")

    body = json.loads(event["body"])
    keyword = body["keyword"]
    result = gourmet_search(keyword)

    return {
        "statusCode": 200,
        "body": json.dumps(result),
    }

GOURMET_SEARCH_URL = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"

def gourmet_search(keyword:str) -> dict:
    api_key = os.environ["GOURMET_SEARCH_API_KEY"]
    params = {
        "key": api_key,
        "keyword": keyword,
        "format": "json",
    }
    resp = requests.get(GOURMET_SEARCH_URL, params=params)
    if resp.status_code < 200 or resp.status_code >= 300:
        raise Exception(f"HTTP {resp.status_code}: {resp.text}")
    resp_dict = resp.json()
    results = list()
    for shop in resp_dict["results"]["shop"]:
        results.append({
            "name": shop["name"],
            "lat": shop["lat"],
            "lon": shop["lng"],
        })
    return results