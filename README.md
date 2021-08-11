# DenguePred

## Project Description: Predicting Local Dengue Epidemics
Dengue is a tropical mosquito-borne viral infection. While many dengue infections result in only mild illness, the disease process can result in an acute flu-like illness with potentially lethal complications. With about 100-400 million infections each year, the global incidence of dengue has grown dramatically in recent decades, especially in America.

Because the dengue virus is spread by mosquitoes, the transmission dynamics are related to meteorological and environmental conditions such as temperature and precipitation. Understanding how these conditions affect dengue dynamics and accurate dengue predictions would help to optimize health care and containment measures.

The aim of this project was to predict the number of dengue fever cases reported each week in two Central and South American cities, San Juan (Puerto Rico) and Iquitos (Peru). We used the weekly number of dengue cases as well as different environmental variables from both cities and applied different predictive modelling approaches based on auto-regression and/or models incorporating environmental variables. 

## Overview
This repository consists of different notebooks: 
[01_data_cleaning.ipynb](01_data_cleaning.ipynb): 
* Data import
* Missing value imputation
* Feature editing 
* Adding population data
* Train test split

[02_feature_engineering.ipynb] (02_feature_engineering.ipynb): 
* Features based on temperature functions
* Cumulative precipitation variables
* Adding lagged values

[03_eda.ipynb](03_eda.ipynb):
* Exploratory data analysis
* Visualisations of the different variables

[03_visualization_cases_america.ipynb](03_visualization_cases_america.ipynb):
* Visualisation of Dengue case numbers over time
* For North and South America
* From 1980 until 2020
* Using Geopandas
* Creating an animated GIF image

[custom_regression_model.ipynb](custom_regression_model.ipynb):
* Poisson Regression using Gradient Boosting
* Regression using environmental variables, a model for seasonality and a variable for the predicted deviance from the seasonal model
* Can predict some of the epidemics
* Larger error rate than regression models that only use environmental variables

[04_granger_causality.ipynb](04_granger_causality.ipynb):
* Algorithm that searches for statistically significant relationships between variables
* Retrieves environmental variables that are highly likely to have a causal relationship with the target variable

[04_holt_winters.ipynb](04_holt_winters.ipynb):
* Holt-Winters Exponential Smoothing
* Prediction of the seasonal fluctuations in reported Dengue case numers

[04_neuralprophet.ipynb](04_neuralprophet.ipynb):
* Time series forecasting model using `neural prophet`
* Using additional regressors (environmental variables)

[04_regression_models.ipynb](04_regression_models.ipynb):
* Random Forest Regression 
* Poisson Regression (Gradient Boosting)
* Using `sklearn`
* Achieving the lowest MAE error rates of our submissions

[04_sarimax.ipynb](04_sarimax.ipynb):
* Seasonal autoregressive model
* Using additional regressors (environmental variables)
* Using `statsmodels`


## Environment
If you work with pip you can use the [requirements](requirements.txt) file in this repo to obtain all necessary packages. And if you have pyenv and pip installed, you can create a virtual environment with the following commands:

```BASH
pyenv local 3.8.5
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
