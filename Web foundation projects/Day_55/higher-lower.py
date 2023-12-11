from flask import Flask
import random

rand_num = random.randint(0, 9)
app = Flask(__name__)


@app.route('/')
def home_text():
    return "<h1>Guess a number between 0 and 9</h1>"\
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route('/<int:num>')
def url(num):
    if rand_num == num:
        return "You found me!"\
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif rand_num > num:
        return "Too low, try again!"\
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "Too high, try again!"\
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)

