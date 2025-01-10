from importlib import reload

import uvicorn
from fastapi import FastAPI
from app.items.router import router as items_router
from app.users.router import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)

@app.get("/", tags=['base'])
async def main_rout():
    return {"status": 200}


# if __name__ == "__main__":
#     uvicorn.run("main:app", port=8000, reload=True)
