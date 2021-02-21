curl "http://localhost:8000/haiku/${ID}/" \
  --include \
  --request PATCH \
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
