from excepciones.empleado_exception import empleado_excepcion
from empleado import empleado
from empresa import empresa


def controlar_salida_empleados():
    empleados_dni = list(emp.finalizar_jornada())
    for dni in empleados_dni:
        dni = empleados_dni.pop()
        empleado = emp.get_empleado(dni)
        if emp.control_salida(empleado):
            print(f"{empleado.nombre} ha finalizado su jornada")


def controlar_entrada_empleados(*dnis):
    
    try:
        for e in [empresa.get_empleado(dni) for dni in dnis if empresa.existe_empleado(dni)]:
            if e is not None:
                if emp.control_entrada(e):
                    print(f"{e.nombre} esta en su puesto de trabajo")        
    except empleado_excepcion as ex:
        print("No se ha encontrado este empleado")
    finally:
        print("Fin proceso de entrada")

    
    """
    try:
        luis = empresa.get_empleado('111H')
    except empleado_excepcion as ex:
        print("No se ha encontrado este empleado")
    except Exception:
        print("Error general")
    else:
        if luis is not None:
            if emp.control_entrada(luis):
                print("Empleado en su puesto de trabajo")
            #empresa.listar_empleados()
    finally:
        print("Fin proceso de entrada")
    """
if __name__ == "__main__":
    
    emp = empresa()
    empresa.setup()
    #'222H', '444H'
    controlar_entrada_empleados('1111H','1111H','1111H','1111H','1111H','444H','1111H','1111H','1111H')
    controlar_salida_empleados()
    
    

    
