from flask import Flask
import os

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "SampleService")
PORT = int(os.getenv("PORT", "8080"))

@app.route("/hello")
def hello():
    return f"Hello from {APP_NAME}!"

@app.route("/about")
def about():
    return f"{APP_NAME}: a simple demo app."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
