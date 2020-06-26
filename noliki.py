
print ('Игра Крестикрестики нолики')

def begin_game():  # Пустое поле
    field=['*','*','*','*','*','*','*','*','*']
    return field

def print_field(pole): # Рисуем поле
    for i in range(0,9,3):
        print (pole[i:i+3])
    print ('\n')

def win(pole, xstep):

    if xstep==True:
        if ((pole[0]=='X' and pole[1]=='X' and pole[2]=='X') or 
          (pole[3]=='X' and pole[4]=='X' and pole[5]=='X') or
          (pole[6]=='X' and pole[7]=='X' and pole[8]=='X') or
          (pole[0]=='X' and pole[3]=='X' and pole[6]=='X') or
          (pole[1]=='X' and pole[4]=='X' and pole[7]=='X') or
          (pole[2]=='X' and pole[5]=='X' and pole[8]=='X') or
          (pole[0]=='X' and pole[4]=='X' and pole[8]=='X') or
          (pole[6]=='X' and pole[4]=='X' and pole[2]=='X')):
            print ('Выиграл игрок Х. Поздравляем!!!')
            win=True
        else: 
            x=False
            win=False
    else:
        if ((pole[0]=='O' and pole[1]=='O' and pole[2]=='O') or ...
           (pole[3]=='O' and pole[4]=='O' and pole[5]=='O') or ... 
           (pole[6]=='O' and pole[7]=='O' and pole[8]=='O') or ...
           (pole[0]=='O' and pole[3]=='O' and pole[6]=='O') or ...
           (pole[1]=='O' and pole[4]=='O' and pole[7]=='O') or
           (pole[2]=='O' and pole[5]=='O' and pole[8]=='O') or
           (pole[0]=='O' and pole[4]=='O' and pole[8]=='O') or
           (pole[6]=='O' and pole[4]=='O' and pole[2]=='O')):
            print ('Выиграл игрок O. Поздравляем!!!')
            win=True
        else: 
            x=False
            win=False
    return win

def handle(turn):
    if turn==True:
        button=str(input ('Ход игрока X. Выберите позицию крестика. Клавиши q,w,e,a,s,d,z,x,c - '))
        if button==q:
            


field=begin_game()
print_field(field)
win_end=win(field, True)
print ('Win_end = ', win_end)


        




#field=begin_game()
#print_field(field)        

