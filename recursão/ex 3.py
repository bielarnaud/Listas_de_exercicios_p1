def binary_search(arr,  x, caminho):
  mid = len(arr) // 2

  if len(arr) >= 1:
    if arr[mid] == x or len(arr) == 1:
      caminho.append("Meio")
      return caminho
    elif x < arr[mid]:
      caminho.append('Esquerda')
      return binary_search(arr[:mid], x, caminho)
    else: 
      caminho.append('Direita')
      return binary_search(arr[mid+1:], x, caminho)
  
  else:
    return caminho

def decimal_para_binario(x):
    return int(format(x, "b"))

numeros_das_salas = input()
numero_escolhido = int(input())
qnt_bits = int(input())

a = [int(item) for item in numeros_das_salas.split()]

#encontrando o caminho e o binário do número caso ele esteja dentro da lista

caminho = binary_search(a,numero_escolhido, [])
binario = decimal_para_binario(numero_escolhido)


#organizando o printando do caminho
if caminho != -1:
  cam = ''
  for i in range(len(caminho) -1):
    cam += caminho[i] + ' -> '
  cam += caminho[-1]

#organiznado o print do binário
binario = str(binario)

if len(binario) < qnt_bits:
  while len(binario) != qnt_bits:
    binario = '0' + binario

#Printando
if (numero_escolhido in a) and (len(binario) == qnt_bits):
  print(f'{cam}, seguindo por essas coordenadas você vai chegar no número {binario}.')

elif (numero_escolhido in a) and (len(binario) > qnt_bits):
  print(f'Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.')

elif ((numero_escolhido < min(a)) or (numero_escolhido > max(a))):
  print('Acho que a Doutora se confundiu, pois é impossível chegar nesse número pois ele é menor que a menor sala ou maior que o maior da sala.')

elif (numero_escolhido not in a) and (len(binario) > qnt_bits):
  print('Busquei muito, mas não achei a sala, que nem posso dizer, já que tenho poucos bits.')

elif (numero_escolhido not in a):
  print(f'{cam}, mas não consegui achar.')
