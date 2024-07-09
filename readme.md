pip freeze > requirements.txt



alembic revision --autogenerate -m "create_project_assignments_table"
alembic upgrade head 
alembic check


