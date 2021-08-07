# DenguePred

## Project Description: Predicting Local Dengue Epidemics
Dengue is a tropical mosquito-borne viral infection. While many dengue infections result in only mild illness, the disease process can result in an acute flu-like illness with potentially lethal complications. With about 100-400 million infections each year, the global incidence of dengue has grown dramatically in recent decades, especially in America.

Because the dengue virus is spread by mosquitoes, the transmission dynamics are related to meteorological and environmental conditions such as temperature and precipitation. Understanding how these conditions affect dengue dynamics and accurate dengue predictions would help to optimize health care and containment measures.

The aim of this project was to predict the number of dengue fever cases reported each week in two Central and South American cities, San Juan (Puerto Rico) and Iquitos (Peru). We used the weekly number of dengue cases as well as different environmental variables from both cities and applied different predictive modelling approaches based on auto-regression and/or models incorporating environmental variables. 

## Overview
This repository consists of different notebooks: 
1. [01_data_cleaning](01_data_cleaning.ipynb): 
* Data import
* Missing value imputation
* Feature editing 
* Adding population data
* Train test split
2. [02_feature_engineering](02_feature_engineering.ipynb): 
* Features based on temperature functions
* Cumulative precipitation variables
* Adding lagged values
3. Needs to be added...

## Environment
Use the [requirements](requirements.txt) file in this repo to create a new environment. For this you can either use `make setup` or the following commands:

```BASH
pyenv local 3.8.5
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```