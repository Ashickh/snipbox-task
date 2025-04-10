
# 📝 SnipBox - Backend API

SnipBox is a short note-saving application that allows users to save snippets of text with titles and associate them with reusable tags. It supports user authentication using JWT and offers full CRUD functionality for snippets and tags.

## 🚀 Features

- 🔐 JWT Authentication (Login + Token Refresh)
- ✍️ Create, Read, Update, Delete snippets
- 🏷️ Reusable tagging system
- 👤 User-specific snippet access
- 📦 API responses follow REST best practices
- 🧪 Test cases and sample requests included

## 📁 Project Structure

```
snipbox/
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests/
├── snipbox/
│   └── settings.py
├── manage.py
├── requirements.txt
├── README.md
└── docker-compose.yml (if added)
```

## 🛠️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/your-username/snipbox.git
cd snipbox
```

2. **Create and activate a virtual environment**
```bash
pipenv shell
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Create a superuser**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

## 🔐 Authentication

SnipBox uses **JWT authentication** via Simple JWT.

- **Login**: `POST /api/token/`
- **Refresh**: `POST /api/token/refresh/`

## 🧪 API Endpoints

| Method | Endpoint                     | Description                        |
|--------|------------------------------|------------------------------------|
| POST   | `/api/token/`                | Login (obtain JWT)                 |
| POST   | `/api/token/refresh/`        | Refresh access token               |
| GET    | `/api/snippets/`             | Overview - list all user snippets |
| POST   | `/api/snippets/create/`      | Create a new snippet               |
| GET    | `/api/snippets/<id>/`        | Detail view of snippet             |
| PUT    | `/api/snippets/<id>/update/` | Update a snippet                   |
| DELETE | `/api/snippets/<id>/delete/` | Delete a snippet                   |
| GET    | `/api/tags/`                 | List all tags                      |
| GET    | `/api/tags/<id>/`            | Snippets linked to a tag           |

> 💡 All endpoints require JWT `Authorization: Bearer <token>` header.

## 🧾 Requirements

```
Django>=4.2
djangorestframework
djangorestframework-simplejwt
```

## 🧪 Test Snippets

Include curl or Postman collection in the `tests/` folder.

## 🗂️ ER Diagram

Describe or link the database schema here.

## 🐳 Docker (Optional)

If Docker is used:
```bash
docker-compose up --build
```

## 🧹 Code Standards

- PEP-8 compliant
- Each feature committed separately with meaningful commit messages

## 📬 Contact

_Contributor: [Your Name]_  
_GitHub: https://github.com/your-username/snipbox_
