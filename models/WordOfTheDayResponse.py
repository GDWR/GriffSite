from typing import Any, Dict, List

from pydantic import BaseModel


class WordOfTheDayResponse(BaseModel):
    word: str
    note: str
    definitions: List[Dict[str, Any]]
