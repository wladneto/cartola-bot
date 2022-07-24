import uuid

def confirmar_status_mercado(status):
    if status == 2:
        return "fechado"
    else: 
        return status

def gerar_uuid():
    return str(uuid.uuid4())

def arredondar_numero(numeroInt):
    numero=str(numeroInt)
    digitos = len(numero)
    if (digitos == 7):
        if (numero[0]==1):
            return(numero[0]+'.'+numero[1]+' milhão')
        return(numero[0]+'.'+numero[1]+' milhões')
    return(digitos)