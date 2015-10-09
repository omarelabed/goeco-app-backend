# goeco-app-backend
This application was created using django framework and runs with python.

## Getting started

### Install `pip` and `virtualenv` (if not installed yet)
If not already installed, see [this documentation](http://pip.readthedocs.org/en/stable/installing/) on how to install `pip`, then install `virtualenv`:

    $ [sudo] pip install virtualenv

See the (documentation)[https://virtualenv.pypa.io/en/latest/installation.html] for more.

### Install python, django and other libraries

    $ virtualenv env
    $ source env/bin/activate
    (env)$ install -r requirements.txt

### Set up mongodb
Follow [the steps described here](http://docs.mongodb.org/manual/tutorial/#installation).

### To get started

Check out the [django rest framework website](http://www.django-rest-framework.org/) and [django website](https://www.djangoproject.com/start/) on how to get started.

### If you have everything installed

Run mongodb then navigate to the project folder (`goeco/`) and on the command line and run:

    $ python manage.py runserver

You're good to go!
