palavra = 'Lorem Ipsum Dolor Sit Amet'

palavra_reverse = ''
i = 0

while i < len(palavra):
    palavra_reverse += palavra[-i]
    i += 1
palavra_reverse = palavra_reverse[1:]
palavra_reverse += palavra[0]


print(palavra_reverse)