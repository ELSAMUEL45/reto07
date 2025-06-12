#hacer listado del 1 al 100 con todo al cuadrado
for i in range(1, 101):
    print(i, "al cuadrado es", i**2)

#Impares del 1 al 999 y luego pares del 2 al 1000:
print("Impares del 1 al 999:")
for i in range(1, 1000, 2):
    print(i)

print("\nPares del 2 al 1000:")
for i in range(2, 1001, 2):
    print(i)

#Pares descendentes desde un número n ≥ 2:
n = int(input("Ingrese un número mayor o igual a 2: "))
if n % 2 != 0:
    n = n - 1
for i in range(n, 1, -2):
    print(i)

#Números hasta n con su factorial:
n = int(input("Ingrese un número natural: "))
for i in range(1, n + 1):
    f = 1
    for j in range(1, i + 1):
        f = f * j
    print("El factorial de", i, "es", f)

# Calcular 2 elevado a la n:
n = int(input("Ingrese el exponente n: "))
resultado = 1
for i in range(n):
    resultado = resultado * 2
print("2 elevado a", n, "es", resultado)

#Calcular x^n sin usar **:
n = int(input("Ingrese el exponente n: "))
x = float(input("Ingrese el número x: "))
resultado = 1
for i in range(n):
    resultado = resultado * x
print(x, "elevado a", n, "es", resultado)

#Tablas de multiplicar del 1 al 9:
for i in range(1, 10):
    print("Tabla del", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()