from flask.views import MethodView
from flask import request, jsonify
from app import db, Session, engine
from app.models import RoleDB
from kanpai import Kanpai

session = Session()

class RoleView(MethodView):

    def get(self, *args, **kwargs):

        data = session.query(RoleDB.rolecode, RoleDB.roledesc, RoleDB.status).all()

        return jsonify({
            "data":tuple(data)
        })

    def post(self, *args, **kwargs):

        data = request.get_json()

        schema = Kanpai.Object({
            "rolecode": (Kanpai.Number().integer().between(1, 10)),
            "roledesc": (Kanpai.String(error="Role desc should be String")
                         .trim()
                         .required(error="Role code is required")),
            "status": (Kanpai.String(error="Role desc should be active, deactive")
                         .trim()
                         .required(error="Role code is required"))
        })

        validation_results = schema.validate(data)

        if validation_results.get('success', False) is False:
            return jsonify({
                "status": "error",
                "errors": validation_results.get('error')
            })

        is_role_duplcate = session.query(RoleDB).filter_by(rolecode=data['rolecode']).first()
        
        if is_role_duplcate:
            return jsonify({
                "status": "error",
                "errors": f"role code {is_role_duplcate.rolecode} already present"
            })
            
        if data:
            role = RoleDB(
                rolecode = data['rolecode'],
                roledesc = data['roledesc'],
                status = data['status']
            )

            db.add(role)
            db.commit()
            return jsonify({
                "status": "success",
                "data": validation_results["data"]
            })
    
    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass