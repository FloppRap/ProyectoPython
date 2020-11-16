class Cliente:

    def __init__(self, apellido, cantidad, dia, mes):
        # crea un nodo
        self.izq = None
        self.der = None
        
        # atributos de clientes
        self.apellido = apellido
        self.cantidad = cantidad
        self.fecha = {}
        self.fecha.setdefault(dia,mes)
        
def Insertar(raiz,nodo):
    if raiz is None:
        raiz = nodo
    else:
        if (raiz.apellido) < (nodo.apellido):
            if raiz.der is None:
                raiz.der = nodo
            else:
                Insertar(raiz.der,nodo)
        else:
            if raiz.izq is None:
                raiz.izq = nodo
            else:
                Insertar(raiz.izq,nodo)

def Mostrar(raiz):
    if raiz is not None:
        Mostrar(raiz.izq)
        if raiz.apellido != "Clientes":
            print(f"Apellido del responsable: {raiz.apellido}, cantidad de personas: {raiz.cantidad}, fecha de compra (dia:mes): {raiz.fecha}")
        Mostrar(raiz.der)
        
def BuscarClientePorFecha(raiz,dia,mes):
    if raiz is not None:
        BuscarClientePorFecha(raiz.izq,dia,mes)
        
        if (dia in raiz.fecha) and (mes in raiz.fecha.values()):
            print(f"Apellido del responsable: {raiz.apellido}, Cantidad de clientes: {raiz.cantidad}")

        BuscarClientePorFecha(raiz.der,dia,mes)