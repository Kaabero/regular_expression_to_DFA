from node import Node
from utils import get_child_number, has_all_children, get_postfix


class SyntaxTree:
    '''
    Luokka kuvaa syntaksipuuta.

    Attribuutit:
        root (Node): puun juurisolmu
        focus_node (Node): käsittelyssä oleva solmu

    '''

    def __init__(self):
        '''
        Luokan konstruktori, joka luo uuden puun


        '''
        self.root = None
        self.focus_node = None
     

    def build_tree(self, postfix):
        '''
        Metodi rakentaa puun postfix-muodossa olevasta säännöllisestä lausekkeesta

        Args:
            postfix (list): säännöllinen lauseke postfix-muodossa 
        '''
        expression = postfix[::-1]
        self.root = Node(1, expression[0])
        self.root.max_children = get_child_number(self.root.character)

        self.focus_node = self.root
        for i in range(1, len(expression)):
            self.add(i+1, expression[i])


  
    def add(self, number: int, character: str):
        '''
        Metodi lisää uuden solmun puuhun

        Args:
            number (int): lisättävän solmun numero
            character (str): lisättävän solmun arvo (säännöllisen lausekkeen operandi tai operaattori)
        '''
        node = Node(number, character)
        node.max_children = get_child_number(node.character)
        if self.focus_node.max_children == 2:
            
            if self.focus_node.right == None:
                
                self.focus_node.right=node
                node.parent = self.focus_node
                
                self.focus_node = node
            
            else:
                
                self.focus_node.left=node
                node.parent = self.focus_node
                
                self.focus_node = node
        
        elif self.focus_node.max_children == 1:
            
            self.focus_node.left=node
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
        nodes[node.number] = {'character': node.character, 'left': node.left, 'right': node.right, 'parent': node.parent, 'max_children': node.max_children}
        self.traverse(node.right, nodes)



'''
postfix = get_postfix('a.(b)*.#')
s = SyntaxTree()
s.build_tree(postfix)
print(s.get_tree())
'''



 



    