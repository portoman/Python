from persona import persona

#empleado es una persona
class empleado(persona):
    
    @property
    def jornada(self):
        return self._jornada

    @jornada.setter
    def jornada(self, nuevo_valor):
        self._jornada = nuevo_valor

    def __init__(self, nombre, dni, jornada = 8):
        super().__init__(nombre, dni)
        self._jornada = jornada
    
    #patron factoria
    @classmethod
    def crear_empleado(cls,nombre, dni, jornada = 8):
        return cls(nombre, dni, jornada)
    
    def __str__(self):
        return f"{self.nombre} -  {self.jornada}"

    