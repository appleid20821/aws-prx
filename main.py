from flask import Flask, request
import requests
app = Flask(__name__)
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    target_url = "http://31.56.204.231:9000" + request.full_path
    resp = requests.request(method=request.method, url=target_url, headers={k: v for k, v in request.headers if k.lower() != 'host'}, data=request.get_data(), allow_redirects=False)
    return resp.content, resp.status_code, dict(resp.headers)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
