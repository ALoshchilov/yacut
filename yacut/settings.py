from sre_parse import SPECIAL_CHARS
from string import ascii_letters, digits

# Настройки генератора коротких ссылок
MAX_GENERATION_BAD_ATTEMPS = 20
MAX_SHORT_LENGTH = 6
SPECIAL_SYMBOLS = r'!@#$%^&*{\}\[\]\|(\)'
SHORT_ALLOWED_SYMBOLS = ascii_letters + digits
SHORT_REGEXP = rf'(^[{SHORT_ALLOWED_SYMBOLS}]*$)'

# Настройки пользовательских коротких ссылок
CUSTOM_SHORT_MAX_LENGTH = 16

# Настройки валидатора оригинальных ссылок
# Cloudflare (CDN) - 32768  знаков, url больше невозможен
ORIGINAL_MAX_URL_LENGTH = 32768
