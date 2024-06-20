# Flask MySQL Connection Checker


### Files Description
- `app.py`: Main application file containing the Flask app and the database check endpoint.
- `config.py`: Configuration file for storing database connection settings.
- `requirements.txt`: List of dependencies required for the project.
- `run.py`: Entry point for running the Flask application.
- `README.md`: Documentation for the project.

## Prerequisites

- Python 3.x
- MySQL Server
- Virtual environment tool (optional but recommended)

## Setup and Installation

### Step 1: Clone the Repository
```sh
git clone <repository-url>
cd flask_mysql_app


### Step 2: Create and Activate Virtual Environment
```sh
python -m venv venv
```
- On Windows:
  ```sh
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```sh
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Configure Database Settings
Update the `config.py` file with your MySQL database settings:
```python
import os

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'your_user')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'your_password')
    MYSQL_DB = os.getenv('MYSQL_DB', 'testdb')
    
    ORACLE_HOST = 'localhost'
    ORACLE_PORT = '1521'
    ORACLE_USER = 'oracle_user'
    ORACLE_PASSWORD = 'oracle_password'
    ORACLE_DB = 'XE'

    TERADATA_HOST = 'localhost'
    TERADATA_USER = 'teradata_user'
    TERADATA_PASSWORD = 'teradata_password'
    TERADATA_DB = 'dbc'

    HIVE_HOST = 'localhost'
    HIVE_PORT = 10000
    HIVE_USER = 'hive_user'
    HIVE_PASSWORD = 'hive_password'
    HIVE_DB = 'default'
```

### Step 5: Run the Application
```sh
python run.py
```

### Step 6: Test the API
Open your web browser or use a tool like `curl` or Postman to test the endpoint:
```sh
curl http://127.0.0.1:5000/check_db
```

## API Endpoint

### Check Database Connection
- **URL**: `/check_db` `/check_oracle` `/check_teradata` `/check_hive`
- **Method**: `GET`
- **Response**:
  - Success: `{"status": "Database online"}`
  - Failure: `{"status": "Database offline", "error": "<error_message>"}`
