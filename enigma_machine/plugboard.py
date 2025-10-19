def plugboard(chave_plug, txt_to_crypt):

    chave = {} # Transformando a variavel "chave" em um dicionario
    config_plug = chave_plug.replace(" ","") # Utilizando o replace para retirar os espaços da string
    chave_inv = {} 
    crypted_txt = "" 

    '''
    Necessário criar dois caminhos, ida e volta, dos quais irá pegar o numero de letras que estão dentro do dicionario, e em uma distancia indicada (para não dar conflito entre o espaçamento e a letra que estava ligada a outra), possibilitando utilizar a função "update" e mesclar ambos os dicionários realizando assim a alteração de variaveis.

    '''
    for i in range(0,len(config_plug),2): 
        chave.update({config_plug[i]: config_plug[i+1]}) # Caminho de IDA
    for i in range(0,len(config_plug),2):
        chave_inv.update({config_plug[i+1]: config_plug[i]}) # Caminho de VOLTA

        '''
        Verificando se a "letra" está dentro do dicionario, caso esteja ela será alterada pelas letras do dicionario, caso contrario, retornarão as letras de entrada.
        '''
    for letra in txt_to_crypt:
        if letra in chave:
            crypted_txt += chave[letra]
        elif letra in chave_inv:
            crypted_txt += chave_inv[letra]
        else:
            crypted_txt += letra
        
            
    return (crypted_txt)
            
