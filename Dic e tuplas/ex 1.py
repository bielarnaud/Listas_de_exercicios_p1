dic = {}

while True:
  try:
    comando, nome = input().split(' ')
    
    if comando == 'ADD':
      if dic.get(nome) == None:
        desc = input()
        dic[nome] = desc
        print('Pokémon adicionado com sucesso')
      
      else:
        print('Pokémon já adicionado na Pokédex')
    elif comando == 'DESC':
      
      if dic.get(nome) == None:
        print('Ainda não há registro desse Pokémon')
      
      else:  
        print(dic[nome])
      
  except EOFError:
      break
