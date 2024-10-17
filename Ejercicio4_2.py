def algoritmo_extendido_euclides(a, b): # Algoritmo extendido de Euclides
    if a == 0: # Caso base
        return b, 0, 1 # Devolver mcd(b, 0) = b y los coeficientes de Bezout s = 0, t = 1
    mcd, s1, t1 = algoritmo_extendido_euclides(b % a, a) # Llamada recursiva
    s = t1 - (b // a) * s1 # Calcular los coeficientes de Bezout s y t
    t = s1 
    return mcd, s, t # Devolver mcd(a, b) = mcd(b % a, a) y los coeficientes de Bezout s y t

def mod_multiplicativo_inverso(e, phi): # Calcular el inverso multiplicativo de e módulo phi
    _, s, _ = algoritmo_extendido_euclides(e, phi) # Calcular el inverso multiplicativo de e módulo phi 
    return s % phi # Devolver el inverso multiplicativo de e módulo phi

def descifrar_rsa_sm(c, d, n): # Descifrar un mensaje cifrado c usando la clave privada d y el módulo n
    return pow(c, d, n) # Devolver el mensaje descifrado

# Parámetros dados
p = 83
q = 97
e = 5
c = 5869  # Valor cifrado obtenido previamente en 4.1

# Calcular n y φ(n)
n = p * q 
phi = (p - 1) * (q - 1)

# Calcular d usando el algoritmo extendido de Euclides
d = mod_multiplicativo_inverso(e, phi) 
print(f"d = {d}") # Imprimir el valor de d

# Descifrar el mensaje cifrado c
m_descifrado = descifrar_rsa_sm(c, d, n) 
print(f"Mensaje descifrado = {m_descifrado}") # Imprimir el mensaje descifrado