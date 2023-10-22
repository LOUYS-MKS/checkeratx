
import os
import sys
import json
import datetime
from flask import Flask, jsonify, request

LISTENING_PORT = int(sys.argv[1])

def get_user(username: str) -> str:
    command = f'userscheck {username} 1'
    result = os.popen(command).readlines()
    return result[0].strip()

def cont_online(username: str) -> str:
    command = f'userscheck {username} 2'
    result = os.popen(command).readlines()
    return result[0].strip()

def limiter_user(username: str) -> str:
    command = f'userscheck {username} 3'
    result = os.popen(command).readlines()
    return result[0].strip()

def userscheck_data(username: str) -> str:
    command = f'userscheck {username} 4'
    result = os.popen(command).readlines()
    return result[0].strip()

def userscheck_dias(username: str) -> str:
    command = f'userscheck {username} 5'
    result = os.popen(command).readlines()
    return result[0].strip()

def get_info(username: str) -> dict:
    user = get_user(username)
    if user == "Not exist":
        return {'username': user, 'cont_conexao': 'Null', 'data_expiracao': 'Null', 'dias_expiracao': 'Null', 'limite_user': 'Null'}
    else:
        return {
            'username': username,
            'cont_conexao': cont_online(username),
            'data_expiracao': userscheck_data(username),
            'dias_expiracao': userscheck_dias(username),
            'limite_user': limiter_user(username)
        }

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

@app.route('/check', methods=['GET'])
def userscheck_user():
    try:
        user_get = request.args.get("user")
        username = get_user(user_get)
        return jsonify(get_info(username))
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(sys.argv[1]) if len(sys.argv) > 1 else LISTENING_PORT,
    )