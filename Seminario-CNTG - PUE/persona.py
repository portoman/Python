class persona:

    @property
    def nombre(self):
        return self._nombre
     
    @property
    def dni(self):
        return self._dni

    def __init__(self, nombre, dni):#La _ por convención quiere decir que es privado (aunque no limite nada, es por best practice)
        self._nombre=nombre
        self._dni=dni
