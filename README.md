<p>
<img src="images/Coronavirus.jpg" width="900" height="585">
</p>

# Coronavirus Prediction

**Authors**: Ning Chen, Elliot Macy

## Overview
The goal of this project is to investigate Coronavirus and make related predictions in regard to time series modeling. The data is accessed by public APIs. Machine learning and deep learning methods such as ARMA, ARIMA, SARIMAX, Facebook PROPHET, Recurrent Neural Network and Long short-term memory (LSTM) Networks are implemented and evaluated.


## Business Understanding

The prediction problem of Coronavirus comes with a significant degree of ambiguity, which is difficult to predict considering the complex circumstances in the real world. While one important task in this project is understanding time series modeling and forecasting related rates for the decision makers to layout some strategies in dealing with covid-19.




## Data Understanding
The Coronavirus data is accessed by open public APIs without authentication. It provides updated information associated with COVID-19. The public data [API](https://github.com/ghcn345/Coronavirus-Research) provides access to all of the data at a national and state level. The death cases, positive cases and mortality are studied to make further predictions. 


## Data Preparation
ACF and PACF 

![graph](/images/acf.jpeg)


## Modeling

SARIMAX Model 

![graph](/images/sarimax.jpeg)

death prediction 

![graph](/images/death.jpeg)

## Evaluation
All models are evaluated by RMSE and MAE.

![graph](/images/lstm.jpeg)

## Conclusion
1. LSTM Networks serve as the best model for coronavirus prediction with small RMSE and MAE. 
2. SARIMAX with opitmized hyperparameters by Gridsearch also work well for the prediction. 
3. Due to limited known condtions, it is difficult to make precise predictions. 
4. It shows less death and positive cases at weekends and more cases on Monday.


## For More Information

Please review our full analysis in [our Jupyter Notebook](https://github.com/ghcn345/Coronavirus-Prediction/blob/master/project_coronavirus.ipynb) or our [presentation](https://github.com/ghcn345/Coronavirus-Prediction/blob/master/Presentation.pdf).

For any additional questions, please contact **Ning Chen—chen.ning345@gmail.com, Elliot Macy—elimacy@gmail.com**.

## Repository Structure

Description of the structure of the repository and its contents:

```
├── README.md                           <- The top-level README for reviewers of this project
├── project_coronavirus                 <- Narrative documentation of analysis in Jupyter notebook
├── death_grid                          <- pickle to store the optimized results by Gridsearch
├── Presentation.pdf                    <- PDF version of project presentation
├── data                                <- Both sourced externally and generated from code
└── images                              <- Both sourced externally and generated from code

```
