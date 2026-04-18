from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from Cloud-Ops Deploy! Host: {socket.gethostname()}"

@app.route("/health")
def health():
    return {"status": "running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
