import txt_format as format
import validation as val




def input_txt(txt):
    txt_to_crypt = format.format_txt(txt)
    val.validar_txt(txt_to_crypt)
    return txt_to_crypt

def input_plugboard(plug_str):
    plugboard = format.format_plug(plug_str)
    return plugboard

def input_rotores(rotores):
    rotores = format.format_rotores(rotores) # NECESSARIO IMPLEMENTAR AINDA
    val.validar_rotores(rotores)
    return rotores


def input_pos_inicial(pos_inicial_str):
    pos_inicial = format.format_pos_inicial(pos_inicial_str)
    val.validar_pos_inicial(pos_inicial)
    return pos_inicial

def input_config_aneis(config_str):
    config_str = format.format_config_aneis(config_str)
    val.validar_aneis(config_str)
    return config_str

def input_refletor(refletor):
    refletor = format.format_refletor_escolhido(refletor)
    val.validar_refletor(refletor)
    return refletor


def testes():
    print(input_txt('Willian 123!@# Caso de Teste.'))
    print(input_txt('Hello, World! This is a Test 456.'))

    print(input_rotores('I II III'))
    print(input_rotores('IV V I'))

    plugboard = input_plugboard('AB CD EF GH IJ')
    print(plugboard)
    
    print(input_pos_inicial('AAA'))
    print(input_pos_inicial('XYZ'))
    print("=========================")
    print(input_config_aneis('AAA'))
    print(input_config_aneis('MNO'))

    print(input_refletor('B'))
    print(input_refletor('C'))




