#!/bin/bash

curl "http://localhost:8000/shows/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
