
from flask import Flask, Blueprint, request, make_response, jsonify
from app.api.v1.models import party_model

PARTY = party_model.Party()

party_route = Blueprint('party',__name__,url_prefix='/api/v1/party')
@party_route.route('',methods=['GET'])
def get_parties():
    data = PARTY.get_parties()
    return make_response(jsonify({
        'status':200,
        'data':{"party":data}
    })),200
@party_route.route('/add',methods=['POST'])
def add_party():
  
    try:
        data = request.get_json(force=True)
    except:
        return make_response(jsonify({
            "status":400,
            "message":"wrong input"
        })),400  
    
    name = data['name']
    hqaddress = data['hqaddress']
    logoUrl = data['logoUrl']

    PARTY.add_party(name,hqaddress,logoUrl)
    return make_response(jsonify({
        "status":201,
        "data":[{"message":"success"}]
    })),201

