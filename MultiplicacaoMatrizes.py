import random

#GERA AS MATRIZES 1 E 2
def matGen():
    m1=[]
    m2=[]
    
    l1=random.randint(2, 3)
    c1=random.randint(2, 3)
    l2=random.randint(2, 3)
    c2=random.randint(2, 3)
    
    m1=[None]*l1
    for i in range(0, l1):
        m1[i]=[None]*c1
        for j in range(0, c1):
            m1[i][j]=random.randint(0, 10)

    m2=[None]*l2
    for i in range(0, l2):
        m2[i]=[None]*c2
        for j in range(0, c2):
            m2[i][j]=random.randint(0, 10)
    return(m1, m2)

#MULTIPLICA AS MATRIZES E GERA A MATRIZ 3
def multMatriz(m1, m2):
    m3=[]
    if len(m1)==len(m2[0]):
        for i in range(0, len(m1)):
            m3.append([])
            for j in range(0, len(m2[0])):
                m3[i].append(0)
                for k in range(0, len(m1[0])):
                    try:
                        m3[i][j]+=m1[i][k]*m2[k][j]
                    except:
                        return(False, 'Não foi possível multiplicar as matrizes.')
        return(True, m3)
    else:
        return(False, 'Não foi possível multiplicar as matrizes.')

#CHAMA AS FUNÇÕES
a, b=matGen()
result, c=multMatriz(a, b)

#IMPRIME OS DADOS
print('MATRIZ 1:')
for i in range(0, len(a)):
    print()
    for j in range(0, len(a[0])):
        print(str(a[i][j]).center(5), end=' ')

print('\n\nMATRIZ 2:')
for i in range(0, len(b)):
    print()
    for j in range(0, len(b[0])):
        print(str(b[i][j]).center(5), end=' ')

if result:
    print('\n\nMATRIZ MULTIPLICADA:')
    for i in range(0, len(c)):
        print()
        for j in range(0, len(c[0])):
            print(str(c[i][j]).center(5), end=' ')
else:
    print('\n\n', c)
