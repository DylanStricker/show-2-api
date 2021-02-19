#!/bin/bash

curl "http://localhost:8000/shows/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
