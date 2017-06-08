__author__ = 'anthonymcclay'
__project__ = 'myFlask'
__date__ = '6/8/17'
__revision__ = '$'
__revision_date__ = '$'


from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World - These Nuts"

if __name__ == '__main__':
    app.run(port=5000, debug=True)

