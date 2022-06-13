'''
## Ejercicio 1
Definir una función ``max_de_tres(nr1, nr2, nr3)``, que tome tres números como argumentos y 
devuelva el mayor de ellos.
'''
def max_de_tres(nr1, nr2, nr3):
    if((nr1 > nr2) and (nr1 > nr3)):
        return nr1
    elif((nr2 > nr1) and (nr2 > nr3)):
        return nr2
    elif((nr3 > nr1) and (nr3 > nr2)):
        return nr3
    elif((nr1 == nr2) and (nr1 > nr3)):
        return nr1
    elif((nr1 == nr3) and (nr1 > nr2)):
        return nr1
    elif((nr2 == nr3) and (nr2 > nr1)):
        return nr2
    elif((nr1 == nr2) and (nr1 == nr3)):
        return nr1
    
print(max_de_tres(1,2,3))