import streamlit as st

from src.data import get_superstore_sales_dataset
from streamlit_extras.dataframe_explorer import dataframe_explorer


def main():
    st.set_page_config(page_title="Streamlit Superstore Dashboard",
                       page_icon=":shopping_trolley:")

    st.title("Sam's Superstore | Sales Dashboard")
    st.write("""
        Hello! This application is built using data from Kaggle 
        (link to listing & dataset below) and showcases some of 
        the many things possible with streamlit.
    """)
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
