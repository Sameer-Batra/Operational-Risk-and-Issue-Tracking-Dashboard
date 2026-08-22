# Operational-Risk-and-Issue-Tracking-Dashboard


## Project Overview
An interactive Power BI dashboard designed to analyze Anti-Money Laundering (AML) and Know-Your-Customer (KYC) governance logs. This project simulates a real-world compliance environment, tracking open issues, monitoring Service Level Agreement (SLA) breaches, and flagging high-risk business units for remediation. 

## Tech Stack
* **Data Generation:** Python (Pandas, Faker) used to synthesize 5,000+ realistic compliance logs.
* **Visualization & Analytics:** Power BI, DAX (Data Analysis Expressions).
* **Data Structure:** Flat file (CSV) mimicking SQL database extracts.

## Key Features & Methodologies
* **Executive Summary:** Real-time monitoring of SLA Breach % and Overdue High-Risk issues using DAX measures.
* **Root Cause Analysis:** Drill-down matrix highlighting compliance bottlenecks by Business Unit and Issue Type (KYC/AML/Sanctions/Fraud).
* **Operational Remediation Tracker:** Dynamic filtering allowing compliance teams to prioritize aging, high-risk cases efficiently.

## Dashboard Previews

### 1. Executive Summary
![alt text](<Executive Summary.png>)

### 2. Risk & Root Cause Analysis
![alt text](<Risk & Root Cause Analysis.png>)

### 3. Remediation Tracker
![alt text](<Remediation Tracker.png>)

## How to Run
1. Run `data_generator.py` to generate a fresh batch of synthetic governance logs.
2. Open `Financial_Crimes_Governance_Dashboard.pbix` in Power BI Desktop.
3. Click "Refresh" to load the latest dataset.