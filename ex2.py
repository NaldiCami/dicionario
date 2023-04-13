dicionario = {'cat': 'chat', 'dog':'chien', 'horse':'cheval'}
palavras = ['cat','lion','horse']

for palavra in palavras:
    if palavra in dicionario:
        print(palavra,'==>', dicionario[palavra])
else:
    print(palavra,'não esta no dicionario')