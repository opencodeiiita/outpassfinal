# Outpass Portal
Outpass Portal is designed to simplify and speeding up the process of seeking an outpass for leave.It aims to eliminate unneccesary paperwork by making the process of creating requests digital.The caretakers can then approve the outpass at the click of a button.

# How it Works-

1. Signup and then login to create a new request.
1. Fill the required form details.
1. An email with the same details will be sent to your parent's email informing them about your leave application.
1. The admin can then view and approve your request.
1. You will receive an email notification on approval.[IN PROGRESS]
1. Forum for discussion regarding hostel and mess issues [TO BE IMPLEMENTED].


Setup for developers (Unix)
---------------------------

1. Make sure you have installed Python 3.6, [pip3](https://pip.pypa.io/en/latest/) and [virtualenv](http://www.virtualenv.org/en/latest/).
1. If working behind a proxy, make sure your environment variables are properly set up. If
   you still get an error due to proxy, use "-E" flag along with "sudo" to export all the
   environment variables.
1. Clone the repo - `git clone ` and cd into
  the directory. If working behind a proxy, follow the instructions [here](https://cms-sw.github.io/tutorial-proxy.html).
1. Create a virtual environment with Python 3 and install dependencies:

     ```bash
     $ virtualenv venv --python=/path/to/python3
     $ source venv/bin/activate
     $ pip install -r requirements.txt
     ```
1. Run `python manage.py makemigrations`.
1. Run `python manage.py migrate`.
1. Run `python manage.py createsuperuser` to create a superuser for the admin panel.
  Fill in the details asked.This user can be then used to login normally or through admin dashboard.
1. Run `python manage.py runserver` to start the development server.

In case if you run into any issues during setup feel free to contact Team Opencode.
