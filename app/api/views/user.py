from flask.views import MethodView
from flask import request, jsonify
from app import db
from app.models import UserDB


class User(MethodView):

    def get(self):
        return jsonify({"name": "Sharan"})

    def post(self):
        data = request.get_json()
        if data:
            user = UserDB(
                id=data['id'],
                name=data['name'],
                email=data['email'] if data['email'] else 'sharan@gmail.com',
                phone=data['phone'],
                createdon=data['createdon']
            )
            db.add(user)
            db.commit()
            return jsonify({"user": data['name']})

    def put(self):
        pass

    def delete(self):
        pass
