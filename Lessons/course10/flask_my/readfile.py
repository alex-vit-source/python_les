# По адресу /serve/<path:filename> должен возвращать содержимое
# запрашиваемого файла из папки ./files. Файлы можно туда положить
# любые текстовые. А если такого нет - 404

import os
from flask import Flask
from read_write_my import read_file

app = Flask(__name__)


@app.route('/serve/<path:filename>', methods =['GET', 'POST'])
def show_file(filename):
    if not os.path.exists('Lessons/course10/flask_my/files/' + filename):
        return '404: File doesnt exist'
    else:
        data= read_file('Lessons/course10/flask_my/files/'+ filename)
        return data


if __name__ == '__main__':
    app.run()