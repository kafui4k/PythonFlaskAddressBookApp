import flask
from flask import Flask, render_template

#app instance
app = Flask(__name__)

#hompage method
@app.route('/')
def home():
    return render_template('index.html')

#main
if __name__ == '__main__':
    app.run()

    