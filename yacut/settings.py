from string import ascii_letters, digits

# Сетевые настройки
PROTOCOL = 'http'
DOMAIN_NAME = 'localhost'
BASE_URL = f'{PROTOCOL}://{DOMAIN_NAME}'

# Настройки генератора коротких ссылок
MAX_GENERATION_BAD_ATTEMPS = 20
MAX_SHORT_LENGTH = 6
SHORT_ALLOWED_SYMBOLS = ascii_letters + digits
SHORT_REGEXP = r'^[a-zA-Z\d]{1,16}$'

# Настройки пользовательских коротких ссылок
CUSTOM_SHORT_MIN_LENGTH = 1
CUSTOM_SHORT_MAX_LENGTH = 16

# Настройки валидатора оригинальных ссылок
URL_REGEXP = (
    r'^(?:http|ftp)s?://'  # http:// или https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+' +
    r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # домен
    r'localhost|'  # localhost
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ... или ip-адрес
    r'(?::\d+)?'  # опционально - порт в URL
    r'(?:/?|[/?]\S+)$'
)