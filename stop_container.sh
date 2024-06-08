#!/bin/bash
set -e

# Stop the running container (if any)
CONTAINERID=$(docker ps -q --filter "label=demoBuildContainer")
echo $CONTAINERID
docker stop $CONTAINERID
docker rm $CONTAINERID
echo "Hi"
