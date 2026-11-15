# Digital Imaging and Diagnostic Center — Django website

A responsive corporate website starter for Digital Imaging and Diagnostic Center, Owerri. Built with Django 5.2 and designed for deployment on Railway.

## Included
- Responsive home, about, services, contact and enquiry pages
- Uploaded centre logo
- Click-to-call telephone links, WhatsApp contact shortcut and Facebook link
- Enquiry form saved to Django database and manageable in Django Admin
- PostgreSQL support through Railway's `DATABASE_URL`
- WhiteNoise static-file serving, Gunicorn start command and `/healthz/` health check
- Africa/Lagos timezone and production-oriented security defaults

## Run locally
```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open `http://127.0.0.1:8000/` and admin at `/admin/`.

## Deploy to Railway
1. Push this project to a new GitHub repository.
2. In Railway, create a project and deploy the GitHub repository as a service.
3. Add a PostgreSQL service to the Railway project. Railway will expose `DATABASE_URL` to services when linked.
4. Set these service variables:
   - `SECRET_KEY`: generate a long random secret
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `.railway.app,your-domain.com,www.your-domain.com`
   - `CSRF_TRUSTED_ORIGINS`: `https://your-domain.com,https://www.your-domain.com,https://your-service.up.railway.app`
5. The included `Procfile` runs migrations then starts Gunicorn. Railway should use it automatically; otherwise set the start command to `python manage.py migrate --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`.
6. Generate a Railway domain or connect your custom domain and configure its DNS as Railway instructs.
7. Create an admin user using Railway's service shell: `python manage.py createsuperuser`.
8. Test `/`, `/admin/`, submit a test enquiry, and confirm it appears in Admin.

## Important content and launch checks
- Facebook's public page could not be fetched by the research browser during preparation. No posts, opening hours, staff biographies, accreditation, equipment claims, or detailed test catalogue have been invented.
- The website currently describes only the broad areas supported by available public listings and the client brief: medical laboratory investigations and diagnostic imaging. Confirm the actual modalities and tests with the centre before publishing a detailed service catalogue.
- Confirm the supplied address format, both phone numbers, operating hours, WhatsApp number, email, and map pin with the client.
- Replace the temporary CSS medical illustration with approved facility/equipment/team photography when supplied.
- Configure a production email service if enquiry notifications to staff are required. The current form stores enquiries in the database and displays a confirmation to the visitor; it does not send email.
- Add a privacy notice and obtain client approval for the website's data collection wording before launch.

## Project structure
```
config/                 Django project settings and URLs
core/                   Website app, enquiry model, admin and views
  templates/core/       Page templates
  static/core/          CSS and supplied logo
manage.py
Procfile
requirements.txt
runtime.txt
```
