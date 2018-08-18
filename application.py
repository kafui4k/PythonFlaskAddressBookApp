from flask import Flask, render_template, request

#app instance
app = Flask(__name__)

#hompage method
@app.route('/')
def home():
    return render_template('index.html')

#add contact page method 
@app.route('/addcontact', methods=['GET', 'POST'])
def addcontact():
    if request.method == 'POST': #this execute upon form submit - by button send.
        return "Success"
    return render_template('addcontact.html')    

#add search page method 
@app.route('/searchcontact')
def searchcontact():
    return render_template('searchcontact.html')

#main
if __name__ == '__main__':
    app.run(debug=True)

