### django demo

#### install python,pip,virtualenv,django

    makedir yourpath
    cd yourpath
    virtualenv vdj
    . vdj/bin/activate
    git clone git://github.com/django/django.git
    pip install -e django/

#### create first project

    $ django-admin startproject mysite


#### run server

    $ python manage.py runserver 0.0.0.0:8000


#### create first app

    python manage.py startapp firstapp
