# Django API application


### Run the project:

```
source env/bin/activate
python manage.py runserver
```

### Fetch data from API

```
curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "email": "admin@example.com",
            "groups": [],
            "url": "http://127.0.0.1:8000/users/1/",
            "username": "admin"
        },
    ]
}
```

### Making migrations
```
python manage.py makemigrations fwbm
python manage.py migrate
```

### Get first N lines from file