import requests

api_address='https://api.cartola.globo.com/partidas'
response = requests.get(api_address).json()
jogos=''
for i in range(len(response['partidas'])):
    clube_casa_id=response['partidas'][i]['clube_casa_id']
    clube_casa=response['clubes'][str(clube_casa_id)]['nome_fantasia']
    clube_visitante_id=response['partidas'][i]['clube_visitante_id']
    clube_visitante=response['clubes'][str(clube_visitante_id)]['nome_fantasia']
    jogos=jogos+"\n"+clube_casa+" x "+clube_visitante
print(jogos)

    
