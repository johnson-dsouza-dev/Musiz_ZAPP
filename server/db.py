from os import close  # Importing the 'close' function, though it isn't used in this script
from sqlalchemy import create_engine  # For creating a connection to the database
from sqlalchemy.orm import sessionmaker  # For managing database sessions

# Database connection URL using PostgreSQL with the pg8000 driver
DATABASE_URL = 'postgresql+pg8000://postgres:admin@localhost:5432/fluttermusicapp'  

# Create a new SQLAlchemy engine instance for connecting to the database
engine = create_engine(DATABASE_URL)  

# Configure sessionmaker:
# - autocommit=False: Changes must be explicitly committed
# - autoflush=False: Prevents automatic flushing of changes to the database
# - bind=engine: Binds the session to the created engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  

# Dependency function for getting a database session
def get_db():
    db = SessionLocal()  # Create a new database session instance
    try:
        yield db  # Provide the session for use in a dependency context
    finally:
        db.close()  # Ensure the session is closed after use to release resources
