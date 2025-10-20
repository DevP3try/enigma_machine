import unicodedata
import re

# ==========================
# CONSTANTES
# ==========================
ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTORES_VALIDOS = ["I", "II", "III", "IV", "V"]
REFLETORES_VALIDOS = ["B", "C"]
# Rotores padrão usados automaticamente

# ==========================
# FORMATADORES
# ==========================
def format_txt(texto: str) -> str:
    """
    Remove acentos, caracteres especiais e retorna texto maiúsculo contendo apenas letras A-Z.
    """
    # Normaliza para decompor acentos e remove caracteres não-ASCII
    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('ascii')
    # Remove tudo que não for letra e converte para maiúsculo
    texto = re.sub(r'[^A-Za-z]', '', texto).upper()
    return texto

def format_plug(plug_str: str) -> str:
    """ Transforma a configuração do plugboard em uma string formatada e valida duplicidade e pares inválidos.
    Cada par deve consistir de duas letras distintas do alfabeto, sem repetições. """
    plugs = plug_str.upper().split()
    plug_dict = {}
    todas_letras = set()
    for par in plugs:
        if len(par) != 2 or not all(c in ALFABETO for c in par):
            raise ValueError("ERRO: Cada par de plugboard deve ter exatamente 2 letras distintas de A-Z.")
        a, b = par[0], par[1]
        if a == b:
            raise ValueError("ERRO: Pares de plugboard devem ser letras distintas.")
        if a in todas_letras or b in todas_letras:
            raise ValueError("ERRO: Letras duplicadas no plugboard não são permitidas.")
        plug_dict[a] = b
        plug_dict[b] = a
        todas_letras.update([a, b])
    # Retorna uma string formatada com os pares
    return " ".join(sorted([f"{a}{b}" for a, b in plug_dict.items() if a < b]))


def format_pos_inicial(pos_inicial_str: str) -> list[str]:
    """
    Processa a posição inicial em uma lista de exatamente 3 letras.
    """
    pos_inicial_str = pos_inicial_str.upper().strip()
    if len(pos_inicial_str) != 3 or not all(c in ALFABETO for c in pos_inicial_str):
        raise ValueError("ERRO: Posição inicial deve ter exatamente 3 letras de A-Z.")
    return list(pos_inicial_str)

def format_config_aneis(config_str: str) -> list[str]:
    """
    Processa a configuração dos anéis em uma lista de exatamente 3 letras.
    """
    config_str = config_str.upper().strip()
    if len(config_str) != 3 or not all(c in ALFABETO for c in config_str):
        raise ValueError("ERRO: Configuração dos anéis deve ter exatamente 3 letras de A-Z.")
    return list(config_str)

def format_refletor_escolhido(refletor_str: str) -> str:
    """
    Processa o refletor escolhido, removendo espaços e convertendo para maiúsculo.
    """
    return refletor_str.strip().upper()

# ==========================
# VALIDADORES
# ==========================
def validar_txt(txt: str) -> None:
    """
    Valida se o texto contém apenas letras do alfabeto A-Z.
    """
    if not txt or not all(letra in ALFABETO for letra in txt):
        raise ValueError("ERRO: O texto inserido não é válido. Reescreva seguindo as regras:\n- Somente letras A-Z\n- Sem acentos ou caracteres especiais")
    
def validar_rotores(rotores: list[str]) -> None:
    """ Valida se os rotores estão na lista de válidos e se há exatamente 3. """
    if len(rotores) != 3:
        raise ValueError("ERRO: Devem ser exatamente 3 rotores.")
    for rotor in rotores:
        if rotor not in ROTORES_VALIDOS:
            raise ValueError(f"ERRO: Rotor '{rotor}' inválido. Use apenas {ROTORES_VALIDOS}.")

def validar_pos_inicial(pos_inicial: list[str]) -> None:
    """
    Valida se a posição inicial contém apenas letras do alfabeto.
    (Nota: A validação principal já é feita em format_pos_inicial, mas mantida para consistência.)
    """
    if not all(letra in ALFABETO for letra in pos_inicial):
        raise ValueError("ERRO: Posição inicial inválida. Use apenas letras do alfabeto A-Z.")

def validar_aneis(aneis: list[str]) -> None:
    """
    Valida se a configuração dos anéis contém apenas letras do alfabeto.
    (Nota: A validação principal já é feita em format_config_aneis, mas mantida para consistência.)
    """
    if not all(letra in ALFABETO for letra in aneis):
        raise ValueError("ERRO: Configuração de anéis inválida. Use apenas letras do alfabeto A-Z.")

def validar_refletor(refletor: str) -> None:
    """
    Valida se o refletor está na lista de válidos.
    """
    if refletor not in REFLETORES_VALIDOS:
        raise ValueError(f"ERRO: Refletor '{refletor}' inválido. Use apenas {REFLETORES_VALIDOS}.")
    
    

# ==========================
# PROGRAMA PRINCIPAL
# ==========================
def main() -> None:
    """
    Função principal que coleta entradas do usuário, formata, valida e exibe as configurações.
    Os rotores são definidos automaticamente como padrão (I, II, III).
    Nota: Esta implementação valida e configura a máquina Enigma, mas não realiza a criptografia real.
    """
    try:
        # Entrada de texto
        texto_usuario = input("Digite o texto a ser criptografado: ").strip()
        txt_to_crypt = format_txt(texto_usuario)
        validar_txt(txt_to_crypt)

        # Plugboard
        plug_input = input("Configuração do plugboard (ex: 'HK LP JB AZ FI'): ").strip()
        plugboard = format_plug(plug_input)

        # Rotores (definidos automaticamente como padrão)
        pos_rotores = input("Rotores escolhidos (padrão 'I II III'): ").strip()
        validar_rotores(pos_rotores)

        # Posição inicial
        pos_inicial_input = input("Posição inicial (ex: 'AAZ'): ").strip()
        pos_inicial = format_pos_inicial(pos_inicial_input)
        validar_pos_inicial(pos_inicial)

        # Anéis
        config_aneis_input = input("Configuração dos anéis (ex: 'AAA'): ").strip()
        config_aneis = format_config_aneis(config_aneis_input)
        validar_aneis(config_aneis)

        # Refletor
        refletor_input = input("Refletor escolhido (B ou C): ").strip()
        refletor = format_refletor_escolhido(refletor_input)
        validar_refletor(refletor)

        # Saída limpa
        print("\nCONFIGURAÇÃO DA MÁQUINA ENIGMA VALIDADA COM SUCESSO!")
        print("\nTEXTO PARA CRIPTOGRAFAR:")
        print(txt_to_crypt)
        print("\nPLUGBOARD CONFIGURADO:")
        if plugboard:
            print(plugboard)
        else:
            print("Nenhum plug configurado.")
        print(f"\nROTORES CONFIGURADOS (padrão): {' '.join(pos_rotores)}")

    except ValueError as erro:
        print(f"\n{erro}")
    except Exception as erro:
        print(f"\nERRO INESPERADO: {erro}")

if __name__ == "__main__":
    main()
