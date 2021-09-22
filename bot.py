import tweepy, time
from datetime import date


# KEYS E TOKENS
CONSUMER_KEY = 'RtlFBbXppCyXsckhxVLWRqIYw'
CONSUMER_SECRET = 'AEqYAfEk77vcKh9042f0thEwRRbyEe1xMrvGdleEyPNUVFTUPG'
ACCESS_KEY = '1439370419253940229-XNo1KXvkDEJqZ6jMgUmNJXAcCY9jAy'
ACCESS_SECRET = 'Xn7788btl7Olw6Sc6uqk4eNepLHrR73nhwcCpEEomUl89'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# INFORMAÇÕES
meses_ano = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
             7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

dias_semana = {1: "Domingo", 2: "Segunda-Feira", 3: "Terça-Feira", 4: "Quarta-Feira", 5: "Quinta-Feira", 6: "Sexta-Feira", 7: "Sábado"}

# API
api = tweepy.API(auth)

# BOT
while True:
    # DIA HOJE
    dia_semana_hoje = 1
    data = date.today()
    dia, mes, ano = data.day, data.month, data.year

    # POST
    api.update_status(f'Hoje é {dias_semana[dia_semana_hoje]}, dia {dia} de {meses_ano[mes]} de {ano}.\n{dia}/{mes}/{ano}')
    time.sleep(86400)
    dia_semana_hoje += 1
    if dia_semana_hoje == 8:

        dia_semana_hoje = 1
