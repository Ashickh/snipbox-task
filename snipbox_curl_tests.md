
# 🧪 SnipBox API - CURL Test Collection

Below are sample curl commands for testing each API endpoint.

---

## 🔐 Authentication

### Login (Obtain Token)
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "yourusername", "password": "yourpassword"}'
```

### Refresh Token
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your_refresh_token"}'
```

---

## 📋 Snippet Endpoints

> ⚠️ Replace `<ACCESS_TOKEN>` with the JWT token.

### Overview - List All Snippets
```bash
curl -X GET http://localhost:8000/api/snippets/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

### Create a New Snippet
```bash
curl -X POST http://localhost:8000/api/snippets/create/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"title": "First Snippet", "note": "Hello World!", "tag": "Work"}'
```

### Get Snippet Detail
```bash
curl -X GET http://localhost:8000/api/snippets/1/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

### Update Snippet
```bash
curl -X PUT http://localhost:8000/api/snippets/1/update/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Title", "note": "Updated note content", "tag": "UpdatedTag"}'
```

### Delete Snippet
```bash
curl -X DELETE http://localhost:8000/api/snippets/1/delete/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

---

## 🏷️ Tag Endpoints

### List All Tags
```bash
curl -X GET http://localhost:8000/api/tags/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

### Get Snippets by Tag
```bash
curl -X GET http://localhost:8000/api/tags/1/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```
