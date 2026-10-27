# Escribir unha función que reciba un número enteiro positivo e devolva o seu factorial.
# O factorial dun número se consegue multiplicando todos os números entre o número orixinal ata 1. Por exemplo:

# O factorial de 5 é:

# f5 = 5 * 4 * 3 * 2 * 1


if __name__ == '__main__':

    def factorial(n):
        f5 = 1
        for i in range(1,n + 1):
            f5 *= i
        return f5
        
    print("Introduzca un numero inteiro positivo")
    n = int(input()) # type: ignore
    print(factorial(n))