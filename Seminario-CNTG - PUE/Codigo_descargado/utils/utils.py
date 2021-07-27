from datetime import datetime
def registrar_intruso(data:str):
    #1 abrir fichero para escritura (modo append)
    f = open('registro.txt','a') 
    #2 escribir data en fichero
    f.write(f"{data}\t{datetime.now()}\n")
    #3 cerrar fichero
    f.close()

def registrar_intruso_v2(data:str):
    with open('registro.txt','a') as f:
        f.write(f"{data}\t{datetime.now()}\n")
