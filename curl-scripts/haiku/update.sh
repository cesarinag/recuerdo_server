curl "http://localhost:8000/haikus/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "haiku": {
      "fiveone": "'"${FO}"'",
      "seven": "'"${SN}"'",
      "fivetwo": "'"${FT}"'"
    }
  }'

echo
