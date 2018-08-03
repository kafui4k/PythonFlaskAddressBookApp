from flask import Flask, render_template, request

#app instance
app = Flask(__name__)

#hompage method
@app.route('/')
def home():
    return render_template('index.html')

#add contact page method 
@app.route('/addContact', methods=['GET', 'POST'])
def addContact():
    if request.method == 'POST': #this execute upon form submit - by button send.
        return "Success"
    return render_template('addcontact.html')    

#add search page method 
@app.route('/searchContact')
def searchContact():
    return render_template('searchcontact.html')

#main
if __name__ == '__main__':
    app.run(debug=True)

