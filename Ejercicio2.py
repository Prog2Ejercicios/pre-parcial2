'''
## Ejercicio 2
Escribir una función ``es_vocal(caracter)`` que tome un carácter y devuelva un valor logico(True si es una vocal, 
de lo contrario devuelve False)
'''

def es_vocal(caracter):

    caracter=caracter.lower()

    if(caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u'):
        return True
    else:
        return False

print(es_vocal(input("Ingrese un caracter: ")))