import json
import os
from typing import List, Dict

from settings.constants import ALL_STACK_PATH, MY_STACK_PATH


def read_stack(stack_path: str) -> dict:
    if not os.path.exists(stack_path):
        add_to_stack({}, stack_path)
    with open(stack_path, 'r') as file:
        return json.load(file)


def add_to_stack(skills: dict, stack_path: str):
    with open(stack_path, 'w') as file:
        json.dump(skills, file, indent=2, ensure_ascii=False)


async def add_skill(value: str, skills: Dict[str, str]):
    skills[value.lower()] = value


def check_skill(skill: str, skills: dict):
    """
    Проверяет скил на вхождение в словарь скилов.
    С помощью исключения вызывает диалог для заполнения словаря скилов.
    """
    try:
        skills[skill.lower()]
    except KeyError:
        pass


def get_relevant_experience(requirements: list):
    relevant = ''
    irrelevant = ''
    user_skills: dict = read_stack(MY_STACK_PATH)
    all_skills: dict = read_stack(ALL_STACK_PATH)
    for i in range(len(requirements)):
        check_skill(requirements[i], all_skills)
        try:
            relevant += f'{user_skills[requirements[i].lower()]}, '
        except KeyError:
            irrelevant += f'{requirements[i]}, '
    add_to_stack(all_skills, ALL_STACK_PATH)
    return relevant.strip(', '), irrelevant.strip(', ')


def iteration_for_check_skills(filtered_skills: list, skills: dict):
    """Итерирует по списку скилов."""
    for skill in filtered_skills:
        check_skill(skill, skills)


def iteration_for_check_user_skills(all_skills, user_skills):
    """Итерирует по списку скилов ползователя."""
    for _, value in all_skills.items():
        check_skill(value, user_skills)


async def add_skill_to_stack(skill: str, stack: str) -> None:
    """Добавляет один скилл в стэк пользователя."""
    skills: Dict[str, str] = read_stack(stack)
    await add_skill(skill, skills)
    add_to_stack(skills, stack)


async def get_all_skills(stack: str):
    """Возвращает все скиллы пользователя."""
    skills: Dict[str, str] = read_stack(stack)
    return (i for i in skills.values())


def requirements_filter(text: str) -> List[str]:
    all_skills = read_stack(ALL_STACK_PATH)
    result = []
    for skill, value in all_skills.items():
        if skill in text.lower():
            result.append(value)
    return result
