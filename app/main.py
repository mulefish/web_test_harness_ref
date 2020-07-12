from fastapi import FastAPI, Request
import events_router
from db import metadata, database, engine
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

metadata.create_all(engine)

app = FastAPI(docs_url="/events_docs/", redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/items/{id}")
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(events_router.router, prefix='/events', tags=['events'])
