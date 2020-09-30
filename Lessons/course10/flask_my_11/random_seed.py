import random
import os
from flask import Flask, request
from flask.json import jsonify
# pip install flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, validators, ValidationError
  # для того чтобы через переменную окружения 



app = Flask(__name__)
#______________________________________________________
#ПРостой вариант установки параметров
'''
app.config.update(
    DEBUG=True,
    SECRET_KEY='S',
    WTF_CSRF_ENABLED=False,
)
'''
#______________________________________________________
#Посложнее вариант установки параметров
app.config.update(**settings.as_dict())
app.debug = settings.DEBUG # На всякий случай


class Number(object):
    def __init__(self):
        self.num = None
        print ('Число не загадано')
        return self.num
    def add(self, limit=100):
        self.num=random.randint(1, limit)
        print ('Загадано новое число', self.num)
        return self.num

class GuessForm(FlaskForm):
    number = DecimalField(label='Number is', validators=[validators.DataRequired()])

@app.route('/<player>/', methods =['GET', 'POST']) # причем вместо test можно в браузере писать что угодно
def home(player):
    
    print (dict_my)
    print (dict_my['pl1'])
    if request.method == 'GET':
        k = dict_my[player].add(10) #chislo.add(10)
        print ('Число ', k)
        return 'Число загадано', 200
      # в переменной лежит адрес маршрута 

@app.route('/<player>/step/', methods =['GET', 'POST']) # причем вместо test можно в браузере писать что угодно
def guest(player):
    if dict_my[player].num is None:
        return '<a href="/">Вы не загадали число</a>' 


    if request.method == 'POST':
        form = GuessForm(request.form)

        if form.validate():
            user_number = form.number.data
            print ('У игрока {} загадано число {}'.format(player, dict_my[player].num))

            if user_number == dict_my[player].num:
                dict_my[player].add(100)
                return 'Угадали! Загадано еще одно число'
            elif user_number > dict_my[player].num:
                return 'Ваше число больше загаданного (>)'
            elif user_number < dict_my[player].num:
                return 'Ваше число меньше загаданного (<)'
        else:
            return str(form.errors)
        
    else:
        return url_for('home')

    
      # в переменной лежит адрес маршрута     

if __name__ == '__main__':
   # print (os.environ['FLASK_RANDOM'])
    flask_random_seed =1 # os.environ['FLASK_RANDOM']
    if (flask_random_seed is None):
        print ('SEED не задан')
        exit()
    else:

        random.seed(flask_random_seed)
        chislo=Number()
        chislo1=Number()
        chislo2=Number()
        chislo3=Number()
        dict_my = {'pl1': chislo1 , 'pl2': chislo2 ,'pl3': chislo3 }
        app.run()

