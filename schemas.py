from pydantic import BaseModel

class User(BaseModel):
    username : str
    email : str

class CreateUser(User):
    password:str

class Blog(BaseModel):
    title : str
    body : str

class ShowBlog(BaseModel):
    id:int
    title : str
    body : str

class ShowUser(User):
    id : int
    blogs : list[ShowBlog]=[]

    class Config:
        orm_model = True
 
class CreateBlog(Blog):
    user_id : int

class Login(BaseModel):
    username : str
    password : str
