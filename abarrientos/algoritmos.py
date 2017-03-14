class Ordenamiento(object):
    aux = None
    listaNoOrdenada = None
    sizeList = None

    def __init__(self):
        self.aux = 0
        self.listaNoOrdenada = list()
        self.sizeList = 0

    def crearLista(self):
        lengthList = int(raw_input('Cuantos elementos tendra su lista?'))

        for index in range(0, lengthList):
            element = 0
            element = int(raw_input(
                "Ingrese el elemento numero {}".format(index)
            ))
            self.listaNoOrdenada.append(element)

        self.sizeList = len(self.listaNoOrdenada)

    def imprimeLista(self):
        for valor in self.listaNoOrdenada:
            print("valor: {}".format(valor))

    def ordenamientoBurbuja(self):
        for index1 in range(self.listaNoOrdenada - 1, 1):
            for index2 in range(1, index1):
                if self.listaNoOrdenada[index2] > self.listaNoOrdenada[index2 +1 ]:
                    self.aux = self.listaNoOrdenada[index2]
                    self.listaNoOrdenada[index2] = self.listaNoOrdenada[index2 + 1]
                    self.listaNoOrdenada[index2 + 1] = self.aux
