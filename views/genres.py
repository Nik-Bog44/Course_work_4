from flask import request
from flask_restx import Resource, Namespace

from model.genre import GenreSchema
from implemented import genre_service
from utils import auth_required, admin_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        genre = genre_service.get_all()
        res = GenreSchema(many=True).dump(genre)
        return res, 200

    def post(self):
        req_json = request.json
        new_director = genre_service.create(req_json)
        return GenreSchema().dump(new_director), 201

@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @admin_required
    def get(self, rid):
        r = genre_service.get_item_by_id(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    def put(self, rid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = rid
        genre_service.update(req_json)
        return "", 200

    def delete(self, rid):
        genre_service.delete(rid)
        return "", 204
