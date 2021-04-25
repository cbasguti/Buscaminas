class Tripleta:
    def __init__(self, fila, columna, valor):
        self.__fila = fila
        self.__columna = columna
        self.__valor = valor

    def asigna_fila(self, fila):
        self.__fila = fila

    def asigna_columna(self, columna):
        self.__columna = columna

    def asigna_valor(self, valor):
        self.__valor = valor

    def retorna_fila(self):
        return self.__fila

    def retorna_columna(self):
        return self.__columna

    def retorna_valor(self):
        return self.__valor

    def to_string(self):
        return "[" + str(self.__fila) + ", " + str(self.__columna) + ", " + str(self.__valor) + "]"