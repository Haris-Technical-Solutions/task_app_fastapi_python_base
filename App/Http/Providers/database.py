from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from configparser import ConfigParser

# HOST = "localhost"
# PORT = "5432"
# DATABASE = "task_app"
# USER_NAME = "postgres"
# PASSWORD = "00000000"
# Construct the database URL
# HOST = os.getenv("HOST")
# PORT = os.getenv("PORT")
# DATABASE = os.getenv("DATABASE")
# USER_NAME = os.getenv("USER_NAME")
# PASSWORD = os.getenv("PASSWORD")

# SQLALCHEMY_DATABASE_URL = f"postgresql://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

# Function to read Alembic configuration
def read_alembic_config():
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '../../../alembic.ini'))
    return config

# # Read Alembic configuration
alembic_config = read_alembic_config()

# Read database credentials from Alembic configuration
SQLALCHEMY_DATABASE_URL = alembic_config.get('alembic', 'sqlalchemy.url')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
db = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)