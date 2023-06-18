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

To update libraries:
pip install -r requirements.txt     


BUG FIXES after updating template styles
Fix file common.js in static/assets/js/common.js so Lightbox section look like this:
    css: 'static/assets/vendors/common/glightbox/css/plyr.css',
    js: 'static/assets/vendors/common/glightbox/js/plyr.js',


To connect database need install this library:
pip install psycopg2-binary

Migration sqlittle -> postersql
sqlite3 your-sqlite3-database.db .dump > dump.sql

python manage.py dumpdata > data.json

pip install pytube


                            {% if post.thumbnail %}
                            <img class="aspect-[16/9] h-full w-full max-w-full object-cover duration-300 group-hover:scale-110 group-hover:opacity-75"
                                 src="{{ post.thumbnail }}"
                                 alt="Thumbnail">
                            {% endif %}