<div align="center">
  <img src="static/logo.jpg" alt="FinTrack Logo" width="150"/>
  <h1>FinTrack</h1>
  <p><em>A full stack expense and budget tracker built to learn the fundamentals.</em></p>
</div>

**Live Demo:** [fintrack-iudq.onrender.com](https://fintrack-iudq.onrender.com) (Hosted on Render's free tier, so it may take a few seconds to spin up on initial load.)

## About

FinTrack is a web application that helps users track their monthly incomes and expenses. It was originally built as my final project for Harvard's CS50x course to practice building a full-stack application from scratch. The project is a technical exercise in implementing core features like schema design, user authentication, and data validation. It is not intended to be a commercial product, but rather a functional demonstration of web development fundamentals.

## Features

- **User Accounts:** Register, log in, and log out securely. Real-time availability checks for usernames.
- **Transaction Management:** Add income and expense transactions with specific dates, categories, and descriptions.
- **Transaction History:** View all past transactions and delete them if a mistake was made.
- **Budgeting:** Set monthly budget limits for different categories and track spending against those limits.
- **Dashboard:** View current balance and recent transactions at a glance.
- **Reports:** View monthly income versus expense summaries and top spending categories.
- **Preferences:** Update account password and change the preferred display currency.
- **Premium Interface:** Features a responsive, Apple-style glassmorphic UI with dynamic color transitions and smooth scrolling.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Database | SQLite |
| Auth | Werkzeug, Flask-Session |
| Frontend | HTML, CSS, Jinja2, Bootstrap 5 |
| Deployment| Gunicorn |

## Architecture

FinTrack uses a monolithic Model-View-Controller (MVC) architecture. All web requests are routed through `app.py`, which acts as the controller. It manages user sessions, processes form data, and executes raw SQL queries against the local SQLite database. Once the data is retrieved or updated, the application renders HTML templates using Jinja2 and sends the response back to the client. This tightly coupled approach was chosen over a separate REST API and frontend (like React) to reduce configuration overhead and focus strictly on learning core server-side routing, raw SQL data modeling, and HTML templating.

## Running Locally

1. **Clone the repository**
```bash
git clone https://github.com/udarshcodes/pft.git
cd pft
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Initialize the database**
```bash
python create_db.py
```

4. **Start the development server**
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your web browser.

## Project Structure

```text
pft/
├── app.py              # Main Flask application and route definitions
├── create_db.py        # Database initialization script
├── finance.db          # SQLite database (created after running create_db.py)
├── helpers.py          # Utility functions for auth, currency formatting, and date parsing
├── Procfile            # Gunicorn command for deployment
├── requirements.txt    # Python package dependencies
├── schema.sql          # Database table definitions
├── static/             
│   ├── hero_graphic.png # Landing page visualization
│   ├── logo.jpg        # App logo
│   └── styles.css      # Custom CSS styles
└── templates/          # Jinja2 HTML templates
    ├── add.html
    ├── apology.html
    ├── budget.html
    ├── contact.html
    ├── history.html
    ├── index.html
    ├── landing.html
    ├── layout.html
    ├── login.html
    ├── register.html
    ├── reports.html
    └── settings.html
```

## What I Learned & Key Decisions

- **Session-Based Authentication:** Chose server-side sessions over JWTs because the application relies entirely on server-rendered HTML templates rather than a separated API and frontend.
- **Raw SQL over ORM:** Used raw SQL queries via the `cs50` library instead of SQLAlchemy to solidify my understanding of relational database concepts and schema design.
- **SQLite Database:** Selected SQLite because the application is designed for individual use and does not require complex concurrent write operations.
- **Backend Data Validation:** Learned the importance of validating user input on the server side (e.g., verifying dates and transaction types) to prevent database corruption, even when HTML forms have built-in validations.


*CS50x Final Project — Harvard University*
