from fastapi import FastAPI

from .routers import applications, auth, games, languages, parties, platforms, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(applications.router)
app.include_router(games.router)
app.include_router(parties.router)
app.include_router(platforms.router)
app.include_router(languages.router)


@app.get("/")
async def root():
    return {"message": "Wegame"}
