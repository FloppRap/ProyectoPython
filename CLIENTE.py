class Cliente:
    def __init__(self):
        
        #Lista de clientes
        self.listaCliente = []

    def cargarCliente(self,apellido,sala):
        dic = {}
        dic.setdefault(apellido,sala)
        self.listaCliente.append(dic)

    def mostrarClientes(self):
        print("Cliente y Sala asistida")
        for i in range(len(self.listaCliente)):
            print(self.listaCliente[i])

    def BuscarPorApellido(self,apellido):
        bandera = False
        print("")
        for iterador in self.listaCliente:
            if apellido in iterador:
                print(f"Apellido : {apellido}, Sala Asistida : {iterador.get(apellido)}")
                bandera = True
        else:
            print("\nBusqueda Finalizada.")
            if not bandera :
                print("\nNo se encontro cliente/s con ese apellido.")