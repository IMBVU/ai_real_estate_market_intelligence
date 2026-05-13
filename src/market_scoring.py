import pandas as pd
from pathlib import Path

DATA_PATH = Path("../data/processed/real_estate_cleaned_sample.csv")
OUTPUT_PATH = Path("../outputs/real_estate_market_scores.csv")

def score_markets(df):
    city_summary = df.groupby(["state", "city"]).agg(
        listings=("price", "count"),
        median_price=("price", "median"),
        avg_price=("price", "mean"),
        median_bed=("bed", "median"),
        median_bath=("bath", "median"),
        median_house_size=("house_size", "median"),
        median_price_per_sqft=("price_per_sqft", "median"),
    ).reset_index()

    city_summary = city_summary[city_summary["listings"] >= 5].copy()

    city_summary["affordability_score"] = 100 - (city_summary["median_price"].rank(pct=True) * 100)
    city_summary["liquidity_score"] = city_summary["listings"].rank(pct=True) * 100
    city_summary["value_score"] = 100 - (city_summary["median_price_per_sqft"].rank(pct=True) * 100)

    city_summary["market_opportunity_score"] = (
        city_summary["affordability_score"] * 0.35
        + city_summary["liquidity_score"] * 0.30
        + city_summary["value_score"] * 0.35
    ).round(1)

    return city_summary.sort_values("market_opportunity_score", ascending=False).fillna("")

if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)
    scored = score_markets(df)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    scored.to_csv(OUTPUT_PATH, index=False)
    print(scored.head())
