curl "http://localhost:8000/haikus/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "haiku": {
      "title": "'"${TITLE}"'",
      "fiveone": "'"${FO}"'",
      "seven": "'"${SN}"'",
      "fivetwo": "'"${FT}"'"
    }
  }'

echo
