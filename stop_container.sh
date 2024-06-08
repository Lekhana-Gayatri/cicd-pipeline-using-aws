#!/bin/bash
set -e

# Stop the running container (if any)
CONTAINERID=$(docker ps -q --filter "label=demoBuildContainer")
echo "Found container ID: $CONTAINERID"

if [ -n "$CONTAINERID" ]; then
  docker stop $CONTAINERID
  docker rm $CONTAINERID
  echo "Container stopped and removed"
else
  echo "No container found with label demoBuildContainer"
fi

echo "Hi"
