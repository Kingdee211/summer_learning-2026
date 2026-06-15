from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load all the environment variables
load_dotenv()

# Fetch the databse URL
db_url = os.getenv("DATABASE_URL")

# Check if a valid database url was fetched
if not db_url:
    raise ValueError("No environment variable corresponding to the provided database Url found!")

def get_db_engine():
    """
    Initializes and returns a SQLAlchemy engine using the DATABASE_URL
    from environment variables. Raises an informative error if connection fails.
    """
    try:
        engine = create_engine(db_url)
        print("Connection to the database was successful🚀🚀🚀!")
        return engine
    
    except Exception as ex:
        print(f"❌ DB connection failed due to the following error 👇👇👇:\n {str(ex).splitlines()[0]}")
        return None # Let the error propagate so the caller can handle/log as needed
 
my_engine = get_db_engine()

if my_engine:
    with my_engine.begin() as connection:
        # Raw sql query - basic select with some filtering
        resutls = connection.execute(text("""
            SELECT * FROM users 
            WHERE name like '%Gai%' 
            ORDER BY name ASC
            LIMIT 3;
        """))
        for user in resutls:
            # print the values as key-value pairs (dictionaries)
            print(dict(user._mapping))