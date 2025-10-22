from rotor import Rotor
from plugboard import plugboard
import input_data as data

 

# Configuração da Máquina:
# Rotores: I, II, III (Lento, Meio, Rápido)
# Posições Iniciais: A, A, A
# Configuração dos Anéis: A, A, A (ou 01, 01, 01)
# Refletor: B


def main():
    
    texto = data.input_txt(input("Digite o texto a ser cifrado/decifrado: "))
    plugboard = data.input_plugboard(input("Digite a configuração do plugboard (ex: 'AB CD EF'): "))
    rotores = data.input_rotores(input("Insira a config dos rotores"))
    pos_inicial = data.input_pos_inicial(input("Digite as posições iniciais dos rotores (3 letras, ex: 'AAA'): "))
    config_aneis = data.input_config_aneis(input("Digite a configuração dos anéis (3 letras, ex: 'AAA'): "))
    refletor = data.input_refletor(input("Digite o refletor escolhido (B ou C): ")) 
    
    config_rotores = {
        rotores,
        pos_inicial,
        config_aneis,
        refletor
    }

    
    
    """
    # 1. Cifrando
    maquina_cifra = Rotor(
        rotores_escolhidos = ['I', 'II', 'III'],
        posicoes_iniciais = ['A', 'A', 'Z'], # Perto de um entalhe
        config_aneis       = ['A', 'A', 'A'],
        refletor_escolhido = 'B'
    )
    """
    print(f"Configuração: I-II-III | Posições: AAZ | Anéis: AAA | Refletor: B")
    cifrado = config_rotores.criptografar_texto(texto)
    print(f"Texto original: {texto}")
    print(f"Texto cifrado:  {cifrado}") # Deve ser 'BDZGO'


    # 2. Decifrando 
    # Basta criar uma máquina EXATAMENTE IGUAL
    maquina_decifra = Rotor(
        rotores_escolhidos = ['I', 'II', 'III'],
        posicoes_iniciais = ['A', 'A', 'Z'],
        config_aneis       = ['A', 'A', 'A'],
        refletor_escolhido = 'B'
    )
    decifrado = maquina_decifra.criptografar_texto(cifrado)
    print(f"Texto decifrado:{decifrado}") # Deve ser 'AAAAA'
    
if main == __name__:
    main()