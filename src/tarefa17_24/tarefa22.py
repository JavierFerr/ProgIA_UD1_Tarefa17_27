#Escribir un programa que pida ao usuario un número enteiro e mostre por pantalla un triángulo rectángulo como o de máis abaixo, de altura o número introducido.
#*
#**
#***
#****
#*****
#Cando un string se multiplica por un número, o resultado é o string duplicado o número de veces indicado.

if __name__ == '__main__':
    print("Introduzca un numero enteiro positivo")
    n = int(input()) # type: ignore
    for i in range(n + 1):
        print((i*"*"))