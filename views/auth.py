from flask import request
from flask_restx import Resource, Namespace
from implemented import user_service, auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthRegisterView(Resource):
    def post(self):
        data = request.json

        if not data.get('email') or not data.get('password'):
            return {'error': 'нет данных'}, 400
        user_service.create(data)

        return '', 201


@auth_ns.route('/login/')
class AuthLoginView(Resource):
    def post(self):
        reg_json = request.json

        email = reg_json.get('email')
        password = reg_json.get('password')

        if not email or not password:
            return {'error': 'нет данных'}, 400

        tokens = auth_service.auth_user(email, password)

        if not tokens:
            return {'error': 'ошибка в логине или пароле'}, 401

        return tokens, 201

    def put(self):
        reg_json = request.json
        refresh_token = reg_json.get('refresh_token')
        if not refresh_token:
            return {'error': 'нет данных'}, 400
        tokens = auth_service.check_refresh_token(refresh_token)

        return tokens, 201
