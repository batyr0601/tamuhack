from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from sentiment import get_weights, get_risk_factor

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    
    # methods go here
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('userId', required=True)  # add args
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)
        
        args = parser.parse_args()  # parse arguments to dictionary
        
        # create new dataframe containing new values
        new_data = pd.DataFrame({
            'userId': args['userId'],
            'name': args['name'],
            'city': args['city'],
            'locations': [[]]
        })
        # read our CSV
        data = pd.read_csv('users.csv')
        # add the newly provided values
        data = data.append(new_data, ignore_index=True)
        # save back to CSV
        data.to_csv('users.csv', index=False)
        return {'data': "glalglalglalga"}, 200  # return data with 200 OK

    @app.route('/getRiskFactor', methods=['POST'])
    def postTickerData():
        request_data = request.get_json()
        ticker_list = []
        quantity_list = []
        for ticker in request_data:
            ticker_list.append(ticker['ticker'])
            quantity_list.append(ticker['amount'])
        print(ticker_list)
        print(quantity_list)
        weights, total = get_weights(ticker_list, quantity_list)
        
        return {'riskFactor': get_risk_factor(ticker_list, weights, total, 3)}
    pass

    @app.route('/peepee/<name>')
    def get1(name):
        # return {'success': True, 'name': name}, 200
        return '<div>' + name + '</div>'
    
    def post(name):
        # return {'success': True, 'name': name}, 200
        return '<div>' + name + '</div>'
    
class Locations(Resource):
    # methods go here
    pass
    
api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # run our Flask app


