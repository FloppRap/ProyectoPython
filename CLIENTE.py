class Cliente:
    def __init__(self):
        
        #Lista de clientes
        self.listaCliente = []

    def cargarCliente(self,apellido,cantidad):
        dic = {}
        dic.setdefault(apellido,cantidad)
        self.listaCliente.append(dic)

    def mostrarClientes(self):
        print("Responsable : Cantidad de Personas\n")
        for i in range(len(self.listaCliente)):
            print(self.listaCliente[i])
