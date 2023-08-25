from flask import request
from flask_restx import Resource, Namespace

from model.movie import MovieSchema
from implemented import movie_service
from utils import admin_required, auth_required

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self):
        data = {
            'stattus': request.args.get('stattus'),
            'page': request.args.get('page')
        }
        movis = movie_service.get_all_movies(data)
        return movis, 200


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    @auth_required
    def get(self, bid):
        movie = movie_service.get_by_id(bid)

        if not movie:
            return "movie not found"
        return movie




