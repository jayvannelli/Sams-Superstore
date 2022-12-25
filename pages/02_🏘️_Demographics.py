import streamlit as st
from src.data import get_superstore_sales_dataset


def groupby_state(data):
    cleaned_df = data[["State", "Sales"]]
    df = cleaned_df.groupby(['State'])
    return df


def main():
    st.title("Demographic Breakdown")
    st.write("---")

    df = get_superstore_sales_dataset()

    all_states_tab, single_state_tab = st.tabs(["All states", "Single state"])

    with all_states_tab:
        st.subheader("Sales by region")
        st.bar_chart(df, x="Region", y="Sales")

        st.write("Click boxes below to see region details (included states, sum & count by region).")
        c1, c2 = st.columns(2)

        with c1:
            with st.expander("South"):
                south = df.loc[df["Region"] == "South"]

                st.write(f"Sum: ${round(sum(south['Sales']), 2):,}")
                st.write(f"Count: {len(south)}")

                southern_states = list(south["State"].unique())
                st.write(southern_states)

            with st.expander("West"):
                west = df.loc[df["Region"] == "West"]

                st.write(f"Sum: ${round(sum(west['Sales']), 2):,}")
                st.write(f"Count: {len(west)}")

                western_states = list(west["State"].unique())
                st.write(western_states)

        with c2:
            with st.expander("Central"):
                central = df.loc[df["Region"] == "Central"]

                st.write(f"Sum: ${round(sum(central['Sales']), 2):,}")
                st.write(f"Count: {len(central)}")

                central_states = list(central["State"].unique())
                st.write(central_states)

            with st.expander("East"):
                east = df.loc[df["Region"] == "East"]

                st.write(f"Sum: ${round(sum(east['Sales']), 2):,}")
                st.write(f"Count: {len(east)}")

                eastern_states = list(east["State"].unique())
                st.write(eastern_states)

        st.write("---")

        st.subheader("Sales by State")
        st.bar_chart(df, x="State", y="Sales")

        st.write("---")
        st.subheader("State stats")

        grouped_state_data = groupby_state(df)
        st.write(grouped_state_data.describe())

    with single_state_tab:

        st.subheader("Single state selection")
        state = st.selectbox("Select state:", options=df["State"].unique())
        state_df = df.loc[df["State"] == state]

        st.subheader(f"{state} | Sales by city")
        st.bar_chart(state_df, x="City", y="Sales")

        st.subheader(f"{state} | Sales over time")
        st.bar_chart(state_df, x="Order Date", y="Sales")

        st.write("---")

        left_state_column, right_state_column = st.columns(2)
        with left_state_column:
            st.subheader("Preferred shipping mode")
            st.bar_chart(state_df, x="Ship Mode", y="Sales")
        with right_state_column:
            st.subheader("Breakdown by sub-category")
            st.bar_chart(state_df, x="Sub-Category", y="Sales")


if __name__ == "__main__":
    main()
