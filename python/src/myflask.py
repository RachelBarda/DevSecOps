from flask import Flask,jsonify

users = { '1':{'id':1,'name':'Rachel'},'2':{'id':2,'name':'Ariel'}}
app = Flask('Test')

@app.route('/')
def test():
    return "Hello user"

@app.route('/users/<userid>')
def getUser(userid):
    return jsonify(users[userid])


app.run()