from random import choice
from string import ascii_letters, digits

def create_random_short(base_url='http://yacut.ru', lenght=6):
    return (
        f'{base_url}/{"".join([choice(ascii_letters + digits) for _ in range(lenght)])}'
    )
print(create_random_short())
