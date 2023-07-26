import json
import numpy as np

'''
with open('data.json','r')as f:
    txt = list(json.load(f))
div3 = np.mean([n for n in txt if n%3 == 0])
print(div3)
'''

def x(dict):

    return {value: len(value) for key, value in dict.items()}
print(x({1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'},))

the = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
for i in the.values:
    for num in i:
