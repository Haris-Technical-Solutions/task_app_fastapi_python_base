pip freeze > requirements.txt



alembic revision --autogenerate -m "create_task_comments_table"
alembic upgrade head 
alembic check


