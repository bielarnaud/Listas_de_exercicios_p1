n = int(input())

a = input().split(' ')
b = input().split(' ')

dic = {'gohan': a , 'piccolo': b }

def verifica_igualdade (a , b):
  igual = True
  
  for i in range(n):
    try:
      dist = a[i]
      b.remove(dist)
    except:
      igual = False
      
  return igual

igual = verifica_igualdade(dic['gohan'], dic['piccolo'])

if igual :
  print('Dale Gohan!')
else:
  print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')