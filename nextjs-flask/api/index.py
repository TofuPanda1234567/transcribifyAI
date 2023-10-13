from flask import Flask
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/test/")
def test():
    return render_template("../nextls-flask/app/test.html")

if __name__ == '__main__':
    app.run(debug=True, port=3000)