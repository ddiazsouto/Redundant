from flask import Flask
from random import randint
app = Flask(__name__)

@app.route('/', methods=['GET'])
def randomizer():

    random = randint(1, 100)

    if request.method == 'GET':

        random = randint(1, 15)
        
    return f'{random}'



if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)