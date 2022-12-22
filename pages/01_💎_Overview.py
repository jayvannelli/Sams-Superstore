import streamlit as st
from src.data import get_superstore_sales_dataset


def display_kpis(data):
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write(f"Total Sales: ${round(sum(data['Sales']), 2):,}")
    with c2:
        st.write(f"Quantity of Sales: {len(data)}")
    #st.dataframe(data)


def main():
    st.title("Sales Overview")
    df = get_superstore_sales_dataset()
    display_kpis(df)


if __name__ == "__main__":
    main()
