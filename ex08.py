#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valorHora = float(input('Informe o valor que você ganha por hora: '))
horasMes = float(input('Informe quantas horas você trabalha por mês: '))

salario = valorHora * horasMes

print('O seu salário no mês foi R$ {total}'.format(total = salario))