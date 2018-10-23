from flask import Flask, render_template, request





#app instance
app = Flask(__name__)

app.secret_key = 'development key'

#home
@app.route('/')
def index():
    #retrieve list of all contacts
    
    return render_template('index.html')


#main
if __name__ == '__main__':
    app.run(debug=True)

