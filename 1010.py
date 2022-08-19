linha1 = input().split('')
linha2 = input().split('')
cod1, qtd1, vlr1 = linha1
cod2, qtd2, vlr2 = linha2
vlrTotal = (qtd1*vlr1) + (qtd2*vlr2)

print('VALOR A PAGAR: R$ %.2f' %vlrTotal)