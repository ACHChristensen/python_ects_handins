#Opgave 1 : Hvor mange monumenter er der i København?

import pandas as pd

'''Denne viser hvor mange monumenter der er i kbh via en CSV fil'''
def number_of_monuments(file):
    df = pd.read_csv(file)
    index = df.index
    return len(index)
 

if __name__ == '__main__':
    print(number_of_monuments('monumenter.csv'))
