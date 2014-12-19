from flask import Flask, render_template
from flask import Markup

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    # return Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
    # return Markup.escape('<blink>hacker</blink>')
    return Markup('<em>Marked up</em> &raquo; HTML').striptags()


@app.route('/show_path/<path:mypath>')
def show_path(mypath):
    return 'This is my path %s' % mypath


@app.route('/<string:page_name>/')
def static_page(page_name):
    return render_template('%s.html' % page_name)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run(debug=True, port=33507)