from flask.views import MethodView
from flask import request, jsonify
from app import db
from app.models import UserDB
from kanpai import Kanpai

class User(MethodView):

    def get(self):
        return jsonify({"name": "Sharan"})

    def post(self):

        schema = Kanpai.Object({
            "name" : ( Kanpai . String ( error = 'User first name must be string.' ) 
                       . trim () 
                       . required ( error = 'Please provide user first name.' ) 
                       . max ( 32 ,  error = 'Maximum allowed length is 32' )),

            "email": ( Kanpai . Email ( error = 'User email must be proper.' ) 
                       . trim () 
                       . required ( error = 'Please provide user email.' ) 
                       . max ( 32 ,  error = 'Maximum allowed length is 32' )),

            "phone": ( Kanpai . String ( error = 'User phone number must be string.' ) 
                       . trim () 
                       . required ( error = 'Please provide user phone number.' ) 
                       . max ( 13 ,  error = 'Maximum allowed length is 13' ))
        })

        data = request.get_json()
        validation_result = schema.validate(data)

        if validation_result.get('success', False) is False:
            return jsonify({
                "status": "Error",
                "errors" : validation_result.get("error")
            })
        if data:
            user = UserDB(
                name=data['name'],
                email=data['email'] if data['email'] else 'sharan@gmail.com',
                phone=data['phone']
            )
            db.add(user)
            db.commit()
            return jsonify({
                "statu": "success",
                "data": validation_result["data"]
            })

    def put(self):
        pass

    def delete(self):
        pass
