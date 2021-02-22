curl "http://localhost:8000/haikus/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
