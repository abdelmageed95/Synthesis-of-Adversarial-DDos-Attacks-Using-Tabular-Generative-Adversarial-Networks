#Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
from kafka import KafkaConsumer
import pickle
from consume_data import consume_traffic
import pandas as pd 
from features_extraction import  feature_names

consumer = KafkaConsumer('GANs_raw', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
loaded_model = pickle.load(open(r'D:\elg7186-project-group_project_6\models\RF_model.pkl', 'rb'))
# send attack to outout topic , return the bengin df and the predicion df
bengin_lists , all_predictions = consume_traffic(loaded_model , consumer , size = 542327 )


consumed_df = pd.DataFrame( all_predictions , columns= feature_names ())
bengin_df= pd.DataFrame(bengin_lists ,  columns= feature_names ())
consumed_df.to_csv('consumed_df.csv')
bengin_df.to_csv('bengin_df.csv')