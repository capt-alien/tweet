from flask import Flask
import random
from stoch import weighted_probablity


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is a test!'



if __name__ == "__main__":
    app.run()
