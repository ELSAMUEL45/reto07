# reto07
Imprimir del 1 al 100 con su respectivo cuadrado
```python
for i in range(1, 101):
    print(i, "al cuadrado es", i * i)
```
Imprimir impares del 1 al 999 y pares del 2 al 1000
```python
print("Impares del 1 al 999:")
for i in range(1, 1000, 2):
    print(i)

print("\nPares del 2 al 1000:")
for i in range(2, 1001, 2):
    print(i)
```
 Imprimir pares en forma descendente hasta 2, menores o iguales a n (n ≥ 2)
 ```python
n = int(input("Ingrese un número mayor o igual a 2: "))
if n % 2 != 0:
    n = n - 1
for i in range(n, 1, -2):
    print(i)
```
 Imprimir números del 1 a n con su respectivo factorial
 ```python
n = int(input("Ingrese un número natural: "))
for i in range(1, n + 1):
    f = 1
    for j in range(1, i + 1):
        f = f * j
    print("El factorial de", i, "es", f)
```

