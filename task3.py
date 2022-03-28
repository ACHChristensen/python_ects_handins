#Opgave 3 : Lav en funktion som kan finde koordinaterne på et monument baseret på monumentets id eller navn: 
# F.eks. 
# def monumentsById(monumentId):
#       return cooridinates

import pandas as pd

'''Denne viser kooridinater til monumenter pr. id eller navn i kbh via en CSV fil'''
def cooridinates_of_monument(file, name = None, id = None):
    try:
        df = pd.read_csv(file)
        if(name == None and id == None):
            raise TypeError
        elif (name == None):
            monument_info = df.loc[df['id'] == id]
        else: 
            monument_info = df.loc[df['navn'] == name]
        longitude = monument_info['longitude']
        latitude = monument_info['latitude']
        return {"longitude": float(longitude), "latitude":float(latitude)}
    except TypeError:
        print("Needs either name or id for momunment")

    
if __name__ == '__main__':
    print("With no name or id = " + str(cooridinates_of_monument('monumenter.csv')))
    #For tests skyld svarer nedenstående id til navnet i de to eksempler
    print("\nWith no name but id no. 50140 = " + str(cooridinates_of_monument('monumenter.csv', id=50140)))
    print("\nWith no name but id no. 50140 = " + str(cooridinates_of_monument('monumenter.csv', name="Vinsugende satyrdreng")))

