#Escribir un programa que lea un enteiro positivo, n, introducido polo usuario e despois mostre en pantalla a suma de todos os enteiros desde 1 ata n.

if __name__ == '__main__':
    print("Introduzca un numero enteiro positivo")
    n = int(input()) # type: ignore
    num = 0
    for i in range(n +1):
        num+=i
    print(num)