#Definindo funções
def soma(m1, m2, n):
  m_soma = []
  
  #calculando as linhas da matriz
  for i in range(n):
    linha = []
    for j in range(n):
      soma = int(m1[i][j]) + int(m2[i][j])
      linha.append(soma)
  
    m_soma.append(linha)
  
  return m_soma

def subtracao(m1, m2, n):
  m_subtracao= []
  
  #calculando as linhas da matriz
  for i in range(n):
    linha = []
    for j in range(n):
      subtracao = int(m1[i][j]) - int(m2[i][j])
      linha.append(subtracao)
  
    m_subtracao.append(linha)
  
  return m_subtracao

def mult_esc (m, esc, n):
  m_mult = []
  
  #calculando as linhas da matriz
  for i in range(n):
    linha = []
    for j in range(n):
      mult = esc * int(m[i][j])
      linha.append(mult)
  
    m_mult.append(linha)
  
  return m_mult

def m_matrizes(m1, m2, n):
  def getLinha(matriz, n):
    return [i for i in matriz[n]]  
  
  def getColuna(matriz, n):
    return [i[n] for i in matriz]
  
  m1lin = len(m2)
  m2col = len(m2[0])
  
  m_mult = []
  for i in range(m1lin): 
    linha = []
    for j in range(m2col):
      mult_matrizes = [int(x)*int(y) for x, y in zip(getLinha(m1, i), getColuna(m2, j))]
      linha.append(sum(mult_matrizes))
  
    m_mult.append(linha)
  
  
  return m_mult

#INICIO DO PROGRAMA
n = int(input())
m1 =[]
m2 = []
esc = 1

#definindo m1 e m2
for i in range(n):
  linha = input().split(' ')
  m1.append(linha)
for i in range(n):
  linha = input().split(' ')
  m2.append(linha)

#Definir as operações a serem feitas
qtd_op = int(input())

operacoes = []
for i in range(qtd_op):
  operacoes.append( input().split(' ') )

#Descobrindo operador e os fatores
for i in range(qtd_op):
  m_r = operacoes[i][0]
  f_1 = operacoes[i][2]
  operador = operacoes[i][3]
  f_2 = operacoes[i][4]

  #Definindo f1
  if f_1 == 'm1':
    f1 = m1
  elif f_1 == 'm2':
    f1 = m2
  else:
    esc = int(f_1)
  
  #Definindo f2
  if f_2 == 'm1':
    f2 = m1
  elif f_2 == 'm2':
    f2 = m2
  else:
    esc = int(f_2)
  
  #aplicando operações em uma matriz resultante
  if operador == '+':
    mr = soma(f1,f2,n)
  
  elif operador == '-':
    mr = subtracao(f1,f2,n)
    
  elif operador == '.':
    mr = m_matrizes(f1, f2, n)
    
  elif operador == '*':
    #verificando qual dos fatores é o inteiro
    if f_1 == 'm1' or f_1 == 'm2':
      mr = mult_esc(f1,esc,n)
      
    else:
      mr = mult_esc(f2,esc,n)
      
  #Atualizando valores de m1 ou de m2
  if m_r == 'm1': #nesse caso m2 vai receber os resultados
    m1 = mr
  else: #nesse caso m2 vai receber os resultados
    m2 = mr

for i in range(n):
  print(*mr[i])
