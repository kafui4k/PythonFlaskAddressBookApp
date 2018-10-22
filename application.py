from flask import Flask, render_template, request
from contactform import AddContact

#app instance
app = Flask(__name__)
app.secret_key = 'development key'

#hompage route
@app.route('/')
def index():
    return render_template('index.html')


#main
if __name__ == '__main__':
    app.run(debug=True)

