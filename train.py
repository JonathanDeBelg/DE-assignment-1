
import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

MODEL_PATH = "model.pkl"

print("Loading data...")
X, y = load_iris(return_X_y=True, as_frame=True)

print("Building & training model...")
model = LogisticRegression(max_iter=100_000)
model.fit(X,y)

print(f"Saving model to \"{MODEL_PATH}\"...")
with open(MODEL_PATH,"wb") as f:
    pickle.dump(model,f)

print("Done.")


# from typing import NamedTuple, Dict
# import pandas as pd
# from keras.layers import Dense
# from keras.models import Sequential
# import logging 
# import sys

# logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# local_file = './static/full_data.csv'
# dict_from_csv = pd.read_csv(local_file, index_col=None, squeeze=True).to_dict()
# logging.info('Returning Data as Dictionary Object!')

# df = pd.DataFrame.from_dict(dict_from_csv)  

# logging.info(df.columns)
    
# # split into input (X) and output (Y) variables
# X = df.loc[:, ["sepal length (cm)","sepal width (cm)","petal length (cm)","petal width (cm)"]].values
# Y = df['target']
# # define model

# print(X)
# print(Y)

# model = Sequential()
# model.add(Dense(12, input_dim=4, activation='relu'))
# model.add(Dense(4, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))
# # compile model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# # Fit the model

# # model.fit(X, Y, epochs=150, batch_size=10, verbose=0)

# # scores = model.evaluate(X, Y, verbose=0)
# # logging.info(model.metrics_names)
# # metrics = {
# #     "accuracy": scores[1],
# #     "loss": scores[0],
# # }
# # print(metrics)