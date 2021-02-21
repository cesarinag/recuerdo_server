curl "http://localhost:8000/haiku/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
