# FastAPI CRUD Application

A basic CRUD API built using FastAPI, demonstrating modular route handling, validation, and clean branching workflow.

# Team Members
- Satyajeet Upadhyay
- Sourav Kumar 

# Features

- **Create User (POST)** → Name & Phone number
- **Get Users (GET)** → List all users
- **Update User (PATCH)** → Update name for an existing phone
- **Delete User (DELETE)** → Remove user by phone number
- **Validation & Error Handling**:
  - Phone number must be **exactly 10 digits** (no letters, no special characters)
  - Name must be **alphabetic only** (e.g., `Satyajeet`, not `Satyaje4t`)

# Project Structure
```
fastapi-crud-app/
├── app/
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   └── routes/
│       ├── create_user.py   # POST endpoint
│       ├── get_user.py     # GET endpoint
│       ├── update_user.py   # PATCH endpoint
│       └── delete_user.py   # DELETE endpoint
├── requirements.txt
├── README.md
```

# Setup Instructions

# 1.Clone the Repository
git clone <repository-url>
cd fastapi-crud-app
# 2.Create Virtual Environment
python3 -m venv venv
source venv/bin/activate   
# 3.Install Dependencies
pip install fastapi uvicorn

# Branching Workflow
| Branch Name     | Description                                                       |
| --------------- | ----------------------------------------------------------------- |
| `dev/satyajeet` | Created **POST** and **DELETE** routes, `main.py`                 |
| `dev/sourav`    | Created **PATCH** and **GET** routes, `models.py` with validation |

# Running the App
uvicorn app.main:app --reload

# Validation & Error Handling
| Input Field | Validation                                      | Error Message                          |
| ----------- | ----------------------------------------------- | -------------------------------------- |
| `phone`     | Must be **10 digits only** (e.g., `9876543210`) | `"Please enter a valid phone number."` |
| `name`      | Must contain **alphabets only** (e.g., `Alice`) | `"Please enter a valid name."`         |

# API Endpoints
| Method | Endpoint         | Description          |
| ------ | ---------------- | -------------------- |
| POST   | `/users`         | Create a new user    |
| GET    | `/users`         | List all users       |
| PATCH  | `/users/{phone}` | Update user name     |
| DELETE | `/users/{phone}` | Delete user by phone |

#




