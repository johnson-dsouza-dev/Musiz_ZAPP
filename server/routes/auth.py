import uuid  # For generating unique IDs
import bcrypt  # For securely hashing passwords
from fastapi import Depends, HTTPException  # For dependency injection and error handling

from models.user import User  # User model representing the database table
from pydantic_schemas.user_create import UserCreate  # Pydantic schema for user creation validation
from fastapi import APIRouter  # For creating modular routes
from sqlalchemy.orm import Session  # For managing database sessions

from db import get_db
from pydantic_schemas.user_login import UserLogin  # Dependency to provide database session
# from db import db  # Commented out, not required if get_db is used
router = APIRouter()  # Create an APIRouter instance to organize routes

@router.post('/signup', status_code=201)  # Define a POST endpoint for user signup
def signup_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Handles user signup by validating input, checking for duplicate emails, 
    and securely storing the user's data in the database.
    """
    # Check if a user with the same email already exists in the database
    user_db = db.query(User).filter(User.email == user.email).first()
    if user_db:  # If a user with the same email exists, raise an error
        raise HTTPException(400, "User with the same name already exist")

    # Securely hash the password using bcrypt
    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())

    # Create a new User instance with the provided data and hashed password
    user_db = User(
        id=str(uuid.uuid4()),  # Generate a unique ID for the new user
        email=user.email,  # Set email from request data
        password=hashed_pw,  # Store the hashed password
        name=user.name  # Set name from request data
    )

    db.add(user_db)  # Add the new user object to the database session
    db.commit()  # Commit the transaction to save changes in the database
    db.refresh(user_db)  # Refresh the instance to reflect any updates made during the commit
  # Define a POST endpoint for user signup
    return user_db  # Return the created user object as the response

@router.post('/login')
def login_user(user:UserLogin,db:Session=Depends(get_db)):
    # check if the user with same email exists 
    
    user_db=db.query(User).filter(User.email==user.email).first()
    if not user_db:
        raise HTTPException(400,"User with this email does not exist ! ")

    # password matching or not 
    ismatch = bcrypt.checkpw(user.password.encode(),user_db.password )
    
    if not ismatch:
        raise HTTPException(400,"INCORRECT PASSWORD ! ")
    return user_db


    

    