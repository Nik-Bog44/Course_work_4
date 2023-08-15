from flask import request
from flask_restx import Resource, Namespace
from implemented import user_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        reg_jons = request.json

        username = reg_jons.get('username')
        password = reg_jons.get('password')

        if not username or not password:
            return {'error': 'нет данных'},400
        token = user_service.auth_user(username, password)

        if not token:
            return {'error': 'нет данных'}, 400
        return token,201

    def put(self):
        reg_jons = request.json
        refresh_token = reg_jons.get('refresh_token')
        if not refresh_token:
            return {'error': 'нет данных'}, 400
        return user_service.check_refresh_token(refresh_token),201

