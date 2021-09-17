from flask import Blueprint, request, jsonify, json

import app.news.funcs as funcs

from app.news.models import News

module = Blueprint('news', __name__, url_prefix ='/news')

@module.route("/", methods=['GET', 'POST', 'DELETE'])
def get_post_all_news():
    actions = {
        'DELETE': funcs.delete_all_news,
        'POST': funcs.create_news,
        'GET': funcs.get_all_news
    }
    return actions.get(request.method)()

@module.route("/<string:id>/", methods=['GET', 'PUT', 'DELETE'])
def get_put_delete_news(id):
    actions = {
        'PUT': funcs.update_news,
        'DELETE': funcs.delete_news,
        'GET': funcs.get_news
    }
    return actions.get(request.method)(id)

@module.route("/statistic/", methods=["GET"])
def get_api_statistic():
    actions = {
        'GET': funcs.get_news_statistic
    }
    return actions.get(request.method)()
    
