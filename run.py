import fastapi
import uvicorn

from api import images, words
from views import main

api = fastapi.FastAPI()


def configure():
    api.include_router(main.router)
    api.include_router(images.router)
    api.include_router(words.router)


configure()
if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=80)
