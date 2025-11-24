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
