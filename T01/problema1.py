dato = int(input("ingresa un numero: "))
for i in range(1, dato + 1):
    x = 0
    for j in range(1, (i // 2) + 1):
        if ((i % j) == 0):
             x = x + j;
    if (x == i):
        print("El numero %s en la lista de numeros, es perfecto" %i)