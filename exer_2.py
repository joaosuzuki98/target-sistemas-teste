from time import sleep


fibo = int(
    input(
        "Digite um número para saber se ele está na sequência de Fibonacci: "
        ))

fibo_seq = [0, 1]
i = 0

while True:
    fibo_num = fibo_seq[i] + fibo_seq[i + 1]
    fibo_seq.append(fibo_num)
    i += 1
    print(fibo_seq)
    sleep(.5)

    if fibo_num > fibo:
        print(f"O número {fibo} não existe na sequência de Fibonacci")
        break

    if fibo in fibo_seq:
        print(f"O número {fibo} está presente na sequência de Fibonacci.")
        break
