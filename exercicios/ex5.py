#Desconto
item = 10
desconto1 = 0.1
desconto2 = 0.2
carrinho = 30
if carrinho <= 10:
    valor_total = item * carrinho
elif carrinho <=20:
    valor_total = carrinho * item *(1-desconto1)
else:
    valor_total = carrinho * item * (1-desconto2)

print(f'O valor total da compra foi {valor_total}')