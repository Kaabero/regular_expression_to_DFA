from src.node import Node

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
        self.root.max_children = self.get_child_number(self.root.character)

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
        node.nullable = self.get_nullable(node)
        node.firstpos = self.get_firstpos(node)
        node.lastpos = self.get_lastpos(node)
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
        self.get_followpos(node)
        self.set_followpos(node.right)

    def add(self, number: int, character: str):
        '''
        Metodi lisää uuden solmun puuhun

        Args:
            number (int): lisättävän solmun numero
            character (str): lisättävän solmun arvo (säännöllisen lausekkeen operandi/operaattori)
        '''
        node = Node(number, character)
        node.max_children = self.get_child_number(node.character)
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

        while self.focus_node != self.root and self.has_all_children(self.focus_node):

            self.focus_node = self.focus_node.parent

    def get_tree(self):
        '''
        Metodi palauttaa syntaksipuun sanakirjamuodossa 
        dfa:n rakentamista varten
        '''
        nodes = {}
        self.traverse(self.root, nodes)
        return nodes

    def traverse(self, node: Node, nodes: dict):
        '''
        Metodi käy läpi puun alkiot ja lisää ne sanakirjaan.

        Args:
            node (Node): vuorossa oleva solmu
            nodes (dict): solmujen tietoja sisältävä sanakirja
        '''
        if not node:
            return
        self.traverse(node.left, nodes)

        if node.max_children == 0:

            nodes[node.number] = {
                'character': node.character,
                'followpos': sorted(n.number for n in node.followpos)
            }
        self.traverse(node.right, nodes)

    def get_child_number(self, character: str):
        '''
        Metodi, joka palauttaa syntaksipuussa olevan solmun 
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


    def has_all_children(self, node: Node):
        '''
        Metodi, joka kertoo, onko solmulla jo tarvittava määrä lapsia

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

    def get_nullable(self, node: Node):
        '''
        Metodi, joka palauttaa True mikäli solmun edustama osalauseke voi tuottaa tyhjän merkkijonon

        Args:
            node (Node): tarkasteltava solmu

        '''
        if node.character in ['€', '*']:
            return True
        if node.character == '.':
            return self.get_nullable(node.left) and self.get_nullable(node.right)
        if node.character == '|':
            return self.get_nullable(node.left) or self.get_nullable(node.right)

        return False


    def get_firstpos(self, node: Node):
        '''
        Metodi, joka palauttaa ne lehtisolmut, 
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
            left = self.get_firstpos(node.left)
            right = self.get_firstpos(node.right)
            return left + right
        if node.character == '.':
            if self.get_nullable(node.left):
                left = self.get_firstpos(node.left)
                right = self.get_firstpos(node.right)
                return left + right
            return self.get_firstpos(node.left)

        if node.character == '*':
            return self.get_firstpos(node.left)

        return [node]


    def get_lastpos(self, node: Node):
        '''
        Metodi, joka palauttaa ne lehtisolmut, 
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
            left = self.get_lastpos(node.left)
            right = self.get_lastpos(node.right)
            return left + right
        if node.character == '.':
            if self.get_nullable(node.right):
                left = self.get_lastpos(node.left)
                right = self.get_lastpos(node.right)
                return left + right
            return self.get_lastpos(node.right)

        if node.character == '*':
            return self.get_lastpos(node.left)

        return [node]


    def get_followpos(self, node: Node):
        '''
        Metodi, joka asettaa solmun followpos arvoksi listan niistä lehtisolmuista, 
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
