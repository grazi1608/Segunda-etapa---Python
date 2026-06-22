from . import db
from .base import ModeloBase


class Filme(ModeloBase):
    __tablename__ = "filmes"

    titulo = db.Column(db.String(150), nullable=False)
    # TODO ALUNO: relationship sessoes #

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    duracao_min = db.Column(db.Integer(100), nullable=False )
    classificacao = db.Column(db.String(2), nullable=False)
    sessoes = db.relationship('Sessao', backref='filme', lazy=True)
    
    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.titulo).all()
