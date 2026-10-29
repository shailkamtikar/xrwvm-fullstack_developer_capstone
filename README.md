# fullstack_developer_capstone

Best Cars dealership portal: a full-stack Django application where customers can look up dealerships by state and read and write reviews.
Capstone project for the IBM Full Stack Software Developer Professional Certificate.

## Structure

```
server/
  djangoapp/    Django application (models, views, proxy services)
  djangoproj/   Django project configuration
  frontend/     HTML, CSS and React front end
  database/     Express and MongoDB service for dealers and reviews
```

## Run the Django app locally

```bash
cd server
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -U -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Pages available so far: `/` (home), `/about/` and `/contact/`.
