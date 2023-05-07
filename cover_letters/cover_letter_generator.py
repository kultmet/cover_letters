from typing import List

# from cover_letters.constants import *
from settings import constants
from cover_letters.hard_skills import read_stack, check_skill, add_to_stack


def get_relevant_experience(requirements: list):
    relevant = ''
    irrelevant = ''
    user_skills: dict = read_stack(constants.MY_STACK_PATH)
    all_skills: dict = read_stack(constants.ALL_STACK_PATH)
    for i in range(len(requirements)):
        check_skill(requirements[i], all_skills)
        try:
            relevant += f'{user_skills[requirements[i].lower()]}, '
        except KeyError:
            irrelevant += f'{requirements[i]}, '
    add_to_stack(all_skills, constants.ALL_STACK_PATH)
    return relevant.strip(', '), irrelevant.strip(', ')


def letter_generator(company: str = '',
                     position: str = '',
                     interest: str = '',
                     requirements: List[str] = None):
    relevant, irrelevant = get_relevant_experience(requirements)
    message = constants.MESSAGE.format(
        first_name=constants.FIRST_NAME,
        last_name=constants.LAST_NAME,
        company=company,
        position=position,
        interest=interest,
        relevant_skills=relevant,
        irrelevant_skills=irrelevant,
        telegram=constants.TELEGRAM,
        phone_number=constants.PHONE_NUMBER
    )
    return message


def save_file(message, company):
    with open(f'{company}.txt', 'w') as file:
        file.write(message)


if __name__ == '__main__':
    company = constants.COMPANY
    generator = letter_generator(
        company=company,
        position=constants.POSITION,
        interest=constants.INTEREST,
        requirements=constants.REQUIREMENTS
    )
    print(letter_generator)
    save_file(generator, company)
