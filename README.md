# DecodeLabs Internship — Week 4: Data Analytics & Visualization

## Project
**E-Commerce Data Analytics Dashboard**

This project converts raw e-commerce order data into an interactive dashboard focused on:
- Revenue and order trends
- Product performance
- Order-status distribution
- Referral-source performance
- Payment-method analysis
- Coupon performance
- Executive/business insights

The dashboard follows the Week 4 focus on choosing appropriate charts, reducing cognitive load, highlighting key insights, and turning analysis into an action-oriented data story.

## Tech Stack
- Python
- Pandas
- Streamlit
- Plotly
- Excel dataset

## Dataset
`data.xlsx` contains 1,200 order records and 14 fields including date, product, quantity, unit price, payment method, order status, referral source, coupon code, and total price.

## Run Locally

```bash
cd Decodelabs_Week4_Data_Analytics
python -m pip install -r requirements.txt
streamlit run app.py
```

If `streamlit` is not recognized:

```bash
python -m streamlit run app.py
```

The browser will open the local dashboard.

## Dashboard Sections
1. Revenue trend
2. Product performance
3. Order status mix
4. Referral source
5. Payment methods
6. Coupon performance
7. Executive takeaways
8. Filtered raw-data view

## Project Outcome
The dashboard is designed to demonstrate exploratory analysis and explanatory delivery: charts are paired with concise observations so a viewer can move from **data → pattern → business insight**.

## Author
**Faiz Elahi**  
DecodeLabs Industrial Training — Week 4
