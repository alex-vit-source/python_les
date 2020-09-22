import os

from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='S',
    WTF_CSRF_ENABLED=False,
)
'''
#@app.route('/sum/<test>') # причем вместо test можно в браузере писать что угодно
@app.route('/sum/<path:test>') # тогда в test можно писать /tea/as/asd
def home(test):  # в переменной лежит адрес маршрута 
    return 'hello user!' + test
'''
@app.route('/<int:first>/<int:second>') # причем вместо test можно в браузере писать что угодно
def home(first,second):  # в переменной лежит адрес маршрута 
    c=first+ second
    return str(c)

if __name__ == '__main__':
    app.run()




















# @app.route('/<user>')
# def username(user):
#     return 'hello, user: ' + user