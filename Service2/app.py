from flask import Flask, request, jsonify
from random import randint
from frasium import binary, azar, phraser
app = Flask(__name__)

@app.route('/', methods=['GET'])
def randomizer():

    output = dict()
     
    question = binary()
    check = phraser(azar([0, 7], 4), question)  

    output['dark'] = binary()
    output['question'] = question
    output['phrase'] = check
    

    return jsonify(output)



if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)