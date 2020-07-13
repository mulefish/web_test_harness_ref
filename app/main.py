from fastapi import FastAPI, Request
import events_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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
    print("Starting up...")

@app.on_event("shutdown")
async def shutdown():
    print("Shutting down...")

app.include_router(events_router.router, prefix='/events', tags=['events'])
