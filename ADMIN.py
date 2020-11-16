#import datetime
from CLIENTE import Cliente, Insertar

class Admin(Cliente):
    def __init__(self):
        #valores por defecto, no se vera en el proceso de uso
        self.clientes = Cliente("Clientes",0,0,0)

        self.Registro = open("Registro de Clientes.txt","wt")
        self.Registro.write("{Cantidad de Clientes : [dia, mes]}\n")
        self.Registro.close()

    def ComprobarDisponibilidad(self,prueba):
        if prueba.salaCine.sala.cantButacas > 0:
            return True
        else:
            return False

    def Comprar(self,prueba,cantidad, apellido, dia, mes):
        if prueba.salaCine.sala.cantButacas >= cantidad:
            
            prueba.salaCine.sala.cantButacas -= cantidad
            prueba.salaCine.sala.cantButacasOcupadas += cantidad

            Insertar(self.clientes,Cliente(apellido,cantidad,dia,mes))

            print("\nCompra exitosa!")
        else:
            print("\nNo hay la cantidad de butacas libres que necesita.")