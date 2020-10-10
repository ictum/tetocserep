print("Készítette: Frantal Attila, 2020.10.10\n")

sz = 9.6  #a tűzfal alapja méterben
m = 3.2   #a tűzfal magassága méterben
h = 23    #a tető egyik oldalának hossza méterben

import math

h2 = math.sqrt( (sz/2)**2 + m**2 )  #a tető másik oldalának hossza méterben

t = h * h2 * 2   #a befedendő tető területe négyzetméterben

print("A tető területe:", '% .2f' % t , 'négyzetméter')

cserep = 0.25 * 0.12 #cserép mérete négyzetméterben

print('Egy darab cserép területe négyzetméterben:',cserep,'\n')

print(math.ceil( (t * 1.1) / cserep) , "db cserép kell a tető befedéséhez 10%-os ráhagyással.")
