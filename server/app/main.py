from fastapi import FastAPI

from .routers import applications, games, parties, users

app = FastAPI()

app.include_router(users.router)
app.include_router(applications.router)
app.include_router(games.router)
app.include_router(parties.router)


@app.get("/")
async def root():
    return {"message": "Wegame"}
