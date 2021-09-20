#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
raio = float(input('Informe o raio do circulo: '))

area = math.pi * math.pow(raio,2)

print('A area do circulo é {area:.2f}'.format(area = area))