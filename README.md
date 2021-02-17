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
- [Sentimental](#Sentimental)
- [Frontend](#Frontend)
- [Next Steps](#Next-Steps)
- [For More Information](#For-More-Information)
- [Repository Structure](#Repository-Structure)

## Overview
Accurate prediction of stock market asset is a significant and challenging task due to complicated nature of the financial stock markets. Considering the increasing availability and affordability of powerful computational engines, deep learning methods of prediction have proved its efficiency in finance.


## Business Understanding

My capstone project is Stock market Prediction. I’m going to build a time series regression model using NN or other advanced techniques to predict the stock market. Stock market prediction aims to determine the future movement of the stock value of a financial exchange. My project is helpful for Stock investors and investment banks to have a better understanding in developing economical Strategy and in making financial decisions.




## Data Collection
Collected data from three different web sources by using webscraping or API calls.

    - [Quarterly Report](https://finance.yahoo.com/quote/AAPL/financials?p=AAPL) for Classification by Web Scrapping 
    - [Yahoo Finance](https://github.com/ranaroussi/yfinance) and [IEX API](https://iexcloud.io) for Time Series data by API calls
    - Twitter for sentimental data


## Exploratory Data Analysis
    - Fundamental data was cleaned and formatted into a Pandas DataFrame.
    - Time series data was downloaded as daily data then resampled into weekly and monthly intervals.
    - Sentimental data was formatted into a Pandas DataFrame.
    
Trade Strategy: local minimum to buy, local maximum to sell, other time to hold.

![graph](/images/trade.jpeg)

![graph](/images/ohlc.jpeg)



## Classification

Fundamental data was then used to train several different classification models.



## Time-Series
Time series data was fitted and trained to two time series models. All models are evaluated by RMSE and MAE.

SARIMAX Model with exogenous features

![graph](/images/SARIMAX.jpeg)

Facebook Prophet

![graph](/images/fbprophet.jpeg)

LSTM

![graph](/images/lstm.jpeg)

## Sentimental

Use NLP & Deep Learning to predict stock prices

## Frontend

Streamlit was used to create a frontend for each form of analysis with their respective machine learning models.

## Next Step
 


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