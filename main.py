from fastapi import FastAPI
import models, database
from routers import blogs, users, login

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(router=blogs.route)
app.include_router(router=users.route)
app.include_router(router=login.route)