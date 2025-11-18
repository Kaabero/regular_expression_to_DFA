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

        transitions = []
        for (from_positions, character), to_positions in self.tran.items():
            transitions.append({
                "from": states[tuple(from_positions)],
                "character": character,
                "to": states[tuple(to_positions)]
        })


        result = {
            "states": self.states,
            "alphabet": self.alphabet,
            "q_0": self.start_state,
            "accepting_states": self.accepting_states,
            "transitions": transitions
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
