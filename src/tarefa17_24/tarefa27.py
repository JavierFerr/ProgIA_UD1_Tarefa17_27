# Escribir un programa que pida ao usuario ou seu peso (en kg) e estatura (en centímetros), calcule ou índice de masa corporal e o almacene nunha variable,
# e mostre por pantalla a frase: O teu índice de masa corporal é <imc> onde <imc> é o índice de masa corporal calculado redondeado con dous decimais.

# O indice de masa corporal de calcula dividindo o peso en Kg polo cuadrado da altura medida en metros.

if __name__ == '__main__':
    print("Introduzca peso en kg e estatura en cm")
    peso,estatura = int(input()),int(input())  # type: ignore

    imc = peso/((estatura/100)**2)

    print(f"O teu índice de masa corporal é {imc}")
    