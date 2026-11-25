from flask import jsonify

def api_response(
    success=True,
    message="Success",
    data=None,
    status_code=200
):

    response = {
        "success": success,
        "message": message,
        "data": data
    }

    return jsonify(response), status_code