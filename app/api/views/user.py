from flask.views import MethodView
from flask import request, jsonify
from app import db,Session, engine
from app.models import UserDB, IdTypeDB
from kanpai import Kanpai
from sqlalchemy import inspect
import uuid

session = Session()

class UserView(MethodView):

    def get(self, *args, **kwargs):
        q = session.query(UserDB.username, UserDB.email).all()
        print(q)
        return '''<h1>The language value is: {}</h1>'''.format(q)

    def post(self, *args, **kwargs):

        schema = Kanpai.Object({
            "username" : ( Kanpai . String ( error = 'User first name must be string.' ) 
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
                       . max ( 13 ,  error = 'Maximum allowed length is 13' )),
            "gender": (Kanpai.String(). trim () ),
            "firstname": Kanpai . String ( error = 'User phone number must be string.' ),
            "surename": Kanpai . String ( error = 'User phone number must be string.' ),
            "DOB": (Kanpai.String(). trim () ),
            "idname": Kanpai.String(error="It's not required")
        })

        data = request.get_json()
        validation_result = schema.validate(data)

        if validation_result.get('success', False) is False:
            return jsonify({
                "status": "Error",
                "errors" : validation_result.get("error")
            })
        if data:
            idtypeid = session.query(IdTypeDB).filter_by(name=data['idname']).first()
            user = UserDB(
                username=data['username'],
                email=data['email'] if data['email'] else 'sharan@gmail.com',
                phone=data['phone'],
                gender=data['gender'],
                firstname=data['firstname'],
                surename=data['surename'],
                DOB=data['DOB'],
                idnumber=idtypeid.id
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
