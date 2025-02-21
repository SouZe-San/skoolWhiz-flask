<h1 align="center">skoolWhiz-flask: Todo REST API 📌</h1>

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue)

![python](https://img.shields.io/badge/python-%2320232a?style=for-the-badge&logo=python&logoColor=3776AB)
![pip](https://img.shields.io/badge/pip-%2320232a?style=for-the-badge&logo=pypi&logoColor=3775A9)
![Flask](https://img.shields.io/badge/flask-%2320232a?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2320232a?style=for-the-badge&logo=sqlite&logoColor=white)
![Swagger](https://img.shields.io/badge/swagger-%2320232a?style=for-the-badge&logo=swagger&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-%2320232a?style=for-the-badge&logo=pytest&logoColor=white)
![MiniConda](https://img.shields.io/badge/miniconda-%2320232a?style=for-the-badge&logo=anaconda&logoColor=green)

</div>

A simple **RESTful API** for managing **Todo items** using **Flask** and **SQLite**. Supports **CRUD operations**, Swagger API documentation, and unit testing.

---

## 🚀 Features

✅ **Flask** backend with RESTful design\
✅ **SQLite** database (without SQLAlchemy)\
✅ **CRUD operations**\
✅ **Swagger API documentation**\
✅ **Unit tests** using **pytest**\
✅ **Error handling & validation**

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SouZe-San/skoolWhiz-flask.git
cd skoolWhiz-flask
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
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Flask App

```bash
python app.py
```

🚀 The server will start at **`http://127.0.0.1:5000/`**

---

## 🔥 API Endpoints

### 📌 **Todo CRUD Endpoints**

| Method   | Endpoint      | Description            |
| -------- | ------------- | ---------------------- |
| `GET`    | `/`           | Api Check              |
| `GET`    | `/todos/`     | Retrieve all todos     |
| `POST`   | `/todos/`     | Create a new todo      |
| `GET`    | `/todos/:id`  | Retrieve a single todo |
| `PUT`    | `/todos/:id`  | Update a todo          |
| `DELETE` | `/todos/:id`  | Delete a todo          |

---

## 📜 API Documentation

Swagger UI is available at:

**`http://127.0.0.1:5000/api/docs/`**

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
- **Swagger UI** - API documentation
- **pytest** - Testing framework
- **Logging** - Integrated logging for debugging

---

## 📂 Project Structure

```
📂 root/
├── 📂 src/
|   |---📂 routes/
│   |   ├── routes.py    # API routes & CRUD controllers
│   ├── database.py      # DB initialization & connection
├── 📂 utils/
│   ├── schema_sql.py    # Database schema
│   ├── test_api.py      # Unit tests
├── app.py               # Main application entry point
├── requirements.txt     # Dependencies list
└── README.md            # Project documentation
```
