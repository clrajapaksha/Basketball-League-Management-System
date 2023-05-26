# Basketball-League-Management-System
REST API for Basketball League Management System


### Migrations
```commandline
python manage.py makemigrations teams
python manage.py migrate
```

### Create super user
```commandline
python manage.py makemigrations users
python manage.py migrate
python group.py
python manage.py createsuperuser
# groups.id = 1 (admin)
```

### Load dummy data
```commandline
python manage.py loaddata ./teams/fixtures/team1.json 
```

### Start server
```commandline
python manage.py runserver 9000
```

* Swagger-UI: http://127.0.0.1:8080/api/schema/swagger-ui/
* Django Admin UI: http://127.0.0.1:8080/admin/

