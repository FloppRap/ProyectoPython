class Registro():
    def __init__(self,apellido,fecha,sala,pelicula):
        #Nodos
        self.izq = None
        self.der = None

        #Atributos
        self.Apellido = apellido
        self.Fecha = fecha
        self.SalaAsistida = sala
        self.Pelicula = pelicula

def Insertar(raiz,nodo):
    if raiz is None:
        raiz = nodo
    else:
        if (raiz.Apellido) < (nodo.Apellido):
            if raiz.der is None:
                raiz.der = nodo
            else:
                Insertar(raiz.der,nodo)
        else:
            if raiz.izq is None:
                raiz.izq = nodo
            else:
                Insertar(raiz.izq,nodo)

#Funcion de prueba, no sera ejecutada en la practica
def MostrarTodo(raiz):
    if raiz is not None:
        MostrarTodo(raiz.izq)
        
        if (raiz.apellido != "Apellido"):
            print(f"""
                    Apellido : {raiz.Apellido}
                    Fecha : {raiz.Fecha}
                    Sala Asistida : {raiz.SalaAsistida}
                    Pelicula vista : {raiz.Pelicula}""")

        MostrarTodo(raiz.der)

def BuscarPorFecha(raiz,fecha):
    if raiz is not None:
        BuscarPorFecha(raiz.izq,fecha)
        
        if (raiz.Apellido != "Apellido"):
            if fecha == raiz.Fecha:
                print(f"""
                        Apellido : {raiz.Apellido}
                        Fecha : {raiz.Fecha}
                        Sala Asistida : {raiz.SalaAsistida}
                        Pelicula vista : {raiz.Pelicula}""")

        BuscarPorFecha(raiz.der,fecha)

def GuardarRegistro(raiz,registro):

    if raiz is not None:
        
        GuardarRegistro(raiz.izq,registro)

        if (raiz.Apellido != "Apellido"):

            registro.write(f"Apellido: {raiz.Apellido}, Fecha: {raiz.Fecha}, Sala Asistida: {raiz.SalaAsistida}, Pelicula Vista: {raiz.Pelicula} \n")

        GuardarRegistro(raiz.der,registro)