#Escribir un programa que pida ao usuario un número enteiro positivo e mostre por pantalla a conta atrás desde ese número ata cero

if __name__ == '__main__':
    print("Introduzca un numero enteiro positivo")
    num = int(input())

    for i in range(num):
        print((num - i))
    