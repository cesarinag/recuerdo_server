curl "http://localhost:8000/haiku/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "haiku": {
      "five1": "'"${FIVE1}"'",
      "seven": "'"${SEVEN}"'",
      "five2": "'"${FIVE2}"'"
    }
  }'

echo
