'''
Exercícios sobre os comandos básicos em Python


#1. Faça um programa que imprima o seu nome.


def q1():
    print('PAULA')
    
q1()
#2. Faça um programa que imprima o produto dos valores 30 e 27.

def q2():
    print(10*3)
q2()
#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.

def q3():
    print((5+8+12)/(3))
q3()



#4. Faça um programa que leia e imprima um número inteiro.
def q4():
    numero = int(input('Digite um número inteiro: '))
    print(numero)
q4()
#5. Faça um programa que leia dois números reais e os imprima.
def q5():
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))
    print(f'{num1}\n{num2}')
q5()

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q6():
    num = int(input('Digite um número: '))
    print(f'Antecessor de {num}: é {num -1}')
    print(f'Sucessor de {num}: é {num +1}')
q6()

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q7():
    nome = input('Digite um nome: ')
    
    endereco = input('Digite o endereço: ')
    
    telefone = input('Digite o telefone: ')
    
    print(f'{nome} \t {endereco} \t {telefone}')
q7()

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.

def q8():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    
    print(f'{num1} - {num2} = {num1 - num2}')
q8()
    
#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9():
    num = float(input('Número: '))
    print(f'1/4 de {num} é: {round(num/4,2)}')
q9()

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    N1 = float(input('Número1: '))
    N2 = float(input('Número2: '))
    N3 = float(input('Número3: '))
    media = (N1+N2+N3)/3
    print(f'A média é:{round(media,2)}')
q10()

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    A = float(input('Valor de A:'))
    B = float(input('Valor de B:'))
    print(f'{A}+{B} = {round(A+B,2)}')
    print(f'{A}-{B} = {round(A-B,2)}')
    print(f'{A}*{B} = {round(A*B,2)}')
    print(f'{A}/{B} = {round(A/B,2)}')
q11()

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    X = float(input('X: '))
    print(pow(X,2))
q12()

#13. Faça um programa
#  que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
saldo = round(float(input('Saldo: R$')),2)
print(f'Saldo atual com reajuste de 2%: R${round(saldo*1.02,2)}')    




#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base * 2) + altura *2) e a área (base * altura).

def q14():
    base = float(input('BASE: '))
    altura = float(input('ALTURA: '))
    area = (base * altura)
    print(f'Área do retângulo é: {round(area,2)}')
    perimetro = (2*(base + altura))
    print(f'Perímetro do retângulo é: {round(perimetro,2)}')
q14()
    #15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():
    produto = round(float(input('Valor do produto é:R$ ')))
    percentual_desconto = round(float(input('Porcentagem de desconto:% ')))
    print(f'Valor do produto:R${produto},2')
    print(f'O desconto oferecido: {percentual_desconto}%')
    print(f'O valor do produto já com desconto fica: R${round(produto-(produto*percentual_desconto/100),2)}')
q15()
#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
def q16():
    salario = float(input('Salário: R$'))
    reajuste_percentual = float(input('Porcentagem de aumento:%'))
    print(f'O salário atualizado com reajuste:R${round(salario+(salario*reajuste_percentual/100))}')


q16()
#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
def q17():
    C = float(input('Graus Celsius:°'))
    F = (9*C+160)/5
    print(f'{C}° C = {F} F')
q17()

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def q18():
    T = int(input('Tempo de viagem (em minutos): '))
    V = int( input('Velocidade média percorrida (em Km): '))
    D = (T/60) * V
    L = D/12
    print(f'Distância é:{D}')
    print(f'Litros consumidos:{L}')
q18()

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.

def q19():
    prestacao = int(input('Valor da prestação vencida:R$'))
    taxa_juros = int(input('Taxa de juros(por dia):%'))
    dias_atrasados = int(input('Dias em atraso:'))
    juros = prestacao*(dias_atrasados*taxa_juros/100)
    pretacao_final = prestacao + juros
    print(f'Multa por atraso:R${juros}')
    print(f'Prestação atualizada com encargos:R${pretacao_final}')
q19()
#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
def q20():
    dolar = round(float(input('Quantidade em Dólares:US$')),2)
    cotacao_dolar = round(float(input('Cotação do Dólar:US$')),2)
    print(f'Quantidade em Reais:R${round(dolar*cotacao_dolar,2)}')
q20() 



#FAÇA UM PROGRAMA DE CONVERSÃO
#REAL PARA DÓLAR, USANDO A COTAÇÃO:
#IMPRIMA:'''
def q21():
    cd = round(float(input('Cotação do Dólar:R$')),2)
    r = round(float(input('Reais:R$')))
    print(f'Dólar:US${round(r/cd,2)}')
q21()