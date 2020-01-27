from flask import jsonify

class Validations:

    def validate_error(obj):
        if obj.get('success', False) is False:
            return jsonify({
                "status": "error",
                "errors": obj.get('error')
                })
    
    def validate_success(obj):
        return jsonify({
            "status": "success",
            "data": obj.get('data')
           })