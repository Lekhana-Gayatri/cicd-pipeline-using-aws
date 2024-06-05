#!/bin/bash
set -e

docker pull lekhana2004/django-code-build:v1
echo

CONTAINERID=$(docker run -d -p 8000:8000 lekhana2004/django-code-build:v1)
echo
