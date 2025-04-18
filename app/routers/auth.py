from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from .. import schemas, models,utils, oauth2
from ..database import get_session

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.Token)

def login(user_credentials: OAuth2PasswordRequestForm = Depends() ,db: Session = Depends(get_session)):
    user = db.exec(select(models.User).where(models.User.email == user_credentials.username)).first() # Here Username is Email

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id,"email":user.email})
        

    return{"access_token":access_token,"token_type":"bearer"}