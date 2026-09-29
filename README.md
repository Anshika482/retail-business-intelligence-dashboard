# 📊 Retail Business Intelligence Dashboard

[Live Demo](https://retail-business-intelligence-dashboard-3kk53fze8kzqsyzusdjnl3.streamlit.app/) | [GitHub Repository](https://github.com/Anshika482/retail-business-intelligence-dashboard)

---

## 📌 1. Project Overview

**Retail Business Intelligence Dashboard** is an end-to-end analytical platform designed to transform raw retail transaction data into actionable business intelligence.

Rather than functioning as a basic sales reporting dashboard, the platform is engineered as an **analytical decision-support system** that combines data quality validation, exploratory data analysis, SQL-based business intelligence, KPI monitoring, interactive visualization, and business insights into a single workflow.

The system enables users to investigate **revenue performance, profitability, regional sales, product performance, customer segments, and sales trends** through an interactive analytical interface.

By combining **Python, Pandas, SQL, Plotly, and Streamlit**, the project demonstrates how raw transactional data can be converted into structured insights that support data-driven business decisions.

---

## 🎯 2. What Does It Do? (Core Capabilities)

The platform consists of **10 analytical capabilities** designed to investigate different areas of retail business performance:

### 📈 1. Executive Performance Intelligence

Provides a centralized overview of business health through key performance indicators including:

- Total Revenue
- Total Profit
- Total Orders
- Units Sold
- Average Order Value
- Profit Margin

This provides an immediate understanding of overall business performance.

### 📅 2. Sales Trend Intelligence

Analyzes revenue and profit performance across time to identify changes in business performance and recurring sales patterns.

### 🌍 3. Regional Performance Analysis

Evaluates revenue contribution across different geographical regions to identify high-performing and underperforming markets.

### 📦 4. Product Performance Intelligence

Profiles individual products based on revenue and profitability to identify the products contributing most significantly to business performance.

### 🏷️ 5. Category Performance Analysis

Compares product categories across revenue and profit metrics to understand which categories are driving sales and which are generating stronger margins.

### 👥 6. Customer Segment Analysis

Analyzes purchasing contribution across customer segments to understand how different customer groups contribute to overall business revenue.

### 💰 7. Profitability Intelligence

Moves beyond simple revenue reporting by analyzing the relationship between **revenue, profit, and profit margin** at product and category levels.

### 🧹 8. Data Quality Monitoring

Performs automated validation checks for missing values, duplicate records, and basic data consistency before the dataset is used for business analysis.

### 🔎 9. Interactive Business Exploration

Users can dynamically filter the analytical environment by:

- Date
- Region
- Category
- Customer Segment

All major KPIs and visualizations respond to the selected filters.

### 📤 10. Analytical Data Export

The platform allows users to export the currently filtered transaction dataset as a CSV file for additional analysis outside the dashboard.

---

## ⚙️ 3. How Does It Work? (Technical Architecture)

The system follows a structured **Data → Analysis → Intelligence → Visualization** architecture.

### 1. Data Ingestion

The platform works with transaction-level retail data containing information about orders, dates, products, categories, regions, customer segments, quantities, pricing, revenue, and profit.

### 2. Data Quality & Processing

**Pandas** is used to validate and process the dataset before analytical operations are performed.

The processing layer handles:

- Missing-value detection
- Duplicate detection
- Data validation
- Data transformation
- Aggregation
- Metric calculation

### 3. Exploratory Data Analysis

Python-based EDA is used to understand the structure and behavior of the dataset and identify important patterns in sales and profitability.

### 4. SQL Business Intelligence

A dedicated SQL analysis layer is used to answer business questions around:

- Revenue
- Profit
- Products
- Categories
- Regions
- Customer segments

This transforms raw transactions into structured business-level information.

### 5. KPI Engine

Core business metrics are calculated dynamically, including:

**Revenue → Profit → Orders → Units Sold → Average Order Value → Profit Margin**

### 6. Interactive Visualization

**Plotly** converts analytical results into interactive visualizations covering sales trends, regional performance, product performance, category contribution, customer segments, and profitability.

### 7. Dashboard Layer

**Streamlit** brings all analytical components together into an interactive business intelligence dashboard where users can filter, investigate, and export data.

---

## 💼 4. Business Value & Use Cases

The platform is designed to answer practical business questions such as:

- Which regions are generating the highest revenue?
- Which products are contributing most to profitability?
- Which categories generate strong revenue but comparatively lower profit?
- How is revenue changing over time?
- Which customer segments contribute most to sales?
- Where are potential profitability improvement opportunities?
- Is the underlying dataset reliable enough for decision-making?

The resulting analysis can support **sales performance monitoring, product strategy, regional planning, customer analysis, profitability analysis, and data-driven decision making**.

---

## 📊 5. Analytical Insights

The dashboard converts transaction-level data into business-level metrics and observations.

For the current dataset, the platform reports:

- **$931K+ Total Revenue**
- **$293K+ Total Profit**
- **1,000 Orders**
- **4,011 Units Sold**
- **$931 Average Order Value**
- **31.6% Profit Margin**

These metrics can be dynamically recalculated as users apply different filters to investigate specific regions, categories, products, or customer segments.

---

## 🧹 6. Data Quality & Reliability

A major focus of the project is ensuring that business insights are supported by reliable data.

The platform performs automated checks for:

- Missing values
- Duplicate transactions
- Data completeness
- Basic data consistency
- Numerical validity

The **Data Quality** module allows users to inspect the underlying dataset before interpreting business results.

This establishes a complete analytical workflow where **data reliability is evaluated before business intelligence is generated**.

---

## 🛠️ 7. Technology Stack

**Programming:** Python

**Data Analysis:** Pandas

**Database Analytics:** SQL

**Visualization:** Plotly

**Dashboard:** Streamlit

**Version Control:** Git & GitHub

**Deployment:** Streamlit Community Cloud

---

## 📁 8. Project Structure

```text
retail-business-intelligence-dashboard/
│
└── retail-sales-analytics-dashboard/
    │
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    │
    ├── data/
    │   └── retail_sales.csv
    │
    ├── analysis/
    │   └── data_cleaning_and_eda.py
    │
    └── sql/
        └── retail_analysis_queries.sql
