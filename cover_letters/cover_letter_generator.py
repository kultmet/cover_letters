from constants import *
from hard_skills import read_stack, check_skill, add_to_stack


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


def generator(
    company: str = '',
    position: str = '',
    interest: str = '',
    requirements: list = None):
    relevant, irrelevant = get_relevant_experience(requirements)
    message = MESSAGE.format(
        first_name=FIRST_NAME,
        last_name=LAST_NAME,
        company=company,
        position=position,
        interest=interest,
        relevant_skills=relevant,
        irrelevant_skills=irrelevant,
        telegram=TELEGRAM,
        phone_number=PHONE_NUMBER
    )
    return message


def save_file(message, company):
    with open(f'{company}.txt', 'w') as file:
        file.write(message)


if __name__ == '__main__':
    company = COMPANY
    generator = generator(
        company=company,
        position=POSITION,
        interest=INTEREST,
        requirements=REQUIREMENTS
    )
    print(generator)
    save_file(generator, company)
