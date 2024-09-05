{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import numpy as np\
from keras.models import Sequential\
from keras.layers import LSTM, Dense, Dropout\
\
# Create sequences of stock data\
def create_dataset(dataset, time_step=1):\
    X, Y = [], []\
    for i in range(len(dataset)-time_step-1):\
        X.append(dataset[i:(i+time_step), 0])\
        Y.append(dataset[i + time_step, 0])\
    return np.array(X), np.array(Y)\
\
# Build LSTM Model\
def build_lstm_model(input_shape):\
    model = Sequential()\
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))\
    model.add(Dropout(0.2))\
    model.add(LSTM(units=50, return_sequences=False))\
    model.add(Dropout(0.2))\
    model.add(Dense(units=1))  # Predict the closing price\
    \
    model.compile(optimizer='adam', loss='mean_squared_error')\
    return model\
}