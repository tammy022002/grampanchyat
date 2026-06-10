from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.modules.users.schemas import Token
from app.core.security import create_access_token
from app.core.exceptions import BusinessRuleException

router = APIRouter()

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Mock authentication - in real system check against User table
    if form_data.username == "admin" and form_data.password == "admin123":
        access_token = create_access_token(subject=form_data.username)
        return {"access_token": access_token, "token_type": "bearer"}
    
    raise BusinessRuleException("Incorrect username or password", status_code=401)
