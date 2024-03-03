#!/usr/bin/python3

NAMES = ["Panashe", "Kumbirai", "Kundiso", "Munashe"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print("{} {}".format(NAMES, AGES))

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

#enumarate - putting the numbering to each iteration 

for i, name in enumerate(NAMES):
    print("{} {}".format(i, NAMES[i]))
