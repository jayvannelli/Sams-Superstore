import streamlit as st
from src.data import get_superstore_sales_dataset


def display_kpis(data):
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("Total Sales ($)")
        st.write(f"${round(sum(data['Sales']), 2):,}")
    with c2:
        st.subheader("Quantity of Sales")
        st.write(f"{len(data):,}")
    with c3:
        st.subheader("Date Range")
        st.write(
            f"{data['Order Date'].min().strftime('%Y-%m-%d')} - {data['Order Date'].max().strftime('%Y-%m-%d')}"
        )


def main():
    st.title("Sales Overview")
    df = get_superstore_sales_dataset()
    display_kpis(df)

    st.write("---")


if __name__ == "__main__":
    main()
