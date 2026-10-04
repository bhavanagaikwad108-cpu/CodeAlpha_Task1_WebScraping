import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Book Analytics Dashboard",
    page_icon="📚",
    layout="wide"
)

# Load data
df = pd.read_csv("books.csv")

# -------------------------------
# CUSTOM UI
# -------------------------------

st.markdown("""
<style>
.main {
    background-color: #f5f3ff;
}

h1 {
    color: #6a1b9a;
    font-weight: 800;
}

h2, h3 {
    color: #4527a0;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, #ffffff, #ede7f6);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.10);
}

[data-testid="stMetricValue"] {
    color: #6a1b9a;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------
# HEADER
# -------------------------------

st.title("📚 Book Analytics Dashboard")

st.markdown(
    "### 🌈 Interactive analysis of scraped book data"
)

st.divider()


# -------------------------------
# KPI CARDS
# -------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📚 Total Books",
        len(df)
    )

with col2:
    st.metric(
        "💰 Average Price",
        f"£{df['Price'].mean():.2f}"
    )

with col3:
    st.metric(
        "⭐ Average Rating",
        f"{df['Rating'].mean():.2f}"
    )

with col4:
    st.metric(
        "💎 Highest Price",
        f"£{df['Price'].max():.2f}"
    )


st.divider()


# -------------------------------
# PRICE DISTRIBUTION
# -------------------------------

st.subheader("💰 Price Distribution")

fig_price = px.histogram(
    df,
    x="Price",
    nbins=20,
    title="Distribution of Book Prices",
    color_discrete_sequence=["#8E44AD"],
    template="plotly_white"
)

fig_price.update_layout(
    title_x=0.5,
    title_font_size=20,
    xaxis_title="Price (£)",
    yaxis_title="Number of Books"
)

st.plotly_chart(
    fig_price,
    use_container_width=True
)


# -------------------------------
# RATING CHART
# -------------------------------

st.subheader("⭐ Books by Rating")

rating_counts = (
    df["Rating"]
    .value_counts()
    .sort_index()
    .reset_index()
)

rating_counts.columns = ["Rating", "Books"]

fig_rating = px.bar(
    rating_counts,
    x="Rating",
    y="Books",
    title="Number of Books by Rating",
    color="Rating",
    color_continuous_scale="Turbo",
    template="plotly_white"
)

fig_rating.update_layout(
    title_x=0.5,
    title_font_size=20,
    xaxis_title="Rating",
    yaxis_title="Number of Books"
)

st.plotly_chart(
    fig_rating,
    use_container_width=True
)


# -------------------------------
# AVERAGE PRICE BY RATING
# -------------------------------

st.subheader("💎 Average Price by Rating")

avg_price = (
    df.groupby("Rating")["Price"]
    .mean()
    .reset_index()
)

fig_avg = px.bar(
    avg_price,
    x="Rating",
    y="Price",
    title="Average Book Price by Rating",
    color="Price",
    color_continuous_scale="Plasma",
    template="plotly_white"
)

fig_avg.update_layout(
    title_x=0.5,
    title_font_size=20,
    xaxis_title="Rating",
    yaxis_title="Average Price (£)"
)

st.plotly_chart(
    fig_avg,
    use_container_width=True
)


# -------------------------------
# SEARCH
# -------------------------------

st.subheader("🔎 Search Books")

search = st.text_input(
    "Enter a book title"
)

if search:

    filtered_df = df[
        df["Title"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

else:

    filtered_df = df


st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)