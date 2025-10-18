class Rotor:
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ROTOR_DATA = {
        # Dic   Fiação             Entalhe (Notch)
        'I':   ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q'),
        'II':  ("AJDKSIRUXBLHWTMCQGZNPYFVOE", 'E'),
        'III': ("BDFHJLCPRTXVZNYEIWGAKMUSQO", 'V'),
        'IV':  ("ESOVPZJAYQUIRHXLNFTGKDCMWB", 'J'),
        'V':   ("VZBRGITYUPSDNHLXAWMJQOFECK", 'Z')
    }

    # Dic Tipos de Refletores B e C
    REFLECTOR_DATA = {
        'B': "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        'C': "FVPJIAOYEDRZXWGCTKUQSBNMHL"
    }
    #Ao Chamar a classe deve executar o init (inicializacao)
    #Init Requisita as informacoes (quais rotores escolhidos, qual a posiciao inicial de cada um, a config dos aneis e qual refletor escolhido)
    #A primeira configuracao da maquina
    def __init__(self, rotores_escolhidos, posicoes_iniciais, config_aneis, refletor_escolhido):
        """
        rotores_escolhidos = ['I', 'II', 'III'] (Lento, Meio, Rápido)
        posicoes_iniciais = ['A', 'A', 'A'] (O que você vê na janela)
        config_aneis = ['A', 'A', 'A'] (O Ring Setting)
        refletor_escolhido = 'B'
        """

        self.rotores = []  # Armazena os dicionários de mapeamento
        self.rotores_inv = [] # Armazena os mapeamentos inversos
        self.entalhes = [] # Armazena as posições dos entalhes
        
        # determina as posições atuais dos rotores 'A' -> 0, 'B' -> 1
        self.posicoes = [self.ALFABETO.find(p) for p in posicoes_iniciais]
        
        # determina a configuração atual dos anéis 'A' -> 0, 'B' -> 1
        self.aneis = [self.ALFABETO.find(a) for a in config_aneis]
        
        # configura os 3 rotores da esquerda para a direita
        for nome_rotor in rotores_escolhidos:
            fio, notch = self.ROTOR_DATA[nome_rotor]
            
            # mapeamento de ida 
            self.rotores.append({self.ALFABETO[i]: fio[i] for i in range(26)})
            
            # mapeamento de volta 
            self.rotores_inv.append({fio[i]: self.ALFABETO[i] for i in range(26)})
            
            # posição do notch 'Q' -> 16
            self.entalhes.append(self.ALFABETO.find(notch))

        # configura o refletor
        fio_refletor = self.REFLECTOR_DATA[refletor_escolhido]
        self.refletor = {self.ALFABETO[i]: fio_refletor[i] for i in range(26)} 
        
    def rotacionar_rotores(self):
        """
        Implementa a lógica de rotação completa, incluindo o passo duplo
        Os rotores são [0: Lento, 1: Meio, 2: Rápido]
        """
        
        # 1. Verificar se o Rotor 2 (meio) está no entalhe
        r2_no_entalhe = (self.posicoes[1] == self.entalhes[1]) # True or False que esta no entalhe 
        
        # 2. Verificar se o Rotor 1 (rápido) está no entalhe
        r1_no_entalhe = (self.posicoes[2] == self.entalhes[2]) # True or False que esta no entalhe 

        '''
          #logica que gira 
            self.pos = [0, 1, 2] # lembrando que foi mapeado anteriormente A -> 0, B -> 1 ...
            rotores_escolhidos = ['I', 'II', 'III'] # (Lento, Meio, Rápido)  entao self.pos[2] e o rotor rapido
            self.posicoes[2] = (self.posicoes[2] + 1) % 26 # define em posicoes[2] Ex: (4 + 1) % 26 = 5
            
            Rotor 1 (self.posicoes[2]) SEMPRE gira
            Rotor 2 (self.posicoes[1]) gira somente se rotor
        '''
        
        # O Rotor 1 (rápido) SEMPRE gira
        self.posicoes[2] = (self.posicoes[2] + 1) % 26 
        
        if r2_no_entalhe:
            # Caso do Passo Duplo: Rotor 2 está no entalhe.
            # Ele gira, e faz o Rotor 3 (lento) girar também.
            self.posicoes[1] = (self.posicoes[1] + 1) % 26 # rotor 2 (medio)
            self.posicoes[0] = (self.posicoes[0] + 1) % 26 # rotor 3 (lento)
            
        elif r1_no_entalhe:
            # Caso normal: Rotor 1 atingiu seu entalhe.
            # Ele faz o Rotor 2 (meio) girar.
            self.posicoes[1] = (self.posicoes[1] + 1) % 26 # rotor 2 (medio)
            
    def passar_pelo_rotor(self, char_idx, id_rotor, reverso=False):
        """
        Calcula a passagem do sinal por um único rotor, 
        considerando a posição e a configuração do anel.
        """
        # Posição do rotor (Ex: 'C' -> 2)
        pos = self.posicoes[id_rotor]
        # Configuração do anel (Ex: 'B' -> 1)
        anel = self.aneis[id_rotor]
        
        # 1. Deslocamento de entrada (Posição - Anel)
        deslocamento = pos - anel
        
        # 2. Ajusta o índice de entrada com o deslocamento
        # (O +26 é para garantir que o módulo de um numero negativo funcione)
        idx_entrada = (char_idx + deslocamento + 26) % 26
        
        # 3. Passa pela fiação (ida ou volta)
        if not reverso:
            mapa = self.rotores[id_rotor]
            char_saida = mapa[self.ALFABETO[idx_entrada]]
        else:
            mapa_inv = self.rotores_inv[id_rotor]
            char_saida = mapa_inv[self.ALFABETO[idx_entrada]]
            
        idx_saida_fio = self.ALFABETO.find(char_saida)
        
        # 4. Remove o deslocamento na saída[]
        idx_final = (idx_saida_fio - deslocamento + 26) % 26
        
        return idx_final
    
    def criptografar_letra(self, letra):
        """Criptografa uma única letra"""
        
        # 1. Rotacionar os rotores ANTES de criptografar
        self.rotacionar_rotores()
        
        idx = self.ALFABETO.find(letra)
        
        # 2. Caminho de IDA (Rápido -> Meio -> Lento)
        # (Note que os rotores estão na ordem [Lento, Meio, Rápido] 
        #  em nossas listas, então passamos 2, 1, 0)
        idx = self.passar_pelo_rotor(idx, 2, reverso=False) # Rotor Rápido (III)
        idx = self.passar_pelo_rotor(idx, 1, reverso=False) # Rotor Meio (II)
        idx = self.passar_pelo_rotor(idx, 0, reverso=False) # Rotor Lento (I)
        
        # 3. Refletor
        char_refletido = self.refletor[self.ALFABETO[idx]]
        idx = self.ALFABETO.find(char_refletido)
        
        # 4. Caminho de VOLTA (Lento -> Meio -> Rápido)
        idx = self.passar_pelo_rotor(idx, 0, reverso=True) # Rotor Lento (I)
        idx = self.passar_pelo_rotor(idx, 1, reverso=True) # Rotor Meio (II)
        idx = self.passar_pelo_rotor(idx, 2, reverso=True) # Rotor Rápido (III)
        
        return self.ALFABETO[idx]

    def criptografar_texto(self, texto):
        """Criptografa uma string completa"""
        texto_cifrado = ""
        for letra in texto:
            if letra in self.ALFABETO:
                texto_cifrado += self.criptografar_letra(letra)
            # (ignora espaços, números, etc.)
        return texto_cifrado