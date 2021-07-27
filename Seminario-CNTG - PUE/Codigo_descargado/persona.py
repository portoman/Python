class persona:
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def dni(self):
        return self._dni


    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni
        