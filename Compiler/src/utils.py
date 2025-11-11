from src.node import Node
from src.stack import Stack


def get_child_number(character: str):
    '''
    Funktio, joka palauttaa syntaksipuussa olevan solmun 
    (säännöllisen lausekkeen operaattorin tai operandin) tarvittavien lasten määrän

    Args:
        character (str): solmun arvo (säännöllisen lausekkeen operandi tai operaattori)

    Returns:
        int: solmun tarvittavien lasten määrä
    '''
    if character in ['|', '.']:
        return 2
    if character == '*':
        return 1
    return 0


def has_all_children(node: Node):
    '''
    Funktio, joka kertoo, onko solmulla jo tarvittava määrä lapsia

    Args:
        node (Node): tarkasteltava solmu

    Returns:
        boolean: palauttaa True vain, jos solmulla on jo tarvittava määrä lapsia
    '''
    if node.character not in ['|', '.', '*']:
        return True
    if node.character == '*' and node.left is not None:
        return True
    if node.character in ['|', '.'] and node.left is not None and node.right is not None:
        return True
    return False


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


def get_nullable(node: Node):
    '''
    Funktio, joka palauttaa True mikäli solmun edustama osalauseke voi tuottaa tyhjän merkkijonon.

    Args:
        node (Node): tarkasteltava solmu

    '''
    if node.character in ['€', '*']:
        return True
    if node.character == '.':
        return get_nullable(node.left) and get_nullable(node.right)
    if node.character == '|':
        return get_nullable(node.left) or get_nullable(node.right)

    return False


def get_firstpos(node: Node):
    '''
    Funktio, joka palauttaa ne lehtisolmut, 
    jotka voivat olla ensimmäisiä merkkejä solmun tuottamissa merkkijonoissa.

    Args:
        node (Node): tarkasteltava solmu

    Returns:
        list:   Joukko lehtisolmuja, jotka voivat olla 
                ensimmäisiä merkkejä solmun tuottamissa merkkijonoissa.

    '''
    if node.character == '€':
        return []
    if node.character == '|':
        left = get_firstpos(node.left)
        right = get_firstpos(node.right)
        return left + right
    if node.character == '.':
        if get_nullable(node.left):
            left = get_firstpos(node.left)
            right = get_firstpos(node.right)
            return left + right
        return get_firstpos(node.left)

    if node.character == '*':
        return get_firstpos(node.left)

    return [node]


def get_lastpos(node: Node):
    '''
    Funktio, joka palauttaa ne lehtisolmut, 
    jotka voivat olla viimeisiä merkkejä solmun tuottamissa merkkijonoissa.

    Args:
        node (Node): tarkasteltava solmu

    Returns:
        list: Joukko lehtisolmuja, 
        jotka voivat olla viimeisiä merkkejä solmun tuottamissa merkkijonoissa.
    '''
    if node.character == '€':
        return []
    if node.character == '|':
        left = get_lastpos(node.left)
        right = get_lastpos(node.right)
        return left + right
    if node.character == '.':
        if get_nullable(node.right):
            left = get_lastpos(node.left)
            right = get_lastpos(node.right)
            return left + right
        return get_lastpos(node.right)

    if node.character == '*':
        return get_lastpos(node.left)

    return [node]


def get_followpos(node: Node):
    '''
    Funktio, joka asettaa solmun followpos arvoksi listan niistä lehtisolmuista, 
    jotka voivat seurata kyseistä solmua lausekkeen mahdollisissa merkkijonoissa.

    Args:
        node (Node): tarkasteltava solmu

    '''

    if node.character == '.':

        for n in node.left.lastpos:
            n.followpos += node.right.firstpos

    elif node.character == '*':
        for n in node.lastpos:
            n.followpos += node.firstpos


def validate_input(user_input: str):
    '''
    Funktio, joka tarkistaa, onko käyttäjän antama syöte on oikeaa muotoa.

    Args:
        user_input (str): käyttäjän antama syöte (säännöllinen lauseke)

    Returns:
        True, jos käyttäjän antama syöte on oikeaa muotoa

    '''

    p = Stack()
    if '#' in user_input:
        raise ValueError("Virheellinen syöte: Syöte ei voi sisältää #-merkkiä.")
    if '.' in user_input:
        raise ValueError("Virheellinen syöte: Syöte ei voi sisältää pistettä.")
    if user_input[0] in ['*', '|']:
        raise ValueError(
            "Virheellinen syöte: Syöte ei voi alkaa operaattorilla.")

    if user_input[-1] in ['(', '|']:
        raise ValueError("Virheellinen viimeinen merkki.")

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
    Funktio, joka palauttaa käyttäjän antaman syötteen infix muodossa.

    Args:
        user_input (str): käyttäjän antama syöte (säännöllinen lauseke)

    Returns:
        list: käyttäjän antama syöte infix muodossa
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
