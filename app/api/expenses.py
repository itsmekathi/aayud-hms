from . import api
from flask import request, flash, jsonify
from app import db
from app.models import ExpenseTypeLu, ExpenseCategoryLu, UnitOfMeasurementLu, Expenses, ExpenseDetails
from app.api.errors import unauthorized
from flask_login import current_user
from .authentication import auth


@api.route('/expenses/types/<int:type_id>', methods=['GET', 'DELETE', 'POST'])
def types(type_id):
    expense_type = ExpenseTypeLu.query.get_or_404(type_id)
    if request.method == "GET":
        return jsonify(expense_type.to_json())
    if request.method == "DELETE":
        db.session.delete(expense_type)
        db.session.commit()
        return jsonify({'status': 'deleted'})
    if request.method == "POST":
        # Code to update the entity
        pass


@api.route('/expenses/categories/<int:category_id>', methods=['GET', 'DELETE', 'POST'])
def categories(category_id):
    expenses_category = ExpenseCategoryLu.query.get_or_404(category_id)
    if request.method == "GET":
        return jsonify(category_id.to_json())
    if request.method == "DELETE":
        db.session.delete(expenses_category)
        db.session.commit()
        return jsonify({'status': 'deleted'})
    if request.method == "POST":
        # Code to update the entity
        pass


@api.route('/expenses/uoms/<int:uom_id>', methods=['GET', 'DELETE', 'POST'])
def uoms(uom_id):
    expenses_uom = UnitOfMeasurementLu.query.get_or_404(uom_id)
    if request.method == "GET":
        return jsonify(expenses_uom.to_json())
    if request.method == "DELETE":
        db.session.delete(expenses_uom)
        db.session.commit()
        return jsonify({'status': 'deleted'})
    if request.method == "POST":
        # Code to update the entity
        pass


@api.route('/expenses/<int:expenses_id>', methods=['GET', 'DELETE', 'POST'])
def expense(expenses_id):
    expense = Expenses.query.get_or_404(expenses_id)
    if request.method == "GET":
        return jsonify(expense.to_json())
    if request.method == "DELETE":
        db.session.delete(expense)
        db.session.commit()
        return jsonify({'status': 'deleted'})
    if request.method == "POST":
        # Code to update the entity
        pass


@api.route('/expenses/details/<int:expense_details_id>', methods=['GET', 'DELETE', 'POST'])
def details(expense_details_id):
    expense_detail = ExpenseDetails.query.get_or_404(expense_details_id)
    if request.method == "GET":
        return jsonify(expense_detail.to_json())
    if request.method == "DELETE":
        db.session.delete(expense_detail)
        db.session.commit()
        return jsonify({'status': 'deleted'})
    if request.method == "POST":
        # Code to update the entity
        pass
