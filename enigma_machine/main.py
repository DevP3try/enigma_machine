from rotor import Rotor
import plugboard as pg
import input_data as data

 

def main():
    # Entrada do texto
    txt_to_crypt = data.input_txt(input("Digite o texto a ser cifrado/decifrado: ")) # O teste ser 'AAAAA'
    
    # configuração do plugboard
    config_plug = data.input_plugboard(input("Digite a configuração do plugboard (ex: 'AB CD EF'): "))
    
    # Configuração dos rotores
    rotores = data.input_rotores(input("Insira a config dos rotores: (ex: 'I II III'): "))
    pos_inicial = data.input_pos_inicial(input("Digite as posições iniciais dos rotores (3 letras, ex: 'AAA'): "))
    config_aneis = data.input_config_aneis(input("Digite a configuração dos anéis (3 letras, ex: 'AAA'): "))
    refletor = data.input_refletor(input("Digite o refletor escolhido (B ou C): "))
     
    # Montando a máquina Enigma com as configurações fornecidas
    config_rotores = Rotor(
        rotores,
        pos_inicial,
        config_aneis,
        refletor
    )
    # criptografando o texto
    print(f"Configuração: {rotores} | Posições: {pos_inicial} | Anéis: {config_aneis} | Refletor: {refletor}")
    print(f"Texto original: {txt_to_crypt}")
    
    txt_to_crypt = pg.plugboard(config_plug, txt_to_crypt) # Passando pelo plugboard 
    txt_crypted = config_rotores.criptografar_texto(txt_to_crypt) # Passando pelo rotor
    txt_crypted = pg.plugboard(config_plug, txt_crypted) # passando novamente pelo plugboard
    
    
    print(f"Texto cifrado:  {txt_crypted}") 

main()