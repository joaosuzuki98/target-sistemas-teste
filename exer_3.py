lista_a = [1, 3, 5, 7]
while len(lista_a) <= 10:
    num_a = lista_a[-1] + 2
    lista_a.append(num_a)
print(lista_a)

lista_b = [2, 4, 8, 16, 32, 64]
while len(lista_b) <= 10:
    num_b = lista_b[-1] * 2
    lista_b.append(num_b)
print(lista_b)

lista_c = [0, 1, 4, 9, 16, 25, 36]
i_c = 13
while len(lista_c) <= 10:
    num_c = lista_c[-1] + i_c
    i_c += 2
    lista_c.append(num_c)
print(lista_c)

lista_d = [4, 16, 36, 64]
i_d = 36
while len(lista_d) <= 10:
    num_d = lista_d[-1] + i_d
    i_d += 8
    lista_d.append(num_d)
print(lista_d)

lista_e = [1, 1, 2, 3, 5, 8]
while len(lista_e) <= 10:
    num_e = lista_e[-1] + lista_e[-2]
    lista_e.append(num_e)
print(lista_e)

lista_f = [2, 10, 12, 16, 17, 18, 19]
while len(lista_f) <= 10:
    num_f = lista_f[-1] + 1
    lista_f.append(num_f)
print(lista_f)
