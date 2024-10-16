def square_and_multiply(base, exponente, modulo):
    """
    Implementa el algoritmo Square and Multiply para exponenciación modular
    Calcula: (base^exponente) mod modulo
    """
    # Convertir el exponente a binario y eliminar el '0b' del inicio
    exp_binario = bin(exponente)[2:]
    
    # Inicializar el resultado como 1
    resultado = 1
    
    print(f"\nPasos Square & Multiply para {base}^{exponente} mod {modulo}:")
    print(f"Exponente en binario: {exp_binario}")
    print("Paso a paso:")
    
    # Iterar sobre cada bit del exponente
    for i, bit in enumerate(exp_binario):
        # Square (siempre se hace el cuadrado)
        if i != 0:  # No hacer el cuadrado en la primera iteración
            resultado = (resultado * resultado) % modulo
            print(f"Square: {resultado}")
        
        # Multiply (solo si el bit es 1)
        if bit == '1':
            resultado = (resultado * base) % modulo
            print(f"Multiply: {resultado}")
    
    return resultado

def cifrar_rsa_sm(m, e, n):
    """Cifra el mensaje m usando RSA con Square & Multiply"""
    return square_and_multiply(m, e, n)

def descifrar_rsa_sm(c, d, n):
    """Descifra el mensaje c usando RSA con Square & Multiply"""
    return square_and_multiply(c, d, n)

# Valores dados en el problema
p = 83
q = 97
e = 5
n = p * q
m = 100

print("RSA usando Square & Multiply")
print(f"Valores iniciales:")
print(f"p = {p}")
print(f"q = {q}")
print(f"e = {e}")
print(f"n = p*q = {n}")
print(f"m = {m}")

# Cifrar usando Square & Multiply
print("\nProceso de cifrado:")
c = cifrar_rsa_sm(m, e, n)
print(f"Mensaje cifrado (c) = {c}")

# Calcular phi(n) y d
phi = (p - 1) * (q - 1)
print(f"\nphi(n) = (p-1)(q-1) = {phi}")

# Calcular d usando el algoritmo extendido de Euclides
def algoritmo_extendido_euclides(a, b):
    if a == 0:
        return b, 0, 1
    mcd, s1, t1 = algoritmo_extendido_euclides(b % a, a)
    s = t1 - (b // a) * s1
    t = s1
    return mcd, s, t

def mod_multiplicativo_inverso(e, phi):
    _, s, _ = algoritmo_extendido_euclides(e, phi)
    return s % phi

d = mod_multiplicativo_inverso(e, phi)
print(f"d = {d}")

# Descifrar usando Square & Multiply
print("\nProceso de descifrado:")
m_descifrado = descifrar_rsa_sm(c, d, n)
print(f"Mensaje descifrado = {m_descifrado}")

# Verificación
print(f"\nVerificación:")
print(f"Mensaje original = {m}")
print(f"Valor cifrado c = {c}")
print(f"Mensaje después de cifrar y descifrar = {m_descifrado}")
print(f"¿Coinciden? {'Sí' if m == m_descifrado else 'No'}")

