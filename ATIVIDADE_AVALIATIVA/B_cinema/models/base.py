# terminar

from datetime import datetime

from . import db


class ModeloBase(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.DateTime, default=datetime.now, nullable=False)
    duracao_min = db.Column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )