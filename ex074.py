import random
n = random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100),\
    random.randint(0, 100)
for i in n:
    print(f'{i} ', end='')
print('\n')
print(max(n))
print(min(n))