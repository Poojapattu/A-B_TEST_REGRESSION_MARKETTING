📊 Marketing Campaign Optimization using A/B Testing & Regression Analysis
📌 Project Overview

This project focuses on analyzing and optimizing digital marketing campaign performance using A/B Testing and Regression Analysis. The goal is to identify the best-performing advertising platform and predict future conversions using statistical and machine learning techniques.

The project simulates a real-world marketing analytics workflow used by digital marketing agencies and data analytics teams.

🎯 Business Objective

A marketing team wants to answer the following questions:

Which platform performs better: Google Ads or Instagram Ads?
Which factors most influence conversions?
How can campaign budget allocation be optimized for better ROI?
🧠 Key Concepts Covered
A/B Testing
Hypothesis Testing
Statistical Analysis
Regression Modeling
Feature Engineering
Marketing KPI Analysis
Data Visualization
Business Insights Generation
📂 Project Structure
SMM_3_ABtesting_marketting/
│
├── data/
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_ab_testing.ipynb
│   ├── 03_regression_analysis.ipynb
│
├── src/
│   ├── generate_dataset_v2.py
│
├── marketing_campaign_data_v2.csv
├── requirements.txt
├── README.md
📊 Dataset Description

The dataset simulates marketing campaign performance data with realistic business behavior.
<img width="1553" height="767" alt="image" src="https://github.com/user-attachments/assets/cfe3b007-e717-46b6-bc29-d48708ac43b1" />


Features Included
Feature	Description
date	Campaign date
platform	Advertising platform
age_group	Audience age category
region	Target region
device	Mobile/Desktop
campaign_type	Video/Image/Text ads
impressions	Ad views
clicks	User clicks
cost	Campaign spending
conversions	Successful conversions
click_rate	Click-through behavior
conversion_rate	Conversion efficiency
⚙️ Technologies Used
Python
Pandas
NumPy
SciPy
Scikit-learn
Matplotlib
Seaborn
Jupyter Notebook
🧪 A/B Testing

The project performs statistical hypothesis testing to compare campaign performance between:

Google Ads
Instagram Ads
Hypothesis
Null Hypothesis (H₀)

There is no significant difference between platform conversion rates.

Alternative Hypothesis (H₁)

There is a significant difference between platform conversion rates.

Statistical Test Used
Independent Two-Sample T-Test
📈 Regression Analysis

A regression model is built to predict:

🎯 Target Variable
Conversions
📌 Features Used
Impressions
Clicks
Cost
CTR
Platform
Device Type
Campaign Type
📊 KPIs Analyzed
Click Through Rate (CTR)
Cost Per Click (CPC)
Conversion Rate (CR)
Cost Per Conversion
ROI Trends
Weekly Performance Trends
📉 Visualizations Included
Platform Comparison Charts
Conversion Trend Analysis
Correlation Heatmap
Clicks vs Conversions Scatter Plot
Campaign Performance Analysis
🚀 Key Outcomes
Identified the highest-performing advertising platform
Analyzed factors influencing campaign conversions
Generated business recommendations for budget optimization
Built predictive analytics workflow using regression models
💼 Business Recommendation

The analysis helps marketing teams:

Improve conversion efficiency
Reduce campaign spending waste
Optimize ad targeting strategy
Allocate budget based on statistical evidence
▶️ How to Run the Project
1️⃣ Clone Repository
git clone <repository_link>
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Generate Dataset
python src/generate_dataset_v2.py
4️⃣ Run Jupyter Notebook
jupyter notebook
📌 Future Enhancements
Streamlit Dashboard Integration
Real-time Campaign Monitoring
Advanced ML Models
ROI Forecasting
Automated Reporting System
👩‍💻 Author
Pooja Pattu

Aspiring Data Analyst and AI & Data Science Engineer passionate about data-driven business solutions, machine learning, and analytics.
