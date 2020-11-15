import datetime

class Admin:
    def __init__(self):
        pass

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
        Registro = open("Registro de Clientes.txt","at")
        Registro.write(str(prueba.cantClientes)+"\n")
        Registro.close()