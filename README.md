# E-Commerce Retail Audit & Customer Retention Strategy

An end-to-end exploratory data analysis (EDA) and customer lifecycle audit of **541,909 transaction records from a UK-based online retailer** (Dec 2010 – Dec 2011). Using a dual-pipeline architecture in Python (`Pandas`, `NumPy`, `Matplotlib`, `Seaborn`), this project separates **completed purchasing behavior** from **net financial transactions** (including cancellations and returns) to diagnose revenue concentration, retention drop-offs, and refund exposure.

---

## Executive Summary & Key Findings

| Metric / Audit Area | Verified Result | Strategic Takeaway |
| :--- | :--- | :--- |
| **Total Gross Revenue** | **£9.75M** (`£9,747,747.93`) | Full dataset top-line volume prior to unattributed/service filtering. |
| **Unattributed Sales** | **£1.45M** (**14.85%** of gross) | 135,080 rows lack `CustomerID`s—representing a major CRM attribution blind spot. |
| **Month-1 Retention Benchmark** | **21.27%** unweighted cohort avg | **78.73%** average Month-1 drop-off; retention stabilizes from Month 2 onward (`2010-12` peaked at **50.23%** in Month 11). |
| **Pareto (80/20) Concentration** | **73.79%** from Top 20% (**864** VIPs) | High-spend VIPs maintain a **69.0%–78.6%** monthly share year-round, showing that high-value customer concentration was present throughout the observed period. |
| **Sep–Nov Sales Surge** | **£3.01M** tracked net sales | Broad-based growth: VIPs jumped **+£193.0K** in Sep while the remaining 80% grew **+£118.1K**. |
| **Segment Refund Exposure** | **4.24%** gross VIP vs. **2.22%** regular | A single large cancellation (`C541433`, **-£77,183.60**) drove **57.19%** of net non-VIP refund value. |
| **Repeat Order Latency** | **50-day** median (**75.60-day** mean) | 75% of repeat buyers reorder within **111 days**, defining a clear CRM intervention window. |

---

## Dataset Overview
- **Source:** [UCI Machine Learning Repository – Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)
- **Scale & Period:** ~541,909 transactional line items spanning **December 1, 2010 – December 9, 2011** across a UK-registered non-store online retailer (all monetary figures in **GBP `£`**).
- **Granularity:** Invoice-line level (`InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`).

---

## Methodology & Data Engineering

To prevent return transactions from distorting customer acquisition dates or first-order baselines while keeping net sales 100% reconciled, the raw UCI Online Retail dataset was engineered into two synchronized pipelines:

1. **Sanitation & Horizon Alignment:**
   - Audited and isolated `135,080` unattributed transactions (`£1.45M`) and `1,754` non-merchandise service entries (`POST`, `D`, `M`, `BANK CHARGES`, `PADS`, `CR`).
   - Truncated incomplete December 2011 records to prevent right-edge time-truncation bias.
2. **Synchronized Dual-Pipeline Architecture:**
   - **`df` (Behavioral Pipeline):** Isolates strictly positive completed orders (`Quantity > 0`) to establish each customer's true acquisition cohort (`CohortMonth`), retention matrices, reorder latency, and `First_Purchase_value` (`£469.19` median) without left-censored return distortions.
   - **`df_all` (Financial Pipeline):** Retains cancellation invoices (`InvoiceNo` starting with `'C'`) and negative quantities, inheriting each customer's behavioral `CohortMonth` from `df` so net sales after returns/cancellations, customer LTV, and Pareto tiers (`Top 20%` by historical net spend) align 1:1 with cohort headcounts.

---

## Deep-Dive Analysis & Actionable Recommendations

### 1. Tracked vs. Unattributed Revenue Audit
![E-commerce Net Sales Distribution](images/NetSales%20Distribution.png)
- **Observation:** Out of **£9.75M** in total gross revenue, **£1.45M (14.85%)** across `135,080` line items lacks a recorded `CustomerID`.
- **Action Plan:** Enforce checkout account-linking or email capture at order confirmation to eliminate unattributed transaction blind spots and expand CRM retargeting coverage.

---

### 2. Customer Acquisition & Peak Seasonality
![Business Month Acquisition Count](images/AcquiredCohort%20HeadCount.png)
![Business Month Net Revenue Data](images/Monthly%20GrossRevenue.png)
- **Observation:** New customer acquisition peaked in `2010-12` (**884** accounts), while tracked net sales surged to **£3.01M** across September–November 2011.
- **Action Plan:** Replicate the `2010-12` acquisition playbook (which generated our largest cohort of high-retention buyers) and introduce **tiered cart-threshold incentives** during peak months to capture high-AOV repeat accounts.

---

### 3. Cohort Retention & Month-1 Drop-Off
![Cohort Retention Rate (%)](images/CohortRetention%20Heatmap.png)
- **Observation:** Unweighted average Month-1 retention across acquisition cohorts drops to **21.27%** (**78.73%** drop-off), before stabilizing from Month 2 onward—with the `2010-12` cohort peaking at **50.23%** in Month 11.
- **Action Plan:** Focus retention spend on converting first-time buyers into second-time buyers within their first 30–50 days rather than over-discounting established repeat customers.

---

### 4. Repeat Purchase Latency & CRM Escalation Workflow
![Customer Re-Order Latency: Statistical Distribution](images/SecondOrder%20DurationChart.png)
- **Observation:** Among returning buyers, the median time between Order 1 and Order 2 is **50 days** (**75.60-day** mean; **111 days** at the 75th percentile).
- **Action Plan (Two-Stage CRM Workflow):**
  - **Day 25 (Zero-Discount Nudge):** Send personalized restock reminders and SKU recommendations ahead of the Month-1 inactivity cliff to convert organic repeat buyers without eroding margin.
  - **Day 45 (Targeted Conversion Offer):** Deploy a time-bound discount or cart-threshold voucher for still-inactive buyers right before the **50-day** median reorder window closes.

---

### 5. Pareto (80/20) Revenue Concentration & Peak Share Dynamics
![Gross Revenue Distribution (80/20 Pareto Rule)](images/Pareto(80%2020)%20Distribution.png)
- **Observation:** Top 20% high-spend customers (`864` accounts) generate **73.79%** of total tracked net sales and maintain **69.0%–78.6%** of monthly net sales across all quarters. During the **£3.01M** September–November sales surge, VIP share diluted from **77.1%** (Aug) to **69.0%** (Nov) not due to VIP slowdown, but because the remaining 80% segment expanded even faster.
- **Action Plan:** Replicate the `2010-12` acquisition playbook (which generated our largest cohort of high-retention buyers) and introduce **tiered cart-threshold incentives** during peak months to capture high-AOV repeat accounts.

---

### 6. Large-Order Cancellation Guardrails & VIP SKU Audits
- **Observation:** While **69.21%** of net VIPs logged at least one return or invoice adjustment (vs. **26.00%** of regular buyers) due to higher purchase frequency, a single large cancellation (`C541433`, **-£77,183.60**) accounted for **57.19%** of all net non-VIP refund value. Defining segments by gross purchase spend prior to returns (`vip_gross`) confirms high-spend buyers carry nearly double the refund rate (**4.24%** vs. **2.22%**).
- **Action Plan:** Require pre-dispatch confirmation or partial deposits on unusually large orders exceeding £10K, and audit top-returned VIP `StockCode`s to distinguish routine invoice adjustments from SKU defects.

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
