<h1 align="center">📌 Flask Todo REST API</h1>

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue)

![pip](https://img.shields.io/badge/pip-%2320232a?style=for-the-badge&logo=pypi&logoColor=3775A9)
![python](https://img.shields.io/badge/python-%2320232a?style=for-the-badge&logo=python&logoColor=3776AB)
![Flask](https://img.shields.io/badge/flask-%2320232a?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2320232a?style=for-the-badge&logo=sqlite&logoColor=white)
![Swagger](https://img.shields.io/badge/swagger-%2320232a?style=for-the-badge&logo=swagger&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-%2320232a?style=for-the-badge&logo=pytest&logoColor=white)
![MiniConda](https://img.shields.io/badge/miniconda-%2320232a?style=for-the-badge&logo=anaconda&logoColor=green)

</div>

A simple, **RESTful API** for managing **Todo items** using **Flask** and **SQLite**. Supports **CRUD operations**, Swagger API documentation, and unit testing.

## 🚀 Features

✅ **Flask** backend with RESTful design\
✅ **SQLite** database (without SQLAlchemy)\
✅ **CRUD operations** (Create, Read, Update, Delete)\
✅ **Swagger API documentation** via **Flasgger**\
✅ **Unit tests** using **pytest**\
✅ **Blueprints** for structured routes\
✅ **Error handling & validation**

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create a Virtual Environment

#### Using Conda (Recommended)

```bash
conda create --name myenv python=3.9 -y
conda activate myenv
```

#### Using venv (Alternative)

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Flask App

```bash
# if using conda
conda run app.py
```

or

```bash
python app.py
```

🚀 The server will start at **`http://127.0.0.1:5000/`**

## 🔥 API Endpoints

### 📌 **Todo CRUD Endpoints**

| Method   | Endpoint      | Description            |
| -------- | ------------- | ---------------------- |
| `GET`    | `/todos/`     | Retrieve all todos     |
| `POST`   | `/todos/`     | Create a new todo      |
| `GET`    | `/todos/<id>` | Retrieve a single todo |
| `PUT`    | `/todos/<id>` | Update a todo          |
| `DELETE` | `/todos/<id>` | Delete a todo          |

## 📜 API Documentation

Swagger UI is available at:

**`http://127.0.0.1:5000/apidocs/`**

---

## ✅ Running Unit Tests

To run tests with `pytest`:

```bash
pytest test_api.py
```

or

```bash
python -m unittest test_api.py
```

---

## 🛠 Built With

- **Flask** - Python microframework
- **SQLite3** - Lightweight database
- **Flasgger** - Swagger UI for API docs
- **pytest** - Testing framework
