# E-Commerce Retail Audit & Retention Strategy

## Executive Summary
This project is an end-to-end exploratory data analysis (EDA) of a retail e-commerce transactional dataset, This engine is designed to identify revenue leaks, map customer retention lifecycles, and extract actionable B2B wholesale strategies to optimize marketing budget allocation.

**Key Commercial Findings:**
* **Ghost Revenue Audit:** Quantified unauthenticated transaction leakage at £1.44M (14.85% of total sales).
* **The B2B "Land & Expand" Funnel:** Discovered that top-tier wholesale buyers initiate relationships via micro-sampling (<$2.00) before scaling to LTVs exceeding $248,000.
* **Q1-Q3 Churn Cliff vs. Q4 Seasonality:** Identified a critical 50-day purchase latency wall and restructured annual marketing timelines to capture the September B2B wholesale surge.

---

## Key Business Insights & Visualizations

### 1. Customer Acquisition Trend & Cohort Headcount
![Acquired Cohort Headcount](images/AcquiredCohort%20HeadCount.png)
* **The Insight:** Customer acquisition peaks sharply at 884 new users in December 2010, maintaining a strong acquisition window through Q1 of the following year before tapering off.

### 2. Cohort Retention & Churn Cliff Matrix
![Cohort Retention Heatmap](images/CohortRetention%20Heatmap.png)
* **The Insight:** Q1–Q3 cohorts suffer a severe Month-1 drop-off cliff (~78%+ churn), whereas Q4 acquisitions display superior baseline loyalty (peaking at 50.2% retention in Month 11 for the Dec-2010 cohort).
* **Strategic Play:** Implement an automated CRM escalation workflow (gentle reminders at Day 25, high-value discount vouchers at Day 45) to bridge users past the 50-day median latency cliff before they churn.

### 3. Revenue Scaling & B2B Seasonality
![Monthly Gross Revenue](images/Monthly%20GrossRevenue.png)
* **The Insight:** Gross revenue doubled from $568K to $1.14M year-over-year, initiated by a massive $306K month-over-month jump in September, confirming bulk B2B inventory pre-stocking ahead of the retail holidays.
* **Strategic Play:** Shift holiday marketing and bulk-discount pitches backward to July/August to intercept wholesale buyers stocking shelves for Q4, while maintaining higher permanent baseline inventory for 2012.

### 4. Pareto Revenue Concentration ("Whale" Dynamics)
![Pareto Distribution](images/Pareto(80%2020)%20Distribution.png)
* **The Insight:** Confirmed a 74/26 Pareto distribution where the top 20% of customers drive nearly three-quarters of total company revenue. Historical tracking reveals these are primarily B2B wholesale accounts acquired during winter windows.
* **Strategic Play:** Cease relying solely on automated marketing for these accounts; assign dedicated Key Account Managers to nurture high-LTV buyers.

### 5. Order Latency & Re-Engagement Windows
![Second Order Duration](images/SecondOrder%20DurationChart.png)
* **The Insight:** The median time between a first and second purchase is exactly 50 days. Once a customer crosses this threshold without returning, their probability of churning increases drastically.

---

## Technical Execution & Data Sanitation
* **Tech Stack:** Python, Pandas, NumPy, Seaborn, Matplotlib.
* **Data Hygiene:** Excluded order cancellations, negative volume entries, and non-merchandise service fee codes (`POST`, `D`, `M`, `BANK CHARGES`, etc.).
* **Memory Optimization:** Engineered custom datatype conversions (`int32`, `float32`) to ensure smooth scaling over large transactional arrays.

---

## Repository Structure
```text
├── images/
│   ├── AcquiredCohort HeadCount.png
│   ├── CohortRetention Heatmap.png
│   ├── GrossRevenue Distribution.png
│   ├── Monthly GrossRevenue.png
│   ├── Pareto(80 20) Distribution.png
│   └── SecondOrder DurationChart.png
├── ecommerce-analytics.ipynb
├── requirements.txt
├── README.md
└── utils.py
```

---

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/MD-Sajid947/ecommerce-retail-analytics.git](https://github.com/MD-Sajid947/ecommerce-retail-analytics.git)
