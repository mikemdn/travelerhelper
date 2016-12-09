# travelerhelper

This project aims at giving the easiest way for someone who wants to go to some place in the Paris area, using public
transportation (subway, bus, autolib', velib') depending on the weather and the load he or she is carrying

This code has been developed with **Python version 3.5** and tested on **Google Chrome** browser

Steps to follow to install and setup the project
- get the code
- go to the thsite folder
- set up the virtual environment :
    * install virtualenv
    * create a virtualenv : $ virtualenv environment_name
    * launch the virtualenv : $ source environment_name/bin/activate
    * install django : $ pip install django
    * install requests : $ pip install requests
    * install xlrd : $ pip install xlrd
- set up the data base :
    * $ python manage.py migrate
    * $ python manage.py makemigrations
    * $ python findways/insert_data.py
- launch the server :
    * $ python manage.py runserver
- open the browser (**Chrome**) and call this url : http://localhost:8000/findways
