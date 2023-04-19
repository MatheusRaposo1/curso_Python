"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
#Exercício 1
#if entrada.isdigit():
    #entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
# entrada = input('Digite um número ')
# try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro')

#Exercicio 2 
# horas = input('Diga as horas: ')
# horas_int = int(horas)
# if horas_int <= 11:
#     print('Bom dia ')
# elif horas_int <= 17:
#     print('Boa tarde ')         
# else:
#     print('Boa noite ')
# try:
#     horas = int(entrada)
#     if horas >=0 and horas <=11:
#         print(f'Bom dia, as horas são {horas} da manhã')
#     elif horas >=12 and horas <= 17:
#         print(f'Boa tarde, as horas são {horas} da tarde ')
#     elif horas >=18 and horas <=23:
#         print(f'Boa noite, as horas são {horas} da noite')       
#     else:
#         print(f'Não conheco essa hora {horas}')
# except:    
#     print('Por favor, digite um número inteiro ')

#Exercicio 3 

nome = input('Digite seu nome ')
tamanho_nome = len(nome)
if tamanho_nome > 1:
    if tamanho_nome <=4:
        print(f'Seu nome é curto {nome}')
    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print(f'Seu nome é normal {nome}')
    else:
        print(f'Seu nome é muito grande {nome}')    
else:
    print('Por favor, digite mais de uma letra')    