class dispositivo_control:
    
    """
    {
        "111H":True o False,
        "222H":True o False,
        "333H":True o False,
        "444H":True o False,
    }
    """
    control = dict()
    #control = {}

    @classmethod
    def get_empleados_presentes(cls):
        return cls.control.keys() 
    
    @classmethod
    #type hint
    def validar_entrada(cls, dni:str) -> bool:
        cls.control[dni] = True
        return True

    @classmethod
    def validar_salida(cls, dni):
        cls.control[dni] = False
        return True

    @classmethod
    def validar_presencia(cls,dni):
        return True
    
    
