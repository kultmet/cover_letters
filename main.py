from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from cover_letters.cover_letter_generator import letter_generator
from cover_letters.hard_skills import (
    add_skill_to_stack,
    get_all_skills,
    read_stack,
    requirements_filter
)
from settings.constants import MY_STACK_PATH, ALL_STACK_PATH

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


class Skill(RequirementText):
    pass


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


@app.post('/requirements/')
async def recognize_skills(item: RequirementText):
    filtered_data = requirements_filter(item.text)
    return {'filtered_data': filtered_data}


@app.get('/my_skills/')
async def get_user_skills():
    user_skills = await get_all_skills(MY_STACK_PATH)
    return {'user_skills': user_skills}


@app.post('/my_skills/')
async def add_user_skill(item: Skill):
    await add_skill_to_stack(item.text, MY_STACK_PATH)
    try:
        skill = read_stack(MY_STACK_PATH)[item.text.lower()]
        return {'message': f'{skill} успешно добавлен в ваш стэк!'}
    except KeyError:
        return {'message': 'Что-то пошло не так!!!'}
    # return {'message': item.text}


@app.post('/common_skill/')
async def add_common_skill(item: Skill):
    await add_skill_to_stack(item.text, ALL_STACK_PATH)
