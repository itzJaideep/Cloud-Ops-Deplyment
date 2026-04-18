from flask import Flask
import logging
import socket

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    logging.info("Home endpoint accessed")
    return f"Hello from Cloud-Ops Deploy! Host: {socket.gethostname()}"

@app.route("/health")
def health():
    return {"status": "running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
