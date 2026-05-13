CREATE TABLE real_estate_listings (
    status TEXT,
    price DECIMAL(12,2),
    bed DECIMAL(5,1),
    bath DECIMAL(5,1),
    acre_lot DECIMAL(10,2),
    city TEXT,
    state TEXT,
    zip_code TEXT,
    house_size DECIMAL(12,2),
    price_per_sqft DECIMAL(12,2),
    prev_sold_date DATE
);

CREATE TABLE real_estate_market_scores (
    state TEXT,
    city TEXT,
    listings INTEGER,
    median_price DECIMAL(12,2),
    avg_price DECIMAL(12,2),
    median_bed DECIMAL(5,1),
    median_bath DECIMAL(5,1),
    median_house_size DECIMAL(12,2),
    median_price_per_sqft DECIMAL(12,2),
    affordability_score DECIMAL(5,1),
    liquidity_score DECIMAL(5,1),
    value_score DECIMAL(5,1),
    market_opportunity_score DECIMAL(5,1)
);
