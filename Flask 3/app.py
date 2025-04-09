from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/old')
def old():
    return redirect(url_for('new'))

@app.route('/new')
def new():
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)