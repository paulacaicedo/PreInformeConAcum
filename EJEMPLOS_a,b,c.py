
#EJEMPLOS A
contador = 0
x = 0
while x <= 30:
    print(x)
    x = x + 1
    if x % 2 == 0:
        contador = contador + 1
print("Numeros pares que hay son: ", contador)

suma = 0
x = 0
while x <= 10:
    print(x)
    x = x + 1
    suma = x + x
print("La suma de los numeros digitados es: ", suma)

negativos = 0
x = -5
do:
x = x + 1
print(x)
print("Los numeros negativos son: ", negativos)
while x <= 2:
    if x < 0:
        negativos = negativos + 1

bucle = 0
x = 0
do:
bucle = bucle + 1
print("El ciclo se realizo: ", bucle)
while x < 5:
    print(x)


#EJEMPLOS B
suma = 0
sumacom = 0
for i in range(5, 20):
    print(i)
    if i == 5:
        suma = suma + i
    if i == 19:
        sumacom = suma + i
print("La suma es: ", sumacom)

acum = 0
for i in range(1, 10):
    x = int(input("Introduce un digito: "))
    if x < 0:
        acum = acum + 1
print("El ciclo se realizo", i)
print("Numeros negativos son: ", acum)

#EJEMPLOS C
for i in range(5):
    z = x
    x = y
    y = z
    print(x, y)

num_inter = 0
for i in range(10):
    print(i)
    if i == 5:
        num_inter = i
print("El numero intermedio es: ", num_inter)


