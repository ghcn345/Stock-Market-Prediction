<p>
<img src="images/stock-chart.jpeg" width="900" height="600">
</p>

# Stock Market Prediction

**Author**: Ning Chen

## Table of Contents
- [Overview](#Overview)
- [Business Understanding](#Business-Understanding)
- [Data Collection](#Data-Collection)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Classification](#Classification)
- [Time Series](#Time-Series)
- [Sentimental Analysis](#Sentimental-Analysis)
- [Frontend](#Frontend)
- [Next Steps](#Next-Steps)
- [For More Information](#For-More-Information)
- [Repository Structure](#Repository-Structure)

## Overview
Accurate prediction of stock market asset is a significant and challenging task due to complicated nature of the financial stock markets. Considering the increasing availability and affordability of powerful computational engines, deep learning methods of prediction have proved its efficiency in finance.


## Business Understanding

A time series regression model using NN or other advanced techniques is built to predict the stock market. Stock market prediction aims to determine the future movement of the stock value of a financial exchange. This project is helpful for Stock investors and investment banks to have a better understanding in developing economical Strategy and in making financial decisions.




## Data Collection
Data was collected from three different web sources by API calls or Web Scraping.

- [Quarterly Report](https://finance.yahoo.com/quote/AAPL/financials?p=AAPL) for Classification by Web Scrapping.
- [Yahoo Finance](https://github.com/ranaroussi/yfinance) and [IEX API](https://iexcloud.io) for Time Series by API calls.
- Twitter for sentimental data by VADER.


## Exploratory Data Analysis

- Quarterly Report data was cleaned and analyzed. A simple Trade Strategy wad made: local minimum of the price to buy, local maximum of the price to sell, and all other time to hold.
- Time series data was joined with Quarterly Report data. The missing data for weekends and holidays was filled by interpolation method. The missing data of exogenous features was filled by propagating nearest valid observation backward/forward to next valid observation. 
- Using TF-IDF for feature extraction in Sentiment Analysis.

    


![graph](/images/trade.jpeg)

![graph](/images/ohlc.jpeg)



## Classification

Quarterly Report data was used to train several different classification models. More than 100 features were presented in the dataframe. Therefore, Principle Component Analysis (PCA) was implemented to reduce the dimensionality. 

![graph](/images/pca.jpeg)

![graph](/images/heatmap.jpeg)

![graph](/images/xgb.jpeg)


## Time-Series
Time series data was fitted and trained to two time series models. All models are evaluated by RMSE and MAPE.

SARIMAX Model with exogenous features

![graph](/images/SARIMAX.jpeg)

Facebook Prophet

![graph](/images/fbprophet.jpeg)

LSTM

![graph](/images/lstm.jpeg)

GRU

![graph](/images/gru.jpeg)

## Sentimental Analysis

Use NLP & Deep Learning to predict stock prices. 

- Count of tweets for the stock is calculated

![graph](/images/count.jpeg)

- Sentiment of the stock is analyzed

![graph](/images/sentiment.jpeg)

- Word Cloud

![graph](/images/word.jpeg)

## Frontend

Streamlit was used to create a frontend for each form of analysis with their respective machine learning models.

<img src="images/stock.gif">


## Next Step
- To access the updated quarterly reports timely and obtain more important features.
- To tune the hyperparameters (exogenous variables) in Time Series models. Technical indicators such as MACD, Stochastic, RSI, etc can be used.
- Besides Twitter, gathering more relevant sentimental data from other web sources.

## For More Information

Please review our full analysis in [Jupyter Notebook](https://github.com/ghcn345/Stock-Market-Prediction/blob/master/stock_market.ipynb) or [presentation](https://github.com/ghcn345/Stock-Market-Prediction/blob/master/Presentation.pdf).

For any additional questions, please contact **Ning Chen—chen.ning345@gmail.com**.

## Repository Structure

Description of the structure of the repository and its contents:

```
├── README.md                           <- The top-level README for reviewers of this project
├── stock_market                        <- Narrative documentation of analysis in Jupyter notebook
├── Presentation.pdf                    <- PDF version of project presentation
├── data                                <- Both sourced externally and generated from code
└── images                              <- Both sourced externally and generated from code
```