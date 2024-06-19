# How to start

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 src/main.py (or, uvicorn src.main:app --host=0.0.0.0)
```

### If dependency changes, please enter this code and commit

```
pip3 freeze > requirements.txt
```


## How to change the DB shema

1. Create (or update) the `XXXTable` class in `src/db/*`.

2. (When creating a new table) Add the corresponding Table class to `__all__` in `src/db/__init__.py`.

3. Automatically generate migration files

```bash
alembic revision --autogenerate -m "message"
```

4. Run migration

```bash
alembic upgrade heads
```

- Rollback

```bash
alembic downgrade -1
```


## How to access Swagger UI
- local: http://localhost:8000/docs

- Docker: http://localhost:80/docs