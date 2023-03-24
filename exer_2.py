def fibonacci(value):
    fibo_seq = [0, 1]
    i = 0

    while i < 100:
        first_num = fibo_seq[i]
        second_num = fibo_seq[i + 1]

        fibo_index = first_num + second_num

        fibo_seq.append(fibo_index)

        i += 1

    if value in fibo_seq:
        return f'{value} pertence à sequência de Fibonacci\n'
    else:
        return f'{value} não pertence à sequência de Fibonacci\n'


while True:
    user_value = input('Digite um número de 0 a 100: ')

    try:
        user_value = int(user_value)
    except ValueError:
        raise ValueError('Digite somente números')

    if user_value > 100:
        print('Digite um número menor que 100\n')
    else:
        print(fibonacci(user_value))