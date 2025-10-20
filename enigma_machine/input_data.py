import txt_format as format
import validation as val




def input_data_txt(txt):
    txt_to_crypt = format.format_txt(txt)
    val.validar_txt(txt)
    return txt_to_crypt





def testes():
    print(input_data_txt('CARALHOOOOOO'))

testes()


