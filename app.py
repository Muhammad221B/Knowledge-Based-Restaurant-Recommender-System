import streamlit as st
import pandas as pd

# Load the cleaned and sorted dataset
df = pd.read_csv("data/sorted_df.csv")

st.title("🍽️ Knowledge-Based Restaurant Recommender")

# --- Sidebar for User Inputs ---
st.sidebar.header("Set Your Preferences")

# Country
countries = sorted(df['Country'].dropna().unique())
selected_country = st.sidebar.selectbox("Select Country", countries)

# Budget Category
budgets = sorted(df['Cost Category'].dropna().unique())
selected_budget = st.sidebar.selectbox("Select Budget Category", budgets)

# Cuisine Type
cuisines = sorted(df['Primary Cuisine'].dropna().unique())
selected_cuisines = st.sidebar.multiselect("Select Cuisine(s)", cuisines)

# Filter button
if st.sidebar.button("Show Recommendations"):
    # Filter the data
    filtered_df = df[
        (df['Country'] == selected_country) &
        (df['Cost Category'] == selected_budget) &
        (df['Primary Cuisine'].isin(selected_cuisines))
    ]

    st.subheader("🍴 Recommended Restaurants")

    if filtered_df.empty:
        st.warning("No matching restaurants found for your preferences.")
    else:
        for _, row in filtered_df.head(10).iterrows():
            st.markdown(f"### {row['Restaurant Name']}")
            st.markdown(f"**Cuisine:** {row['Primary Cuisine'].title()}")
            st.markdown(f"**Rating:** {row['Aggregate rating']} ⭐ ({int(row['Votes'])} votes)")
            st.markdown(f"**Budget Category:** {row['Cost Category']}")
            st.markdown(f"**Country:** {row['Country']}")
            st.markdown(f"**🔍 Why this recommendation?** {row['Explanation']}")
            st.markdown("---")
