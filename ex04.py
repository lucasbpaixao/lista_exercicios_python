#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
n1 = int(input('Informe a primeira nota: '))
n2 = int(input('Informe a segunda nota: '))
n3 = int(input('Informe a terceira nota: '))
n4 = int(input('Informe a quarta nota: '))

media = (n1 + n2 + n3 + n4) / 4

print('A média do aluno foi: {media}'.format(media = media))