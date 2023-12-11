from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index_2.html")


if __name__ == "__main__":
    app.run(debug=True)


'''By using 
document.body.contentEditable=true,
we can edit changes in the browser
& it is NOT saved in index_2.html'''


