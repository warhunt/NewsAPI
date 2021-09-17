from dataclasses import dataclass
from datetime import datetime

from app.database import db

class News(db.Document):
    header = db.StringField(required=True)
    news_from = db.StringField(required=True, default="ВА РБ")
    news_to = db.StringField(required=True, default="Всем")
    date = db.DateTimeField(required=True, default=datetime.utcnow)
    text = db.ListField(field=db.StringField(), required=True)
    link = db.StringField(required=False)

    meta = {
        'name': 'News'
    }