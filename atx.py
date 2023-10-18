from crypt import methods
import os
import sys
import typing as t
import json

from datetime import datetime
from flask import Flask, jsonify, request

a = "{"
b = "}"
LISTENING_PORT = int(sys.argv[1])
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

def get_user(username: str) -> t.Optional[str]:
    command = 'check %s 1' % username
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

def cont_online(username: str) -> t.Optional[str]:
    command = 'check %s 2' % username
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

def limiter_user(username: str) -> t.Optional[str]:
    command = 'check %s 3' % username
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

def check_data(username: str) -> t.Optional[str]:
    command = 'check %s 4' % username
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

def check_dias(username: str) -> t.Optional[str]:
    command = 'check %s 5' % username
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

@app.route('/check', methods=['GET'])
def check_user():
    try:
        user_get = request.args.get("user")
        username = get_user(user_get)
        user = get_user(username)
        if user == "Not exist":
            return (
                "{0}\"username\":\"{1}\",\"cont_conexao\":\"Null\",\"data_expiracao\":\"Null\",\"dias_expiracao\":\"Null\",\"limite_user\":\"Null\"{2}".format(
                    a, user, b
                )
            )
        else:
            return (
                "{0}\"username\":\"{1}\",\"cont_conexao\":\"{2}\",\"data_expiracao\":\"{3}\",\"dias_expiracao\":\"{4}\",\"limite_user\":\"{5}\"{6}".format(
                    a, username, cont_online(username), check_data(username), check_dias(username), limiter_user(username), b
                )
            )
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(sys.argv[1]) if len(sys.argv) > 1 else LISTENING_PORT,
    )
