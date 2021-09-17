from functools import wraps

from flask import current_app, request
from app.utils import create_response
from app.database import db

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            current_app.logger.info(f"{func.__name__} is started")
            return func(*args, **kwargs)
        except Exception as ex:
            current_app.logger.warning(ex)
            return create_response(code=400, message=str(ex), error=1)
        finally:
            current_app.logger.info(f"{func.__name__} is finished")
    return wrapper

def check_exist_by_id(model: db.Document):
    def decorator(func):
        @wraps(func)
        def wrapper(id, *args, **kwargs):
            obj = model.objects(id=id)
            if obj:
                return func(id=id,obj=obj)
            else:
                return create_response(code=404, message=f"{model.__name__} with id: {id} is not exist")
        return wrapper
    return decorator

def sort(model: db.Document, sort_func):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            params_dict = request.args.to_dict()

            sort = sort_func(params_dict)

            obj = model.objects(**sort)

            if obj:
                return func(obj=obj, params_dict=params_dict)
            else:
                return create_response(code=404, message=f"{model.__name__} with sort: {sort} is not exist")
        return wrapper
    return decorator

