#  Sales Prediction & Marketing Analytics

##  Project Overview

This project builds an end-to-end machine learning pipeline to **predict product sales based on advertising spend** across different marketing channels (TV, Radio, Newspaper).

It not only focuses on prediction accuracy but also provides **business insights** to support marketing strategy decisions.

---

##  Objectives

* Predict future sales using advertising spend data
* Perform data cleaning and transformation
* Apply feature engineering to improve model performance
* Train and evaluate regression models
* Analyze the impact of advertising channels on sales
* Deploy the model as an interactive web application

---

##  Dataset Description

The dataset contains 200 records with the following features:

* **TV**: Advertising spend on TV
* **Radio**: Advertising spend on Radio
* **Newspaper**: Advertising spend on Newspaper
* **Sales**: Target variable (sales revenue)

---

##  Exploratory Data Analysis (EDA)

### Key Observations:

* Strong positive correlation between **TV spend and Sales**
* Moderate relationship between **Radio and Sales**
* Weak impact of **Newspaper on Sales**

### Interpretation:

* TV is the most influential advertising channel
* Newspaper campaigns may not significantly affect sales

---

## Feature Engineering

To enhance model performance, new features were created:

* **Total_Spend = TV + Radio + Newspaper**
* **TV_Radio Interaction**
* **TV_Newspaper Interaction**

### Why?

These features capture:

* Combined marketing effort
* Interaction effects between channels

---

##  Model Building

### Models Used:

* Linear Regression
* Random Forest Regressor ✅ (Final Model)

### Why Random Forest?

* Handles non-linear relationships
* Provides better accuracy
* Reduces overfitting compared to simple regression

---

##  Model Performance

| Metric   | Value     |
| -------- | --------- |
| R² Score | **0.989** |
| RMSE     | **0.587** |

### Interpretation:

* Model explains ~99% of variance in sales
* Prediction error is very low
* Model is highly reliable for this dataset

---

## Business Insights

* 📺 **TV advertising has the highest impact on sales**
* 📻 **Radio contributes moderately**
* 📰 **Newspaper has minimal influence**

---

## Marketing Recommendations

* Increase investment in **TV advertising**
* Use **Radio as a supporting channel**
* Optimize or reduce spending on **Newspaper ads**

---

##  Deployment

The model is deployed using **Streamlit** as an interactive web application.

### Features:

* User inputs advertising spend
* Real-time sales prediction
* Simple and user-friendly interface

---

##  How to Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
streamlit run app.py
```

---

##  Project Structure

```
sales_project/
│── app.py              # Streamlit application
│── model.pkl           # Trained ML model
│── data.csv            # Dataset
│── notebook.ipynb      # Full analysis & modeling
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```

---

## Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Streamlit

---

## Key Learnings

* Importance of feature engineering in improving model accuracy
* Handling real-world deployment issues (feature mismatch, model consistency)
* Converting ML results into actionable business insights
* Building end-to-end data science projects

---

##Future Improvements

* Add more real-world features (customer demographics, seasonality)
* Use time-series models for forecasting
* Deploy online for public access
* Enhance UI/UX of the application

---

## 👩‍💻 Author

**Sania**

---

## Conclusion

This project demonstrates a complete **data science workflow**, from raw data to deployment, while focusing on both **technical accuracy and business impact**.
