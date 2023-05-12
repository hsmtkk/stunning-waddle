import json
import os

import requests


def lambda_handler(event, context):
    print(f"{event=}")
    print(f"{context=}")

    decoded = json.loads(event)
    keyword = decoded["keyword"]

    result = gourmet_search(keyword)

    return {
        "statusCode": 200,
        "body": json.dumps(result),
    }

GOURMET_SEARCH_URL = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"

def gourmet_search(keyword:str) -> dict:
    api_key = os.environ["GOURMET_SEARCH_API_KEY"]
    data = {
        "key": api_key,
        "keyword": keyword,
    }
    resp = requests.post(GOURMET_SEARCH_URL, data=data)
    if resp.status_code < 200 or resp.status_code >= 300:
        raise Exception(f"HTTP {resp.status_code}: {resp.text}")
    return resp.json()
