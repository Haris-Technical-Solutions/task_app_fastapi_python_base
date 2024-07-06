import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Database connection details
HOST = "localhost"
PORT = "5432"
DATABASE = "ams"
USER_NAME = "postgres"
PASSWORD = "00000000"

# Database connection string
SQLALCHEMY_DATABASE_URL = f"postgresql://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

try:
    TABLE_NAME = "workflow_request_states"
    # Load the CSV file into a DataFrame
    df = pd.read_csv(f'C:\\Users\\pkhar\\Downloads\\{TABLE_NAME}.csv')

    # Begin a transaction
    with engine.begin() as connection:
        # Defer foreign key checks
        connection.execute(text(f"ALTER TABLE {TABLE_NAME} DISABLE TRIGGER ALL"))

        # Insert the DataFrame into the PostgreSQL table
        df.to_sql(TABLE_NAME, connection, if_exists='append', index=False)

        connection.execute(text(f"ALTER TABLE {TABLE_NAME} ENABLE TRIGGER ALL"))
        # Commit the transaction
        connection.commit()

except SQLAlchemyError as e:
    print(f"Error occurred: {e}")

finally:
    # Dispose of the engine connection
    print('done')
    engine.dispose()
