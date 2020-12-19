import fastapi

from models.ImageOfTheDayResponse import ImageOfTheDayResponse
from services import bingService

router = fastapi.APIRouter()



@router.get("/api/image_of_the_day")
async def image_of_the_day():
    data = await bingService.getImageOfTheDay()
    url = f"https://www.bing.com/{data.get('images')[0].get('url')}"

    return ImageOfTheDayResponse(
        url=url
    )

