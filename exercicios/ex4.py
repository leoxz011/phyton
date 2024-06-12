#Roprovado ou Não?
nota = 2
if nota >= 7:
    print(f'Sua nota foi {nota}, Você foi aprovado!!!')
elif nota <= 7 and nota >= 5:
    print(f'Sua nota foi {nota}, Você está de recuperação.')
else:
    print(f'Sua nota foi {nota}, Você foi reprovado.')