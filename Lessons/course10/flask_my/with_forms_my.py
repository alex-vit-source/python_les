import re
from flask import Flask, request
from flask.json import jsonify
from threading import Lock
# pip install flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

def my_birthday_check(form, field):        ####Свой валидатор. Проверка даты
    month = re.findall(r'\d\d+\.(\d\d)+\.\d{4}', field.data, flags=re.IGNORECASE)
    print('-------------------------', type(month), month)
    if int(month[0]) > 12:
        raise ValidationError('Field must be less than 5 characters')

class MyForm(FlaskForm):
    myname = StringField(label='Name', validators=[my_birthday_check])

#class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25, message='pooiiuu')
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35, message='qweerr'),
        validators.Email()
    ])
    job = StringField(label='JOB', validators=[
        validators.DataRequired(),
        validators.Length(min=1, max=35),
        validators.AnyOf(['IT','PR','driver'],message='sadasdasdsad')
        ##validators.Optional()
    ])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = MyForm(request.form) #ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200

# По адресу /form/user должен принимать POST запрос с

# Возрващать пользователю json вида: "status" - 0 или 1 (если ошибка валидации),
# "errors" - список ошибок, если они есть, или пустой список.

@app.route('/form/user', methods =['GET', 'POST'])
def post_data():
    if request.method == 'POST':
        user_form = MyForm(request.form)
        status_output = {0:'Проверка пройдена', 1: 'Ошибка валидации'}
        if user_form.validate():
            # print('email:', request.form['email'])
            # print('pass:', request.form['password'])
            status_check = jsonify(status_output[0])
            print(type(status_check), type(status_output[0]))
            return status_check
        else:
            status_check = jsonify(status_output[1])
            error_list = jsonify(user_form.errors)
            print(error_list)
            print(type(user_form.errors))
            return status_check # and error_list
    return 'Done!'
if __name__ == '__main__':
    app.run()
