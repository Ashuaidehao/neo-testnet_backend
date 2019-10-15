#!/bin/bash

git pull
git checkout master-2.x
sudo docker rm -f neo2-backend
sudo docker rmi neo2-back
sudo docker build -t neo2-back .
sudo docker run -it  --name=neo2-backend  --net=host neo2-back

