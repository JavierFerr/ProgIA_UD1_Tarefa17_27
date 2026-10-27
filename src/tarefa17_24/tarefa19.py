#Escribir un programa que pida ao usuario un número enteiro positivo e mostre por pantalla todos os números impares desde 1 ata ese número.

if __name__ == '__main__':
    print("Introduzca un par")
    par = input()

    for i in range(int(par)):
        if i%2 == 1:
            print(i)
