#Criando a lista de caracteres!
caracteres = []

#pegando todas as letras minúsculas
for i in range(ord('a'), ord('z')+1): 
	caracteres.append(chr(i))

#O segundo for só vai até x pois só há 50 letras minúsculas
for i in range (ord('a'), ord('x')+1):
	caracteres.append(chr(i))

#repetindo o código para letras maiúsculas
for i in range (ord('A'), ord('Z')+1):
	caracteres.append(chr(i))

for i in range (ord('A'), ord('X')+1):
	caracteres.append(chr(i))
	
#Add o espaço ao ultimo número da lista
caracteres.append(' ')

######################################
#defitindo uma  função para codificar#

def codificador (codigos):
  
  mensagem =''
  identificavel = True
  
  for codigo in codigos:
    if int(codigo) in list(range(101)):
      caracter = caracteres[int(codigo)]
      mensagem = mensagem + caracter
    
    else:
      identificavel = False
      
  if identificavel == True:
    return mensagem
  else:
    return ('Infelizmente os números nao dizem nada')

#################################
#iniciando o programa
codigos = input().split(' ')
mensagem = codificador(codigos)
print(mensagem)