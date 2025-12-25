#import Flask class from flask module
from flask import Flask

#create server instance usinf class
server = Flask(__name__)

@server.get('/')
def hamepage():
    return "This is home page"

@server.get('/welcome')
def welcome():
    return "<html><body><h1>Welcome to Student Management System</h1></body></html>"

# run server continuously to listen client
server.run(host='0.0.0.0', port=4000, debug=True)