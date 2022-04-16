docker-compose -f docker-compose.yml up -d
rem docker-compose -f docker_compose_ELK.yml up -d
rem -f kafkalogstash.conf up -d
rem timeout /t 5
docker exec kafka /bin/bash -c "cd /opt/kafka/bin; kafka-topics.sh --create --topic GANs_raw --bootstrap-server localhost:9092"
docker exec kafka /bin/bash -c "cd /opt/kafka/bin; kafka-topics.sh --create --topic GANs_raw_predictions --bootstrap-server localhost:9092"
pip install -r requirements.txt
python data_ingestion_script.py

