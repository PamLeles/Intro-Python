
num = int(input('Digite um número para você descobrir o dobro, o triplo e a raiz quadrada desse número: '))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print('o Dobro de {} é {}, e o seu triplo é {} e sua raiz quadrada é {:.2f}'.format(num,dobro,triplo,raiz))