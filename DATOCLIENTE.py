class DATOS:
    def __init__(self):
        self.__apellido = ""
        self.__fecha = {}
        self.__salaAsistida = ""
        self.__pelicula = ""

    @property
    def Apellido(self):
        return self.__apellido

    @Apellido.setter
    def Apellido(self,apellido):
        self.__apellido = apellido


    @property
    def Fecha(self):
        return self.__fecha

    @Fecha.setter
    def Fecha(self,fecha):
        #self.__fecha.update(fecha)
        self.__fecha = fecha


    @property
    def Sala(self):
        return self.__salaAsistida

    @Sala.setter
    def Sala(self,sala):
        self.__salaAsistida = sala

    @property
    def Pelicula(self):
        return self.__pelicula

    @Pelicula.setter
    def Pelicula(self,pelicula):
        self.__pelicula = pelicula