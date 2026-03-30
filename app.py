from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Loan App Running 🚀"

import os
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
