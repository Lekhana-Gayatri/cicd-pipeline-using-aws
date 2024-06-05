#!/bin/bash
set -e

# Stop the running container (if any)
cd /opt/codedeploy-agent
sudo rm -r deployment-root
sudo mkdir deployment-root
cd /home/ubuntu
echo "Hi"
