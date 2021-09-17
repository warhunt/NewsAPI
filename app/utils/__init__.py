from typing import Dict
from typing import Dict

from datetime import datetime, timedelta

from flask import jsonify

def create_response(code, data = None, message: str = "", error: int = 0):
    return jsonify({"Data": data, "Message": message, "Error": error}), code

def news_sort(params_dict: Dict):
    sort = {}

    if 'From' in params_dict.keys():
        sort['news_from'] = params_dict.get('From')

    if 'To' in params_dict.keys()in params_dict.keys():
        sort['news_to'] = params_dict.get('To')

    if 'DateFrom' in params_dict.keys():
        sort['date__gte'] = params_dict.get('DateFrom')

    if 'DateTo' in params_dict.keys():
        format = "%Y-%m-%d"
        date = datetime.strptime(params_dict.get('DateTo'), format)
        date += timedelta(days=1)
        sort['date__lte'] = date.strftime(format)

    return sort