from app import app
from flask import jsonify, request
from .views import (
    IdTypeView, UserView, RoleView, UserRoleView
)

idtype_view = IdTypeView.as_view('idtype_view')
user_view = UserView.as_view('user_view')
role_view = RoleView.as_view('role_view')
user_role_view = UserRoleView.as_view('user_role_view')

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