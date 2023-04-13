students = {
    'joão': {
        'idade': 18,
        'cidade': 'sp',
        'notas': [7.5,8.0,9.0]

    },
    'Maria': {
        'idade': 18,
        'cidade': 'rj',
        'notas': [6.5,7.0,8.5]
    },
    'pedro':{
        'idade': 18,
        'cidade': 'sp',
        'notas': [7.5,8.0,9.0]
    }
}

### imprimir a idade de joao
print('a idade de joao é: '+ str(students['joão']['idade']))

### add uma nova nota a maria 
students['Maria']['notas'].append(9.0)

### imprimir as informções dos alunos 
for student,info in students.items():
    print(student + ':')
    print('idade:' + str(info['idade']))
    print('cidade:' + info['cidade'])
    print('notas:' + str(info['notas']))
    print('medio:' + str(sum(info['notas']) / len(info['notas'])))
    print()