import pandas as pd
from pathlib import Path

SCORES_PATH = Path("../outputs/real_estate_market_scores.csv")

def build_market_summary(row):
    return (
        f"{row['city']}, {row['state']} has {int(row['listings'])} listings in the cleaned sample, "
        f"a median price of ${row['median_price']:,.0f}, and a median price per square foot of "
        f"${row['median_price_per_sqft']:,.0f}. The market opportunity score is "
        f"{row['market_opportunity_score']}/100, based on affordability, inventory depth, and value signals."
    )

if __name__ == "__main__":
    df = pd.read_csv(SCORES_PATH)
    for _, row in df.head(10).iterrows():
        print("-", build_market_summary(row))
