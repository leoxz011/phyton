nome = input('Qual seu nome?')
idade = input(f'{nome} quantos anos você tem?')
peso = input(f'{nome} qual é o seu peso?')
print(nome, idade, peso)

dia = input(f'Certo {nome}, em que dia você nasceu?')
mes = input(f'E o mês?')
ano = input(f'Por ultimo o ano?')
print(f'Então você nasceu no dia {dia} de {mes} de {ano}')