# Travelerhelper

This project aims at giving the easiest way for someone who wants to go to some place in the Paris area, using public
transportation (subway, bus, autolib', velib') depending on the weather and the load he or she is carrying.

This code has been developed with **Python version 3.5** and tested on **Google Chrome** browser

Steps to follow to install and setup the project
- Clone this repository (ex : git clone git@github.com:mikamedioni/travelerhelper.git)
- Go to the thsite folder
- Set up the virtual environment :
    * install virtualenv : sudo apt-get install virtualenv
    * create a virtualenv : $ virtualenv environment_name
    * launch the virtualenv : $ source environment_name/bin/activate
    * install django : $ pip install django
    * install requests : $ pip install requests
    * install xlrd : $ pip install xlrd
- Set up the data base :
    * $ python manage.py migrate
    * $ python manage.py makemigrations
    * $ python findways/insert_data.py
- Launch the server :
    * $ python manage.py runserver
- Open the browser (**Chrome**) and call this url : http://localhost:8000/findways

- ENJOY !