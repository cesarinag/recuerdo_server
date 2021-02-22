curl "http://localhost:8000/haiku/" \
  --include \
  --request POST \
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
