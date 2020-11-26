class Registro:
    def __init__(self,apellido,cantidad,dia,mes,sala):
        # crea un nodo
        self.izq = None
        self.der = None

        # atributos de clientes
        self.apellido = apellido
        self.cantidad = cantidad
        self.fecha = {}
        self.fecha.setdefault(dia,mes)
        self.salaAsistida = sala

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

def BuscarClientePorFecha(raiz,dia,mes):
    if raiz is not None:
        BuscarClientePorFecha(raiz.izq,dia,mes)
        
        if (dia in raiz.fecha) and (mes in raiz.fecha.values()):
            print(f"Apellido del responsable: {raiz.apellido}, Cantidad de personas: {raiz.cantidad}, sala asistida: '{raiz.salaAsistida}'")

        BuscarClientePorFecha(raiz.der,dia,mes)


def GuardarRegistro(raiz,registro):
    
    if raiz is not None:
        GuardarRegistro(raiz.izq,registro)

        if (raiz.apellido != "Clientes"):
            registro.write(raiz.apellido + "\t\t" + f"{raiz.cantidad}" + "\t\t" + f"{raiz.fecha}" + "\n")

        GuardarRegistro(raiz.der,registro)