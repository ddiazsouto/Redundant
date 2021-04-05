from flask import Flask
app = Flask(__name__)

@app.route('/number', methods=['GET'])
def randomization():
    return 3

if __name__ == '__main__':
    app.run(port=5005, host='0.0.0.0', debug=True)