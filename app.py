import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

from keras.models import Model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler



st.title('Stock Market Prediction')


@st.cache
def data_load(stock):
    '''
    Loads the stock we want to predict
    '''
    tick = yf.Ticker(stock)
    # get historical market data
    data = tick.history(period="max")
    data = data.reindex(pd.date_range(data.index[0], data.index[-1], freq='D')).interpolate()
    
    return data



def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)





def main():
    '''
    The main code for Streamlit
    '''
    #allows us to Pick what page we want to be on
    st.sidebar.title("type in the stock you want to predict")
    stock = st.sidebar.text_input('stock name', 'Type Here')
    
    app_mode = st.sidebar.selectbox("Choose how many months to predict", [ "one month", "two months", "three months"])

    
      

    if app_mode == "one month":
        time = 30
    elif app_mode == "two months":
        time = 60           
    elif app_mode == "three months":
        time = 90
        
    if stock != 'Type Here':
        
        df = data_load(stock)    

        df_lstm = pd.DataFrame()
        df_lstm['close'] = df.Close

        #df_lstm = df_lstm.reindex(pd.date_range(df_lstm.index[0], df_lstm.index[-1]+datetime.timedelta(days=time), freq='D')).interpolate()
    
        scaler = MinMaxScaler(feature_range=(0, 1))
        dataset = scaler.fit_transform(df_lstm)
    
        train, test = dataset[:-time], dataset[-time:]
        look_back = 1
        trainX, trainY = create_dataset(train, look_back)
        testX, testY = create_dataset(test, look_back)

        trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
        testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

        model = Sequential()
        model.add(LSTM(4, input_shape=(1, look_back)))
        model.add(Dense(1))
        model.compile(loss='mean_squared_error', optimizer='adam')
        model.fit(trainX, trainY, epochs=1, batch_size=1, verbose=0)

        trainPredict = model.predict(trainX)
        testPredict = model.predict(testX)

        trainPredict = scaler.inverse_transform(trainPredict)
        trainY = scaler.inverse_transform([trainY])
        testPredict = scaler.inverse_transform(testPredict)
        testY = scaler.inverse_transform([testY])

    
    
        trainPredictPlot = np.empty_like(dataset)
        trainPredictPlot[:, :] = np.nan
        trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
        # shift test predictions for plotting
        testPredictPlot = np.empty_like(dataset)
        testPredictPlot[:, :] = np.nan
        testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict
        # plot baseline and predictions
        fig, ax = plt.subplots()
        ax.plot(df_lstm.index, scaler.inverse_transform(dataset), label='original')
        ax.plot(df_lstm.index, trainPredictPlot,label='trian prediction')
        ax.plot(df_lstm.index, testPredictPlot,label='test prediction')
        ax.set_xlabel('Date')
        ax.set_ylabel('Close Price')
        ax.set_title(f'{app_mode} price prediction')
        ax.legend()

        st.pyplot(fig)

        lstm = pd.DataFrame(testPredictPlot[-time+1:-1])
        lstm.index = df_lstm.index[-time+1:-1]
        lstm.index.name = 'Date'
        lstm.columns = ['price']
    
        st.table(lstm)
    

if __name__ == "__main__":
    main()
