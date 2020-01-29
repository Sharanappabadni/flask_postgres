from app import app
from flask import jsonify, request
from .views import (
    IdTypeView, UserView, RoleView, UserRoleView,
    CorperateAccountView, BankCodeView, BranchCodeView 
)

idtype_view = IdTypeView.as_view('idtype_view')
user_view = UserView.as_view('user_view')
role_view = RoleView.as_view('role_view')
user_role_view = UserRoleView.as_view('user_role_view')
corperate_account_view = CorperateAccountView.as_view('corperate_account_view')
bank_view = BankCodeView.as_view('bank_view')
branch_view = BranchCodeView.as_view("branch_view")

app.add_url_rule(
    '/user', methods=['GET', 'POST'], view_func=user_view
)

app.add_url_rule(
    '/idtype', methods=['GET', 'POST'], view_func=idtype_view
)

app.add_url_rule(
    '/role', methods=['GET', 'POST'], view_func=role_view
)

app.add_url_rule(
    '/userrole', methods=['GET', 'POST'], view_func=user_role_view
)

app.add_url_rule(
    '/corpaccount', methods=['GET', 'POST'], view_func=corperate_account_view
)

app.add_url_rule(
    '/bank', methods=['GET', 'POST'], view_func=bank_view
)

app.add_url_rule(
    '/branch', methods=['GET', 'POST'], view_func=branch_view
)