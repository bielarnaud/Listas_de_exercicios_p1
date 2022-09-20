#definindo dados das armas
chifre = 2
cajado = 4
espada = 6
grande_espada = 8
dardo = 12

#definindo valores das proteções
armadura_pesada = 0 
armadura_media =  1 
armadura_leve = 3

# dicionário do grupo com suas armas e armaduras
grupo = {'Bobby': [grande_espada , armadura_media],
        'Diana': [dardo , armadura_leve],
        'Eric': [grande_espada , armadura_pesada],
        'Hank': [espada , armadura_media],
        'Presto': [cajado , armadura_leve],
        'Sheila': [espada , armadura_leve],
        'Uni': [chifre , armadura_leve]}
        

#pontos de vida adversario
dic_adv = {'Vingador': 30,
          'Tiamat': 20,
          'Vingador das Sombras': 14}

#iniciando a batalha

adversario = input()
if adversario not in ['Vingador', 'Tiamat', 'Vingador das Sombras']:
  vida_adv = 9
else:
  vida_adv = dic_adv[adversario]
  
  
turnos = int(input())

while (int(turnos) > 0) or (int(vida_adv) > 0):
  try:
    personagem = input()
    if personagem == 'Mestre dos Magos':
      vida_adv = 0
    else:
      vida_adv = vida_adv - grupo[personagem][0]
      turnos = turnos - grupo[personagem][1]
  except:
    break

#prints
if personagem == 'Mestre dos Magos':
  print('Muito obrigado amigo, que nos vejamos novamente um dia')
elif vida_adv <= 0:
  print(f'{personagem} executou o ultimo golpe em {adversario}, estamos livres!')
elif vida_adv > 0:
  print(f'Oh nao, {adversario} e muito forte, este e o fim!')
    
  


  