rotor_1 = "JGDQOXUSCAMIFRVTPNEWKBLZYH"
rotor_2 = "NTZPSFBOKMWRCJDIVLAEYUXHGQ"
rotor_3 = "JVIUBHTCDYAKEQZPOSGXNRMWFL"
refletor = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dRotor_1 = {}
dRotor_2 = {}
dRotor_3 = {}

#refletor = {"A": "","B": "","C": "","D": "","E": "","F": "","G": "","H": "","I": "","J": "","K": "","L": "","M": "","N": "","O": "","P": "","Q": "","R": "","S": "","T": "","U": "","V": "","W": "","X": "","Z":""}
crypted_txt = "OPZMUNDO"

for i in range(len(rotor_1)):
    dRotor_1.update({refletor[i]: rotor_1[i]})
    dRotor_2.update({refletor[i]: rotor_2[i]})
    dRotor_3.update({refletor[i]: rotor_3[i]})
    
print(f"rotor 1 {dRotor_1}")
print(f"rotor 2 {dRotor_2}")
print(f"rotor 3 {dRotor_3}")