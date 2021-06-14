from excepciones.empleado_exception import empleado_excepcion
from dispo_control import dispositivo_control
from empleado import empleado as emp
from utils.utils import registrar_intruso as reg_intruso

class empresa:
    #atributo de clase
    empleados=list() #empleados=[]

    #atributo
    def __init__(self):#constructor
        #atributo de instancia
        #self.dispo_control=dispositivo_control()
        pass


    @classmethod
    def setup(clase):#metodo de instancia
            clase.empleados.append(emp.crear_empleado("Alfonso", "47353500L"))
            clase.empleados.append(emp.crear_empleado("Marta", "87878796K"))
            clase.empleados.append(emp.crear_empleado("Maria", "47358787L"))
            clase.empleados.append(emp.crear_empleado("Luisa", "445689874L", 5))
            clase.empleados[-1].jornada=8 #Usando el setter
        
    def control_entrada(self, empleado):
        return dispositivo_control.validar_entrada(empleado.dni)

    def control_salida(self, empleado):
        dispositivo_control.validar_salida(empleado.dni)   

    @classmethod
    def get_empleado(cls, dni):
        #Casting
        #Función Lambda
        emp_list = list(filter(lambda emp : emp.dni==dni, cls.empleados))
        if len(emp_list) > 0:
            return emp_list[0]
        else:
            #raise empleado_excepcion()
            reg_intruso(dni)


    @classmethod
    def listar_empleados(cls):
        for empleado in cls.empleados:
            print(empleado)

