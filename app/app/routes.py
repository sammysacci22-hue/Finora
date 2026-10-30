from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def dashboard():
    return "Welcome to Finora!"


@main.route('/transactions')
def transactions():
    return "Finora Transactions"


@main.route('/budgets')
def budgets():
    return "Finora Budgets"
