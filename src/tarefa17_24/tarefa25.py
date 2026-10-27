# Escribir un programa que lea un enteiro positivo, n, introducido polo usuario e despois mostre en pantalla a suma de todos vos enteiros desde 1 ata n.

# Para facelo implementa unha función que reciba un valor n e calcule ou resultado usando a seguinte formula:

# resultado =  n * ( n + 1)  / 2

if __name__ == '__main__':

    def potencia (n):
        resultado =  n * ( n + 1)  / 2
        return resultado
    
    
    print("Introduzca un numero inteiro positivo")
    n = int(input()) # type: ignore
    print(potencia(n))