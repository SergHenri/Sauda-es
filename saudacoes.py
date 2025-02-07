"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora: ')

try:
    # Tenta converter a entrada do usuário para um número de ponto flutuante
    conversao_float = float(hora)

    # Verifica se a hora está no período da manhã (entre 0 e 11.59)
    if 0 <= conversao_float <= 11.59:
        print('Tenha um bom dia')
    # Verifica se a hora está no período da tarde (entre 12 e 17.59)
    elif 12 <= conversao_float <= 17.59:
        print('Tenha uma boa tarde')
    # Qualquer outro valor corresponde ao período da noite
    else:
        print('Tenha uma boa noite')
except:
    # Exibe uma mensagem de erro caso a conversão falhe (entrada inválida)
    print('Você não digitou um número válido')
