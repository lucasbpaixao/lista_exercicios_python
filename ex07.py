#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
base = float(input('Informe o valor da base do quadrado: '))

altura = base
area = base * altura
dobroArea = area * 2

print('O dobro da area do quadrado é {area}.'.format(area = dobroArea))