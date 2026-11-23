# E-Commerce Retail Audit & Retention Strategy

## Executive Summary
An end-to-end exploratory data analysis (EDA) of UK-based online retail transactions designed to audit unattributed sales, map cohort retention lifecycles, and identify high-value B2B purchasing patterns to guide account management and CRM timing.

**Key Commercial Findings:**
- **Unattributed Transactions Audit:** Quantified **£1.44M (14.85% of net sales)** in transactions lacking a `CustomerID` (guest checkouts or unlinked orders), highlighting a major opportunity for checkout identity capture.
- **High-Value Buyers Start Big From Order #1:** Aggregating at the full invoice level revealed that top-tier buyers do **not** start with micro-transactions—their median first order is **£474.19** (IQR: **£308.60 – £853.73**), scaling to Lifetime Values (LTV) of up to **£267,410**.
- **Pareto Concentration & Q4 B2B Surge:** Confirmed a **74/26 revenue split** where the top 20% of customers generate 74% of completed product revenue (**~11x** the per-customer value of the bottom 80%) and drive **70.3% (£2.18M of £3.10M)** of the Sep–Nov peak sales window.
- **Repeat-Purchase Latency Window:** Among repeat customers, the median interval between first and second purchase is **50 days**, establishing Days 25–45 as the critical window for automated win-back campaigns.

---

## Dataset Overview
- **Source:** [UCI Machine Learning Repository – Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)
- **Scale & Period:** ~541,909 transactional line items spanning **December 1, 2010 – December 9, 2011** across a UK-registered non-store online retailer (all monetary figures in **GBP `£`**).
- **Granularity:** Invoice-line level (`InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`).

---

## Key Business Insights & Visualizations

### 1. Customer Acquisition Trend & Cohort Headcount
![Acquired Cohort Headcount](images/AcquiredCohort%20HeadCount.png)
- **The Insight:** Tracked customer acquisition opens strongly with 884 first-time buyers in December 2010 and maintains steady acquisition through Q1 2011 before tapering in later months.

### 2. Cohort Retention & Month-1 Drop-Off Matrix
![Cohort Retention Heatmap](images/CohortRetention%20Heatmap.png)
- **The Insight:** Q1–Q3 cohorts experience a steep Month-1 drop-off (~78%+ non-return rate), whereas the December 2010 cohort demonstrates strong long-term stickiness (reaching 50.2% retention in Month 11).
- **Strategic Play:** Deploy an automated CRM re-engagement sequence (product check-in at Day 25, targeted incentive at Day 45) to convert one-time buyers before repeat momentum stalls around Day 50.

### 3. Monthly Revenue Trajectory & Sep–Nov B2B Surge
![Monthly Gross Revenue](images/Monthly%20GrossRevenue.png)
- **The Insight:** Monthly completed product revenue climbed from **£568K** in December 2010 to **£1.14M** in November 2011, driven by a **£306K month-over-month jump in September**. Isolating the Sep–Nov window (£3.10M total) confirms that top-20% accounts generated **£2.18M (70.3%)** of peak-period sales through bulk restocking.
- **Strategic Play:** Launch wholesale pre-booking outreach and volume-tier incentives in July/August to capture Q4 B2B inventory budgets early.

### 4. Pareto Revenue Concentration ("Whale" Dynamics)
![Pareto Distribution](images/Pareto(80%2020)%20Distribution.png)
- **The Insight:** The top 20% of customers account for **74%** of completed product revenue while the remaining 80% account for **26%**—meaning an average top-tier buyer generates roughly **11x** the revenue of a standard buyer.
- **Strategic Play:** Use **First Order Value** ($\ge$ **£300**) as an early lead-scoring trigger to flag high-potential B2B accounts immediately after Order #1 and assign dedicated Key Account Managers.

### 5. Repeat-Purchase Latency Window
![Second Order Duration](images/SecondOrder%20DurationChart.png)
- **The Insight:** Among customers who make a repeat purchase, the median time between their first and second order is **50 days**, giving marketing teams a clear benchmark for pre-churn intervention.

---

## Technical Execution & Data Hygiene
- **Tech Stack:** Python (`pandas`, `numpy`, `matplotlib`, `seaborn`), JupyterLab.
- **Two-Stage Accounting Separation:**
  - *Pre-Filter Net Sales (`£9.74M`):* Evaluated full transactional records (including returns) to quantify tracked customer sales (**£8.30M / 85.15%**) vs. unattributed transactions missing a `CustomerID` (**£1.44M / 14.85%**).
  - *Post-Filter Completed Product Revenue:* Removed unattributed rows, order cancellations (`InvoiceNo` starting with `C`), negative quantities, and non-merchandise service codes (`POST`, `D`, `M`, `BANK CHARGES`, etc.) prior to cohort, Pareto, and LTV modeling.
- **Memory Optimization:** Applied explicit downcasting (`int32`, `float32`) to reduce DataFrame memory footprint across 540K+ records.

---

## Analytical Scope & Limitations
- **Single ~12-Month Window:** Because the dataset spans Dec 2010 – Dec 2011, comparing December 2010 against November 2011 reflects a combination of business growth and Q4 holiday seasonality rather than confirmed multi-year Year-over-Year (YoY) seasonality.
- **Repeat-Buyer Latency Scope:** The 50-day median inter-purchase interval is calculated across repeat purchasers only (excluding single-order customers who never placed a second order).
- **No Marketing Cost (CAC) Data:** The dataset does not include customer acquisition or ad-spend records; pairing these cohort LTV benchmarks with internal CAC data is recommended as a next step to model payback periods.

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


1. **Clone the repository:**
   ```bash
   git clone [https://github.com/MD-Sajid947/ecommerce-retail-analytics.git](https://github.com/MD-Sajid947/ecommerce-retail-analytics.git)
   cd ecommerce-retail-analytics
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Launch JupyterLab and run the notebook:**
   ```bash
   jupyter lab ecommerce-analytics.ipynb
   ```
   *(The notebook automatically downloads and extracts the dataset from the UCI repository on first run.)*
