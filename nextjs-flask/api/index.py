from flask import Flask
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("https://shiny-adventure-g77jv9qrxxxhvqxr-3000.app.github.dev/api/test")
def test():
    return "<p>Hello, World!</p>"