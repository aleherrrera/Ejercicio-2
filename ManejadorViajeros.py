from ViajeroFrecuente import Viajero

class Lista:

    __viajeros = []

    def __init__(self):
        self.__viajeros = []

    def agregarViajero(self,viajero):
        self.__viajeros.append(viajero)

    def testArchivo(self):
        import csv
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            num = fila[0]
            dni = fila[1]
            nom = fila[2]
            apell = fila[3]
            milla = int(fila[4])
            unViajero = Viajero(num,dni,nom,apell,milla)
            self.agregarViajero(unViajero)
        archivo.close()

    def buscaViajero(self,numero):
        for indice, viajero in enumerate(self.__viajeros):
            if viajero.getNumero() == numero:
                return indice

    def getViajero(self, indice):
        return self.__viajeros[indice]

    def acumula(self,numero,millas):
        i = self.buscaViajero(numero)
        if i != None:
            v = self.getViajero(i)
            v.acumularMillas(millas)

    def canje(self,numero,millas):
        i = self.buscaViajero(numero)
        if i != None:
            v = self.getViajero(i)
            v.canjearMillas(millas)

    def getMillas(self,numero):
        i = self.buscaViajero(numero)
        if i != None:
            v = self.getViajero(i)
            print('{}'.format(v.cantidadTotaldeMillas()))


    def __str__(self):
        s = 'Numero Apellido  Nombre    DNI      Millas acumuladas\n'
        for viajero in self.__viajeros:
            s += str(viajero) + '\n'
        return s






