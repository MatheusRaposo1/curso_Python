nome = input('Digite o seu nome ')
idade = input('Qual a sua idade ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome comtém espacos')
    else:
        print(f'Seu nome não espacos {nome}')

    print(f'Seu nome tém {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    print('Desculpe, voce deixou campos vazios ')


