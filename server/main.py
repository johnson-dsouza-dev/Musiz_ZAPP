from fastapi import FastAPI  # FastAPI framework and HTTP exception handling
from routes import auth  # Importing routes for authentication
from db import engine  # Importing the database engine instance
from models.base import Base  # Importing the SQLAlchemy Base class

# Create a FastAPI application instance
app = FastAPI()  

# Include the authentication routes with a prefix `/auth`
app.include_router(auth.router, prefix='/auth')

Base.metadata.create_all(engine)
