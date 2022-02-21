'''
Main Module: Dummy Code for testing
'''
import builtins
import math as m                # Importem el mòdul math i li creem el alias 'm'
import random as rnd            # Importem el mòdul random i li creem el alias 'rnd'
import string
import datetime as dt           # Importem el mòdul datetime i li creem el alias 'dt'
import time
import os                       # Accions de sistema (Crear/esborrar directoris, arxius,...)
import platform                 # Informació de la plataforma (Windows, Linus, Nom d'usuaris,...)
from random import randint      # Creem un apuntador directe a la funció randint del mòdul random
from random import randrange    # Creem un apuntador directe a la funció randrange del mòdul random
from random import choice       # Creem un apuntador directe a la funció choice del mòdul random


print(m.pi)
print(m.e)
print(m.sqrt(9))

print(rnd.randint(1, 10))
print(rnd.randrange(1, 10, 2))
print(rnd.choice("AEIOU"))

'''
Manera transparent de crear un string, cridem a la class i li passem el estat del objecte que es crearà (contingut)
'''
string_dani = builtins.str("DANI")
print(f"String dani: {string_dani}")

# Creem un objecte amb la class datetime del mòdul datetime
fecha = dt.datetime(2022,2,16)

# Cridem a les funcions randint, randrange i choice directament amb els apuntadors a aquestes funcions del mòdul random que hem creat a la secció inicial d'importacions
print(randint(1, 10))
print(randrange(1, 10, 2))
print(choice("AEIOU"))


gen1 = rnd.Random()     # Passem com estat la seed (semilla inicial)
gen2 = rnd.Random(100)  # Passem l'estat '100'

i = 0
while i < 20:
    i += 1
    print(gen1.randint(1,10))
    print(gen1.randrange(1,100,1))
    print(gen1.uniform(1,10))
    print(gen1.random())
    print("*" * 50)
    print(gen2.randint(1,10))
    print(gen2.randrange(1,100,1))
    print(gen2.uniform(1,10))
    print(gen2.random())
    print("-" * 50)


for c in "hola":
    print(c)

