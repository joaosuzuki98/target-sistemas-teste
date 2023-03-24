valor_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'outros': 19849.53
}

valor_total = 0
for value in valor_estado.values():
    valor_total += value

for state, value in valor_estado.items():
    porcentagem = (value / valor_total) * 100

    print(f'{state} contribuiu com {value}, correspondendo a {porcentagem:.2f}% do faturamento mensal')
