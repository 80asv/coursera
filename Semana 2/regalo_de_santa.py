from ctypes.wintypes import PINT


def esPalindromo(num: int) -> bool:
    num_invertido = str(num)[::-1]    
    return num_invertido == str(num)

def parImpar(num: int)-> str:
    if num%2 == 0:
        res = "par"
    else:
        res = "impar"
    return res

def clasificar_regalo(id: int)->str:
    # Si el número es palíndromo e impar
    if esPalindromo(id) and parImpar(id) == "impar":
        res = "girl"
    # Si el número es palíndromo y par
    elif esPalindromo(id) and parImpar(id) == "par":
        res = "boy"
    # Si el número es par, pero no palíndromo
    elif parImpar(id) == "par" and not esPalindromo(id):
        res = "man"
    # Si el número es impar, pero no palíndromo
    else:
        res = "woman"
    return res

print(clasificar_regalo(864))
print(esPalindromo(864))
print(parImpar(864))