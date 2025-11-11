ALFABETO_BR_52 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÁÀÂÃÇÉÊÍÓÔÕÚ.,?"
ROTORES_VALIDOS = ["I", "II", "III", "IV", "V"]
REFLETORES_VALIDOS = ["B", "C"]
ROTORES_PADRAO = ["I", "II", "III"]  # Rotores padrão usados automaticamente


# ==========================
# VALIDADORES
# ==========================
def validar_txt(txt: str) -> None:
    """
    Valida se o texto contém apenas letras do alfabeto A-Z.
    """
    if not txt or not all(letra in ALFABETO_BR_52 for letra in txt):
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
    if not all(letra in ALFABETO_BR_52 for letra in pos_inicial):
        raise ValueError("ERRO: Posição inicial inválida. Use apenas letras do alfabeto A-Z.")

def validar_aneis(aneis: list[str]) -> None:
    """
    Valida se a configuração dos anéis contém apenas letras do alfabeto.
    (Nota: A validação principal já é feita em format_config_aneis, mas mantida para consistência.)
    """
    if not all(letra in ALFABETO_BR_52 for letra in aneis):
        raise ValueError("ERRO: Configuração de anéis inválida. Use apenas letras do alfabeto A-Z.")

def validar_refletor(refletor: str) -> None:
    """
    Valida se o refletor está na lista de válidos.
    """
    if refletor not in REFLETORES_VALIDOS:
        raise ValueError(f"ERRO: Refletor '{refletor}' inválido. Use apenas {REFLETORES_VALIDOS}.")
    
    
