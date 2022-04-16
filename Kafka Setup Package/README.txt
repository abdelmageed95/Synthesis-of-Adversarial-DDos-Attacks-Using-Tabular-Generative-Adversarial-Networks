Please follow the below steps for setting up kafka and zookeeper using Docker-Compose

1. Make sure that you have Docker and Docker-Compose installed on your system. You can download Docker from here: https://docs.docker.com/get-docker/ (Docker comes packaged with docker-compose, no need to install it separately)
2. Also make sure that python and pip are installed on your system.
2. Paste the files provided (aggregated_data.csv, data_ingestion_script.py, docker-compose.yml, docker_script.sh, docker_script.bat, requirements.txt) into a common folder.
3. Run the docker_script file depending upon the operating system. If you are using windows then run the docker_script.bat file otherwise run the docker_script.sh file on Linux/MacOS.

Special Notes:
1. If you face issues in running .bat or .sh file, try the following: simply copy and paste the commands one-by-one in your terminal.
2. If you face issues related to ports being busy for some other processes, simply kill the process which is using the respective port.
3. If you face any other issues, check it on stackoverflow or just google it.
