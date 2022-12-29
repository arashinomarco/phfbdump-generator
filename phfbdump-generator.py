import os
import random as ran

with open('First Names.txt', 'r', encoding='utf-8') as File1, open('First Names 2.txt', 'r', encoding='utf-8') as File2, open('First Names 3.txt', 'r', encoding='utf-8') as File3, open('Middle Names.txt', 'r', encoding='utf-8') as File4, open('Last Names.txt', 'r', encoding='utf-8') as File5:
    FirstName = File1.readlines()
    FirstName2 = File2.readlines()
    FirstName3 = File3.readlines()
    MiddleName = File4.readlines()
    LastName = File5.readlines()

DummyName = []

if 'Suffixes.txt' in os.listdir():
    with open('Suffixes.txt', 'r', encoding='utf-8') as File6:
        Suffix = File6.readlines()

Chance1 = 1
Chance2 = 1
Chance3 = 1
Chance4 = 1
Chance5 = 1

SuffixChance = []

ranges = [(0, 20, Chance1), (21, 40, Chance2), (41, 60, Chance3), (61, 80, Chance4), (81, 100, Chance5)]

for (start, end, Chance) in ranges:
    for i in range(Chance):
        SuffixChance.append(ran.uniform(start, end))

DummyName = []
for i, chance in enumerate(SuffixChance):
    first = ran.choice(FirstName).strip()
    first2 = ran.choice(FirstName2).strip()
    first3 = ran.choice(FirstName3).strip()
    middle = ran.choice(MiddleName).strip()
    last = ran.choice(LastName).strip()
    if chance < 2.5:
        name = f'{first} {middle} {last}'
    elif chance < 5:
        name = f'{first} {first2} {middle} {last}'
    elif chance < 7.5:
        name = f'{first} {first2} {first3} {middle} {last}'
    elif chance < 10:
        suffix = Suffix[i // Chance1]
        name = f'{first} {middle} {last} {suffix}'
    elif chance < 12.5:
        name = f'{first} {middle} {last}'
    elif chance < 15:
        name = f'{first} {first2} {middle} {last}'
    elif chance < 17.5:
        name = f'{first} {first2} {first3} {middle} {last}'
    elif chance < 20:
        suffix = Suffix[i // Chance2]
        name = f'{first} {middle} {last} {suffix}'
    elif chance < 22.5:
        name = f'{first} {middle} {last}'
    elif chance < 25:
        name = f'{first} {first2} {middle} {last}'
    elif chance < 27.5:
        name = f'{first} {first2} {first3} {middle} {last}'
    elif chance < 30:
        suffix = Suffix[i // Chance3]
        name = f'{first} {middle} {last} {suffix}'
    elif chance < 32.5:
        name = f'{first} {middle} {last}'
    elif chance < 35:
        name = f'{first} {first2} {middle} {last}'
    elif chance < 37.5:
        name = f'{first} {first2} {first3} {middle} {last}'
    elif chance < 40:
        suffix = Suffix[i // Chance4]
        name = f'{first} {middle} {last} {suffix}'
    elif chance < 42.5:
        name = f'{first} {middle} {last}'
    elif chance < 45:
        name = f'{first} {first2} {middle} {last}'
    elif chance < 47.5:
        name = f'{first} {first2} {first3} {middle} {last}'
    elif chance < 50:
        suffix = Suffix[i // Chance5]
        name = f'{first} {middle} {last} {suffix}'
    elif chance < 52.5:
        name = f'{first} {middle} {last}'
    elif chance < 55:
        name = f'{first} {first2} {middle} {last}'
    elif chance < 57.5:
        name = f'{first} {first2} {first3} {middle} {last}'
    elif chance < 60:
        suffix = Suffix[i // Chance1]
        name = f'{first} {middle} {last} {suffix}'
    elif chance < 62.5:
        name = f'{first} {middle} {last}'
    elif chance < 65:
        name = f'{first} {first2} {middle} {last}'
    elif chance < 67.5:
        name = f'{first} {first2} {first3} {middle} {last}'
    elif chance < 70:
        suffix = Suffix[i // Chance2]
        name = f'{first} {middle} {last} {suffix}'
    elif chance < 72.5:
        name = f'{first} {middle} {last}'
    elif chance < 75:
        name = f'{first} {first2} {middle} {last}'
    elif chance < 77.5:
        name = f'{first} {first2} {first3} {middle} {last}'
    elif chance < 80:
        suffix = Suffix[i // Chance3]
        name = f'{first} {middle} {last} {suffix}'
    elif chance < 82.5:
        name = f'{first} {middle} {last}'
    elif chance < 85:
        name = f'{first} {first2} {middle} {last}'
    elif chance < 87.5:
        name = f'{first} {first2} {first3} {middle} {last}'
    elif chance < 90:
        suffix = Suffix[i // Chance4]
        name = f'{first} {middle} {last} {suffix}'
    elif chance < 92.5:
        name = f'{first} {middle} {last}'
    elif chance < 95:
        name = f'{first} {first2} {middle} {last}'
    elif chance < 97.5:
        name = f'{first} {first2} {first3} {middle} {last}'
    else:
        suffix = Suffix[i // Chance5]
        name = f'{first} {middle} {last}'
    DummyName.append(name)

for i, name in enumerate(DummyName):
    print(f'\nSuffix Appearance Randomness: {SuffixChance[i]:.2f}%')
    print('\nYour Dummy Name:', name)
