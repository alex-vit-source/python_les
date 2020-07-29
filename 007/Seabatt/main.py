# -*- coding: utf-8 -*-

from commands import (
    ExitCommand,
    UserExitException,
)


def main():
    

    while True:
        try:
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