#Escribir un programa que pregunte ao usuario a súa idade e mostre por pantalla todos os anos que cumpriu (desde 1 ata a súa idade).

if __name__ == '__main__':
    print("Introduzca unha idade")
    idade = input()


    for i in range(int(idade)):
        print(f"Cumpliche {i}")