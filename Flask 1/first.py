import random
from flask import Flask
app = Flask (__name__)

@app.route("/")
def home():
    num = random.randrange(0, 101)
    return str(num)
if __name__ == "__main__":
    app.run(debug=True)