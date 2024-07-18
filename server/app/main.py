from fastapi import FastAPI

from .routers import applications, games, parties, users, platforms, languages, userlanguages, userplatforms, partymembers

app = FastAPI()

app.include_router(users.router)
app.include_router(applications.router)
app.include_router(games.router)
app.include_router(parties.router)
app.include_router(platforms.router)
app.include_router(languages.router)
app.include_router(userlanguages.router)
app.include_router(userplatforms.router)
app.include_router(partymembers.router)


@app.get("/")
async def root():
    return {"message": "Wegame"}
