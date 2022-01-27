from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/home/<data>")
def hello_world(data=None):
    if data == None:
        return render_template('home.html')
        
    else:
        return render_template('home.html', input = data)

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])