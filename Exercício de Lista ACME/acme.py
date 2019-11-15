'''A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no 
seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa 
saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço 
ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, 
chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar 
um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, 
caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço 
ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, 
que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser 
feito através de uma função, que será chamada pelo programa principal. '''

#FUNÇÃO QUE CONVERTE BYTES PRA MEGABYTES
def conMB(bts):
    mB=bts/1024**2
    return(mB)





#FUNÇÃO QUE CALCULA A PORCENTAGEM DE USO
def percent(x):
    arq=open('/home/yuri/Área de Trabalho/Git/Gituri/Python/Exercício de Lista ACME/usuarios.txt', 'r')
    
    total=0
    for i in arq:
        nome, x=i.split()
        x=float(x)
        total+=x
    
    arq.close()
    
    arq2=open('/home/yuri/Área de Trabalho/Git/Gituri/Python/Exercício de Lista ACME/usuarios.txt', 'r')

    for j in arq2:
        nome, y=j.split()
        y=float(y)
        xcons=(y*100)/total
        return(xcons)







#LENDO OS DADOS DO ARQUIVO 1 E ESCREVENDO NO ARQUIVO 2
f=open('/home/yuri/Área de Trabalho/Git/Gituri/Python/Exercício de Lista ACME/usuarios.txt', 'r')
f2=open('/home/yuri/Área de Trabalho/Git/Gituri/Python/Exercício de Lista ACME/relatorio.txt', 'w')

#ESCREVE O 'CABEÇALHO'
f2.write('ACME Inc.             Uso do espaço em disco pelos usuários\n')
f2.write('----------------------------------------------------------------\n')
f2.write('Nr.     Usuário              Espaço Utilizado            % do uso\n')

#ESCREVE AS LINHAS COM CADA UMA DAS INFORMAÇÕES PEDIDAS
num=0
for i in f:
    num+=1
    nome, cons=i.split()
    cons=float(cons)
    f2.write('{:1d}       {:1s}           {:1.2f} MB {:1s}    {:1.2f}%\n'.format(num, nome.ljust(10), conMB(cons),str('             ').ljust(15) , percent(cons)))






#FECHA OS ARQUIVOS
f.close()
f.close()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                #'Ainda falta ajeitar a parte da % de uso.'
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#