import json
import re
import os
from typing import List

from settings.constants import ALL_STACK_PATH, MY_STACK_PATH


def read_txt():
    with open('req.txt', 'r', encoding='utf-8') as file:
        return file.read()


def read_stack(stack: str) -> dict:
    with open(stack, 'r') as file:
        return json.load(file)


def add_to_stack(skills: dict, stack: str):
    with open(stack, 'w') as file:
        json.dump(skills, file, indent=2, ensure_ascii=False)


def add_skill(value: str, skills):
    skills[value.lower()] = value


def submit_for_verification(keyword: str, skills: dict):
    check = {
        'y': add_skill,
    }
    answer = input(f'{keyword}>>')
    try:
        check[answer](keyword, skills)
    except KeyError:
        pass


def check_skill(skill: str, skills: dict):
    """
    Проверяет скил на вхождение в словарь скилов.
    С помощью исключения вызывает диалог для заполнения словаря скилов.
    """
    try:
        skills[skill.lower()]
    except KeyError:
        pass
        # submit_for_verification(skill, skills)# Это нужно на будущее


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


def filtering_skills(data: str) -> List[str]:
    """
    Фильтрует строку с требованиями из вакансии и превращает ее в список.
    """
    regex_filter = re.compile(r'([a-zA-Z]+)')
    data = ' '.join(data.split('\n'))
    fuck = ''.join(
        [i for i in (data) if i not in (',', ';', '.', '-', ')', '(')]
    )
    return [i for i in filter(regex_filter.match, fuck.split(' '))]


def split_requirements_string(data: str) -> List[str]:
    fuck = data.split('\n')
    return fuck


def get_work_requirements(text: str):
    """Функция для наполнения словаря
    со всевозможными скилами c помощью консоли."""
    skills = read_stack(ALL_STACK_PATH)
    # data_string = read_txt()
    data_string = text
    filtered_skills = filtering_skills(data_string)
    iteration_for_check_skills(filtered_skills, skills)
    add_to_stack(skills, ALL_STACK_PATH)


def add_my_skills():
    """Функция заполняет словарь со скилами пользователя."""
    all_skills = read_stack(ALL_STACK_PATH)
    if not os.path.exists(MY_STACK_PATH):
        add_to_stack({}, MY_STACK_PATH)
    user_skills = read_stack(MY_STACK_PATH)
    iteration_for_check_user_skills(all_skills, user_skills)
    add_to_stack(user_skills, MY_STACK_PATH)


if __name__ == '__main__':
    # add_my_skills()
    split_requirements_string(
        ('PostgreSQL\nPython\nKafka\nDocker\nDjango Framework\nMongoDB'
         '\nRabbitMQ\nElasticsearch\nRedis\nCelery\nNginx')
    )
