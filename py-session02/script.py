"""
Python DocString
"""
import builtins
import math
import os
import random


print("Strings simples \n--------------")
# Print d'una frase
print("Hello World from Python!!")
# Print de variables
print("A", "B", "C", 'C', 'D')
print()

'''
Funcions del mòdul math
math.e: Ens dona el valor de la constant de Euler
math.pi: Ens dona el valor de la constant pi
math.sqrt(9): Ens dona el valor de l'arrel quadrada de 9
'''
print("Constants \n--------------")
print(math.e)
print(math.pi)
print(math.sqrt(9))
print()

'''
Utilitzem la funció randint del mòdul random per posició o per nom
per possició: passem només el valor de les variables
per nom: al passar el valor de les variables definim per a quin paràmetre és cada valor
'''
print("Utilitzem la funció randint del mòdul random per posició o per nom \n--------------")
# per possició
print(random.randint(1, 100))
# per nom
print(random.randint(a=1, b=100))
print()

'''
Utilitzem la funció randrange del mòdul random per crear un número indicant
start: número inicial del rang
stop: número final del rang
step: número amb el que la funció farà salts (el valor per defecte és '1'), en el següent exemple acabarà donant-nos un número aleatori múltiple de 5
'''
print("Utilitzem la funció randrange del mòdul random per crear un número indicant \n--------------")
print(random.randrange(start = 0, stop = 500, step = 5))
print()

'''
Declarem variables i fem un print per veure els seus valors
op1: La variable tindrà un número aletori entre 1 i 100 inclós (El número final sempre està inclós si utilitzem la funció randint del mòdul random)
op2: La variable tindrà un número aleatori entre 0 i 200 sense incloure i amb salts de 10 números a l'hora de triar un número aleatori
rmax: La variable tindrà el valor superior entre les variables op1 i op2
rmin: La variable tindrà el valor inferior entre les variables op1 i op2
rqsrt: La variable tindrà el valor de l'arrel quadrada de la variable op3
Printem el contingut de totes les variables amb print()
'''
print("Declarem variables i fem un print per veure els seus valors \n--------------")
op1 = random.randint(1, 100)
op2 = random.randrange(start=0,stop=200,step=10)
op3 = random.randint(1,100)
rmax = max(op1, op2)
rmin = min(op1, op2)
rsqrt = math.sqrt(op3)
print(op1,op2,op3,rmax,rmin,rsqrt)
print()

print("Format de sortida en mode pueblerino \n--------------")
# Donem el format a les sortides
print("MAX(", op1, ", ", op2, ")=", rmax, sep = "")
print("MIN(", op1, ", ", op2, ")=", rmin)
print("SQRT(", op3, ")=", rsqrt)
print()

'''
Per concatener amb '+' s'ha de transformar els valors que no són string a string amb la funció str() sinó tindrem un error perquè ens dirà que hi han valors que són del tipus int
El següent exemple veiem una mala utilització de concatenació "RES RECOMANABLE"
'''
print("Concatenació pueblerina amb '+' \n--------------")
print("MAX(" + str(op1) + ", " + str(op2) + ") =" + str(rmax))
print()

'''
Mètode d'string format()
Aquest mètode s'utilitza per triar el format de sortida d'un string al nostre gust
'''
print("Mètode d'string format() \n--------------")
print("1MAX({}, {}) = {} \n MIN({}, {}) = {}".format(op1, op2, rmax, op1, op2, rmin))
print("2MAX({0}, {1}) = {2} \n MIN({0}, {1}) = {3}".format(op1, op2, rmax, rmin))
print("MAX({p1}, {p2}) = {p3} \nMIN({p1}, {p2}) = {p4}".format(p1 = op1, p2 = op2, p3 = rmax, p4 = rmin))
print("SQRT({p1}) = {result:.2f}".format(p1 = op3, result = rsqrt))
print("Decimal: {0:d} Hexadecimal: {0:X} Octal: {0:o}".format(255))
print()

'''
També podem donar format a la nostra sortida utilitzant print(f"<string que volem formatejar>")
'''
print("Format de sortida amb print(f\"<string que volem formatejar> \n--------------")
print(f"MAX({op1}, {op2}) = {rmax}")
print(F"MAX({op1}, {op2}) = {rmax}")
print(f"MAX({op1}, {op2} = {rmax}")
print(f"SQRT({op3}) = {rsqrt:.2f}")
print()

'''
Funció input del mòdul builtins (no fa falta utilitzar builtin.input perquè aquest mòdul ve per defecte)
Aquesta funció et demana entrada per teclat i no finalitza fins que no fem un ENTER, en el següent cas es fa el següent:
1- Ens demana una entrada de teclat
2- La desa a la variable 'v'
3- La mostra per pantalla amb el print()
'''
print("Funció input del mòdul builtins \n--------------")
v = input("Dime cosas: ")
print("Resultat:",v)

'''
MANEL
'''