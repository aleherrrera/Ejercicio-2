
class Viajero:

    __numero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas = 0

    def __init__(self,numero,dni,noombre,apellido,millas=0):
        self.__numero = numero
        self.__dni = dni
        self.__nombre = noombre
        self.__apellido = apellido
        self.__millasAcumuladas = millas

    def acumularMillas(self,millas):
        self.__millasAcumuladas += millas

    def cantidadTotaldeMillas(self):
        return self.__millasAcumuladas

    def canjearMillas(self,millas):
        if self.__millasAcumuladas >= millas:
            print("Canje de millas aprobado")
            self.__millasAcumuladas-=millas
        else:
            print("Error de operacion(millas acumuladas insufucientes)")
    def getNumero(self):
        return self.__numero

    def __str__(self):
        return "%1s %8s %7s %10s %10d" % (self.__numero, self.__apellido, self.__nombre, self.__dni, self.__millasAcumuladas)

