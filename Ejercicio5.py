# Cifrado afín que preserva espacios y caracteres especiales
alfabeto_ingles = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def texto_a_numeros(texto):
    texto = texto.upper()
    numeros = []
    estructura = []  # Lista de tuplas (es_letra, caracter)
    
    for letra in texto:
        if letra in alfabeto_ingles:
            numeros.append(alfabeto_ingles.index(letra))
            estructura.append(('letra', None))
        else:
            estructura.append(('especial', letra))
    
    return numeros, estructura

def numeros_a_texto(numeros, estructura):
    texto = ""
    texto_sin_espacios = ""
    i = 0  # índice para los números
    
    for tipo, caracter in estructura:
        if tipo == 'letra':  # Si es una letra
            letra_cifrada = alfabeto_ingles[numeros[i]]
            texto += letra_cifrada
            texto_sin_espacios += letra_cifrada
            i += 1
        else:  # Si es un carácter especial
            texto += caracter
    
    return texto, texto_sin_espacios

def cifrado_afin(texto, a, b):
    numeros, estructura = texto_a_numeros(texto)
    numeros_cifrados = []
    
    for numero in numeros:
        numeros_cifrados.append((a * numero + b) % 26)
    
    return numeros_a_texto(numeros_cifrados, estructura)

def descifrado_afin(texto_cifrado, a, b):
    # Primero obtenemos los números y estructura del texto cifrado
    numeros, estructura = texto_a_numeros(texto_cifrado)
    numeros_descifrados = []
    
    for numero in numeros:
        numeros_descifrados.append((numero - b) * pow(a, -1, 26) % 26)
    
    return numeros_a_texto(numeros_descifrados, estructura)[0]

# Probamos el código con la frase
frase = "Si la gente no cree que las matemáticas son simples, es solo porque no se dan cuenta de lo complicado que es la vida"
a = 11
b = 15

# Obtenemos las dos versiones del cifrado
frase_cifrada, frase_cifrada_sin_espacios = cifrado_afin(frase, a, b)

print("\nFrase original:", frase)
print("\nFrase cifrada (sin espacios):", frase_cifrada_sin_espacios)
print("\nFrase cifrada (con espacios):", frase_cifrada)
print("\nFrase descifrada:", descifrado_afin(frase_cifrada, a, b))