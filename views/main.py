import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from api.images import image_of_the_day
from api.words import word_of_the_day

templates = Jinja2Templates("templates")

router = fastapi.APIRouter()


@router.get("/", include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "word": await word_of_the_day(),
        "image": await image_of_the_day(),
    })


@router.get("/countdown", include_in_schema=False)
async def countdown(request: Request):
    return templates.TemplateResponse("countdown.html", {
        "request": request,
        "image": await image_of_the_day(),
    })
