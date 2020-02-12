#!/bin/bash

git pull
sudo docker rm -f neo3-backend
sudo docker rmi neo3-back
sudo docker build -t neo3-back .
sudo docker run -it --name=neo3-backend  --net=host neo3-back
