"""
Brain storm
Posibles entidades:
Empresa, Trabajador, Report de horas, Reloj, Dispositivo de control, ....
"""

from excepciones.empleado_exception import empleado_excepcion
from empresa import empresa
from empleado import empleado

def controlar_entrada_empleados(*dnis):
   
    try: 
        for e in [empresa.get_empleado(dni) for dni in dnis]:
                    if e is not None:
                        if emp.control_entrada(e):
                            print(f"{e.nombre} está en su puesto de trabajo")
    except empleado_excepcion as ex:
            print("No se ha encontrado el empleado")
        
    finally:
            print("Fin de proceso de control")

if __name__=="__main__":



    emp= empresa() #instaciar POO
    empresa.setup()
    controlar_entrada_empleados("47353500L", "87878796K")





