# dive-shop

An e-commerce catalog and order management application for scuba diving equipment built with Python and Django. Features product search, customer order tracking, and inquiry contact mechanisms.

## Features

- **Product Search Engine**: Case-insensitive search for diving gear, accessories, and wear with query validation.
- **Order & Client Management**: Database models and administration views for customer orders, shipping addresses, and inventory status.
- **Contact & Inquiry System**: Dynamic contact forms utilizing Django's forms API with automated email dispatch.
- **Database Flexibility**: Support for SQLite in local development and PostgreSQL in production via environment configuration.
- **Defensive API**: Safe query retrieval preventing uncaught server exceptions on malformed requests.

## Prerequisites

- **Python**: 3.8 or higher
- **pip**: Latest package installer for Python
- **PostgreSQL**: (Optional) For production relational storage; defaults to SQLite for local development.

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AntonioHellin/dive-shop.git
   cd dive-shop
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file from `.env.example`:
   ```bash
   # Windows
   copy .env.example .env

   # Linux / macOS
   cp .env.example .env
   ```

5. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create an administrative user (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

## Usage

Start the development server:
```bash
python manage.py runserver
```

Open your browser at `http://127.0.0.1:8000` to interact with the catalog, or visit `http://127.0.0.1:8000/admin` to manage orders and articles.

## Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `SECRET_KEY` | Django cryptographic signing key | Safe development fallback |
| `DEBUG` | Enables or disables Django debug mode | `True` |
| `ALLOWED_HOSTS` | Comma-separated allowed hostnames | `127.0.0.1,localhost` |
| `DB_ENGINE` | Database backend engine | `django.db.backends.sqlite3` |
| `DB_NAME` | Database name or SQLite file path | `db.sqlite3` |
| `DB_USER` | Database username (for PostgreSQL) | Empty |
| `DB_PASSWORD` | Database password (for PostgreSQL) | Empty |
| `DB_HOST` | Database host | `127.0.0.1` |
| `DB_PORT` | Database port | `5432` |
| `EMAIL_BACKEND` | Django email backend | `django.core.mail.backends.console.EmailBackend` |
| `EMAIL_HOST` | SMTP server address | `smtp.gmail.com` |
| `EMAIL_PORT` | SMTP port | `587` |
| `EMAIL_USE_TLS` | Enables TLS for email transmission | `True` |
| `EMAIL_HOST_USER` | Email account username | Empty |
| `EMAIL_HOST_PASSWORD` | Email account application password | Empty |
| `CONTACT_RECIPIENT_EMAIL` | Destination email for contact messages | Empty |

## License

This project is licensed under the [MIT License](LICENSE).
