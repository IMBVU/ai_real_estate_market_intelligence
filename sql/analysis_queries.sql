-- Top opportunity markets
SELECT
    city,
    state,
    listings,
    median_price,
    median_price_per_sqft,
    market_opportunity_score
FROM real_estate_market_scores
ORDER BY market_opportunity_score DESC
LIMIT 20;

-- Median price by city
SELECT
    city,
    state,
    COUNT(*) AS listings,
    MEDIAN(price) AS median_price
FROM real_estate_listings
GROUP BY city, state
ORDER BY listings DESC;

-- Price per square foot leaders
SELECT
    city,
    state,
    median_price_per_sqft,
    listings
FROM real_estate_market_scores
ORDER BY median_price_per_sqft DESC
LIMIT 20;
