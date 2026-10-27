#Escribir un programa que pida ao usuario unha palabra e a amose por pantalla 10 veces.

if __name__ == '__main__':
    print("Introduzca unha palabra")
    palabra = input()

    for i in range(10):
        print(palabra)