import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  host_name = socket.gethostname()
  host_ip = socket.gethostbyname(host_name)
  return f"<h2>Hello World!</h2></br>Hostname: {host_name}</br>IP: {host_ip}"

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=80)