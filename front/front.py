import os

import pandas as pd
import requests
import streamlit as st

lambda_function_url = os.environ["LAMBDA_FUNCTION_URL"]

with st.form("gourmet"):
    keyword = st.text_input(label="キーワード", value="新宿")
    submitted = st.form_submit_button("送信")
    if submitted:
        data = {"keyword": keyword}
        resp = requests.post(lambda_function_url, json=data)
        if resp.status_code < 200 or resp.status_code >= 300:
            raise Exception(f"HTTP {resp.status_code}: {resp.text}")
        shops = resp.json()
        # st.write(shops)
        df = pd.DataFrame.from_dict(shops)
        st.dataframe(df)
        st.map(df)
