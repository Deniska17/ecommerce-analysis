# E-Commerce Sales Analysis

# E-Commerce Sales Analysis

SQL portfolio project analyzing customer behavior, sales trends, and product performance.

## Dataset

Synthetic e-commerce database with 5 tables and 400+ rows:

- `customers` — 30 customers with RFM segments
- `products` — 50 products across 10 categories
- `orders` — 130 orders with status, channel, discount
- `order_items` — 212 line items
- `categories` — 10 product categories

## Projects

- **RFM Analysis** — customer segmentation by Recency, Frequency, Monetary
- **Monthly Trends** — sales evolution over time
- **Product Performance** — top products and categories by revenue
- **Customer Retention** — repeat purchase behavior

## Setup

```bash
pip install pandas sqlalchemy
python data/setup_db.py
```

## Stack

SQL · SQLite · Python · DBeaver
