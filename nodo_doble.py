class NodoDoble:
    def __init__(self, dato):
        self.__dato = dato
        self.__ligaIzq = None
        self.__ligaDer = None

    def set_liga_izq(self, liga_izq):
        self.__ligaIzq = liga_izq

    def set_liga_der(self, liga_der):
        self.__ligaDer = liga_der

    def set_dato(self, dato):
        self.__dato = dato

    def get_liga_izq(self):
        return self.__ligaIzq

    def get_liga_der(self):
        return self.__ligaDer

    def get_dato(self):
        return self.__dato

    def to_string(self):
        return "[" + str(self.__ligaIzq) + ", " + str(self.__dato) + ", " + str(self.__ligaDer) + "]"