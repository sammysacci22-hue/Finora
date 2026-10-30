from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def dashboard():
    return render_template('index.html')


@main.route('/transactions')
def transactions():
    return "Finora Transactions"


@main.route('/budgets')
def budgets():
    return "Finora Budgets"
