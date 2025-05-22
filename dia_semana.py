from enum import Enum
from typing import Final
class Dias(Enum):
    Lunes="Lunes"
    Martes="Martes"
    Miercoles="Miércoles"
    Jueves="Jueves"
    VIernes="Viernes"
    Sabado="Sabado"
    Domingo="Domingo"


class Verificador:
    def __init__(self,dia:Dias):
        self.dia=dia
v=Verificador("Martoles")
print(v.dia)
print ("XDXD")

class Intento:
    Max_intento:Final=5