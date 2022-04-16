
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle


df = pd.read_csv('../data/raw/Wednesday-workingHours.pcap_ISCX.csv')

def train(df):
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace = True)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace = True)
    X = df.drop(columns=[' Label']).values
    y = df[' Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, shuffle=True, random_state=123)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    with open('../models/model.pkl','wb') as model_pkl:
        pickle.dump(model, model_pkl, protocol=2)
    y_pred = model.predict(X_test)
    return X_train, X_test, y_train, y_test , y_pred 


X_train, X_test, y_train, y_test , y_pred  = train(df)