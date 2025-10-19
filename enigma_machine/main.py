from rotor import Rotor

# Configuração da Máquina:
# Rotores: I, II, III (Lento, Meio, Rápido)
# Posições Iniciais: A, A, A
# Configuração dos Anéis: A, A, A (ou 01, 01, 01)
# Refletor: B

# 'AAAAA' para ver o giro
texto = "AAAAA"

# 1. Cifrando
maquina_cifra = Rotor(
    rotores_escolhidos = ['I', 'II', 'III'],
    posicoes_iniciais = ['A', 'A', 'Z'], # Perto de um entalhe
    config_aneis       = ['A', 'A', 'A'],
    refletor_escolhido = 'B'
)
print(f"Configuração: I-II-III | Posições: AAZ | Anéis: AAA | Refletor: B")
cifrado = maquina_cifra.criptografar_texto(texto)
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