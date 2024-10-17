import math

# Funcion para calcular los factores primos de un numero
def factores_primos(n):
    factores_primos = []
    # Probar divisibilidad por 2 primero
    while n % 2 == 0:
        factores_primos.append(2)
        n = n // 2
    # Probar divisibilidad por números impares desde 3 hasta la raíz cuadrada de n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factores_primos.append(i)
            n = n // i
    # Si n es un número primo mayor que 2
    if n > 2:
        factores_primos.append(n)
    return factores_primos

# Ejemplo de uso
print(factores_primos(111475))