from datetime import datetime

from db import DB


class Feedback(DB.Model):
    """Feedback
    """
    __tablename__ = 'feedback'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    service = DB.Column(DB.String(255), nullable=False)
    title = DB.Column(DB.String(255), nullable=False)
    detail = DB.Column(DB.String(255), nullable=False)
    created_date = DB.Column(
        DB.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, service, title, detail):
        self.service = service
        self.title = title
        self.detail = detail

    def to_dict(self):
        """to_dict
        """
        return {
            'id': self.id,
            'service': self.service,
            'title': self.title,
            'detail': self.detail,
            'created_date': self.created_date
        }
