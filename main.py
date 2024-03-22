from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def first():
    return "Миссия Колонизация Марса"


@app.route('/index')
def second():
    return 'И на Марсе будут яблоки цвести!'


@app.route('/promotion')
def ads():
    return"""Человечество вырастает из детства.<br>
    Человечеству мала одна планета.<br>
    Мы сделаем обитаемыми безжизненные пока планеты.<br>
    И начнем с Марса!<br>
    Присоединяйся!<br>"""


@app.route('/image_mars')
def image_mars():
    return '''
    <head><title>Привет, Марс!</title></head>
    <h1>Жди нас, Марс!</h1>
    <img src="static/assets/MARS.png" alt="здесь должна была быть картинка, но не нашлась">
    </br>Вот она какая, красная планета.
    '''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')