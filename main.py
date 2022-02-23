import math


v1 = 'u'
v2 = 'u'
lastValue = 'u'
UseLastValue = 'N'

while(True):

    command = input('Digite o commando: ')
    if command == '+':
        UseLastValue = input('Usar o último valor? ')
        if UseLastValue == 'n': 
            v1 = input('Digite o primeiro valor: ')
            v2 = input('Digite o segundo valor: ')
            lastValue = str(float(v1) + float(v2))
            print(lastValue)
        elif UseLastValue == 's':
            if lastValue == 'u':
                print('Não foi possível usar o último valor porque ele não existe')
            else:    
                v1 = lastValue
                v2 = input('Digite o segundo valor: ')
                lastValue = str(float(v1) + float(v2))
                print(lastValue)
    elif command == '*':
        UseLastValue = input('Usar o último valor? ')
        if UseLastValue == 'n': 
            v1 = input('Digite o primeiro valor: ')
            v2 = input('Digite o segundo valor: ')
            lastValue = str(float(v1) * float(v2))
            print(lastValue)
        elif UseLastValue == 's':
            if lastValue == 'u':
                print('Não foi possível usar o último valor porque ele não existe')
            else:    
                v1 = lastValue
                v2 = input('Digite o segundo valor: ')
                lastValue = str(float(v1) * float(v2))
                print(lastValue)
    elif command == '-':
        UseLastValue = input('Usar o último valor? ')
        if UseLastValue == 'n': 
            v1 = input('Digite o primeiro valor: ')
            v2 = input('Digite o segundo valor: ')
            lastValue = str(float(v1) - float(v2))
            print(lastValue)
        elif UseLastValue == 's':
            if lastValue == 'u':
                print('Não foi possível usar o último valor porque ele não existe')
            else:    
                v1 = lastValue
                v2 = input('Digite o segundo valor: ')
                lastValue = str(float(v1) - float(v2))
                print(lastValue)
    elif command == '/':
        UseLastValue = input('Usar o último valor? ')
        if UseLastValue == 'n': 
            v1 = input('Digite o primeiro valor: ')
            v2 = input('Digite o segundo valor: ')
            lastValue = str(float(v1) / float(v2))
            print(lastValue)
        elif UseLastValue == 's':
            if lastValue == 'u':
                print('Não foi possível usar o último valor porque ele não existe')
            else:    
                v1 = lastValue
                v2 = input('Digite o segundo valor: ')
                lastValue = str(float(v1) / float(v2))
                print(lastValue)
    elif command == 'man':
        print('Para somar use o comando: "+"\n')
        print('Para multiplicar use o comando: "*"\n')
        print('Para subtrair use o comando: "-"\n')
        print('Para dividir use o comando: "/"\n')
        print('Para tirar raiz use o comando: "st"\n') 
        print('Para usar o valor da operação anterior digite "s" ao ser perguntado, para não usar digite "n"')
    elif command == 'st':
        v1 = input('De qual valor você deseja tirar a raiz: ')
        lastValue = (str(math.sqrt(float(v1))))
        print(math.sqrt(float(v1)))
    elif command == 'exit':
        break   