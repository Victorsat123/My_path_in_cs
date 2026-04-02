from fastapi import FastAPI
from API import users, categories, goals, tasks, progress

app = FastAPI(title="Progress Hub API")

app.include_router(users.router)
app.include_router(categories.router)
app.include_router(goals.router)
app.include_router(tasks.router)
app.include_router(progress.router)

@app.get("/")
def read_root():
    return {"message": "API працює! Перейдіть на /docs для перегляду Swagger"}