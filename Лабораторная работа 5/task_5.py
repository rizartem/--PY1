import string
import random


def get_random_password(n=8) -> str:
    pull = string.ascii_letters + string.digits
    return ''.join(random.sample(pull, n))


print(get_random_password())
