from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def verifyPost(postData, funcName):

    if (funcName == 'add'):
        if ('x' not in postData) or ('y' not in postData):
            return 301
        else:
            return 200
    elif (funcName == 'subtract'):
        if ('x' not in postData) or ('y' not in postData):
            return 301
        else:
            return 200
    elif (funcName == 'multiply'):
        if ('x' not in postData) or ('y' not in postData):
            return 301
        else:
            return 200
    elif (funcName == 'divide'):
        if ('x' not in postData) or ('y' not in postData):
            return 301
        elif (postData['y'] == 0):
            return 302
        else:
            return 200



class Add(Resource):
    def post(self):
        postData = request.get_json()

        status = verifyPost(postData, 'add')
        if status != 200:
            resultMap = {
                'Message': 'Missing Value',
                'Status': status
            }
        else:
            x = postData['x']
            y = postData['y']
            result = int(x) + int(y)

            resultMap = {
                'Message': result,
                'Status': 200
            }

        return jsonify(resultMap)



class Subtract(Resource):
    def post(self):
        postData = request.get_json()

        status = verifyPost(postData, 'subtract')
        if status != 200:
            resultMap = {
                'Message': 'Missing Value',
                'Status': status
            }
        else:
            x = postData['x']
            y = postData['y']
            result = int(x) - int(y)

            resultMap = {
                'Message': result,
                'Status': 200
            }

        return jsonify(resultMap)

class Multiply(Resource):
    def post(self):
        postData = request.get_json()

        status = verifyPost(postData, 'multiply')
        if status != 200:
            resultMap = {
                'Message': 'Missing Value',
                'Status': status
            }
        else:
            x = postData['x']
            y = postData['y']
            result = int(x) * int(y)

            resultMap = {
                'Message': result,
                'Status': 200
            }

        return jsonify(resultMap)

class Divide(Resource):
    def post(self):
        postData = request.get_json()

        status = verifyPost(postData, 'divide')
        if status != 200:
            resultMap = {
                'Message': 'Missing or error Value',
                'Status': status
            }
        else:
            x = postData['x']
            y = postData['y']
            result = int(x) / int(y)

            resultMap = {
                'Message': result,
                'Status': 200
            }

        return jsonify(resultMap)


api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hithere')
def hi_there():
    return 'Welcome to Hi There!'

@app.route('/addnum', methods=['POST'])
def add_two_nums():
    dataDict = request.get_json()

    x = dataDict['x']
    y = dataDict['y']
    z = x + y

    retJson = {
        'z': z
    }

    return jsonify(retJson), 200


@app.route('/bye')
def bye_now():
    c = 14*152000
    s= str(c)

    retJson  =  {
        "field1": "Theres the answer",
        "field2": "testing"
    }

    return jsonify(retJson)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
