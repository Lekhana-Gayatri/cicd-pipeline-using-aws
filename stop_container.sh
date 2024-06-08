#!/bin/bash
set -e

# Stop the running container (if any)
CONTAINERID=$(docker ps -q --filter "label=demoBuildContainer")
docker stop $CONTAINERID
docker rm $CONTAINERID
echo "Container stopped and removed"
echo "Hi"
