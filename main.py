from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
     'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
     'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
     'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
     'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
     'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
     'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
     'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
     'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
     'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
     'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564627800, 'start': 1564626000},
]


def classify_by_phone_number(records):
    dicionario = {}
    lista = []

    for record in records:
        horaInicio = datetime.fromtimestamp(record['start'])
        horaFinal = datetime.fromtimestamp((record['end']))

        if record['source'] not in dicionario.keys():
            dicionario[record['source']] = calcula_preco(horaInicio,
                                                         horaFinal)

        else:
            dicionario[record['source']] += calcula_preco(horaInicio,
                                                          horaFinal)

    for key, value in dicionario.items():
        lista.append({'source': key, 'total': round(value, 2)})

    lista = sorted(lista, key=lambda item: item['total'], reverse=True)

    return lista


def calcula_preco(horaInicio, horaFinal):
    taxa_minuto = 0.09
    taxa_fixa = 0.36
    total = 0

    if 6 <= horaInicio.hour < 22:
        if horaFinal.hour < 22:
            hora_total = (horaFinal - horaInicio)
            total += taxa_fixa + (hora_total.seconds // 60 % 60) * taxa_minuto
        else:
            horaFinal = datetime(horaInicio.year, horaInicio.month,
                                 horaInicio.day, 22)
            hora_total = horaFinal - horaInicio
            total += (((hora_total.seconds // 60 % 60) * taxa_minuto)
                      + taxa_fixa)
    else:
        total += taxa_fixa
    return total
