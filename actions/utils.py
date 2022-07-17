import uuid

def confirmar_status_mercado(status):
    if status == 2:
        return "fechado"
    else: 
        return status

def gerar_uuid():
    return str(uuid.uuid4())

