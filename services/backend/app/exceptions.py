from fastapi import HTTPException, status


class Exc:
    """
    Exceptions returned by the API to consumers.
    """
    UserNotFoundException = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found.")
    
    ProfileNotFoundException = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User Profile not found.")
    
    InvalidUsernameOrPasswordException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password.")
    
    InvalidCredentialsException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials.",
        headers={"WWW-Authenticate": "Bearer"})
