# -*- coding: utf-8 -*-
"""HelloFlask.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ii8Qs90D94OcOja4ng1vo5D_iWL2-pW8
""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self, name):
        return {"Hello":name}

api.add_resource(Hello, '/hello/<name>')

if __name__ == '__main__':
 app.run(debug=True)
