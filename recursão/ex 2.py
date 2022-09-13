#definindo funções
#############################################################
# essa função codifica as letras e aplica o mod 11 para elas
def codificar (palavra):
  palavra_codificada = []
  for letra in palavra:
     palavra_codificada.append( (ord(letra) - 97) % 11 )
  return palavra_codificada
##############################################################
#cria uma sequencia de x termos fatorial
def fat(termo):
  if termo == 0 :
      return 1 
  else:
    return termo * fat(termo-1)
    
def aplica_fat (num):
  lista_fat = []
    
  for i in range(0,num):
    lista_fat.append( fat(i) )
    
  return lista_fat
###############################################################
#cria uma sequencia de x termos fibo
def fib(termo):
  if(termo == 0 or termo == 1):
    return termo
  else:
    return fib(termo-1) + fib(termo-2)
    
def aplica_fib (num):
  lista_fib = []
    
  for i in range(0,num):
    lista_fib.append( fib(i) )
    
  return lista_fib
################################################################
def decodificar(palavra_codificada):
  senha = ''
  
  for cod in palavra_codificada:
    if cod == '1':
      senha += '1'
    
    else:  
      if cod < 26:
        pass
      else:
        cod = cod % 26
    
      letra = chr(cod + 97)
      senha += letra
  
  return senha
#################################################################

#inicio do programa

senha = input()
n = int(input())

senha_certa = False

palavras = []
for i in range(n):
  palavra = codificar(input())
  palavras.append(palavra)

for palavra in palavras:
  senha_codificada = []
  
  for cod in palavra:
    fato = aplica_fat(cod)
    fibo = aplica_fib(cod)
    
    if cod == 0:
      senha_codificada.append('1')
    elif cod % 2 == 1:
      for n in range(len(fato)):
        senha_codificada.append((fato[n] * fibo[n]))
    else:
      for n in range(len(fato)):
        senha_codificada.append((fato[n] + fibo[n]))
  
  senha_teste = decodificar(senha_codificada)
  
  if senha_teste == senha:
    senha_certa = True
    
if senha_certa == True:
  print('Achamos! Achamos a senha.')
else:
  print('É... Temos que procurar mais.')