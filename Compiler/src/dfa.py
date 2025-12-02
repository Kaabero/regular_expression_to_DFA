class DFA:
    '''
    Luokka kuvaa determinististä automaattia (DFA), joka on rakennettu syntaksipuun perusteella. 

    Attribuutit:
        syntax_tree (dict): syntaksipuun tiedot
        states (list): DFA:n tilat
        tran (dict): DFA:n siirtymät
        start_state (list): DFA:n alkutila
        accepting_states (list): DFA:n hyväksyvät tilat
        alphabet (list): DFA:n aakkosto
        accepting_position (int | None): syntaksipuussa hyväksyvän merkin # paikka
    '''

    def __init__(self, syntax_tree: dict, start_state: list):
        '''
        Luokan konstruktori, joka luo uuden DFA:n.

        Args:
            syntax_tree (dict): syntaksipuun tiedot
            start_state (list): DFA:n alkutila
        '''
        self.syntax_tree = syntax_tree
        self.states = [start_state]
        self.tran = {}
        self.start_state = start_state
        self.accepting_states = []
        self.alphabet = []
        self.accepting_position = None
        for node in syntax_tree:
            if syntax_tree[node]['character'] not in ['#', '€']:
                if syntax_tree[node]['character'] not in self.alphabet:
                    self.alphabet.append(syntax_tree[node]['character'])
            elif syntax_tree[node]['character'] =='#':
                self.accepting_position=node

    def get_transitions(self, states: dict):
        '''
        Metodi, joka palauttaa DFA:n siirtymät käyttöliittymän tarvitsemassa muodossa
        
        '''
        trans = []
        nodes = set()
        selfconnecting = {}
        for (from_pos, character), to_pos in self.tran.items():
            nodes.add((states[tuple(from_pos)], states[tuple(to_pos)]))

            if states[tuple(from_pos)] == states[tuple(to_pos)]:
                if (states[tuple(from_pos)], states[tuple(to_pos)]) not in selfconnecting:
                    selfconnecting[(states[tuple(from_pos)], states[tuple(to_pos)])]=[]
                selfconnecting[(states[tuple(from_pos)], states[tuple(to_pos)])].append(character)
                trans.append({
                    "from": states[tuple(from_pos)],
                    "character": character,
                    "to": states[tuple(to_pos)],
                    "type": 'selfconnecting',
                    "labels": []
                })
            elif  (states[tuple(to_pos)], states[tuple(from_pos)]) in nodes:
                trans.append({
                    "from": states[tuple(from_pos)],
                    "character": character,
                    "to": states[tuple(to_pos)],
                    "type": 'bidirectional'
                })
            else:
                trans.append({
                    "from": states[tuple(from_pos)],
                    "character": character,
                    "to": states[tuple(to_pos)],
                    "type": 'default'
        })
        for i in range(len(trans)):
            if trans[i]['type'] == 'selfconnecting':
                trans[i]['labels'] = selfconnecting[(trans[i]['from'], trans[i]['to'])]
            else:
                for j in range(i+1, len(trans)):
                    if trans[i]['from'] ==trans[j]['from'] and trans[i]['to'] ==trans[j]['to']:
                        if 'labels' not in trans[i]:
                            trans[i]['labels']=[]
                        if 'labels' not in trans[j]:
                            trans[j]['labels']=[]
                        if trans[i]['character'] not in trans[i]['labels']:
                            trans[i]['labels'].append(trans[i]['character'])
                        if trans[j]['character'] not in trans[i]['labels']:
                            trans[i]['labels'].append(trans[j]['character'])
                        if trans[i]['character'] not in trans[j]['labels']:
                            trans[j]['labels'].append(trans[i]['character'])
                        if trans[j]['character'] not in trans[j]['labels']:
                            trans[j]['labels'].append(trans[j]['character'])
        return trans


    def build_dfa(self):
        '''
        Metodi, joka rakentaa DFA:n ja palauttaa sen sanakirjamuodossa
        
        '''
        self.add_tran(self.start_state)
        for state in self.states:
            if self.accepting_position in state:
                self.accepting_states.append(state)
        states = {tuple(s): i + 1 for i, s in enumerate(self.states)}
        self.states = [states[tuple(s)] for s in self.states]
        self.start_state = states[tuple(self.start_state)]
        self.accepting_states = [states[tuple(s)] for s in self.accepting_states]

        result = {
            "states": self.states,
            "alphabet": self.alphabet,
            "q_0": self.start_state,
            "accepting_states": self.accepting_states,
            "transitions": self.get_transitions(states)
        }
        return result

    def add_tran(self, positions: list):
        '''
        Metodi, joka muodostaa DFA:n tilat ja lisää jokaiseen tilaan aakkoston mukaiset siirtymät.

        Args:
            positions (list): Vuorossa oleva DFA:n tila

        '''
        for character in self.alphabet:
            tran_state = []

            for position in positions:
                if self.syntax_tree[position]['character'] == character:
                    for number in self.syntax_tree[position]['followpos']:
                        if number not in tran_state:
                            tran_state.append(number)
            tran_state.sort()
            self.tran[tuple(positions), character] = tran_state

            if tran_state not in self.states:
                self.states.append(tran_state)
                self.add_tran(tran_state)
