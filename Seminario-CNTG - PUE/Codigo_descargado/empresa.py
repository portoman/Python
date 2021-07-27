from excepciones.empleado_exception import empleado_excepcion
from dispo_control import dispositivo_control
from empleado import empleado as emp
from utils.utils import registrar_intruso, registrar_intruso_v2 as reg_intruso

class empresa:
    #atributo de clase
    empleados = list()
    #empleados = []
    #atributo
    def __init__(self): #constructor
        #atributo de instancia
        #self.dispo_control = dispositivo_control()
        pass
    
    @classmethod
    def setup(cls): #metodo de instancia
        print("Iniciando empresa...")
        cls.empleados.append(emp.crear_empleado('Luis','111H'))
        cls.empleados.append(emp.crear_empleado('Maria','222H'))
        cls.empleados.append(emp.crear_empleado('Jan','333H'))
        cls.empleados.append(emp.crear_empleado('Silvia','444H', 5))
        cls.empleados[-1].jornada = 8

    def control_entrada(self, empleado):
        return dispositivo_control.validar_entrada(empleado.dni)
    
    def control_salida(self, empleado):
        return dispositivo_control.validar_salida(empleado.dni)
        

    def finalizar_jornada(self):
        return dispositivo_control.get_empleados_presentes()

    @classmethod
    def get_empleado(cls, dni):
        #cast
        emp_list = list(filter(lambda emp : emp.dni == dni, cls.empleados))
        if len(emp_list) > 0:
            return emp_list[0]
        else:
            #raise empleado_excepcion()
            reg_intruso(dni)

        
    @classmethod
    def listar_empleados(cls):
        for empleado in cls.empleados:
            print(empleado)

    @classmethod
    def existe_empleado(cls, dni:str) -> bool:
        return  filter(lambda e: e.dni == dni, cls.empleados) != None
