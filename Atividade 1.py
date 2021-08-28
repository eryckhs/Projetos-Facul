#   Integrantes:
#   Eryck Henrique Santos RA:1680972111036
#   Alexandre Angelo Teran Candia RA:1680972111009

def valid(p,a,s):
    #Dentro desta função a validação dos dados será feita. Caso ocorra no mínimo 1 erro o valor da valid será = 1,
    #indicando que o programa não pode fazer o processamento do IMC. Dentro desta função também será feita 
    #a exibição do erro ocorrido para o usuário
    valid = 0
    try:
        if p < 30 or p > 300:
            print('Valor do Peso Inválido')
            valid = 1
        if a < 1 or a > 2.5:
            print('Valor da Altura Inválido')
            valid = 1
        if s != 'M' and s != 'F':
            print('Valor do Sexo Inválido')
            print(s)
            valid = 1
    except:
       print('Erro Desonhecido')
       valid = 1
    
    return valid 

def cat(s,valor):
    #Dentro da função o programa irá identificar o sexo do usuário e prosseguir com o resto da categorização de acordo com o valor do IMC.
    #  Dentro desta função também será fetia a exibição do valor do IMC e a categoria em que o usuário se encaixa.
    if s == 'M':
        if valor > 30:
            print(f'O Valor do seu IMC é: {valor:.2f}, você está Acima Do Peso')   
        if valor <= 30 and valor >25:
            print(f'O Valor do seu IMC é: {valor:.2f}, você está com o Peso Normal')     
        if valor <=25:
            print(f'O Valor do seu IMC é: {valor:.2f}, você está Abaixo do peso')
    else:
        if valor > 26:
            print(f'O Valor do seu IMC é: {valor:.2f}, você está Acima Do Peso')   
        if valor <= 26 and valor >20:
            print(f'O Valor do seu IMC é: {valor:.2f}, você está com o Peso Normal')     
        if valor <= 20:
            print(f'O Valor do seu IMC é: {valor:.2f}, você está Abaixo do peso')
    

resp = 's'
while resp == 's':
    #início do programa pedindo os dados do usuário
    peso = float(input('Insira o seu peso (30kg -- 300kg): '))
    altura = float(input('Insira a sua altura (1m -- 2,5m): '))
    sexo = input('Insira o seu sexo (M/F): ').upper()

    valid = valid(peso,altura,sexo)#A função valid é chamada para validar os dados inseridos
    
    #Caso o valor de valid seja 0 a fórmula do IMC será executada
    if valid == 0:
        imc = (peso/(altura**2))
    #O valor de valid será diferente de 0 quando apresentar algum erro nos dados inseridos,
    # portanto não será capaz de prosseguir com a fórmula do IMC, contudo o usuário pode refazer o programa caso desejado. 
    else:
        resp = input('Programa Finalizado! \nDeseja Continuar? (s/n)').lower()
        if resp == 'n':
            print('Obrigado por usar o programa!')
            break
        else:
            continue
    
    #Após os dados serem validados e o IMC é calculado, a função categ será chamada para identificar 
    # o sexo do usuário e a sua categoria de acordo com o valor do IMC.
    categ = cat(sexo, imc)

    #Após todo o processamento e exibição do resultado o usuário pode escolher se deseja refazer o programa 
    # com outros dados ou se deseja encerrar e sair.
    resp = input('Programa Finalizado! \nDeseja Continuar? (s/n)').lower()
    if resp == 'n':
        print('Obrigado por usar o programa!')
        break

        




