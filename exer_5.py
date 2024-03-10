palavra = 'Lorem Ipsum Dolor Sit Amet'

palavra_reverse = ''
i = 1

while i < len(palavra) + 1:
    palavra_reverse += palavra[-i]
    i += 1

print(palavra_reverse)
