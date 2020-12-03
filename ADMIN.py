from CLIENTE import Cliente
from REGISTRO import Registro, Insertar, BuscarPorFecha, GuardarRegistro

class Admin:
    def __init__(self):
        self.ListaClientes = Cliente()
        self.RegistroClientes = Registro("Apellido",{0:0},"Sala","Pelicula")

    def ComprobarDisponibilidad(self,EntidadCine):
        if EntidadCine.salaVip.cantButacasLibres > 0 and EntidadCine.salaComun.cantButacasLibres:
            return True
        else:
            return False
    
    def MostrarClientes(self):
        self.ListaClientes.mostrarClientes()

    #agregar pedido luego
    def Comprar(self,EntidadCine,EntidadDatos):
        if self.ComprobarDisponibilidad:
            
            if EntidadDatos.Sala == "COMUN":
                #Agregar cliente con dato minimo
                EntidadCine.salaComun.cantButacasLibres -= 1
                EntidadCine.salaComun.cantButacasOcupadas += 1

                self.ListaClientes.cargarCliente(EntidadDatos.Apellido,EntidadDatos.Sala)

                #Agregar cliente con todos los datos
            
                Insertar(self.RegistroClientes, Registro(EntidadDatos.Apellido,EntidadDatos.Fecha,EntidadDatos.Sala,EntidadDatos.Pelicula))

            else:
                #Agregar cliente con dato minimo
                EntidadCine.salaVip.cantButacasLibres -= 1
                EntidadCine.salaVip.cantButacasOcupadas += 1

                self.ListaClientes.cargarCliente(EntidadDatos.Apellido,EntidadDatos.Sala)

                #Agregar cliente con todos los datos

                Insertar(self.RegistroClientes, Registro(EntidadDatos.Apellido,EntidadDatos.Fecha,EntidadDatos.Sala,EntidadDatos.Pelicula))
        
        else:
            print("Lo sentimos, no hay butacas disponible en la sala!")

    def Buscar(self,apellido):
        self.ListaClientes.BuscarPorApellido(apellido)

    def BuscarPorFecha(self,fecha):
        BuscarPorFecha(self.RegistroClientes,fecha)

    def Guardar(self):

        registro = open("Registro de clientes.txt","w")

        GuardarRegistro(self.RegistroClientes,registro)

        registro.close()

    #No sera utilizada en la practica, solo estaba para comprobar
    """
    def mostrar(self):
        MostrarTodo(self.RegistroClientes)
    """