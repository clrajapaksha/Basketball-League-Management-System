# Basketball-League-Management-System
REST API for Basketball League Management System


### Migrations
```commandline
python manage.py makemigrations <app-name>
python manage.py migrate
```

### Create super user
```commandline
python manage.py createsuperuser
```

### Load dummy data
```commandline
python manage.py loaddata ./teams/fixtures/team1.json 
```

### Start server
```commandline
python manage.py runserver 9000
```

Swagger-UI: http://127.0.0.1:8080/api/schema/swagger-ui/
