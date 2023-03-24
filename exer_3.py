faturamento = [
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]

fatura_values = {}
i = 0
# Simplificando o dicionário
while i <  len(faturamento):    
    day = faturamento[i].get('dia')
    value = faturamento[i].get('valor')
    fatura_values.update({day: value})
    i += 1

# Ordenando o dicionário pelo maior valor
fatura_values_desc = sorted(fatura_values.items(), key=lambda x:x[1], reverse=True)
fatura_values_desc = dict(fatura_values_desc)

# Pegando a primeira chave do dicionário
maior_valor = list(fatura_values_desc.keys())[0]


print(f'O maior valor ocorreu no dia {maior_valor} e foi de {fatura_values_desc[maior_valor]:.2f}')

# Criação da média mensal do faturamento
v = 1
media_div = 0
media_n = 0
valor_md = fatura_values_desc
contador = len(fatura_values_desc) + 1

while v < contador:
    if valor_md[v] != 0.0:
        media_div += 1
        media_n += valor_md[v]

    v += 1

media = media_n / media_div
print(f'A média mensal foi {media:.2f}')

# Calculando o número de dias em que o faturamento ultrapassou a média
dias_md = 0
v = 1
while  v < contador:
    if valor_md[v] > media and valor_md[v] != 0.0:
        dias_md += 1
    
    v += 1
    
print(f'O número de dias em que o faturamento ultrapassou a média foi {dias_md}')
