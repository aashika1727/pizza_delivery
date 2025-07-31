
#  Pizza Delivery API – FastAPI Project

A backend API built with FastAPI and MySQL to manage pizza orders, customers, and menu items. This project follows a modular and scalable design.

---

##  Features

- Create & manage customers
- Add and view pizza menu items
- Place orders with multiple pizzas
- Track and update order status
- Uses FastAPI, SQLAlchemy, Pydantic, and MySQL
- Secure environment variables via `.env`

---

##  Tech Stack

- **Backend**: FastAPI  
- **Database**: MySQL  
- **ORM**: SQLAlchemy  
- **Validation**: Pydantic  
- **Environment Handling**: python-dotenv

---

##  Project Structure

```
pizza_delivery/
├── app/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routers/
│   ├── schemas.py
├── init_db.py
├── requirements.txt
└── README.md
```

---

##  How to Run Locally

1. Clone the repo  
2. Create a virtual environment and activate it  
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your `.env` file with:

```ini
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=pizza_db
```

5. Initialize the database:

```bash
python init_db.py
```

6. Run the server:

```bash
uvicorn app.main:app --reload
```

---

##  API Endpoints


| Method | Endpoint              | Description           |
|--------|-----------------------|-----------------------|
| POST   | `/customers/`         | Create customer       |
| GET    | `/customers/{id}`     | Get customer info     |
| POST   | `/menu/`              | Add menu item         |
| GET    | `/menu/`              | View all menu items   |
| POST   | `/orders/`            | Place new order       |
| PUT    | `/orders/{id}/status` | Update order status   |




