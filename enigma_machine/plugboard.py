def plugboard(chave_plug, txt_to_crypt):

    chave = {}
    config_plug = chave_plug.replace(" ","")
    chave_inv = {}
    crypted_txt = ""

    for i in range(0,len(config_plug),2):
        chave.update({config_plug[i]: config_plug[i+1]})
    for i in range(0,len(config_plug),2):
        chave_inv.update({config_plug[i+1]: config_plug[i]})

    for letra in txt_to_crypt:
        if letra in chave:
            crypted_txt += chave[letra]
        elif letra in chave_inv:
            crypted_txt += chave_inv[letra]
        else:
            crypted_txt += letra
            
    return (crypted_txt)
            
