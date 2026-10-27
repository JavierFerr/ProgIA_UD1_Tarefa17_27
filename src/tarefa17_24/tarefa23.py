#Escribir un programa que almacene a cadea de caracteres contrasinal nunha variable,
# pregunte ao usuario polo contrasinal ata que introduza o contrasinal correcto.

#Parecido a un dos anteriores, pero neste caso se trata de conseguir mediante un bucle a repetición ata acertar co contrasinal

if __name__ == '__main__':
    print("Introduzca unha contrasinal para gardar")
    con = input() # type: ignore

    print("Introduzca a contrasinal")
    intento = input()

    while con != intento:
        print("La contraseña es incorrecta intentelo de nuevo\n")
        print("Introduzca a contrasinal")
        intento = input()
    print("Contraseña correcta")
 