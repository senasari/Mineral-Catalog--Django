#Credit most of the html & css and images are provided by teamtreehouse.com, I mainly did the back-end part and contributed to html and css.
#DJANGO-MINERALS_PROJECT

This minerals project is a website displaying various minerals.

To install the requirements:  
-> pip3 install -r requirements.txt .   
Migrate changes for the database:  
-> python3 manage.py migrate .  
To load database use following line in terminal:  
-> python3 manage.py loaddata minerals_app/fixtures/fixtures.json .   

!!Run the project with the following line in terminal:  
-> python3 manage.py runserver 0.0.0.0:8000 .   
To test the project:  
-> python3 manage.py test minerals_app .   

