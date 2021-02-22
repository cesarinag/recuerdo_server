curl "http://localhost:8000/haikus/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
