# 📦 Inventory Demand Forecasting

An AI-powered inventory demand forecasting and stock optimization project that predicts future product demand and generates inventory reorder recommendations.

## 🎯 Project Objective

The goal of this project is to help businesses make better inventory decisions by:

- Predicting future product demand
- Identifying upcoming stock requirements
- Calculating reorder recommendations
- Generating future inventory plans
- Visualizing inventory insights using Power BI

## 🧠 Machine Learning

The project uses **Machine Learning with Random Forest Regression** to forecast inventory demand.

### Model Performance

| Metric | Result |
|---|---:|
| MAE | 4.04 |
| RMSE | 6.21 |

The trained model was developed using historical inventory and sales data along with time-based and demand-related features.

## 🔄 Project Workflow

```text
Raw Inventory Data
       ↓
Data Inspection
       ↓
Feature Engineering
       ↓
Time & Lag Features
       ↓
Train/Test Split
       ↓
Random Forest Model
       ↓
Demand Prediction
       ↓
Reorder Recommendations
       ↓
Future Inventory Planning
       ↓
Power BI Dashboard
