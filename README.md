Starting up (add to PyCharm configuration to do it from button)
python manage.py runserver


===Each change to database model===

# Creates the migrations file.
python manage.py makemigrations
# Executes the migrations and updates the database with your model changes.
python manage.py migrate


===Creating new pages (called apps in Wagtail)===

# To do so, run 
python manage.py startapp HERENAMEOFNEWPAGE
# for example
python manage.py startapp newpage
# to create a new page

Add the new page to INSTALLED_APPS in EsportCenter/settings/base.py.

In some cases it is neccessery to add page of admin panel too.