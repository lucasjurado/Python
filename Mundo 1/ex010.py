nome=input('Digite o nome do aluno: ')
n1=float(input('Digite a nota da primeira prova: '))
n2=float(input('Digite a nota da segunda prova: '))
n3=float(input('Digite a nota da terceira prova: '))
nt=(n1+n2+n3)
md=(nt/3)
print('A nota final do aluno(a) {} foi de {:.2f}.'.format(nome,md))
