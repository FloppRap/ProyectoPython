from TIPOSALAS import *

class Cine():
    def __init__(self):
        #cartelera
        self.PeliChicos = ["mickey","dumbo","etc"]
        self.PeliAdolescentes = ["avengers","joker","etc"]
        self.PeliAdultos = ["50 sombras de grey","escupire sobre tu tumba","etc"]

        #Salas disponibles
        self.salaComun = COMUN()
        self.salaVip = VIP()

    def DesplegarCartelera(self):
        print("\nPeliculas para Chicos: ")
        for pelicula in self.PeliChicos:
            print(f" '{pelicula}' ")

        print("\nPeliculas para Adolescentes: ")
        for pelicula in self.PeliAdolescentes:
            print(f" '{pelicula}' ")
        
        print("\nPeliculas para Adultos: ")
        for pelicula in self.PeliAdultos:
            print(f" '{pelicula}' ")