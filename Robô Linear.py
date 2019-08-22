# Respostas das questões:
# 1) 2
# 2) d)

import re

while True:
    string = input('Moves: ')

    if string == '0':
        break

    F = re.findall("F", string)
    T = re.findall("T", string)

    numberOfF = len(F)
    numberOfT = len(T)

    distance = numberOfF - numberOfT
    print(distance)