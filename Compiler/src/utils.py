from src.stack import Stack

def get_postfix(expression: str):
    '''
    Funktio, joka tuottaa infix-muotoa olevasta säännöllisestä lausekkeesta postfix-muotoa olevan.

    Args:
        expression (str): säännöllinen lauseke infix-muodossa

    Returns:
        list: säännöllinen lauseke postfix-muodossa
    '''

    stack = Stack()
    postfix = []
    operator_precedence = {'|': 1, '.': 2, '*': 3, '(': 0}
    operators = ['*', '|', '.']

    for character in expression:

        if character not in operators and character != '(' and character != ')':
            postfix.append(character)
        else:
            if character == '(':
                stack.push(character)
            elif character in operators:
                stack_top_operator = stack.top()
                if stack_top_operator is None:
                    stack.push(character)
                else:
                    stack_top_operator_precedence = operator_precedence[stack_top_operator]
                    character_precedence = operator_precedence[character]
                    if stack_top_operator_precedence < character_precedence:
                        stack.push(character)
                    elif stack_top_operator_precedence >= character_precedence:
                        operator_to_postfix_queue = stack.pop()
                        postfix.append(operator_to_postfix_queue)
                        stack.push(character)
            elif character == ')':
                while True:
                    operator_to_postfix_queue = stack.pop()
                    if operator_to_postfix_queue != '(' and operator_to_postfix_queue is not None:
                        postfix.append(operator_to_postfix_queue)
                    else:
                        break

    while len(stack) > 0:
        operator_to_postfix_queue = stack.pop()
        postfix.append(operator_to_postfix_queue)

    return postfix

def validate_input(user_input: str):
    '''
    Funktio, joka tarkistaa, onko käyttäjän antama syöte on oikeaa muotoa.

    Args:
        user_input (str): käyttäjän antama syöte (säännöllinen lauseke)

    Returns:
        True, jos käyttäjän antama syöte on oikeaa muotoa. 
        Muussa tapauksessa funktio nostaa virheen (ValueError).

    '''

    for character in user_input:
        if character==' ':
            raise ValueError("Virheellinen syöte: Poista välilyönnit.")
        if character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789€|*()":
            raise ValueError("Syöte sisältää virheellisiä merkkejä.")

    p = Stack()
    if user_input == '':
        raise ValueError("Virheellinen syöte: Syöte ei voi olla tyhjä.")
    if user_input[0] in ['*', '|'] or user_input[-1] in ['(', '|']:
        raise ValueError(
            "Virheellinen ensimmäinen tai viimeinen merkki.")

    for i in range(len(user_input)):
        if user_input[i] == '(':
            if user_input[i+1] == ')' or user_input[i+1] in ['*', '|']:
                raise ValueError(
                    "Virheellinen syöte: Tarkista sulkeiden käyttö.")
            p.push(user_input[i])
        if user_input[i] == ')':
            parenthesis = p.pop()
            if parenthesis != '(':
                raise ValueError(
                    "Virheellinen syöte: Tarkista sulkeiden käyttö.")
        if user_input[i] == '*':
            if user_input[i-1] in ['*', '|', '€']:
                raise ValueError("Virheellinen tähtioperaation käyttö.")
        if user_input[i] == '|':
            if user_input[i-1] == '|' or user_input[i+1] in ['*', '|', ')']:
                raise ValueError("Virheellinen yhdisteoperaation käyttö.")

    if len(p) != 0:
        raise ValueError("Virheellinen syöte: Tarkista sulkeiden käyttö.")

    return True


def format_input_for_syntax_tree(user_input: str):
    '''
    Funktio, joka palauttaa käyttäjän antaman syötteen 
    oikeassa muodossa syntaksipuun rakentamista varten.

    Args:
        user_input (str): käyttäjän antama syöte (säännöllinen lauseke)

    Returns:
        str: käyttäjän antama syöte oikeassa muodossa syntaksipuun rakentamista varten.
    '''
    infix = '('
    for i in range(len(user_input)-1):
        infix += user_input[i]
        if user_input[i] not in ['(', '|']:
            if user_input[i+1] not in ['*', '|', ')']:
                infix += '.'

    infix += user_input[-1]
    infix += ')'
    infix += '.'
    infix += '#'

    return infix

def format_dfa_for_ui(states: list, start: list, alphabet: list, accepting: list, tran: dict):
    '''
    Funktio, joka palauttaa DFA:n käyttöliittymän tarvitsemassa muodossa ilman solmujen numeroita

    Args:
        states (list): DFA:n tilat muodossa, joka sisältää solmujen numerot
        start (list): DFA:n aloitustila muodossa, joka sisältää solmujen numerot
        alphabet (list): DFA:n aakkosto
        accepting (list): DFA:n hyväksyvät tilat muodossa, joka sisältää solmujen numerot
        tran (list): DFA:nsiirtymät muodossa, joka sisältää solmujen numerot


    Returns:
        dict: DFA käyttöliittymän tarvitsemassa muodossa tilat nimettyinä ilman solmujen numeroita
    '''

    state_numbers = {tuple(s): i + 1 for i, s in enumerate(states)}
    states_for_ui = [state_numbers[tuple(s)] for s in states]
    start_state = state_numbers[tuple(start)]
    accepting_states = [state_numbers[tuple(s)] for s in accepting]

    result = {
        "states": states_for_ui,
        "alphabet": alphabet,
        "q_0": start_state,
        "accepting_states": accepting_states,
        "transitions": get_transitions(state_numbers, tran)
    }
    return result



def get_transitions(states: dict, tran: dict):
    '''
    Funktio, joka palauttaa DFA:n siirtymät käyttöliittymän tarvitsemassa muodossa.
    
    Args:
        state_numbers (dict): DFA:n tilojen numerot ja niitä vastaavat solmujen numerot
        tran (dict): DFA:nsiirtymät muodossa, joka sisältää solmujen numerot

    Returns:
        list: DFA:n siirtymät käyttöliittymän tarvitsemassa muodossa 
        tilat nimettyinä ilman solmujen numeroita
        
    '''
    trans = []
    nodes = set()
    selfconnecting = {}
    for (from_pos, character), to_pos in tran.items():
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
