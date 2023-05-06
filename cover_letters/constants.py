import os
MESSAGE = """Добрый день, Здравствуйте!
Меня зовут {first_name} {last_name}. Имею опыт в сфере разработки ПО, благодаря которому могу внести свой вклад в успешный рост компании {company}.
Предлагаю на рассмотрение свою кандидатуру на позицию {position}. Имею потребность, наносить пользу обществу, и прилагаю для этого максимальные усилия! Люблю бесконечное развитие и не останавливаю его, даже во время отдыха.

Мой выбор был мотивирован интересом к {interest}.
Владею релевантными знаниями по {relevant_skills}.
Моя экспертиза по {irrelevant_skills} недостаточна для ваших требований но, готов быстро изучить, так как успешно делал это на предыдущих проектах.

Готов выполнить тестовое задание.

Всегда на связи в:
Telegram - {telegram}
WhatsApp - {phone_number}

Спасибо за внимание!"""

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALL_STACK_PATH = 'hard_skills.json'

MY_STACK_PATH = 'user_skills.json'

FIRST_NAME = 'Дмитрий'
LAST_NAME = 'Майстренко'
TELEGRAM = '@kultmet_1'
PHONE_NUMBER = '+79676411880'

COMPANY = 'Бар'
POSITION = 'Хороший парень'
INTEREST= 'пить пиво вместе'
REQUIREMENTS = ['Python', 'PostgreSQL', 'Linux', 'Docker', 'Asyncio', 'Redis', 'Git', 'GraphQL', 'Kubernetes', 'fuck']

