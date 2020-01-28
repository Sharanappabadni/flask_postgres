from flask.views import MethodView 
from flask import jsonify, request
from app import Session, engine, db
from app.models import CorperateAccountDB
from kanpai import Kanpai
from .baseview import Validations

session = Session()

class CorperateAccountView(MethodView, Validations):

    def get(self, *args, **kwargs):
        
        data = session.query(CorperateAccountDB.accountnumber, CorperateAccountDB.accountname).all()

        return jsonify({
            "data":tuple(data)
        })

    def post(self, *args, **kwargs):

        data = request.get_json()

        accountnumber = data.get('accountnumber', "")
        accountname = data.get('accountname', "")

        schema = Kanpai.Object({
            "accountnumber": Kanpai.String().required(),
            "accountname": Kanpai.String().required()
        })

        validation_results = schema.validate(data)

        Validations.validate_error(obj=validation_results)

        is_accountnumber = session.query(CorperateAccountDB).filter_by(accountnumber=accountnumber).first()
        is_accountname = session.query(CorperateAccountDB).filter_by(accountname=accountname).first()

        if is_accountnumber:
            return jsonify({
                "status": "error",
                "errors": f"account number {is_accountnumber} already present"
            })
        
        if is_accountname:
            return jsonify({
                "status": "error",
                "errors": f"account name {is_accountname} already present"
            })
        
        if data:
            corpaccount = CorperateAccountDB(
                accountnumber=accountnumber,
                accountname=accountname
            )

            db.add(corpaccount)
            db.commit()

            return jsonify({
                "status": "success",
                "data": validation_results["data"]
            })
    
    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass
        


