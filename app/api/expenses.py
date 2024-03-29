from . import api
from flask import request, flash, jsonify
from app import db
from app.models import ExpenseTypeLu, ExpenseCategoryLu, UnitOfMeasurementLu, Expenses, ExpenseDetails


@api.route('/expenses/types/<int:type_id>', methods=['GET', 'DELETE', 'POST'])
def expenses_types(type_id):
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
def expenses_categories(category_id):
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
def expenses_uoms(uom_id):
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
        ExpenseDetails.query.filter_by(expenses_id=expenses_id).delete()
        db.session.delete(expense)
        db.session.commit()
        return jsonify({'status': 'deleted'})
    if request.method == "POST":
        # Code to update the entity
        pass

