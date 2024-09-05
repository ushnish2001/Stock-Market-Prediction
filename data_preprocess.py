{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red183\green111\blue179;\red23\green23\blue23;\red202\green202\blue202;
\red89\green156\blue62;\red212\green212\blue212;\red194\green126\blue101;\red167\green197\blue152;}
{\*\expandedcolortbl;;\cssrgb\c77255\c52549\c75294;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c41569\c66275\c30980;\cssrgb\c86275\c86275\c86275;\cssrgb\c80784\c56863\c47059;\cssrgb\c70980\c80784\c65882;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf4 \strokec4  sklearn.preprocessing \cf2 \strokec2 import\cf4 \strokec4  MinMaxScaler\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  pandas \cf2 \strokec2 as\cf4 \strokec4  pd\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Load data\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 data = pd.read_csv\cf6 \strokec6 (\cf7 \strokec7 'AAPL_stock_data.csv'\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Select features for modeling\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 features = data\cf6 \strokec6 [[\cf7 \strokec7 'Open'\cf6 \strokec6 ,\cf4 \strokec4  \cf7 \strokec7 'High'\cf6 \strokec6 ,\cf4 \strokec4  \cf7 \strokec7 'Low'\cf6 \strokec6 ,\cf4 \strokec4  \cf7 \strokec7 'Close'\cf6 \strokec6 ,\cf4 \strokec4  \cf7 \strokec7 'Volume'\cf6 \strokec6 ]]\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Scale the data\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 scaler = MinMaxScaler\cf6 \strokec6 (\cf4 \strokec4 feature_range=\cf6 \strokec6 (\cf8 \strokec8 0\cf6 \strokec6 ,\cf8 \strokec8 1\cf6 \strokec6 ))\cf4 \cb1 \strokec4 \
\cb3 scaled_data = scaler.fit_transform\cf6 \strokec6 (\cf4 \strokec4 features\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
}