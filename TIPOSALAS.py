#Tipos de Salas

class COMUN():
    def __init__(self):

        self.cantButacasLibres = 50
        self.cantButacasOcupadas = 0

        self.servicioComida = False
        self.TresDe = False

class VIP():
    def __init__(self):

        self.cantButacasLibres = 100
        self.cantButacasOcupadas = 0

        self.servicioComida = True 
        self.TresDe = True
