from flask import request, jsonify

from typing import Dict

from app.news.models import News
from app.utils.decorators import logging_decorator, check_exist_by_id, sort
from app.utils import create_response, news_sort

@logging_decorator
@sort(News, news_sort)
def get_all_news(*args, **kwargs) -> Dict[str, any]:
    params_dict = kwargs.get('params_dict')
    news = kwargs.get('obj')

    if {'Count', 'Page'}.issubset(params_dict.keys()):
        count = int(params_dict.get('Count'))
        page = int(params_dict.get('Page'))
        if count > 0 and page > 0:
            news = news[(page - 1) * count : page * count]
        else:
            raise ValueError("Count and Page must be greater than zero")    
    
    return create_response(code=200, data=news)

@logging_decorator
@sort(News, news_sort)
def delete_all_news(*args, **kwargs) -> Dict[str, any]:
    news = kwargs.get('obj')
    news.delete()
    return create_response(code=204, message=f'News is deleted. Total deleted {len(args[0])} news')

@logging_decorator
def create_news() -> Dict[str, any]:
    body = request.get_json()
    new_news = News(**body)
    new_news.save()

    return create_response(code=201, message=f'News is added. Id: {new_news.id}')

@logging_decorator
@check_exist_by_id(model=News)
def get_news(id:str, *args, **kwargs) -> Dict[str, any]:
    news = kwargs.get('obj')
    return create_response(code=200, data=news)

@logging_decorator
@check_exist_by_id(model=News)
def delete_news(id: str, *args, **kwargs) -> Dict[str, any]:
    news = kwargs.get('obj')
    news.delete()
    return create_response(code=204, message=f"News with id: {id} is deleted")

@logging_decorator
@check_exist_by_id(model=News)
def update_news(id: str, *args, **kwargs) -> Dict[str, any]:
    body = request.get_json()
    news = kwargs.get('obj')
    news.modify(**body)
    return create_response(code=204, message=f"News with id: {id} is updated by: {body}")

@logging_decorator
def get_news_statistic() -> Dict[str, any]:
    lenght = len(News.objects())
    Page = int(lenght / 15)
    if lenght % 15 > 0:
        Page += 1
    return create_response(code=200, data={"Page": Page, "Count": lenght})


