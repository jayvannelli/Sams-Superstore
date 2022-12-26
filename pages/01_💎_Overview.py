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

    shallow_df_copy = df.copy()
    shallow_df_copy['Order Date Name'] = shallow_df_copy['Order Date'].dt.day_name()
    st.bar_chart(shallow_df_copy, x="Order Date Name", y="Sales")


if __name__ == "__main__":
    main()
