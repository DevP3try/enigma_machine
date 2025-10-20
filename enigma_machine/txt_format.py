import unicodedata
import re

# ==========================
# CONSTANTES
# ==========================
ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTORES_VALIDOS = ["I", "II", "III", "IV", "V"]
REFLETORES_VALIDOS = ["B", "C"]
ROTORES_PADRAO = ["I", "II", "III"]  # Rotores padrão usados automaticamente

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
