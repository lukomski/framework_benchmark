### Recreate dockers
```
docker rm fwbm_django fwbm_db fwbm_dotnet
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
