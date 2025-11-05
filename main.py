from fastapi import FastAPI
from app.routes import cases, channels, comments, users

app = FastAPI()

app.include_router(cases.router, prefix="/cases")
app.include_router(channels.router, prefix="/channels")
app.include_router(comments.router, prefix="/comments")
app.include_router(users.router, prefix="/users")

@app.get("/")
def read_root():
    return {"message": "Welcome to TrueCrimeHub!"}

