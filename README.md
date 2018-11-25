# techdegree-project-6
To install the requirements:  
-> pip3 install -r requirements.txt .   
Migrate changes for the database:  
-> python3 manage.py migrate .  
To load database use following line in terminal:  
-> python3 manage.py loaddata minerals_app/fixtures/fixtures.json .   
Run the project with the following line in terminal:  
-> python3 manage.py runserver 0.0.0.0:8000 .   
To test the project:  
-> python3 manage.py test minerals_app .   
