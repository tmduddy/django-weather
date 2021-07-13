# django-weather

A quick webapp to practice working with Django.

The end goal of this project is a web application that allows users to find out the current weather conditions anywhere in the U.S. searching by zipcode or city and state.

---

## Objectives

- [x] setup local dev workspace

      `pyenv`, `venv`, `pip install django`
- [x] initialize git repo

- [x] commit empty django project

- [x] create a `weather` app in the project

- [x] create a /search/zip/ route to allow users to get weather by zip

- [x] create a /search/city/state/ route to allow users to get weather by city, state

- [x] build a basic frontend for users to search from

- [x] build a basic frontend to display the results

- [x] create a /report-weather/ route to allow users to enter the weather at a location

- [x] create a /browse-reports/ route to allow users to enter the weather at a location

- [x] set up a data model to hold user submitted weather data

- [x] build a basic frontend for user input

- [x] add ability to browse submitted reports (either searches or filters)

- [ ] add basic signin functionality so only authenticated users can submit reports

---

## Installation

1. Download or clone the repo
1. Setup a Python (virtual) environment using any version of Python >= `3.7.4`
    - note, I've only tested this with `3.7.X`, `3.8.X`, `3.9.X`
1. Update and install all dependencies with

        pip install --U pip && pip install -r requirements.txt

1. Set up your databases and make all migrations using

        python manage.py makemigrations weather
      python manage.py migrate

    - Optional: create an admin user for yourself using

          python manage.py createsuperuser
1. Run the devserver and explore the app using

        python manage.py runserver
