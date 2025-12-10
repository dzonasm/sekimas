from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='expenses')

@app.route('/')
def index():
    category_filter = request.args.get('category')
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    
    query = Expense.query
    
    if category_filter:
        query = query.filter_by(category_id=category_filter)
    if date_from:
        query = query.filter(Expense.date >= datetime.strptime(date_from, '%Y-%m-%d').date())
    if date_to:
        query = query.filter(Expense.date <= datetime.strptime(date_to, '%Y-%m-%d').date())
    
    expense_list = query.order_by(Expense.date.desc()).all()
    categories = Category.query.all()
    
    total = sum(expense.amount for expense in expense_list)
    
    return render_template('base.html', 
                         expense_list=expense_list, 
                         categories=categories,
                         total=total)

@app.route('/expense/create', methods=["POST"])
def add_expense():
    amount = request.form.get("amount")
    description = request.form.get("description")
    date_str = request.form.get("date")
    category_id = request.form.get("category_id")
    
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    
    new_expense = Expense(
        amount=float(amount),
        description=description,
        date=date_obj,
        category_id=int(category_id)
    )
    
    with app.app_context():
        db.session.add(new_expense)
        db.session.commit()
    
    return redirect(url_for("index"))

@app.route('/expense/delete/<int:expense_id>')
def delete_expense(expense_id):
    with app.app_context():
        expense = Expense.query.filter_by(id=expense_id).first()
        db.session.delete(expense)
        db.session.commit()
    
    return redirect(url_for("index"))

@app.route('/categories')
def categories():
    category_list = Category.query.all()
    return render_template('categories.html', category_list=category_list)

@app.route('/category/create', methods=["POST"])
def add_category():
    name = request.form.get("name")
    new_category = Category(name=name)
    
    with app.app_context():
        db.session.add(new_category)
        db.session.commit()
    
    return redirect(url_for("categories"))

@app.route('/category/delete/<int:category_id>')
def delete_category(category_id):
    with app.app_context():
        category = Category.query.filter_by(id=category_id).first()
        db.session.delete(category)
        db.session.commit()
    
    return redirect(url_for("categories"))

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
        # Create default categories if database is empty
        if Category.query.count() == 0:
            default_categories = ["Food", "Transport", "Entertainment", "Bills", "Other"]
            for cat_name in default_categories:
                db.session.add(Category(name=cat_name))
            db.session.commit()
    
    app.run(debug=True)
