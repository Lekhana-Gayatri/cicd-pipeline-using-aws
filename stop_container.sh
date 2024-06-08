#!/bin/bash
set -e

# Stop the running container (if any)
docker stop $CONTAINERID
docker rm $CONTAINERID
echo "Hi"
