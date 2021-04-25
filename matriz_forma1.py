import nodo_doble as nd
import tripleta as tr


class MatrizForma1:
    def __init__(self, m, n):
        self.__t = tr.Tripleta(m, n, None)
        self.__mat = nd.NodoDoble(self.__t)
        self.__t.asigna_valor(self.__mat)
        self.__mat.set_dato(self.__t)

    def nodo_cabeza(self):
        return self.__mat

    def primer_nodo(self):
        tp = self.__mat.get_dato()
        p = tp.retorna_valor()
        return p

    def es_vacia(self):
        p = self.primer_nodo()
        return p == self.__mat

    def fin_recorrido(self, p):
        return p == self.__mat

    def construye_nodos_cabeza(self):
        ultimo = self.nodo_cabeza()
        x = nd
        t = ultimo.get_dato()
        m = t.retorna_fila()
        n = t.retorna_columna()
        mayor = m
        if n > m:
            mayor = n
        for i in range(1, mayor):
            t = tr.Tripleta(i, i, self.nodo_cabeza())
            x = nd.NodoDoble(t)
            x.set_liga_der(x)
            x.set_liga_izq(x)
            t = ultimo.get_dato()
            t.asigna_valor(x)
            ultimo.set_dato(t)
            ultimo = x

    def conecta_filas(self, x):
        tx = x.get_dato()
        p = self.primer_nodo()
        for i in range(1, tx.retorna_fila()):
            tp = p.get_dato()
            p = tp.retorna_valor()
        anterior = p
        q = p.get_liga_der()
        tq = q.get_dato()
        while (q != p) and (tq.retorna_columna() < tx.retorna_columna()):
            anterior = q
            q = q.get_liga_der()
            tq = q.get_dato()
        anterior.set_liga_der(x)
        x.set_liga_der(q)

    def conecta_columnas(self, x):
        tx = x.get_dato()
        p = self.primer_nodo()
        for i in range(1, tx.retorna_fila()):
            tp = p.get_dato()
            p = tp.retorna_valor()
        anterior = p
        q = p.get_liga_izq()
        tq = q.get_dato()
        while (q != p) and (tq.retorna_fila() < tx.retorna_fila()):
            anterior = q
            q = q.get_liga_izq()
            tq = q.get_dato()
        anterior.set_liga_izq(x)
        x.set_liga_izq(q)

    def busca_coord(self, m, n):  # Método que busca la existencia de una mina en una coordenada dada.
        p = self.primer_nodo()
        while not self.fin_recorrido(p):
            q = p.get_liga_der()
            while q != p:
                tq = q.get_dato()
                qf = tq.retorna_fila()
                qc = tq.retorna_columna()
                if (qf == m) and (qc == n):
                    return True
                q = q.get_liga_der()
            tp = p.get_dato()
            p = tp.retorna_valor()
        return False