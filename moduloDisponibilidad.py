def disponibilidad(prueba):
    print(f"""\nSala Comun :
            Butacas Libres -> {prueba.salaComun.cantButacasLibres}
            Butacas Ocupadas -> {prueba.salaComun.cantButacasOcupadas}
            Incluye 3D -> {prueba.salaComun.TresDe}
            Incluye servicio de comida -> {prueba.salaComun.servicioComida}""")

    print(f"""Sala Vip :
            Butacas Libres -> {prueba.salaVip.cantButacasLibres}
            Butacas Ocupadas -> {prueba.salaVip.cantButacasOcupadas}
            Incluye 3D -> {prueba.salaVip.TresDe}
            Incluye servicio de comida -> {prueba.salaVip.servicioComida}""")