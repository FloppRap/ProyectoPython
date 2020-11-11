from CINE import Cine
from SUPERSU import Mantener


print(Cine.cartelera)
print(Cine.cantidadButacas)
print(Cine.cantidadClientes)

probar = Mantener()

probar.LimpiarRegistroClientes()
probar.ModificarButacas()

print(Cine.cartelera)
print(Cine.cantidadButacas)
print(Cine.cantidadClientes)