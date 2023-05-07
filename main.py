from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from cover_letters.cover_letter_generator import letter_generator

app = FastAPI()


class InputItem(BaseModel):
    company: str
    position: str | None = None
    interest: str
    requirements: List[str] | None = None


@app.post('/cover_letters/')
async def create_items(item: InputItem):
    response: dict[str, str] = item.dict()
    response.update({'letter': letter_generator(
        company=item.company,
        position=item.position,
        interest=item.interest,
        requirements=item.requirements
    )})
    return response
