from TIPOSALAS import Salas

class Cine(Salas):
    def __init__(self):
        super().__init__()
        self.cartelera = {
            "Mickey":0,
            "Ted":18
        }
        #instancia de Salas como atributo de Cine
        self.salaCine = Salas()
        self.cantClientes = {}