import fastapi
import httpx

from models.WordOfTheDayResponse import WordOfTheDayResponse
from services import wordnikService

router = fastapi.APIRouter()



@router.get("/api/word_of_the_day")
async def word_of_the_day():
    data = await wordnikService.getWordOfTheDay()
    word = data.get("word")
    note = data.get("note")
    definitions = data.get("definitions")

    return WordOfTheDayResponse(
        word=word.capitalize(),
        note=note,
        definitions=definitions,
    )

