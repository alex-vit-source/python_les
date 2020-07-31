# -*- coding: utf-8 -*-




class Board (object):
    def __init__(self, size, ship_total):
        self.size=size
        self.ship_total=ship_total
        self.board={}
        self.emptyfield=['~','~','~','~','~','~','~','~','~','~']
        self.board_1={}
        self.board_2={}
    
    def set_emptyboard (self): # Заполняем пустое поле
        self.board_1={ 1 : self.emptyfield,  2 : self.emptyfield, 3 : self.emptyfield,
                       4 : self.emptyfield,  5 : self.emptyfield, 6 : self.emptyfield,
                       7 : self.emptyfield,  8 : self.emptyfield, 9 : self.emptyfield,
                      10 : self.emptyfield}
        print ('Создание пустого поля завершено ', self.board_1)
    
    def print_board (self):
        print ('_A_____B____C____D____E____F____J____K____L____M_')
        print ('_________________________________________________')
        for key, values in self.board_1.items():
            print (values)
        print ('-------------------------------------------------')

#s=Board(100,10)
#s.set_emptyboard()
#s.print_board()

                


        
