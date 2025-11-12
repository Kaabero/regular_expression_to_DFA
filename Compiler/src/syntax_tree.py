from src.node import Node
from src.utils import get_child_number, has_all_children
from src.utils import get_nullable, get_firstpos, get_lastpos, get_followpos


class SyntaxTree:
    '''
    Luokka kuvaa syntaksipuuta deterministisen automaatin (DFA) rakentamista varten. 

    Attribuutit:
        root (Node | None): puun juurisolmu
        focus_node (Node | None): käsittelyssä oleva solmu

    '''

    def __init__(self):
        '''
        Luokan konstruktori, joka luo uuden puun


        '''
        self.root = None
        self.focus_node = None

    def build_tree(self, postfix):
        '''
        Metodi rakentaa syntaksipuun postfix-muodossa olevasta säännöllisestä lausekkeesta

        Args:
            postfix (list): säännöllinen lauseke postfix-muodossa 
        '''
        expression = postfix[::-1]
        self.root = Node(1, expression[0])
        self.root.max_children = get_child_number(self.root.character)

        self.focus_node = self.root
        for i in range(1, len(expression)):
            self.add(i+1, expression[i])

        self.set_nullable_firstpos_and_lastpos(self.root)
        self.set_followpos(self.root)

    def set_nullable_firstpos_and_lastpos(self, node: Node):
        '''
        Metodi käy läpi puun alkiot ja lisää niille nullable, firstpos ja lastpos arvot.

        Args:
            node (Node): vuorossa oleva solmu
        '''
        if not node:
            return
        self.set_nullable_firstpos_and_lastpos(node.left)
        node.nullable = get_nullable(node)
        node.firstpos = get_firstpos(node)
        node.lastpos = get_lastpos(node)
        self.set_nullable_firstpos_and_lastpos(node.right)

    def set_followpos(self, node: Node):
        '''
        Metodi käy läpi puun alkiot ja lisää niille followpos arvon.

        Args:
            node (Node): vuorossa oleva solmu
        '''
        if not node:
            return
        self.set_followpos(node.left)
        get_followpos(node)
        self.set_followpos(node.right)

    def add(self, number: int, character: str):
        '''
        Metodi lisää uuden solmun puuhun

        Args:
            number (int): lisättävän solmun numero
            character (str): lisättävän solmun arvo (säännöllisen lausekkeen operandi/operaattori)
        '''
        node = Node(number, character)
        node.max_children = get_child_number(node.character)
        if self.focus_node.max_children == 2:

            if self.focus_node.right is None:

                self.focus_node.right = node
                node.parent = self.focus_node

                self.focus_node = node

            else:

                self.focus_node.left = node
                node.parent = self.focus_node

                self.focus_node = node

        elif self.focus_node.max_children == 1:

            self.focus_node.left = node
            node.parent = self.focus_node

            self.focus_node = node

        while self.focus_node != self.root and has_all_children(self.focus_node):

            self.focus_node = self.focus_node.parent

    def get_tree(self):
        '''
        Metodi palauttaa puun sanakirjamuodossa
        '''
        nodes = {}
        self.traverse(self.root, nodes)
        return nodes

    def traverse(self, node: Node, nodes: dict):
        '''
        Metodi käy läpi puun alkiot ja lisää ne sanakirjaan.

        Args:
            node (Node): vuorossa oleva solmu
            nodes (dict): solmujen tiedot sisältävä sanakirja
        '''
        if not node:
            return
        self.traverse(node.left, nodes)

        nodes[node.number] = {
            'character': node.character,
            'left': node.left.number if node.left else None,
            'right': node.right.number if node.right else None,
            'parent': node.parent.number if node.parent else None,
            'max_children': node.max_children,
            'nullable': node.nullable,
            'firstpos': {n.number for n in node.firstpos} if node.firstpos else set(),
            'lastpos': {n.number for n in node.lastpos} if node.lastpos else set(),
            'followpos': {n.number for n in node.followpos} if node.followpos else set()
        }
        self.traverse(node.right, nodes)
