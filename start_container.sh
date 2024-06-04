#!/bin/bash
set -e

docker pull -t lekhana2004/django-code-build:latest
echo

docker run -d -p 8000:8000 lekhana2004/django-code-build:latest
echo