from string import ascii_letters, digits

# Сетевые настройки
PROTOCOL = 'http'
DOMAIN_NAME = 'yacut.ru'
BASE_URL = f'{PROTOCOL}://{DOMAIN_NAME}'

# Настройки генератора коротких ссылок
MAX_GENERATION_BAD_ATTEMPS = 20
MAX_SHORT_LENGTH = 6
SHORT_ALLOWED_SYMBOLS = ascii_letters + digits

# Настройки пользовательских коротких ссылок
CUSTOM_SHORT_MIN_LENGTH = 1
CUSTOM_SHORT_MAX_LENGTH = 16