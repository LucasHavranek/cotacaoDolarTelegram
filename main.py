import requests
from time import sleep

token = ''
chat_id = ''
verificador = True
contador = 0

def envia_mensagem_telegram():
    message = f'Oportunidade de comprar dólar, valor atual: {consulta_valor_dolar()}'
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
    try:
        requests.get(url)
    except:
        return "Falha ao enviar mensagem via telegram"

def consulta_valor_dolar():
    try:
        res = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL').json()
        dolar = float(res["USDBRL"]["bid"])
        return dolar
    except:
        return "Falha ao requisitar API Awesome"

while verificador:
    if consulta_valor_dolar() <= 5:
        envia_mensagem_telegram()
        contador +=1
        sleep(3600)
    if contador > 5:
        break
    else:
        sleep(3600)
