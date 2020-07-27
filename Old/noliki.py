
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

def handle(turnX,pole):
    dict_button={'q':0,'w':1,'e':2,'a':3,'s':4,'d':5,'z':6,'x':7,'c':8}
    if turnX==True:
        znak='X'
    else:
        znak='O'
    while True:
        try:
            button= dict_button[str(input ('Ход игрока {}. Выберите позицию крестика. Клавиши q,w,e,a,s,d,z,x,c - '.format(znak)))]
            if pole[button]=='*':
                return button, znak
            else:
                print ('Эта позиция занята.')    
        except KeyError as e:
            print ('Не правильно нажата кнопка. Введите ещё раз')

def change_list(but,znak,pole):
    print ('change_list - позиция ', but, 'Кто ходит - ', znak, 'матрица ', pole)
    pole[but]=znak
    return pole



field=begin_game()
print_field(field)
win_end=win(field, True)
print ('Win_end = ', win_end)
but,who=handle(True, field)
print ('Позиция - ', but, type(but), ' Знак ', who, type(who))
field=change_list(but,who,field)
print ('Новое значение матрицы - ', field)
print_field(field)
        




#field=begin_game()
#print_field(field)        

