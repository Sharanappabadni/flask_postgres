from flask.views import MethodView
from flask import request, jsonify
from app import engine, db, Session
from app.models import BankCodeDB, BranchCodeDB
from kanpai import Kanpai
from .baseview import Validations

session = Session()

class BranchCodeView(MethodView, Validations):

    def get(self, *args, **kwargs):
        data = session.query(BranchCodeDB.branchname, BranchCodeDB.branchaddress).all()

        return jsonify({
            "data": data
        })
    
    def post(self, *args, **kwargs):

        data = request.get_json()

        bankname = data.get("bankname", "")
        branchname = data.get("branchname", "")
        branchaddress = data.get("branchaddress", "")

        schema = Kanpai.Object({
            "bankname": (Kanpai.String().required().max(32)),
            "branchname": (Kanpai.String().required()),
            "branchaddress": (Kanpai.String().required())
        })

        validation_results = schema.validate(data)

        Validations.validate_error(validation_results)

        bankcode = session.query(BankCodeDB).filter_by(bankname=bankname).first()
        if not bankcode:
            return jsonify({
                "status": "error",
                "errors": f"user {bankname} not present in db"
            })

        if data:
            branchcode = BranchCodeDB(
                bankcode = bankcode,
                branchname = branchname,
                branchaddress = branchaddress
            )
            db.add(branchcode)
            db.commit()

            return jsonify({
                "status": "success",
                "data": validation_results["data"]
            })
    
    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass