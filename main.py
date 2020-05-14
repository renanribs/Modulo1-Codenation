from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000},
]


def calcula_segundos():
    for record in records:
        segundosini = datetime.fromtimestamp(record['start'])
        segundosfin = datetime.fromtimestamp(record['end'])
        segundos = segundosfin.second - segundosini.second
        return segundos


def calcula_minutos():
    for record in records:
        start = datetime.fromtimestamp(record['start'])
        end = datetime.fromtimestamp((record['end']))
        minutostotal = end.minute - start.minute
        return minutostotal


def calcula_hora_inicio():
    for record in records:
        start = datetime.fromtimestamp(record['start'])
        hora_inicio = start.hour
        return hora_inicio


def calcula_hora_final():
    for record in records:
        end = datetime.fromtimestamp(record['end'])
        hora_final = end.hour
        return hora_final


horaInicio = calcula_hora_inicio()
horaFinal = calcula_hora_final()
totalsegundos = calcula_segundos()
totalminutos = calcula_minutos()
taxa_fixa = 0.36
taxa_minuto = 0.09


def calcula_preco():
    preco_total = 0

    if horaInicio >= 6:
        if horaFinal <= 21 and totalminutos <= 59:
            preco_total = totalsegundos * taxa_minuto + taxa_fixa

        if horaFinal >= 22 and totalminutos > 0:
            preco_total += taxa_fixa
    else:
        preco_total = taxa_fixa
    return preco_total


def classify_by_phone_number(records):
    ligacoes = []
    for record in records:
        lista = next((i for i in range(len(ligacoes)) if ligacoes[i]['source'] == record['source']), -1)
        valor = calcula_preco()
        if lista == -1:
            ligacoes.append({'source': record['source'], 'total': valor})
        else:
            ligacoes[lista]['total'] = round(valor + ligacoes[lista]['total'], 2)
    ligacoes.sort(key=lambda k: k['total'], reverse=True)
    return ligacoes


print(classify_by_phone_number(records))
