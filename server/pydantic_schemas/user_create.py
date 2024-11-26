from pydantic import BaseModel  # Importing BaseModel for creating data validation schemas

# Define a Pydantic schema for user creation
class UserCreate(BaseModel):                         
    name: str  # Field to store the user's name (must be a string)
    email: str  # Field to store the user's email (must be a string)
    password: str  # Field to store the user's password (must be a string)
