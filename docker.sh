#!/bin/bash
echo $1 $2 $3

## Ref: https://github.com/mfatihaktas/edge-flow-control/blob/master/docker.sh

DOCKER=docker
IMG_NAME=img-sampler
CONT_NAME=my-img-sampler

if [ $1 = 'b' ]; then
  $DOCKER build -t $IMG_NAME .
elif [ $1 = 'ri' ]; then
  $DOCKER run --name $CONT_NAME -it --rm -p 8080:5000 $IMG_NAME /bin/bash
elif [ $1 = 'rd' ]; then
  $DOCKER run --name $CONT_NAME -d -p 8080:5000 $IMG_NAME
elif [ $1 = 'stop' ]; then
  $DOCKER stop $CONT_NAME
elif [ $1 = 'bash' ]; then
  $DOCKER exec -it $CONT_NAME bash
elif [ $1 = 'lsc' ]; then
  $DOCKER ps --all
elif [ $1 = 'lsi' ]; then
  $DOCKER images
elif [ $1  = 'rm' ]; then
  $DOCKER rm $CONT_NAME
elif [ $1 = 'rmi' ]; then
  $DOCKER image rm $IMG_NAME
else
  echo "Arg did not match!"
fi
