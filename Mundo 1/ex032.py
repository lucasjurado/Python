frase=str(input('Digite uma frase: ')).strip().upper()
letra=str(input('Qual letra você gostaria de procurar? ')).strip().upper()
print('A letra {} aparece {} vezes na frase {}.'.format(letra,frase.count(letra),frase.capitalize()))
print('A primeira letra {} apareceu na posição {}º.'.format(letra, frase.find(letra)+(1)))
print('A última letra {} apareceu na posição {}º.'.format(letra, frase.rfind(letra)+(1)))