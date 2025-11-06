class Node:
    '''
    Luokka kuvaa syntaksipuun yksittäistä solmua. 
    
    Attribuutit: 
        number: solmun numero
        left: solmun vasen lapsi
        right: solmun oikea lapsi
        parent: solmun vanhempi
        character: solmun arvo (säännöllisen lausekkeen operandi tai operaattori)
        max_children: solmun lapsisolmujen maksimimäärä
    '''

    def __init__(self, number: int, character: str):
        """
        Luokan konstruktori, joka luo uuden solmun

        Args:
            number (int): solmun numero
            character (str): solmun arvo (säännöllisen lausekkeen operandi tai operaattori)
        """
        self.number = number
        self.left = None
        self.right = None
        self.parent= None
        self.character = character
        self.max_children = None
    
    def __repr__(self):
        '''
        Metodi palauttaa solmun numeron merkkijonona
        '''
        return str(self.number)