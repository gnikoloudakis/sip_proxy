from flask import Flask, request
import os, json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    data = json.loads(request.data)
    # print (data['sender'])
    sender = data['sender']
    username = data['username']
    password = data['password']
    recipient = data['recipient']
    message = data['message']
    command_1 = """sip-settings -a add %s %s"""%(sender, password)
    command_2 = """sip-message -a %s %s -m "%s" """%(username, recipient, message)
    os.system(command_1)
    os.system(command_2)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
