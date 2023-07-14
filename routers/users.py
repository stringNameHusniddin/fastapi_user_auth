import schemas, models, database
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from hashing import Hash

getdb = database.getdb
route = APIRouter(prefix="/user", tags=["user"])


@route.get('/user', response_model=list[schemas.ShowUser])
def list_user(limit:int | None=None, db:Session=Depends(getdb)):
    if limit:
       users = db.query(models.User).limit(limit=limit).all()
    else:
       users = db.query(models.User).all()
    return users

@route.get('/user/{id}', response_model=schemas.ShowUser)
def detail_user(id:int, db:Session=Depends(getdb)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    return user

@route.post('/user')
def create_user(req:schemas.CreateUser, db:Session=Depends(getdb)):
    new_user = models.User(username=req.username, password=Hash.hash_password(req.password), email=req.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@route.put('/user/{id}')
def update_user(id:int, req:schemas.User, db:Session=Depends(getdb)):
    user = db.query(models.User).filter(models.User.id == id)
    user.update({"username":req.username, "password":Hash.hash_password(req.password), "email":req.email})
    db.commit()
    return user.first()

@route.delete('/user/{id}')
def delete_user(id:int, db:Session=Depends(getdb)):
    db.query(models.User).filter(models.User.id == id).delete()
    db.commit()
    return "delete"