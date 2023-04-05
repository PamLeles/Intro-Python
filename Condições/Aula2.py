media = float(input('Informe a média do estudante: '))
presenca = float(input('Informe o percentual de presença do estudante: '))

if media >= 7 and presenca >= 70:
  print('Você foi aprovado(a)!')
elif media >= 5 and presenca >= 70:
  print('Recuperação.')
else:
  print('Você foi reprovado(a).')