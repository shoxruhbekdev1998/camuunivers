from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from models import categories, categories2, for_inquiries, informations, informations2, menus, numbers, partners, users, journals, shorts, videos, bot_api, documents
from routes import auth, informations2, numbers, users, menus, categories, categories2, informations, for_inquiriens,partners, journals, shorts, videos, bot_api, documents

from db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Shablon",
    responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
               401: {'desription': 'Unauthorized'}}
)

from fastapi.middleware.cors import CORSMiddleware

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {"message": "Welcome"}

#login
app.include_router(
    auth.login_router,
    prefix='/auth',
    tags=['User auth section'])

#users
app.include_router(
    users.router_user,
    prefix="/user",
    tags=['User section']
)

#menu
app.include_router(
    menus.router_menu,
    prefix="/menu",
    tags=['Menu section']
)

#category
app.include_router(
    categories.router_category,
    prefix="/category",
    tags=['Category section']
)

#category2
app.include_router(
    categories2.router_category2,
    prefix="/category2",
    tags=['Category2 section']
)

#informations
app.include_router(
    informations.router_information,
    prefix="/informations",
    tags=['Informations section']
)

#inquiries
app.include_router(
    for_inquiriens.router_inquire,
    prefix="/inquiries",
    tags=['Inquiries section']
)

#partnerss
app.include_router(
    partners.router_partner,
    prefix="/partners",
    tags=['Partners section']
)

#numbers
app.include_router(
    numbers.router_number,
    prefix="/numbers",
    tags=['Numbers section']
)

#informations2
app.include_router(
    informations2.router_information2,
    prefix="/informations2",
    tags=['Informations2 section']
)

#Journals
app.include_router(
    journals.router_journals,
    prefix="/Journals",
    tags=['Journals section']
)

#Shorts
app.include_router(
    shorts.router_shorts,
    prefix="/Shorts",
    tags=['Shorts section']
)

#Videos
app.include_router(
    videos.router_videos,
    prefix="/Videos",
    tags=['Videos section']
)

#Bot
app.include_router(
    bot_api.router_bot,
    prefix="/Bot_api",
    tags=['Bot section']
)

#Documents
app.include_router(
    documents.router_document,
    prefix="/Documents",
    tags=['Documents section']
)