from node import Node
from stack import Stack


def get_child_number(character: str):
    """
    Funktio, joka palauttaa syntaksipuussa olevan solmun (säännöllisen lausekkeen operaattorin tai operandin) tarvittavien lasten määrän

    Args:
        character (str): solmun arvo (säännöllisen lausekkeen operandi tai operaattori)

    Returns:
        int: solmun tarvittavien lasten määrä
    """
    if character in ['|', '.']:
        return 2
    if character == '*':
        return 1
    return 0

def has_all_children(node: Node):
    """
    Funktio, joka kertoo, onko solmulla jo tarvittava määrä lapsia

    Args:
        node (Node): tarkasteltava solmu

    Returns:
        boolean: palauttaa True vain, jos solmulla on jo tarvittava määrä lapsia
    """
    if node.character not in ['|', '.', '*']:
        return True
    if node.character == '*' and node.left != None:
        return True
    if node.character in ['|', '.'] and node.left != None and node.right != None:
        return True
    return False

def get_postfix(expression: str):

    """
    Funktio, joka tuottaa infix-muotoa olevasta säännöllisestä lausekkeesta postfix-muotoa olevan.

    Args:
        expression (str): säännöllinen lauseke infix-muodossa

    Returns:
        list: säännöllinen lauseke postfix-muodossa
    """

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
                if stack_top_operator == None:
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
                    if operator_to_postfix_queue != '(' and operator_to_postfix_queue != None:
                        postfix.append(operator_to_postfix_queue)
                    else:
                        break

    while len(stack) > 0:
        operator_to_postfix_queue = stack.pop()
        postfix.append(operator_to_postfix_queue)

    return postfix


