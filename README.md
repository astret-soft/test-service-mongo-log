# Service mongo log (Arrival interview)

## Launch with dockers:
* Build docker image for service
```docker build -t service-mongo-log:0.1 -f docker/Dockerfile .```
* Build docker image for vehicle emulator
```docker build -t vehicle-emulator:1.0 -f vehicleEmulator/Dockerfile .```
* Pull docker image for mongodb
```docker pull mongo:4.0.4```
* Start docker compose
```docker-compose -f docker/compose/docker-compose.yml up -d```
* Touch REST API
```
curl --request GET --url 'http://127.0.0.1:65333/logs'
curl --request GET --url 'http://127.0.0.1:65333/logs?offset=0&limit=10'
curl --request GET --url 'http://127.0.0.1:65333/logs?offset=10&limit=10'
curl --request GET --url 'http://127.0.0.1:65333/logs?limit=10&last=5ee736d9eb72c7f9b3eabee2'
```

## Launch for debugging:
* Build docker image for vehicle emulator and pull image for mongodb. Launch them.
```
docker build -t vehicle-emulator:1.0 -f vehicleEmulator/Dockerfile .
docker pull mongo:4.0.4

docker run -d -p 27017:27017 mongo:4.0.4
docker run -d -p 8080:8080 vehicle-emulator:1.0
```
* Setup venv(optional) with Python 3.7.6 and install requirements
```
pip install -r app/requirements.txt
```
* Check code by pylint
```
pylint "--msg-template='{abspath}:{line:5d}:{column}: {msg_id}: {msg} ({symbol})'" --output-format=colorized --rcfile .pylintrc service-mongo-log/app
```
* Launch server
```
cd app
python3 main.py 
```