cadastro = {}
while True:
    nome = input('digite o nome completo: ')
    if nome == '':
        break
        
        
idade = int(input('digite a idade: '))
cidade = input('digite a cidade: ')


## adiciona dados ao dicionario
cadastro[nome] = {'idade': idade, 'cidade': cidade}

## imprime o cadastro completo 
print('cadastro: ')
print(cadastro)
for nome, dados in cadastro.items():
    print('- nome:', nome)
    print('- idade:',dados['idade'])
    print('- cidade:',dados['cidade'])
    
    