import datetime as dt #responsavel por pegar a hora na qual a estimativa foi coletada
import json           #para conseguir ler o arquivo json onde os dados sobre os pontos estão armazenados
from time import sleep#a função sleep faz o programa 'dormir' por um tempo
import pandas as pd   #aqui a biblioteca pandas está responsavel por salvar os dados de maneira mais fácil

#a biblioteca uber_rides é a API da Uber responsavel por informar as estimativas de tempo de viagem
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

uber_token = 'token'                                # você necessita de um token para fazer as requisições ao servidor da Uber
product_id = 'd19e0080-4039-4a6f-97de-d00e0f43f3cc' #este ID informa o produto UberX que é o unico produto disponivel na cidade de Campina Grande-PB

session = Session(server_token=uber_token)   #Inicialização da sessão com base no token informado
client = UberRidesClient(session)

data = open('..\\res\\geo.json')
points = json.load(data)        

#no loop a seguir, a cada 30 minutos, é salvo o horario bem como a requisição de previsão de tempo de espera em cada um dos pontos de cg em um arquivo csv
while True:
    horario = dt.datetime.now()
    nbhoods_data = {}
    for point in points:
        response = client.get_pickup_time_estimates(
            start_latitude=point['lat'],
            start_longitude=point['lng'],
            product_id=product_id
        )
        estimate = response.json.get('times')[0]['estimate']
        nbhoods_data[point['address']] = pd.Series([estimate], index=[horario])
        print(estimate)

    dataFrame = pd.DataFrame(nbhoods_data)
    dataFrame.to_csv('bairros_estimativas.csv', mode='a', header=False)
    print('waiting 30 minutes')
    sleep(1800)