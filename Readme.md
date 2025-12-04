# 💰 Expense Tracker

A simple Flask-based expense tracking application with category management and date filtering capabilities.

## Features

- ✅ Add, view, and delete expenses
- ✅ Manage custom categories
- ✅ Filter expenses by category and date range
- ✅ Calculate running totals
- ✅ Clean Bootstrap UI
- ✅ SQLite database (no external database required)

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

### For macOS

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/dzonasm/sekimas.git
   cd sekimas
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   
   Navigate to: `http://127.0.0.1:5000`

### For Windows

1. **Clone or download the repository**
   ```cmd
   git clone https://github.com/dzonasm/sekimas.git
   cd sekimas
   ```

2. **Create a virtual environment**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```cmd
   pip install flask flask-sqlalchemy
   ```

4. **Run the application**
   ```cmd
   python app.py
   ```

5. **Open your browser**
   
   Navigate to: `http://127.0.0.1:5000`

## Project Structure

```
expense-tracker/
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   ├── base.html      # Main expenses page
│   └── categories.html # Category management page
└── instance/
    └── expenses.db    # SQLite database (auto-created)
```
