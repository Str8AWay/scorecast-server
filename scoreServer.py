from flask import Flask, jsonify, url_for, redirect, request, render_template
from flask.ext.cors import CORS
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
from bson.json_util import dumps, loads

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "scores_db"
CORS(app)
mongo = PyMongo(app, config_prefix='MONGO')

class Score(Resource):
    def get(self, user_id):
        user = mongo.db.users.find_one_or_404({'user_id': user_id})
        return jsonify(mongoToOutput(user))

    def put(self, user_id):
        data = request.get_json()
        if not data:
            return {"response": "no json body",
                    "usage": '{"score":<score>}'}, 400
        score = data.get('score')
        if not score:
            return {"response": "did not include score in request body",
                    "usage": '{"score":<score>}'}, 400

        mongo.db.users.update({'user_id': user_id}, 
                {'$set': {'score': score}, 
                '$max': {'highScore': score}, 
                '$currentDate': {'lastModified': True}}, True)

        return {"response": "Player " + user_id + " score updated"}

    def delete(self, user_id):
        mongo.db.users.remove({'user_id': user_id})
        return {"response": "Player " + user_id + " deleted"}

class BatchScores(Resource):
    def get(self):
        users = []
        for user in mongo.db.users.find({}):
            users.append(mongoToOutput(user))
        return jsonify({"players": users})

    def post(self):
        data = request.get_json()
        if not data:
            return {"response": "no json body",
                    "usage": '{"user_ids":[<user_id1>, <user_id2>, ...]}'}, 400
        user_ids = data.get('user_ids')
        if not user_ids:
            return {"response": "did not include user_ids in json body",
                    "usage": '{"user_ids":[<user_id1>, <user_id2>, ...]}'}, 400
 
        users = []
        for user in mongo.db.users.find({'user_id': {'$in': user_ids}}):
            users.append(mongoToOutput(user))
        return jsonify({"players": users})

    def put(self):
        data = request.get_json()
        if not data:
            return {"response": "no json body",
                    "usage": '{"players":[{"user_id": <user_id1>, "score": <score1>}, ...]}'}, 400
        users = data.get('players')
        for user in users:
            user_id = user.get('user_id')
            score = user.get('score')
            if not (user_id and score):
                return {"response": "malformed json body",
                        "usage": '{"players":[{"user_id": <user_id1>, "score": <score1>}, ...]}'}, 400
            mongo.db.users.update({'user_id': user_id}, 
                {'$set': {'score': score}, 
                '$max': {'highScore': score}, 
                '$currentDate': {'lastModified': True}}, True)
        return {"response": "Players " + str(users) + " scores updated"}
                       
 
    def delete(self):
        data = request.get_json()
        if not data:
            return {"response": "no json body",
                    "usage": '{"user_ids":[<user_id1, user_id2>]}'}, 400
        user_ids = data.get('user_ids')
        if not user_ids:
            return {"response": "did not include user_ids in json body",
                    "usage": '{"user_ids":[<user_id1, user_id2>]}'}, 400

        mongo.db.users.remove({'user_id': {'$in': user_ids}})
        return {"response": "Players " + str(user_ids) + " deleted"}

def mongoToOutput(user):
    return {"user_id": user['user_id'],
            "score": user['score'],
            "highScore": user['highScore'],
            "lastModified": user['lastModified']}

@app.route('/highscores')
def highScoreView():
    players = mongo.db.users.find().sort('highScore', -1)
    return render_template('highScores.html', players=players)

api = Api(app)
api.add_resource(Score, '/score/<string:user_id>')
api.add_resource(BatchScores, '/scores')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

