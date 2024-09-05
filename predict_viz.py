{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import matplotlib.pyplot as plt\
\
# Plot actual vs predicted prices\
plt.plot(Y_test, color='blue', label='Actual Stock Price')\
plt.plot(predicted_stock_price, color='red', label='Predicted Stock Price')\
plt.title('Stock Price Prediction')\
plt.xlabel('Time')\
plt.ylabel('Stock Price')\
plt.legend()\
plt.show()\
}