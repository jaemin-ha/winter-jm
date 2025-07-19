### 백준 1076 저항
##  2초

resistance_1 = {
    'black': '0',
    'brown': '1',
    'red': '2',
    'orange': '3',
    'yellow': '4',
    'green': '5',
    'blue': '6',
    'violet': '7',
    'grey': '8',
    'white': '9',
}

resistance_2 = {
    'black': 1,
    'brown': 10,
    'red': 100,
    'orange': 1000,
    'yellow': 10000,
    'green': 100000,
    'blue': 1000000,
    'violet': 10000000,
    'grey': 100000000,
    'white': 1000000000,
}

color_1 = input()
color_2 = input()
color_3 = input()

result = int(resistance_1[color_1] + resistance_1[color_2]) * resistance_2[color_3]

print(result)