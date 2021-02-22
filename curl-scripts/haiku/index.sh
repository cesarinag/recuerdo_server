curl "http://localhost:8000/haikus/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
