# demo-fastapi-async-sqlalchemy
Demo of set up for Web App Backend using FastAPI + Async SQLAlchemy.

See https://medium.com/@tclaitken/setting-up-a-fastapi-app-with-async-sqlalchemy-2-0-pydantic-v2-e6c540be4308

## Commands
Start project:
```
docker compose up -d
```

Create migration file:
```
backend/scripts/autogenerate_migrations.sh "My migration"
```

Run migration:
```
backend/scripts/run_migrations.sh
```







