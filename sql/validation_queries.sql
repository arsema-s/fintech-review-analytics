-- TOTAL REVIEWS

SELECT COUNT(*)
FROM reviews;


-- REVIEWS PER BANK

SELECT
    b.bank_name,
    COUNT(r.review_id) AS total_reviews
FROM reviews r
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY b.bank_name;


-- SENTIMENT DISTRIBUTION

SELECT
    sentiment_label,
    COUNT(*)
FROM sentiments
GROUP BY sentiment_label;


-- THEMES BY BANK

SELECT
    b.bank_name,
    s.theme,
    COUNT(*) AS total
FROM sentiments s
JOIN reviews r
ON s.review_id = r.review_id
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY
    b.bank_name,
    s.theme
ORDER BY total DESC;


-- AVERAGE RATING BY BANK

SELECT
    b.bank_name,
    AVG(r.rating) AS avg_rating
FROM reviews r
JOIN banks b
ON r.bank_id = b.bank_id
GROUP BY b.bank_name;