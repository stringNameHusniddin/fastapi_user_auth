from fastapi import APIRouter, Depends, HTTPException, status
import schemas, database, models
from sqlalchemy.orm import Session
from hashing import Hash
from token_1 import create_access_token

route = APIRouter(prefix='/login', tags=["login"])

@route.post("login")
def login(req:schemas.Login, db:Session=Depends(database.getdb)):
    user = db.query(models.User).filter(models.User.email == req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{req.username} didn't find")
    if not Hash.verify(user.password, req.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"incorrect password")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}