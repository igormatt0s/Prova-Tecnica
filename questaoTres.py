import json

def questaoTres():
    with open('dados.json', 'r') as file:
        data = json.load(file)

    total_faturamento = 0
    menor_faturamento = float('inf')
    maior_faturamento = float('-inf')
    dias_com_faturamento = 0

    for item in data:
        valor = item['valor']
        if valor > 0:
            total_faturamento += valor
            dias_com_faturamento += 1
            if valor < menor_faturamento:
                menor_faturamento = valor
            if valor > maior_faturamento:
                maior_faturamento = valor

    if dias_com_faturamento > 0:
        media_mensal = total_faturamento / dias_com_faturamento
    else:
        media_mensal = 0

    dias_acima_media = sum(1 for item in data if item['valor'] > media_mensal)

    print(f'Menor faturamento: {menor_faturamento}')
    print(f'Maior faturamento: {maior_faturamento}')
    print(f'Dias com faturamento acima da média mensal: {dias_acima_media}')

questaoTres()
