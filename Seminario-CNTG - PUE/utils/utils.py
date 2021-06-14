def registrar_intruso(data:str):
    #1 abrir ficheto para escritura
    f=open("registro.txt", "w")
    #2 escribir data en fichero
    f.write(f"{data}\n")
    #3 cerrar fichero
    f.close()