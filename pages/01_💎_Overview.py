import streamlit as st
from src.data import get_superstore_sales_dataset


def display_kpis(data):
    c1, c2, c3 = st.columns(3)
    total_sales = round(sum(data['Sales']), 2)
    items_sold = len(data)
    unique_orders = len(data['Order ID'].unique())

    with c1:
        st.subheader("Sales ($)")
        st.write(f"Total: ${total_sales:,}")
        st.write(f"Average order size: ${round(total_sales/unique_orders, 2):,}")
    with c2:
        st.subheader("Quantity of sales")
        st.write(f"Total items: {items_sold:,}")
        st.write(f"Unique orders: {unique_orders:,}")
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

    year_selection = st.selectbox("Select year:", options=[2015, 2016, 2017, 2018])
    year_df = df[df["Order Date"].dt.year.eq(year_selection)]

    c1, c2 = st.columns([3, 1])
    with c1:
        st.bar_chart(year_df, x="Sub-Category", y="Sales")
    with c2:
        st.bar_chart(year_df, x="Segment", y="Sales")

    st.write("---")

    col1, col2 = st.columns([2, 2])
    with col1:
        st.bar_chart(year_df, x="Region", y="Sales")
    with col2:
        st.bar_chart(year_df, x="Category", y="Sales")


if __name__ == "__main__":
    main()
