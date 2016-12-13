from flask import Flask, request
import os, json
from config import *

app = Flask(__name__)
app.config.from_object(__name__)
userAccount = USER_ACCOUNT
userName = USERNAME
userPassword = USER_PASSWORD
command_1 = """sip-settings -a add %s %s""" % (userAccount, userPassword)
os.system(command_1)


@app.route('/', methods=['POST'])
def hello_world():
    global userName
    data = json.loads(request.data)
    # print (data['sender'])
    recipient = data['recipient']
    message = data['message']

    command_2 = """sip-message -a %s %s -m "%s" """ % (userName, recipient, message)

    os.system(command_2)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
