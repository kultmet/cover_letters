from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from cover_letters.cover_letter_generator import letter_generator
from cover_letters.hard_skills import get_work_requirements, filtering_skills, get_relevant_experience, split_requirements_string

app = FastAPI()


class LetterData(BaseModel):
    company: str
    position: str | None = None
    interest: str
    requirements: List[str] | None = None

class RequirementText(BaseModel):
    text: str

class Skills(BaseModel):
    requirements: List[str]


@app.post('/cover_letters/')
async def create_letter(item: LetterData):
    response: dict[str, str] = item.dict()
    response.update({'letter': letter_generator(
        company=item.company,
        position=item.position,
        interest=item.interest,
        requirements=item.requirements
    )})
    return response

# @app.get('/cover_letters/')
# async def get_letter(item: LetterData):
#     response: dict[str, str] = item.dict()
#     response.update({'letter': letter_generator(
#         company=item.company,
#         position=item.position,
#         interest=item.interest,
#         requirements=item.requirements
#     )})
#     return response

@app.post('/recognize_req/')
async def recognize_skills(item: RequirementText):
    filtered_data = split_requirements_string(item.text)
    return {'filtered_data': filtered_data}

@app.get('/recognize_req/')
async def get_recognize_skills(text: str):
    filtered_data = split_requirements_string(text)
    return {'filtered_data': filtered_data}
