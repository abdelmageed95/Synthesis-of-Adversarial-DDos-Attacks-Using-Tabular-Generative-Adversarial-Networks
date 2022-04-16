
from features_extraction import extraction
from attack_producer import send_attack_to_logstash , instantiate_kafka_producer

producer = instantiate_kafka_producer()

def consume_traffic(predication_model , consumer , size):
    bengin = []
    all_predictions = []
    for index ,msg in enumerate(consumer):
        if index < size:
            txt = msg.value.decode()
            li ,arr = extraction(txt)
            pred_attack = predication_model.predict(arr)
            confidence_score = round(predication_model.predict_proba(arr)[0][pred_attack[0]], 2)
            row = li
            row.append(pred_attack[0])
            row.append(confidence_score)
            all_predictions.append(row)
            if pred_attack[0] == 1 :
                row = [str(i) for i in row]
                send_attack_to_logstash(row , producer) 
            else :
                bengin.append(row)
            print("index : {}  label : {}".format(index , pred_attack[0]))

        else :
            break
      
    return bengin , all_predictions
