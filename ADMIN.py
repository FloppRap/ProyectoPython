from CLIENTE import Cliente
from REGISTRO import Registro ,Insertar
from TIPOSALAS import SalaChica, SalaGrande

class Admin(Cliente):
    def __init__(self):
        #valores por defecto, no se vera en el proceso de uso
        self.clientes = Registro("Clientes",0,0,0,"Salas")
        self.clientesLista = Cliente()

    def ComprobarDisponibilidad(self,prueba):
        if prueba.salaCine.sala.cantButacas > 0:
            return True
        else:
            return False

    def MostrarClientes(self):
        self.clientesLista.mostrarClientes()

    def Comprar(self,prueba,cantidad, apellido, dia, mes):
        if prueba.salaCine.sala.cantButacas >= cantidad:
            
            #Guardar registro de clientes
            prueba.salaCine.sala.cantButacas -= cantidad
            prueba.salaCine.sala.cantButacasOcupadas += cantidad

            if(isinstance(prueba.salaCine.sala,SalaChica)):
                sala = "Comun"
            elif (isinstance(prueba.salaCine.sala,SalaGrande)):
                sala = "Vip"

            Insertar(self.clientes,Registro(apellido,cantidad,dia,mes,sala))


            #Guardar lista de clientes basica
            self.clientesLista.cargarCliente(apellido,cantidad)
            

            print("\nCompra exitosa!")
        else:
            print("\nNo hay la cantidad de butacas libres que necesita.")