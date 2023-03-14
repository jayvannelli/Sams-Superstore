import streamlit as st

from src.data import get_superstore_sales_dataset
from streamlit_extras.dataframe_explorer import dataframe_explorer


def main():
    st.set_page_config(page_title="Streamlit Superstore Dashboard",
                       page_icon="🛒",
                       layout="wide")

    st.title("Sam's Superstore | Sales Dashboard | Streamlit | Kaggle")
    st.image("images/acsi-supermarket-industry-scaled.jpg")

    st.subheader("Link to full Kaggle listing & dataset")
    st.write("https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting?resource=download")

    st.write("---")

    st.subheader("DataFrame Explorer")
    df = get_superstore_sales_dataset()

    filtered_df = dataframe_explorer(df)
    st.dataframe(filtered_df, use_container_width=True)


if __name__ == "__main__":
    main()
