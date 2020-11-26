class Salas():
    def __init__(self):
        self.cantButacas = int()
        self.cantButacasOcupadas = int()
    
    def ElegirSala(self,opcSala):
        if opcSala == 1:
            self.sala = SalaChica()
        elif opcSala == 2:
            self.sala = SalaGrande()

    

#Tipos de Salas
class SalaChica(Salas):
    def __init__(self):
        super().__init__()
        self.cantButacas = 50
        self.cantButacasOcupadas = int()

        self.servicioComida = "No"
        self.TresDe = "No"

class SalaGrande(Salas):
    def __init__(self):
        super().__init__()
        self.cantButacas = 100
        self.cantButacasOcupadas = int()

        self.servicioComida = "Si"
        self.TresDe = "Si"
