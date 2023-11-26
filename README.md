
## Description

Information about this project:
Wagtail website (Django + Python). Uses Tailwind.

Running here: https://bloodrush.gg

## Features

- News
- Streams/streamers
- Events & premiers
- About Us
- Sliders
- Countdown
- and more


## Screenshots
![Slider](docs/img/1.png)
![Podcast](docs/img/2.png)
![Banners](docs/img/3.png)
![Countdown](docs/img/4.png)

## Roadmap

- Additional browser support

- Add more integrations


## Deployment and running

Clone the project.

Go to the project directory and activate environment

```bash
  cd EsportCenter
  source env/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Creates the migrations file.
```bash
  python manage.py makemigrations
```

Executes the migrations and updates the database with your model changes.
```bash
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```


Wagtail update

```bash
  pip install wagtail==new_version_number
```



## Useful links

 - [Wagtail](https://wagtail.org/)


