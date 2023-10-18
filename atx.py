import os
import sys
import typing as t
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

a = "{"
b = "}"
LISTENING_PORT = int(sys.argv[1])

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

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            user_get = query_params.get("user", [None])[0]

            if user_get is not None:
                username = get_user(user_get)
                user = get_user(username)

                if user == "Not exist":
                    response = (
                        "{0}\"username\":\"{1}\",\"cont_conexao\":\"Null\",\"data_expiracao\":\"Null\",\"dias_expiracao\":\"Null\",\"limite_user\":\"Null\"{2}".format(
                            a, user, b
                        )
                    )
                else:
                    response = (
                        "{0}\"username\":\"{1}\",\"cont_conexao\":\"{2}\",\"data_expiracao\":\"{3}\",\"dias_expiracao\":\"{4}\",\"limite_user\":\"{5}\"{6}".format(
                            a, username, cont_online(username), check_data(username), check_dias(username), limiter_user(username), b
                        )
                    )

                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(response.encode("utf-8"))
            else:
                self.send_response(400)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write("Bad Request: 'user' parameter is missing in the query string.".encode("utf-8"))
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e}).encode("utf-8"))

if __name__ == '__main__':
    httpd = HTTPServer(('0.0.0.0', LISTENING_PORT), MyHandler)
    httpd.serve_forever()
