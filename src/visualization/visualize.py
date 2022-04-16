
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
import pickle
from models.train_model import train


df = pd.read_csv('../data/raw/Wednesday-workingHours.pcap_ISCX.csv')

X_train, X_test, y_train, y_test , y_pred  = train(df)
loaded_model = pickle.load(open('..\models\model.pkl', 'rb'))
y_pred = loaded_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
f = sns.heatmap(cm, annot=True, fmt='d')