### Recreate dockers
```
docker rm fwbm_django fwbm_db
docker compose up --build
```

### Run intialize_database script
```
docker exec -it fwbm_django python manage.py initialize_database
```

## Inspect postgres SQL
```
docker exec -it fwbm_db psql fwbm postgres
```
