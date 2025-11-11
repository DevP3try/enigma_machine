class Rotor:
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ÁÀÂÃÇÉÊÍÓÔÕÚ .,?°:"
    N = len(ABC)  # Tamanho do alfabeto
    
    ROTOR_DATA = { # Dic Tipos de Rotores I a V ADAPTADOS PARA N=54
    'I': ('ÕFXÚIY,VMÊ3Á5ÍN2ÀPQ:ÂLK6B4A0CWSÓ71Z?JHEÔ.Ç9U8R°OD GÃÉT', '°'),
    'II': ('PA?OY C9LÃXTÊRÓGÁMWÚBÍ0HJV83UNQ°7.:ÔÕK1SÉÇ2ZÀ6,I4E5DFÂ', 'L'),
    'III': ('° A,LÍWÔVÉ60T2GB1Ã4Q:C7P3HKO?ÂÕÀJ8MÇSUZ5ÚY9Á.ÓFXRÊNEID', 'M'),
    'IV': ('WAK7CÚ?,LHFÔRXN3É9641ODBÍÇSÂÁT5:GUPIÊÓ2°ÃQ8VÕEZÀY0. JM', 'A'),
    'V': ('GÚO.ÔLCV?ÊQ°1Á8:B9ÓÃK37HFÉÂSTZÇE2,U6YXÕDI4 MJWR50ÀAÍPN', 'Í'),
    }

    # Dic Tipos de Refletores B e C ADAPTADOS PARA N=54
    REFLECTOR_DATA = {
    'B': 'Ú9T6U?MÁÀÍÕSGÂ.W51LCEÊPÓ3°:RÃY QD,ÉBHIN2Ô8VJXÇKA4O7FZ0',
    'C': 'L2 .ÍGF5QNÕA,JTÓIW?OY7R8UÁ9ÚBÉ:H°VX0ZÊÃÂÔ3ÀEPÇK1CDMS64',
    }
    
    def __init__(self, rotores_escolhidos, posicoes_iniciais, config_aneis, refletor_escolhido):

        self.rotores = []  # Armazena os dicionários de mapeamento
        self.rotores_inv = [] # Armazena os mapeamentos inversos
        self.entalhes = [] # Armazena as posições dos entalhes
        
        # determina as posições atuais dos rotores 'A' -> 0, 'B' -> 1
        self.posicoes = [self.ABC.find(p) for p in posicoes_iniciais]
        
        # determina a configuração atual dos anéis 'A' -> 0, 'B' -> 1
        self.aneis = [self.ABC.find(a) for a in config_aneis]
        
        # configura os 3 rotores da esquerda para a direita
        for nome_rotor in rotores_escolhidos:
            fio, notch = self.ROTOR_DATA[nome_rotor]
            
            # mapeamento de ida 
            self.rotores.append({self.ABC[i]: fio[i] for i in range(self.N)})
            
            # mapeamento de volta 
            self.rotores_inv.append({fio[i]: self.ABC[i] for i in range(self.N)})
            
            # posição do notch 'Q' -> 16
            self.entalhes.append(self.ABC.find(notch))

        # configura o refletor
        fio_refletor = self.REFLECTOR_DATA[refletor_escolhido]
        self.refletor = {self.ABC[i]: fio_refletor[i] for i in range(self.N)} 
        
    def rotacionar_rotores(self):
        
        # 1. Verificar se o Rotor 2 (meio) está no entalhe
        r2_no_entalhe = (self.posicoes[1] == self.entalhes[1]) # True or False que esta no entalhe 
        
        # 2. Verificar se o Rotor 1 (rápido) está no entalhe
        r1_no_entalhe = (self.posicoes[2] == self.entalhes[2]) # True or False que esta no entalhe 

        # O Rotor 1 (rápido) SEMPRE gira
        self.posicoes[2] = (self.posicoes[2] + 1) % self.N 
        
        if r2_no_entalhe:
            # Caso do Passo Duplo: Rotor 2 está no entalhe.
            # Ele gira, e faz o Rotor 3 (lento) girar também.
            self.posicoes[1] = (self.posicoes[1] + 1) % self.N # rotor 2 (medio)
            self.posicoes[0] = (self.posicoes[0] + 1) % self.N # rotor 3 (lento)
            
        elif r1_no_entalhe:
            # Caso normal: Rotor 1 atingiu seu entalhe.
            # Ele faz o Rotor 2 (meio) girar.
            self.posicoes[1] = (self.posicoes[1] + 1) % self.N # rotor 2 (medio)
            
    def passar_pelo_rotor(self, char_idx, id_rotor, reverso=False):
        # Posição do rotor (Ex: 'C' -> 2)
        pos = self.posicoes[id_rotor]
        # Configuração do anel (Ex: 'B' -> 1)
        anel = self.aneis[id_rotor]
        
        # 1. Deslocamento de entrada (Posição - Anel)
        deslocamento = pos - anel
        
        # 2. Ajusta o índice de entrada com o deslocamento
        # (O +26 é para garantir que o módulo de um numero negativo funcione)
        idx_entrada = (char_idx + deslocamento + self.N) % self.N
        
        # 3. Passa pela fiação (ida ou volta)
        if not reverso:
            mapa = self.rotores[id_rotor]
            char_saida = mapa[self.ABC[idx_entrada]]
        else:
            mapa_inv = self.rotores_inv[id_rotor]
            char_saida = mapa_inv[self.ABC[idx_entrada]]
            
        idx_saida_fio = self.ABC.find(char_saida)
        
        # 4. Remove o deslocamento na saída[]
        idx_final = (idx_saida_fio - deslocamento + self.N) % self.N
        
        return idx_final
    
    def criptografar_letra(self, letra):
        """Criptografa uma única letra"""
        
        # 1. Rotacionar os rotores ANTES de criptografar
        self.rotacionar_rotores()
        
        idx = self.ABC.find(letra)
        
        # 2. Caminho de IDA (Rápido -> Meio -> Lento)
        # (Note que os rotores estão na ordem [Lento, Meio, Rápido] 
        #  em nossas listas, então passamos 2, 1, 0)
        idx = self.passar_pelo_rotor(idx, 2, reverso=False) # Rotor Rápido (III)
        idx = self.passar_pelo_rotor(idx, 1, reverso=False) # Rotor Meio (II)
        idx = self.passar_pelo_rotor(idx, 0, reverso=False) # Rotor Lento (I)
        
        # 3. Refletor
        char_refletido = self.refletor[self.ABC[idx]]
        idx = self.ABC.find(char_refletido)
        
        # 4. Caminho de VOLTA (Lento -> Meio -> Rápido)
        idx = self.passar_pelo_rotor(idx, 0, reverso=True) # Rotor Lento (I)
        idx = self.passar_pelo_rotor(idx, 1, reverso=True) # Rotor Meio (II)
        idx = self.passar_pelo_rotor(idx, 2, reverso=True) # Rotor Rápido (III)
        
        return self.ABC[idx]

    def criptografar_texto(self, texto):
        """Criptografa uma string completa"""
        texto_cifrado = ""
        for letra in texto:
            if letra in self.ABC:
                texto_cifrado += self.criptografar_letra(letra)
        return texto_cifrado