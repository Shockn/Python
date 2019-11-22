''' A prefeitura de uma cidade resolveu fazer uma pesquisa entre os seus
trabalhadores. Para isso ela coletou alguns dados como idade, sexo (M ou F) e salario.
Crie um algoritmo que leia estes dados e que escreva ao final:
a) a media salarial dos homens, a media salarial das mulheres
b) o maior salario encontrado entre as pessoas abaixo de 30 anos.
Obs:
(1) Considere que existem N trabalhadores
(2) O final da leitura de dados e marcado por uma idade negativa.'''


def Dados():
    arq = open('Ajudando o Argos\Prefeitura.txt','w')
    conth = contf = salh = salf = maiorsalario = 0
    arq.write('====INFORMAÇÃO====\n')
    while True:
        idade = int(input('Idade: [x < 0, para sair]: '))
        if idade < 0: break
        sexo = input('Sexo [M ou F]: ').upper()
        salario = float(input('Salario: '))
        if idade < 30:
            if salario >= maiorsalario:
                maiorsalario = salario
        if sexo == 'M':
            conth += 1
            salh += salario
        if sexo == 'F':
            contf += 1
            salf += salario 
    arq.write('A media salarial dos homens e R$ {:<.2f} \n'.format(salh/conth))
    arq.write('A media salarial das mulheres e R$ {:<.2f} \n'.format(salf/contf))
    arq.write('O maior salario entre pessoas com menos de 30 anos e R$ {:<.2f}'.format(maiorsalario))
    arq.close()

Dados()

