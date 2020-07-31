# -*- coding: utf-8 -*-
from field import Board



class Ship (Board):
    def __init__(self):
        super().__init__(100,10)

    def set_ship(self, player):
        pass      


#c=Ship()
#print('Запрос из board',c.emptyfield)
#c.set_emptyboard()
#print ('обращение к функции ', c.print_board())