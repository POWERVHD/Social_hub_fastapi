# 🚀 Social Hub FastAPI

A social media API built with FastAPI featuring user accounts, posts, likes, and JWT-based authentication.

---

## 📦 Features

- **User Registration & Authentication**  
  Sign up, log in, and log out using JWT tokens.

- **Post Management**  
  Create, update, delete, fetch all or single posts.

- **Like/Unlike Posts**  
  Vote on posts with proper constraints.

- **Ownership and Access Control**  
  Users can only manage their own posts.

- **Pydantic Schemas**  
  Input validation and response models.

- **Secure Passwords**  
  Passwords hashed using industry-standard mechanisms.

- **Dockerized with Docker Compose**  
  Quick local development environment setup.

---

## 💻 Technology Stack

| Component            | Library / Tool          |
|---------------------|--------------------------|
| Backend Framework   | FastAPI                  |
| Database            | PostgreSQL               |
| ORM                 | SQLAlchemy               |
| Migrations          | Alembic                  |
| Authentication      | OAuth2 JWT               |
| Containerization    | Docker & Docker Compose  |
| Testing             | pytest                   |
| Documentation       | Swagger UI & ReDoc       |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose (optional but recommended)

### Run without Docker

```bash
git clone https://github.com/POWERVHD/Social_hub_fastapi.git
cd Social_hub_fastapi
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

### Run with Docker

```bash
docker-compose up -d --build
```

Visit the app at: `http://localhost:8000`

---

## 🧩 API Documentation

- Swagger UI: `http://localhost:8000/docs`  
- ReDoc: `http://localhost:8000/redoc`

---

## 🧪 Testing

```bash
pytest
```

---

## ⚙ TO DO / Future Improvements

- 🚀 Already deployed on DigitalOcean (but free credits said goodbye 😅) – exploring alternatives like Heroku, AWS, etc.
- Add frontend (React/Vue or Jinja2)
- Implement refresh token
- Add comments support
- Add pagination and filtering
- Admin/moderator roles
- Enhanced error handling

---

## 🙌 Contributing

Contributions are welcome!  
To contribute:

1. Fork the repo  
2. Create a new branch  
3. Make your changes  
4. Submit a Pull Request

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

Made by [KSHITIJ PRASAD]  
- GitHub: [https://github.com/POWERVHD/Social_hub_fastapi](https://github.com/POWERVHD/Social_hub_fastapi)  
- Twitter: [https://x.com/kshitijprasad5](https://x.com/kshitijprasad5)  
- Gmail: kshitijprasad6@gmail.com
