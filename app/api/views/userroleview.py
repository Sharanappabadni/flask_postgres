from flask.views import MethodView
from flask import request, jsonify
from app import db, Session, engine
from app.models import UserRoleDB, IdTypeDB, UserDB, RoleDB
from kanpai import Kanpai
from .baseview import Validations

session = Session()

class UserRoleView(MethodView, Validations):

    def get(self, *args, **kwargs):
        
        data = session.query(UserRoleDB.username, UserRoleDB.roledesc, UserRoleDB.status).all()

        return jsonify({
            "data":tuple(data)
        })


    def post(self, *args, **kwargs):

        data = request.get_json()

        username = data.get("username", "")
        roledesc = data.get("roledesc", "")
        status = data.get("status", "")

        schema = Kanpai.Object({
            "username": (Kanpai.String(error="user name should be string")
                        .trim().required(error="user name should required")
                        . max (32, error="should not be more than 32 characters")),

            "roledesc": (Kanpai.String(error="role desc should be string")
                        .trim().required(error="role desc should required")
                        . max (32, error="should not be more than 32 characters")),

            "status": (Kanpai.String(error="role desc should be string")
                        .trim().required(error="role desc should required")
                        . max (32, error="should not be more than 32 characters"))
        })

        validation_results = schema.validate(data)

        Validations.validate_error(obj=validation_results)

        check_username_indb = session.query(UserDB).filter_by(username=username).first()
        check_roledesc_indb = session.query(RoleDB).filter_by(roledesc=roledesc).first()
        
        if not check_username_indb:
            return jsonify({
                "status": "error",
                "errors": f"user {check_username_indb} not present in db"
            })
        
        if not check_roledesc_indb:
            return jsonify({
                "status": "error",
                "errors": f"role description {check_roledesc_indb} not present in db"
            })
        
        if data:
            userrole = UserRoleDB(
                userid=check_username_indb.id,
                roleid=check_roledesc_indb.id,
                status=status
            )

            db.add(userrole)
            db.commit()

            return jsonify({
                "status": "success",
                "data": validation_results["data"]
            })
    
    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass



        
