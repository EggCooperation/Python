import random


def lotería():
    for i in range(9):
        yield random.randint(0, 100)
    yield random.randint(1, 9)


for número_azar in lotería():
    print(f"Y el próximo número es {número_azar}!!!")
