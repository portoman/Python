class dispositivo_control:

    """
    DNI y True o False, para indicar si el empleado está o no
    {"DNI1": True o False,
     "DNI2": True o False,
     "DNI3": True o False,
     "DNI4": True o False}
    """

    #control=dict()
    control={}

    @classmethod
    #type hint-> Investigar    
    def validar_entrada(cls, dni):
        cls.control[dni]=True
        return True

    @classmethod    
    def validar_salida(cls, dni):
        cls.control[dni]=False

    @classmethod    
    def validar_presencia(cls, dni):
        return True