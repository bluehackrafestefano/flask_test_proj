from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Updated</h1><br><p>Hello, World!</p>"

if __name__ == '__main__':
    # app.run(debug=True, port=3003)
    app.run(host='0.0.0.0', port=80)
