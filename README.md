## Virtual Environment Setup
- `python -m venv <venv-file>` : Create venv file.
- `<venv-file>/Scripts/activate` : Activate venv file.
- `Set-ExecutionPolicy -Scope Currentuser -ExecutionPolicy Unrestricted` : If venv is not activate, use this command.
## DJango Install
- `pip install django` : Install DJango
## Create Project
- `django-admin startproject <project-name>` : Create Project
## Create App
- `cd <project-name>` : Go inside the project directory from current working directory.
- `python manage.py startapp <app-name>` : Create App
## Connect Database
- `python manage.py makemigrations`
- `python manage.py migrate`
## Run Server
- `python manage.py runserver` : Run The DJango Server.
- `localhost:8000` or `http://127.0.0.1:8000/` : Open this web url on browser.
