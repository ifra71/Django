# Django IP Logging and Rate Limiting

A Django project for practicing middleware, Redis, rate limiting, authentication, custom users, and testing.

## Features

### IP Logging

The middleware gets the IP address and request time for each request.

The logs are saved in:

```text
ip_requests.log
```

### Rate Limiting

Redis is used to count requests.

The request limits are:

| User | Limit |
|---|---:|
| Gold | 10 requests/minute |
| Silver | 5 requests/minute |
| Bronze | 2 requests/minute |
| Not logged in | 1 request/minute |

When the limit is exceeded, a `429 Too Many Requests` response is returned.

The request counter expires after 60 seconds.

### Custom User

A custom user model is used instead of Django's default user model.

Users log in with their email instead of a username.

There are three roles:

- Gold
- Silver
- Bronze

The role is also used for rate limiting.

### Login and Logout

The project has login and logout functionality.

Class-based views are used for:

- Home
- Profile
- Dashboard
- Login
- Logout

### Admin

The custom user model is added to the Django admin panel.

The admin can manage users, roles, and account permissions.

## Setup

Clone the repository:

```bash
git clone https://github.com/ifra71/Django.git
cd Django/first_project
```

Create a virtual environment:

```bash
python -m venv myworld
```

Activate it on Windows:

```powershell
.\myworld\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project folder.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=1

CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

Run migrations:

```bash
python manage.py migrate
```

Make sure Redis/Memurai is running.

Start the Django server:

```bash
python manage.py runserver
```

## Tests

Run the tests with:

```bash
python manage.py test
```

The current tests check:

- Home page
- Login page
- Email login
- User roles

## Pre-commit

Pre-commit is used to check and format Python files.

The project uses:

- Black
- isort

Install the pre-commit hooks:

```bash
pre-commit install
```

Run the checks manually:

```bash
pre-commit run --all-files
```

## Useful Commands

Check the Django project:

```bash
python manage.py check
```

Run tests:

```bash
python manage.py test
```

Start the server:

```bash
python manage.py runserver
```

Run pre-commit:

```bash
pre-commit run --all-files
```