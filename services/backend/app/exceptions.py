from fastapi import HTTPException, status


class Exc:
    """
    Exceptions returned by the API to consumers.
    """
    @staticmethod
    def ObjectNotFoundException(obj_name: str):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{obj_name} not found.")
    
    @staticmethod
    def NameTakenException(obj_name: str):
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{obj_name} already exists. Please choose a different one.")
    
    InvalidUsernameOrPasswordException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password.")
    
    InvalidCredentialsException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials.",
        headers={"WWW-Authenticate": "Bearer"})

    AdminRequiredException = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You don't have enough permissions to access this resource. Please contact your administrator"
    )
