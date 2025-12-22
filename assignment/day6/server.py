from flask import Flask

server = Flask(__name__)


# ---------- API TO RECEIVE DATA FROM CLIENT ----------
@server.get('/')
def homepage():
    return "This is a home page"

@server.get('/welcome')
def welcome():
    return "<html><body><h1>Welcome to Student Management System</h1></body></html>"

@server.post('/temperature/<float:temp>')
def post_temperature(temp):
    print(f"temp = {temp}")
    return f"{temp} is recieved"

# ---------- WEB SERVICE TO GET LIGHT INTENSITY ----------

@server.post('/light_intensity/<float:li>')
def post_light_intensity (li):
    print(f"light intensity = {li}")
    return f"{li} is recieved"


# run server continuously to listen client
server.run(host='0.0.0.0', port=4000, debug=True)
