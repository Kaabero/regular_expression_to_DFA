class Stack:
    '''
    Luokka toteuttaa pinotietorakenteen
    '''
    def __init__(self):
        '''
        Luokan konstruktori, joka luo uuden pinon
        '''
        self.stack = []

    def push(self, x: str):
        '''
        Metodi lisää alkion x pinon ylimmäksi

        Args:
            x: lisättävä alkio
        '''
        self.stack.append(x)

    def top(self):
        '''
        Metodi palauttaa pinon ylimmän alkion
        '''
        
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def pop(self):
        '''
        Metodi poistaa pinon ylimmän alkion

        Returns: Poistettu alkio
        '''
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
   
    def __len__(self):
        '''
        Metodi palauttaa pinon koon
        '''
        return len(self.stack)