-- Step 1: Create the tables
CREATE TABLE customers (
    Customer_Id INT PRIMARY KEY,
    Occupation VARCHAR(255),
    Type VARCHAR(255)
);


CREATE TABLE interactions (
    date_start TIMESTAMP,
    interaction VARCHAR(255),
    customers INT
);

CREATE TABLE products (
    date VARCHAR(7),
    product VARCHAR(255)
);

-- Ensure the topics table exists
CREATE TABLE IF NOT EXISTS topics (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

-- Add topic and sentiment columns to interactions
ALTER TABLE interactions ADD COLUMN topic_id INT REFERENCES topics(id);
ALTER TABLE interactions ADD COLUMN sentiment VARCHAR(50);
