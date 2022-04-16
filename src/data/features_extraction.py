
import numpy as np 

def extraction(txt):
    li = txt.split(",")
    li = [ i  for i in li]
    index = [17, 4, 16,  58, 56 , 46, 44, 14 , 71 , 45]
    wil_sent = [0,1,2,3,17, 4, 16,  58, 56 , 46, 44, 14 , 71 , 45]
    will_sent = [li[i] for i in wil_sent ]
    most_im = [ li[i] for i in index ]
    arr = np.array(most_im)
    arr = arr.reshape(1,-1)
    return  will_sent , arr 



def feature_names():
     feature_names = ['Flow_ID','Source_IP' ,'Source_Port','Destination_IP' ,'Bwd_Packet_Length Std', 'Destination_Port', 'Bwd_Packet_Length_Mean', 'Avg_Bwd_Segment_Size',
                      'Average_Packet_Size', 'Packet_Length_Variance', 'Packet_Length_Mean', 'Bwd_Packet_Length_Max',
                      'Init_Win_bytes_backward', 'Packet_Length_Std', 'predict','confidence_score']

     return feature_names

def all_feature_names():
    all_feature_names = [' Destination Port', 
        ' Flow Duration',
         ' Total Fwd Packets',
       ' Total Backward Packets',
        'Total Length of Fwd Packets',
       ' Total Length of Bwd Packets',
        ' Fwd Packet Length Max',
       ' Fwd Packet Length Min',
        ' Fwd Packet Length Mean',
       ' Fwd Packet Length Std', 
       'Bwd Packet Length Max',
       ' Bwd Packet Length Min', 
       ' Bwd Packet Length Mean',
       ' Bwd Packet Length Std',
        'Flow Bytes/s', 
        ' Flow Packets/s',
       ' Flow IAT Mean',
        ' Flow IAT Std', 
        ' Flow IAT Max',
        ' Flow IAT Min',
       'Fwd IAT Total',
       ' Fwd IAT Mean', ' Fwd IAT Std', ' Fwd IAT Max',
       ' Fwd IAT Min', 'Bwd IAT Total', ' Bwd IAT Mean', ' Bwd IAT Std',
       ' Bwd IAT Max', ' Bwd IAT Min', 'Fwd PSH Flags', ' Bwd PSH Flags',
       ' Fwd URG Flags', ' Bwd URG Flags', ' Fwd Header Length',
       ' Bwd Header Length', 'Fwd Packets/s', ' Bwd Packets/s',
       ' Min Packet Length', ' Max Packet Length', ' Packet Length Mean',
       ' Packet Length Std', ' Packet Length Variance', 'FIN Flag Count',
       ' SYN Flag Count', ' RST Flag Count', ' PSH Flag Count',
       ' ACK Flag Count', ' URG Flag Count', ' CWE Flag Count',
       ' ECE Flag Count', ' Down/Up Ratio', ' Average Packet Size',
       ' Avg Fwd Segment Size', ' Avg Bwd Segment Size',

       ' Fwd Header Length.1', 'Fwd Avg Bytes/Bulk', ' Fwd Avg Packets/Bulk',
       ' Fwd Avg Bulk Rate', ' Bwd Avg Bytes/Bulk', ' Bwd Avg Packets/Bulk',
       'Bwd Avg Bulk Rate', 'Subflow Fwd Packets', ' Subflow Fwd Bytes',
       ' Subflow Bwd Packets', ' Subflow Bwd Bytes', 'Init_Win_bytes_forward',
       ' Init_Win_bytes_backward', ' act_data_pkt_fwd',
       ' min_seg_size_forward', 'Active Mean', ' Active Std', ' Active Max',
       ' Active Min', 'Idle Mean', ' Idle Std', ' Idle Max', ' Idle Min',
       ' Label' , 'confidence_score']
    return all_feature_names