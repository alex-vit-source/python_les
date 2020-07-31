# -*- coding: utf-8 -*-

from commands import (
    ExitCommand,
    UserExitException,
)
from field import Board
from ship import Ship
from boom import Shut
from player import Player

def main():
    board_1={}
    board_2={}
    
    player1=Player('Alex', True)
    player1.set_emptyboard()
    while True:
        try:
            #player1=Player('Alex', True)
            #player.set_emptyboard()
            command1=input('Введите команду: ')
            if command1=='exit':
                ExitCommand.perform('exit')
            else:
                pass
                
                
        except UserExitException as ex:
            print('OK! ', ex)
            raise KeyboardInterrupt
            break
        except Exception as e:
           print('You have done something wrong!', e)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')