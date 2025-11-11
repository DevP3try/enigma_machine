import random

# A especificação N=52 da Tabela 1
ALFABETO_BR_52 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÁÀÂÃÇÉÊÍÓÔÕÚ .,?°:"
N = len(ALFABETO_BR_52) # N == 52

def gerar_fiacao_rotor(alfabeto: str) -> str:
    """
    Gera uma fiação de rotor válida (uma permutação aleatória simples).
    """
    lista_alfabeto = list(alfabeto)
    random.shuffle(lista_alfabeto)
    fiacao = "".join(lista_alfabeto)
    
    # Heurística simples para evitar pontos fixos (ex: A->A)
    # Embora rotores históricos pudessem ter pontos fixos, evitá-los é uma boa prática.
    fiacao_lista = list(fiacao)
    for i in range(len(alfabeto)):
        if alfabeto[i] == fiacao_lista[i]:
            # Se encontramos um ponto fixo, trocamos com o vizinho (wrap-around)
            j = (i + 1) % len(alfabeto)
            fiacao_lista[i], fiacao_lista[j] = fiacao_lista[j], fiacao_lista[i]
            
    return "".join(fiacao_lista)

def gerar_fiacao_refletor(alfabeto: str) -> str:
    """
    Gera uma fiação de refletor válida (uma involução sem pontos fixos).
    Isto é composto de N/2 pares de troca (ex: A->Y, Y->A).
    """
    if len(alfabeto) % 2!= 0:
        raise ValueError("O alfabeto do refletor DEVE ser de tamanho par.")
    
    indices = list(range(len(alfabeto)))
    random.shuffle(indices)
    
    fiacao = [''] * len(alfabeto) # Array de saída
    
    # Itera pelos índices embaralhados, pegando-os em pares
    for i in range(0, len(alfabeto), 2):
        idx1 = indices[i]
        idx2 = indices[i+1]
        
        char1 = alfabeto[idx1]
        char2 = alfabeto[idx2]
        
        # Aplica a troca recíproca:
        fiacao[idx1] = char2
        fiacao[idx2] = char1
        
    return "".join(fiacao)

print("--- NOVOS COMPONENTES ENIGMA-BR-52 (N=52) ---")

# Gerar novos Rotores I-V e seus entalhes (Notches)
# O entalhe pode ser qualquer caractere do alfabeto
print("\nROTOR_DATA = {")
for rotor_nome in ['I', 'II', 'III', 'IV', 'V']:
    fiacao = gerar_fiacao_rotor(ALFABETO_BR_52)
    entalhe = random.choice(ALFABETO_BR_52)
    print(f"    '{rotor_nome}': ('{fiacao}', '{entalhe}'),")
print("}")

# Gerar novos Refletores B e C
print("\nREFLECTOR_DATA = {")
for refletor_nome in ['B', 'C']:
    fiacao = gerar_fiacao_refletor(ALFABETO_BR_52)
    print(f"    '{refletor_nome}': '{fiacao}',")
print("}")