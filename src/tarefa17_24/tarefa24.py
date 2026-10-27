# Escribir un programa que pida ao usuario un número enteiro e mostre por pantalla se é un número primo ou non.
# Para iso basta que tentes dividir o número polos números menores a n/2.
# Se algún deles divide de xeito exacto ao número entón non é primo, noutro caso debes seguir ata o final.

# Se chegas ata o último divisor e non houbo ningún deles que dividise o número enteiro orixinal entón tes un número primo.

if __name__ == '__main__':
    print("Introduzca un numero inteiro")
    num = int(input()) # type: ignore

    primo = True;
    for i in range(2,num//2):
        
        if num % i == 0:
            primo = False
            print("Non é primo")
            break
    if primo:
        print("É primo")