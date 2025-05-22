import Vuelo


class VueloEspecial(Vuelo.Vuelo):
    def __init__(self, numero, origen, destino, capacidad_maxima, motivo):
        super().__init__(numero, origen, destino, capacidad_maxima)
        self.motivo = motivo
