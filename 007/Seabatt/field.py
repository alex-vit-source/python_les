# -*- coding: utf-8 -*-




class Board (object):
    def __init__(self, size, ship_total):
        self.size=size
        self.mystep=ship_total
        self.board={}
        self.emptyfield=['~','~','~','~','~','~','~','~','~','~']
        
    
    def set_emptyboard (self): # Заполняем пустое поле
        self.board_1={'a': self.emptyfield, 'b': self.emptyfield, 'c': self.emptyfield,
                      'd': self.emptyfield, 'e': self.emptyfield, 'f': self.emptyfield,
                      'j': self.emptyfield, 'k': self.emptyfield, 'l': self.emptyfield,
                      'm': self.emptyfield}
        print ('Создание пустого поля завершено ', self.board_1)
    
    def print_board (self):
        print ('_A_____B____C____D____E____F____J____K____L____M_')
        print ('_________________________________________________')
        for key, values in self.board_1.items():
            print (values)
        print ('-------------------------------------------------')

s=Board(100,10)
s.set_emptyboard()
s.print_board()

                


        
