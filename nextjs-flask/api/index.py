from flask import Flask
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test/")
def test():
    return render_template("/workspaces/transcribifyAI/nextjs-flask/app/test.html")

if __name__ == '__main__':
    app.run(debug=True)