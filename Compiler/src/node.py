class Node:
    '''
    Luokka kuvaa syntaksipuun yksittäistä solmua 
    deterministisen automaatin (DFA) rakentamista varten.

    Attribuutit: 
        number (int): solmun numero
        left (Node | None): solmun vasen lapsi
        right (Node | None): solmun oikea lapsi
        parent (Node | None): solmun vanhempi
        character (str): solmun arvo (säännöllisen lausekkeen operandi tai operaattori)
        max_children (int): solmun lapsisolmujen maksimimäärä
        nullable (boolean | None): 
            solmun nullable arvo on True, mikäli solmun edustama osalauseke voi 
            tuottaa tyhjän merkkijonon.
        firstpos (list | None | []): 
            Joukko lehtisolmuja, jotka voivat olla ensimmäisiä merkkejä solmun 
            tuottamissa merkkijonoissa.
        lastpos (list | None | []): 
            Joukko lehtisolmuja, jotka voivat olla viimeisiä merkkejä solmun 
            tuottamissa merkkijonoissa.
        followpos (list | None | []): 
            Joukko, joka kertoo mitkä lehtisolmut voivat seurata kyseistä 
            solmua lausekkeen mahdollisissa merkkijonoissa.


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
        self.parent = None
        self.character = character
        self.max_children = None
        self.nullable = None
        self.firstpos = None
        self.lastpos = None
        self.followpos = []


    def __repr__(self):
        '''
        Metodi palauttaa solmun numeron merkkijonona
        '''
        return str(self.number)
