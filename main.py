from ManejadorViajeros import Lista

def getNumero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input('Introduce un numero entero: '))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num

if __name__ == '__main__':

    listaViajeros = Lista()
    listaViajeros.testArchivo()
    print(listaViajeros)

    numero = (input('Ingrese numero de viajero(0 para terminar):'))
    while numero != '0':

        i = listaViajeros.buscaViajero(numero)
        if i != None:

            salir = False
            opcion = 0
            while not salir:

                print("1. Connsultar cantidad de millas")
                print("2. Acumular millas")
                print("3. Canjear millas")
                print('4. Salir')

                print("Elige una opcion")

                opcion = getNumero()

                if opcion == 1:
                    listaViajeros.getMillas(numero)

                elif opcion == 2:
                    milla = int(input('Ingrese cantidad de millas a acumular:'))
                    listaViajeros.acumula(numero,milla)

                elif opcion == 3:
                    millas = int(input('Ingrese millas a canjear:'))
                    listaViajeros.canje(numero,millas)

                elif opcion == 4:
                    salir = True

                else:
                    print("Introduce un numero entre 1 y 4")
        else:
            print('Numero de viajero incorrecto')
        numero = (input('Ingrese numero de viajero(0 para terminar):'))

    print(listaViajeros)


