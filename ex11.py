agenda = {}
while True:
    nome = input('digite o nome da pessoa: ')
    if nome == '':
        break
    
    telefone = input('digite o tell: ')

## adiciona o tell ao dicionario 
    agenda[nome] = telefone

## pesquisa um tell na agenda 


nome_pesquisa = input('digite o nome para pesquisar: ')
if nome_pesquisa in agenda:
    print('telefone de', nome_pesquisa, ':', agenda[nome_pesquisa])
else:
    print('nome nao encontrado na agenda')