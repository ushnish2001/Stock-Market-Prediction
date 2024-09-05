{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from sklearn.model_selection import train_test_split\
\
# Prepare dataset\
X, Y = create_dataset(scaled_data, time_step=60)\
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, shuffle=False)\
\
# Reshape data to fit LSTM input\
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))\
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))\
\
# Build and train model\
model = build_lstm_model((X_train.shape[1], 1))\
model.fit(X_train, Y_train, epochs=100, batch_size=32)\
}