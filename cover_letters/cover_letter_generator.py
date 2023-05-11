from typing import List

# from cover_letters.constants import *
from settings import constants
from cover_letters.hard_skills import get_relevant_experience


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
