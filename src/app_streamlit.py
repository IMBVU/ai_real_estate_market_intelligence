import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Real Estate Market Intelligence", layout="wide")

st.title("AI Real Estate Market Intelligence Platform")
st.caption("Built with real-world real estate listing data")

scores = pd.read_csv("../outputs/real_estate_market_scores.csv")
scores = scores.fillna("")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Markets Scored", len(scores))
k2.metric("Median Listing Price", f"${scores['median_price'].median():,.0f}")
k3.metric("Median $/SqFt", f"${scores['median_price_per_sqft'].median():,.0f}")
k4.metric("Top Score", f"{scores['market_opportunity_score'].max():.1f}")

st.subheader("Market Scorecard")
st.dataframe(scores)

st.subheader("Top Markets by Opportunity Score")
top = scores.sort_values("market_opportunity_score", ascending=False).head(15)
st.bar_chart(top.set_index("city")["market_opportunity_score"])

selected = st.selectbox("Select a city", scores["city"].dropna().unique())
row = scores[scores["city"] == selected].iloc[0]

st.subheader("AI-Style Market Summary")
st.write(
    f"{row['city']}, {row['state']} has a median price of ${row['median_price']:,.0f}, "
    f"median price per square foot of ${row['median_price_per_sqft']:,.0f}, "
    f"and a market opportunity score of {row['market_opportunity_score']}/100."
)
