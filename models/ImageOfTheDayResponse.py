from typing import Any, Dict, List

from pydantic import BaseModel


class ImageOfTheDayResponse(BaseModel):
    url: str
