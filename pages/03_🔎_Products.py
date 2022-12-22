import streamlit as st
from src.data import get_superstore_sales_dataset


def main():
    st.title("Product Breakdown")
    st.write("---")

    df = get_superstore_sales_dataset()

    c1, c2 = st.columns([2, 4])
    with c1:
        st.subheader("By Category")
        st.bar_chart(df, x="Category", y="Sales")
    with c2:
        st.subheader("By Sub-Category")
        st.bar_chart(df, x="Sub-Category", y="Sales")

    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("Furniture"):
            furniture = df.loc[df["Category"] == "Furniture"]
            furniture_items = list(furniture["Sub-Category"].unique())
            st.write(furniture_items)

    with col2:
        with st.expander("Office Supplies"):
            office_supplies = df.loc[df["Category"] == "Office Supplies"]
            office_supplies_items = list(office_supplies["Sub-Category"].unique())
            st.write(office_supplies_items)

    with col3:
        with st.expander("Technology"):
            technology = df.loc[df["Category"] == "Technology"]
            technology_items = list(technology["Sub-Category"].unique())
            st.write(technology_items)

    st.write("---")

    product = st.selectbox("Select product:", options=df["Sub-Category"].unique())
    product_df = df.loc[df["Sub-Category"] == product]

    st.bar_chart(product_df, x="Order Date", y="Sales")


if __name__ == "__main__":
    main()
