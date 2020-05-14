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


def calcula_hora_inicio():
    for record in records:
        start = datetime.fromtimestamp(record['start'])
        hora_inicio = start.hour
        return hora_inicio


def calcula_minutos_inicio():
    for record in records:
        minutos = datetime.fromtimestamp(record['start'])
        minutos_inicio = minutos.minute
        return minutos_inicio


def calcula_segundos_inicio():
    for record in records:
        segundos = datetime.fromtimestamp(record['start'])
        segundos_final = segundos.second
        return segundos_final


def calcula_hora_final():
    for record in records:
        end = datetime.fromtimestamp(record['end'])
        hora_final = end.hour
        return hora_final


def calcula_minutos_final():
    for record in records:
        minutos = datetime.fromtimestamp(record['end'])
        minutos_final = minutos.minute
        return minutos_final


def calcula_segundos_final():
    for record in records:
        segundos = datetime.fromtimestamp(record['end'])
        segundos_final = segundos.second
        return segundos_final


horaInicio = calcula_hora_inicio()
minutoInicio = calcula_minutos_inicio()
segundosInicio = calcula_segundos_inicio()

horaFinal = calcula_hora_final()
minutoFinal = calcula_minutos_final()
segundosFinal = calcula_segundos_final()

taxa_fixa = 0.36
taxa_minuto = 0.09


def calcula_preco():
    if 22 > horaInicio >= 6:
        soma_minutos = (horaInicio * 60) + minutoInicio + (segundosInicio // 60)
        total_minutos = 0
        if horaFinal < 22 or (horaFinal == 22 and minutoFinal == 0):
            total_minutos = (horaFinal * 60) + minutoFinal + (segundosFinal // 60)
        else:
            total_minutos = 22 * 60
        preco_total = (int(total_minutos - soma_minutos) * taxa_minuto) + taxa_fixa
    return round(preco_total, 2)


def classify_by_phone_number(records):
    ligacoes = []
    for record in records:
        lista = next((i for i in range(len(ligacoes)) if ligacoes[i]['source'] == record['source']), -1)
        valor = calcula_preco()
        if lista == -1:
            ligacoes.append({'source': record['source'], 'total': valor})
        else:
            ligacoes[lista]['total'] = valor + ligacoes[lista]['total']
    ligacoes.sort(key=lambda k: k['total'], reverse=True)
    return ligacoes
