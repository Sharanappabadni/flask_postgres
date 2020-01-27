from flask.views import MethodView
from flask import request, jsonify
from app import db, Session, engine
from app.models import IdTypeDB
from kanpai import Kanpai
from sqlalchemy import inspect

session = Session()

class IdTypeView(MethodView):

    def get(self, *args, **kwargs):

        ids = session.query(IdTypeDB.name, IdTypeDB.idnumber).all()

        return jsonify({
            "idtypes": ids
        })

    def post(self, *args, **kwargs):

        schema = Kanpai.Object({
            'name' : (Kanpai.String(error = "Description should be string")
                      .trim().required(error="Description should required")
                      .max(64, error="Should not be more than 64 characters")),
            'idnumber' : (Kanpai.String(error = "Description should be string")
                      .trim().required(error="Description should required")
                      .max(64, error="Should not be more than 64 characters"))
        })

        data = request.get_json()
        validation_result = schema.validate(data)
        if validation_result.get('success', False) is False:
            return jsonify({
                "status": "error",
                "errors": validation_result.get('error')
            })

        if data:
            idtype = IdTypeDB(
                name = data['name'],
                idnumber = data['idnumber']
            )
            db.add(idtype)
            db.commit()
            return jsonify({
                "status": "success",
                "result": validation_result['data']
            })
    
    
    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass
        