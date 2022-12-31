Starting up (set it up in Pycharm so you dont have to do it each time)
python manage.py runserver

You need to install library Pillow
python -m pip install Pillow

You need to install Ckeditor
pip3 install django-ckeditor

You need to install Taggit
pip3 install django-taggit


===Each change to database model===
Migration after adding new model to database
python manage.py makemigrations

and then 
python manage.py migrate
