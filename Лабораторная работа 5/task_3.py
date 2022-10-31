import random
def get_unique_list_numbers() -> list[int]:
    flag = False
    while not flag:
        list_random = [random.randint(-10, 10) for _ in range(16)]
        compare = set(list_random)
        if len(compare) == len(list_random):
            flag = True
    return list_random

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
