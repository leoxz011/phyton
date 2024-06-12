#sistema para calcular descontos
preço = float(input('Qual o preço do Produto? R$'))
desconto = float(input('Qual vai ser o desconto aplicado neste produto? %'))
preço_final = preço - (preço * desconto / 100)
print(f'O preço final deste produto já com o desconto aplicado será de R${preço_final:.2f}')