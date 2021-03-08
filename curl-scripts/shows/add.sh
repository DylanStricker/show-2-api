#!/bin/bash

curl "http://localhost:8000/myshows/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
      "id": "'"${ID}"'"
  }'
echo
