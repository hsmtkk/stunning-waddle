import os
import requests
import streamlit as st

lambda_function_url = os.environ["LAMBDA_FUNCTION_URL"]
keyword = st.text_input(label="キーワード", value="魚のおいしい店")
data = {"keyword": keyword}
resp = requests.post(lambda_function_url, data=data)
if resp.status_code < 200 or resp.status_code >= 300:
    raise Exception(f"HTTP {resp.status_code}: {resp.text}")
st.write(resp.json())
