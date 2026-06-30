# 🌿 Cannabis Retail Intelligence Platform

An end-to-end business intelligence platform built with Python, PostgreSQL, SQL, and Streamlit for analyzing cannabis retail operations.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![SQL](https://img.shields.io/badge/SQL-Analytics-green)

---

# Project Overview

This project simulates the analytics platform used by a multi-store cannabis retailer.

The application ingests raw retail datasets, cleans and validates the data through an ETL pipeline, loads it into PostgreSQL, and presents executive business insights through an interactive Streamlit dashboard.

The goal of this project is to demonstrate the skills expected of a Junior Data Analyst, including:

- SQL
- Python
- ETL Development
- Data Cleaning
- Data Validation
- Data Visualization
- Dashboard Development
- Business Intelligence

---

# Dashboard

## Executive KPIs

- Total Revenue
- Estimated Profit
- Profit Margin
- Transactions
- Units Sold
- Average Sale

## Interactive Filters

- Store
- Category
- Brand
- Date Range

## Visualizations

- Revenue by Category
- Revenue by Store
- Top Brands
- Monthly Revenue Trend

---

# Project Structure

```
cannabis-retail-intelligence-platform/
│
├── dashboard/
│   ├── app.py
│   ├── charts.py
│   ├── metrics.py
│   ├── queries.py
│   └── styles.py
│
├── src/
│   ├── etl/
│   ├── database/
│   └── ...
│
├── sql/
│   └── business_analysis_queries.sql
│
├── data/
│
└── README.md
```

---

# Technologies Used

- Python
- PostgreSQL
- SQL
- Pandas
- SQLAlchemy
- Plotly
- Streamlit
- Git
- GitHub

---

# Features

## Data Engineering

- ETL Pipeline
- Data Cleaning
- Data Validation
- Duplicate Removal
- Category Standardization

## Database

- PostgreSQL relational database
- SQL joins
- Aggregations
- Business KPI calculations

## Dashboard

- Executive KPI cards
- Interactive filters
- Dynamic charts
- Modular architecture

---

# Business Questions Answered

The platform answers questions such as:

- Which store generates the most revenue?
- Which product categories perform best?
- Which brands generate the highest profit?
- What are monthly sales trends?
- How does store performance compare?
- What is the average transaction size?

---

# Skills Demonstrated

- Data Cleaning
- SQL Analytics
- Dashboard Development
- Business Intelligence
- Python Programming
- ETL Development
- Data Visualization
- Git Version Control

---

# Future Improvements

- Inventory forecasting
- Customer analytics
- Revenue forecasting
- Machine learning models
- User authentication
- Cloud deployment
- Docker support
- CI/CD pipeline

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/cannabis-retail-intelligence-platform.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the dashboard

```bash
streamlit run dashboard/app.py
```

---

# Author

**Chris Toon**

Post-Baccalaureate Computer Science Student

Interested in Data Analytics, Business Intelligence, and Cloud Computing.
