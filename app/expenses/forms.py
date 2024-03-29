from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField, DateTimeField, \
    BooleanField, DecimalField, SelectMultipleField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError, Email
from wtforms.fields import DateField, TimeField


class ExpenseTypeLuForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(
        min=1, max=100, message="Maximum length for name is 100 characters")])
    description = TextAreaField('Description', validators=[DataRequired(
    ), Length(min=1, max=300, message="Maximum length for description is 300 characters.")], render_kw={"placeholder": "Description", "rows": "3"})
    icon = StringField('Icon', validators=[DataRequired(), Length(
        min=1, max=100, message='Icon length exceeds the specified lenght of 100')])
    style_class = StringField('Style Class', validators=[DataRequired(), Length(
        min=1, max=100, message='Style class length exceeds the specified lenght of 100')])
    submit = SubmitField('Create')


class ExpenseCategoryLuForm(ExpenseTypeLuForm):
    pass


class UOMForm(ExpenseTypeLuForm):
    pass


class ExpenseFilterForm(FlaskForm):
    contact_id = SelectField('Expense Contact', coerce=int)
    type_id = SelectField('Expense Types', coerce=int)
    category_id = SelectField('Expense Category', coerce=int)
    from_date = DateField('Expense From Date', validators=[
                          DataRequired()], render_kw={"placeholder": "MM/dd/YYYY"})
    to_date = DateField('Expense To Date', validators=[
                        DataRequired()], render_kw={"placeholder": "MM/dd/YYYY"})
    submit = SubmitField('Search')


class ExpenseForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(
        min=1, max=100, message="Maximum length for title is 100 characters")])
    contact_id = SelectField('Expense Contact', coerce=int)
    type_id = SelectField('Expense Type', coerce=int,
                          validators=[DataRequired()])
    category_id = SelectField('Expense Category', coerce=int,
                              validators=[DataRequired()])
    expense_amount = DecimalField(
        'Expense amount', places=2, validators=[DataRequired()])
    expense_date = DateField(
        'Expense Date time', validators=[DataRequired()], render_kw={"placeholder": "MM/dd/YYYY"})
    expense_time = TimeField(
        'Expense time', validators=[DataRequired()], render_kw={"placeholder": "HH:MM:SS"})
    description = TextAreaField('Description', validators=[DataRequired(), Length(
        max=300)], render_kw={"placeholder": "Description", "rows": "3"})

class AddExpenseForm(ExpenseForm):
    submit = SubmitField('Create')

class EditExpenseForm(ExpenseForm):
    submit = SubmitField('Update')


class ExpenseItemForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired(), Length(
        min=1, max=200, message="Maximum length of title is 200 characters")])
    uom_id = SelectField('UOM',
                         coerce=int, validators=[DataRequired()])
    unit_price = DecimalField(
        'Unit Price', places=2, validators=[DataRequired()])
    quantity = DecimalField(
        'Quantity', places=2, validators=[DataRequired()])
    gross_price = DecimalField(
        'Gross Price', places=2, validators=[DataRequired()])

class AddExpenseItemForm(ExpenseItemForm):
    submit = SubmitField('Create')

class EditExpenseItemForm(ExpenseItemForm):
    submit = SubmitField('Update')
