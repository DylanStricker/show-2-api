#!/bin/bash

curl "http://localhost:8000/shows/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "title": "'"${TITLE}"'",
    "director": "'"${DIRECTOR}"'",
    "rating": "'"${RATING}"'",
    "description": "'"${DESCRIPTION}"'"
  }'

echo
