import streamlit as st
import pandas as pd
from datetime import datetime


@st.cache
def get_superstore_sales_dataset():
    d_parser = lambda x: datetime.strptime(x, "%d/%m/%Y")
    _df = pd.read_csv(
        "data/train.csv", parse_dates=['Order Date', 'Ship Date'], date_parser=d_parser
    ).drop(columns="Row ID")
    return _df
