-- CREATE BANKS TABLE

CREATE TABLE banks (

    bank_id SERIAL PRIMARY KEY,

    bank_name VARCHAR(100) UNIQUE NOT NULL
);


-- CREATE REVIEWS TABLE

CREATE TABLE reviews (

    review_id VARCHAR(255) PRIMARY KEY,

    bank_id INTEGER REFERENCES banks(bank_id),

    review TEXT NOT NULL,

    rating INTEGER,

    review_date DATE,

    source VARCHAR(100)
);


-- CREATE SENTIMENTS TABLE

CREATE TABLE sentiments (

    sentiment_id SERIAL PRIMARY KEY,

    review_id VARCHAR(255) REFERENCES reviews(review_id),

    sentiment_label VARCHAR(50),

    sentiment_score FLOAT,

    theme VARCHAR(100)
);