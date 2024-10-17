def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

# Parámetros dados
p = 83
q = 97
e = 5
m = 100

# Calcular n y φ(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Verificar que e es coprimo con φ(n)
if gcd(e, phi_n) != 1:
    raise ValueError("e no es coprimo con φ(n)")

# Calcular el cifrado c
c = mod_exp(m, e, n)

print(f"El cifrado de m = {m} usando RSA es c = {c}")