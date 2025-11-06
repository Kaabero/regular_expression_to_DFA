class Stack:
    '''
    Luokka toteuttaa pinotietorakenteen
    '''
    def __init__(self):
        self.stack = []

    def push(self, x):
        '''
        Metodi lisää alkion x pinon ylimmäksi
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