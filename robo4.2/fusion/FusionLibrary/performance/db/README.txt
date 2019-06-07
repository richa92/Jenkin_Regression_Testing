OneView Performance Testing

Authors: 
 - Chuck Fowler [chuck.fowler@hpe.com]
 - Joseph A Rodrigo [joseph.a.rodrigo@hpe.com]
 - Hung Dinh [hung.dinh2@hpe.com]

Implementation:
	 Technologies used
		○ Django
		○ Django Rest Framework
		○ SQL Lite

	Host: OneViewPerformance.rsn.rdlabs.hpecorp.net:8080
	
	The database is viewable via the Interactive REST API interface provided by Django. The administrator interface allows a user to view and manipulate the data in the database. This interface is accessible through the admin credentials (admin/hpvse123).
	
	 Django Apps
		○ Performance Records
		○ Performance Dashboard
	
Deployment:
	 Get Respository
		○ $ git clone ssh://<firstname-lastname>@cgit-pro.houston.hp.com:29418/fusion
		○ $ cd fusion/FusionLibrary/performance/db
	 Install necessary dependencies
		○ $ pip install -r requirements.txt
	 Deploy Django Apps
		○ Create admin Databases
		    $ python manage.py migrate
		○ $ python manage.py createsuperuser
			§ Follow the instruction to setup an admin user.
		○ Create Performance Databases
		    $ python manage.py makemigrations performance_records
		    $ python manage.py migrate
		    $ python manage.py inspectdb
		○ $ python manage.py runserver <ip>:8080 &

==============================================================================================

