from flask import Flask
app = Flask(__name__)

# the below decorator gives the function additional functionality
@app.route('/')             # '/' tells code that we are at home page
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>'\
            '<p>This is a paragraph</p>'\
            '<iframe src="https://giphy.com/embed/MDJ9IbxxvDUQM" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cat-kisses-hugs-MDJ9IbxxvDUQM">via GIPHY</a></p>'

@app.route('/bye')
def bye():
    return "Bye!"

@app.route('/user/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}! You are {number} years old."


'''We use decorators, when we have want to add some functionality
to multiple functions at a time.
Decorator is actually a function which has a function inside it

import time
def delay_decor(function):
    def wrap_func():
        time.sleep(2)
        function()
    return wrap_func

@delay_decor
def hello():
    print("hello")

hello()
'''

# TODO : Create 3 decorators naming make bold, emphasis, underlined

def make_bold(function):
    def wrapper():
        return f"<b>function</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>function</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>function</u>"
    return wrapper

@app.route('/check')
@make_emphasis
def check():
    return "This is a text check"


if __name__ == "__main__":      # print(__name__) ---> __main__ : that means __name__ is not imported
    app.run(debug=True)

