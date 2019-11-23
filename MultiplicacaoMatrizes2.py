import random

#GERANDO AS DUAS MATRIZES
def matGen():
    A=[]
    lA=int(input('Digite o número de linhas da 1° matriz: '))
    cA=int(input('Digite o número de colunas da 1° matriz: '))
    for i in range(0, lA):
        A.append(0)
        A[i]=[]
        for j in range(0, cA):
            A[i].append(random.randint(0, 10))

    B=[]
    lB=int(input('Digite o número de linhas da 2° matriz: '))
    cB=int(input('Digite o número de colunas da 2° matriz: '))
    for i in range(0, lB):
        B.append(0)
        B[i]=[]
        for j in range(0, cB):
            B[i].append(random.randint(0, 10))
    return(A, B)

#MULTIPLICANDO AS MATRIZES
def matMult(A, B):
    C=[]
    if len(A)==len(B[0]):
        for i in range(0, len(A)):
            C.append([])
            for j in range(0, len(B[0])):
                C[i].append(0)
                for k in range(0, len(A[0])):
                    try:
                        C[i][j]+=A[i][k]*B[k][j]
                    except:
                        return(False, '\n\nNão é possível multiplicar as matrizes.')
        return(True, C)
    else:
        return(False, '\n\nNão é possível multiplicar as matrizes.')

#CHAMADA DAS FUNÇÕES
m1, m2=matGen()
resultado, m3=matMult(m1, m2)

#IMPRESSÃO DAS MATRIZES
print('\n1° MATRIZ:')
for i in range(0, len(m1)):
    print()
    for j in range(0, len(m1[0])):
        print(str(m1[i][j]).center(5), end=' ')

print('\n\n2° MATRIZ:')
for i in range(0, len(m2)):
    print()
    for j in range(0, len(m2[0])):
        print(str(m2[i][j]).center(5), end=' ')

if resultado:
    print('\n\n3° MATRIZ:')
    for i in range(0, len(m3)):
        print()
        for j in range(0, len(m3[0])):
            print(str(m3[i][j]).center(5), end=' ')
else:
    print(m3)