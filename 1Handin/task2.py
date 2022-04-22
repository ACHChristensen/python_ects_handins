#Opgave 2 : Hvor mange monumenter bliver vedligeholdt? Dv. graffitirenhold = ja

import pandas as pd

'''Denne viser hvor mange monumenter der bliver vedligeholdt/graffitirenholdt i kbh via en CSV fil'''
def maintaint_monuments(file):
    df = pd.read_csv(file)
    return df['graffitirenhold'].value_counts()['Ja']

if __name__ == '__main__':
    print(maintaint_monuments('monumenter.csv'))
