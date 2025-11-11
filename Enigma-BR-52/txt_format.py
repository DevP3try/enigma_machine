import unicodedata
import re

# ==========================
# CONSTANTES
# ==========================
ALFABETO_BR_52 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÁÀÂÃÇÉÊÍÓÔÕÚ .,?°:"
ROTORES_VALIDOS = ["I", "II", "III", "IV", "V"]
REFLETORES_VALIDOS = ["B", "C"]


# ==========================
# FORMATADORES
# ==========================
def format_txt(texto: str) -> str:

    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('ascii').upper()
    texto_limpo = "".join(c for c in texto if c in ALFABETO_BR_52)
    return texto_limpo

def format_plug(plug_str: str) -> str:
    """ Transforma a configuração do plugboard em uma string formatada e valida duplicidade e pares inválidos.
    Cada par deve consistir de duas letras distintas do alfabeto, sem repetições. """
    plugs = plug_str.upper().split()
    plug_dict = {}
    todas_letras = set()
    for par in plugs:
        if len(par) != 2 or not all(c in ALFABETO_BR_52 for c in par):
            raise ValueError("ERRO: Cada par de plugboard deve ter exatamente 2 letras distintas.")
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

def format_rotores(rotor_str: str) -> list:
    """
    Processa o rotores escolhidos, removendo espaços e convertendo para maiúsculo.
    """
    
    rotor_str = rotor_str.upper().split(' ')
    
    return list(rotor_str)

def format_pos_inicial(pos_inicial_str: str) -> list[str]:
    """
    Processa a posição inicial em uma lista de exatamente 3 letras.
    """
    pos_inicial_str = pos_inicial_str.upper().strip()
    if len(pos_inicial_str) != 3 or not all(c in ALFABETO_BR_52 for c in pos_inicial_str):
        raise ValueError("ERRO: Posição inicial deve ter exatamente 3 letras de A-Z.")
    return list(pos_inicial_str)

def format_config_aneis(config_str: str) -> list[str]:
    """
    Processa a configuração dos anéis em uma lista de exatamente 3 letras.
    """
    config_str = config_str.upper().strip()
    if len(config_str) != 3 or not all(c in ALFABETO_BR_52 for c in config_str):
        raise ValueError("ERRO: Configuração dos anéis deve ter exatamente 3 letras de A-Z.")
    return list(config_str)

def format_refletor_escolhido(refletor_str: str) -> str:
    """
    Processa o refletor escolhido, removendo espaços e convertendo para maiúsculo.
    """
    return refletor_str.strip().upper()
