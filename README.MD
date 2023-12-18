1. Install deps:
```
pip install -r requirements.txt
```

2. Run docker postgres.
```
docker run -p 5432:5432 -e POSTGRES_PASSWORD=password postgres
```

3. Make migrations.
```
python manage.py migrate
```

4. Run Django web server.
```
python manage.py runserver
```