import schemas, models, database
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

getdb = database.getdb
route = APIRouter(prefix="/blog", tags=["blog"])


@route.get('/', response_model=list[schemas.ShowBlog])
def list_blog(limit:int | None=None, db:Session=Depends(getdb)):
    if limit:
       blogs = db.query(models.Blog).limit(limit=limit).all()
    else:
       blogs = db.query(models.Blog).all()
    return blogs


@route.get('/{id}', response_model=schemas.ShowBlog)
def detail_blog(id:int, db:Session=Depends(getdb)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    return blog

@route.post('/')
def create_blog(req:schemas.CreateBlog, db:Session=Depends(getdb)):
    new_blog = models.Blog(title=req.title, body=req.body, user_id = req.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog

@route.put('/{id}')
def update_blog(id:int, req:schemas.Blog, db:Session=Depends(getdb)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    blog.update(req.dict())
    db.commit()
    return blog.first()

@route.delete('/{id}')
def delete_blog(id:int, db:Session=Depends(getdb)):
    db.query(models.Blog).filter(models.Blog.id == id).delete()
    db.commit()
    return "delete"