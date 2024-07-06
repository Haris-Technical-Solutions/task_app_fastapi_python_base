// create migration
alembic revision --autogenerate -m "create_users_table"

alembic revision -m "create account table"

alembic revision -m "Add a column"

// migrate run
alembic upgrade head
alembic downgrade -1

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbkBodHMucGsiLCJleHAiOjE3MjAyNTg4NDR9.xxywzvF-LSviYgxNR4jq6Q3gX-W6jrXPlQDAAlFOWC0