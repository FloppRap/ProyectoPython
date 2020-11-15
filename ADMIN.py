import datetime

class Admin:
    def __init__(self):
        self.Registro = open("Registro de Clientes.txt","wt")
        self.Registro.write("{Cantidad de Clientes : [dia, mes]}\n")
        self.Registro.close()

    def ComprobarDisponibilidad(self,prueba):
        if prueba.salaCine.sala.cantButacas > 0:
            return True
        else:
            return False

    def Comprar(self,prueba,cantidad):
        if prueba.salaCine.sala.cantButacas >= cantidad:
            prueba.salaCine.sala.cantButacas -= cantidad
            prueba.salaCine.sala.cantButacasOcupadas += cantidad

            ahora = datetime.datetime.now()
            prueba.cantClientes.setdefault(cantidad,[ahora.day,ahora.month])

            print("\nCompra exitosa!")
        else:
            print("\nNo hay la cantidad de butacas libres que necesita.")

    def GuardarRegistroClientes(self,prueba):
        self.Registro = open("Registro de Clientes.txt","at")
        self.Registro.write(str(prueba.cantClientes))
        self.Registro.close()

    def VerRegistroClientes(self,prueba):
        self.Registro = open("Registro de Clientes.txt","r")
        
        for linea in self.Registro:
            print(linea)

        self.Registro.close()