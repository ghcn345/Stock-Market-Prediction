<p>
<img src="images/stock-chart.jpeg" width="900" height="600">
</p>

# Stock Market Prediction

**Author**: Ning Chen

## Table of Contents
- [Overview](#Overview)
- [Business Understanding](#Business-Understanding)
- [Data Collection](#Data Collection)
- [Exploratory Data Analysis](#Exploratory Data Analysis)
- [Classification](#Classification)
- [Time Series](#Time-Series)
- [Sentimental](#Sentimental)
- [Streamlit](#Streamlit)
- [Presentation](#Presentation)
- [Next Steps](#Next-Steps)

## Overview
Accurate prediction of stock market asset is a significant and challenging task due to complicated nature of the financial stock markets. Considering the increasing availability and affordability of powerful computational engines, deep learning methods of prediction have proved its efficiency in finance.


## Business Understanding

My capstone project is Stock market Prediction. I’m going to build a time series regression model using NN or other advanced techniques to predict the stock market. Stock market prediction aims to determine the future movement of the stock value of a financial exchange. My project is helpful for Stock investors and investment banks to have a better understanding in developing economical Strategy and in making financial decisions.




## Data Collection

[IEX API](https://iexcloud.io), [Yahoo Finance](https://github.com/ranaroussi/yfinance) and [Quarterly Report](https://finance.yahoo.com/quote/AAPL/financials?p=AAPL) 

## Exploratory Data Analysis

Trade Strategy: local minimum to buy, local maximum to sell, other time to hold.

![graph](/images/trade.jpeg)

![graph](/images/ohlc.jpeg)



## Classification
All models are evaluated by RMSE and MAE.

## Time-Series

SARIMAX Model with exogenous features

![graph](/images/SARIMAX.jpeg)

Facebook Prophet

![graph](/images/fbprophet.jpeg)

LSTM

![graph](/images/lstm.jpeg)

## Next Step
 


## For More Information

Please review our full analysis in [our Jupyter Notebook](https://github.com/ghcn345/Stock-Market-Prediction/blob/master/stock_market.ipynb) or our [presentation](https://github.com/ghcn345/Stock-Market-Prediction/blob/master/Presentation.pdf).

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