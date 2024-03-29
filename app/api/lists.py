from . import api
from flask import request, jsonify
from app import db
from app.models import ListTypeLu, ListHeader, ListItem
from flask_login import current_user
from datetime import datetime


@api.route('/lists', methods=['GET', 'POST'])
def list_headers():
    if request.method == "GET":
        list_headers = ListHeader.query.all()
        return jsonify([list_header.to_json() for list_header in list_headers])
    if request.method == "POST":
        list_header = ListHeader(name=request.json['name'],
                                 type_id=int(request.json['typeId']),
                                 description=request.json['description'],
                                 sort_order=int(request.json['sortOrder']),
                                 created_by_id=current_user.id)
        db.session.add(list_header)
        db.session.commit()
        return jsonify(list_header.to_json())


@api.route('/lists/<int:list_id>', methods=['GET', 'DELETE', 'POST'])
def list_header(list_id):
    list_headers = ListHeader.query.get_or_404(list_id)
    if request.method == "GET":
        return jsonify(list_header.to_json())
    if request.method == "DELETE":
        db.session.delete(list_header)
        db.session.commit()
        return jsonify({'status': 'deleted'})
    if request.method == "POST":
        list_header.name = request.json['name']
        list_header.type_id = int(request.json['typeId'])
        list_header.description = request.json['description']
        list_header.sort_order = int(request.json['sortOrder'])
        list_header.modified_on = datetime.now()
        db.session.commit()
        return jsonify(list_header.to_json())


@api.route('/lists/types', methods=['GET', 'POST'])
def list_types():
    if request.method == "GET":
        list_types = ListTypeLu.query.all()
        return jsonify([list_type.to_json() for list_type in list_types])
    if request.method == "POST":
        ltu = ListTypeLu(name=request.json['listName'],
                         description=request.json['description'],
                         icon=request.json['iconClass'],
                         style_class=request.json['styleClass'],
                         sort_order=int(request.json['sortOrder']))
        db.session.add(ltu)
        db.session.commit()
        return jsonify(ltu.to_json())


@api.route('/lists/types/<int:type_id>', methods=['GET', 'DELETE', 'POST'])
def list_type(type_id):
    list_type = ListTypeLu.query.get_or_404(type_id)
    if request.method == "GET":
        return jsonify(list_type.to_json())
    if request.method == "DELETE":
        db.session.delete(list_type)
        db.session.commit()
        return jsonify({'status': 'deleted'})
    if request.method == "POST":
        list_type.name = request.json['name']
        list_type.description = request.json['description']
        list_type.icon = request.json['icon']
        list_type.style_class = request.json['styleClass']
        list_type.sort_order = request.json['sortOrder']
        db.session.commit()
        return jsonify(list_type.to_json())


@api.route('/lists/<int:list_id>/items', methods=['GET', 'POST'])
def list_item(list_id):
    if request.method == "GET":
        return jsonify([item.to_json() for item in ListItem.query.filter_by(list_id=list_id)])        
    if request.method == "POST":
        """ Updates the entity if POST and Id is valid, create should always be done
        through form
        """
        list_item = ListItem.query.get_or_404(int(request.json["id"]))
        list_item.modified_on = datetime.utcnow()
        list_item.name = request.json['name']
        list_item.description = request.json['description']
        list_item.sort_order = request.json['sortOrder']
        list_item.stars = request.json['stars']
        db.session.commit()
        return jsonify(list_item.to_json())
    
@api.route('/lists/items/<int:item_id>', methods=['DELETE'])
def delete_list_item(item_id):
    """ Deletes the list item entity from table if found
        """
    list_item = ListItem.query.get_or_404(item_id)
    db.session.delete(list_item)
    db.session.commit()
    return jsonify({'status': 'deleted'})
       
