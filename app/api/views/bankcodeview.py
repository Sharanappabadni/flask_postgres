from flask.views import MethodView
from flask import request, jsonify
from app import db, Session, engine
from app.models import BankCodeDB
from kanpai import Kanpai
from .baseview import Validations

session = Session()

class BankCodeView(MethodView):

    def get(self, *args, **kwargs):

        data = session.query(BankCodeDB.bankname, BankCodeDB.universalbranchcode).all()

        return jsonify({
            "data": data
        })
    
    def post(self, *args, **kwargs):

        data = request.get_json()

        bankname = data.get("bankname", '')
        universalbranchcode = data.get("universalbranchcode", "")

        schema = Kanpai.Object({
            "bankname": (Kanpai.String().required().max(32)),
            "universalbranchcode": (Kanpai.String().required())
        })

        validation_results = schema.validate(data)

        Validations.validate_error(validation_results)
        
        if data:
            bankcode = BankCodeDB(
                bankname = bankname,
                universalbranchcode = universalbranchcode
            )
            db.add(bankcode)
            db.commit()

            return jsonify({
                "status": "success",
                "data": validation_results["data"]
             })
    
    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass
