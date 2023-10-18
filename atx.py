from flask import Flask, jsonify, request
import os

app = Flask(__name)

def get_user(username):
    command = f'check {username} 1'
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

def cont_online(username):
    command = f'check {username} 2'
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

def limiter_user(username):
    command = f'check {username} 3'
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

def check_data(username):
    command = f'check {username} 4'
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

def check_dias(username):
    command = f'check {username} 5'
    result = os.popen(command).readlines()
    final = result[0].strip()
    return final

@app.route('/checkUser', methods=['POST'])
def check_user():
    try:
        req_data = request.get_json()
        user_get = req_data.get("user")
        username = get_user(user_get)
        
        if username == "Not exist":
            return jsonify({
                "username": user_get,
                "cont_conexao": "Null",
                "data_expiracao": "Null",
                "dias_expiracao": "Null",
                "limite_user": "Null"
            })
        else:
            return jsonify({
                "username": username,
                "cont_conexao": cont_online(username),
                "data_expiracao": check_data(username),
                "dias_expiracao": check_dias(username),
                "limite_user": limiter_user(username)
            })
    except Exception as e:
        return jsonify({'error': str(e)}, 400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=LISTENING_PORT)
