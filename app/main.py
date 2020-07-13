from fastapi import FastAPI, Request
import events_router
from db import metadata, database, engine
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

metadata.create_all(engine)

app = FastAPI(docs_url="/events_docs/", redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/testmenu/")
async def test_menu(request: Request):

    import random
    seed = "abcdefghijklmnopqrstuvwxyz0123456789"
    ary = list(seed)
    fake_jwt = ""
    for loop in range(100):
        fake_jwt += random.choice(ary)
    return templates.TemplateResponse("test_page.html", {"request": request, "jwt": fake_jwt})

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(events_router.router, prefix='/events', tags=['events'])
