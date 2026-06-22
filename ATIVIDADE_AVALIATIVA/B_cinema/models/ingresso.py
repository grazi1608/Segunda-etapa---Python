from . import db
from .base import ModeloBase


class Ingresso(ModeloBase):
    """Opcional — vale ponto extra se implementar compra de ingresso."""

    __tablename__ = "ingressos"

    # TODO ALUNO: FK sessao_id → sessoes.id #
    assento = db.Column(db.String(10), nullable=False)
    nome_comprador = db.Column(db.String(120), nullable=False)
    sessao_id = db.Column(db.Integer, db.ForeignKey('sessoes.id'), nullable=False) # chave estrangeira 
    sessao = db.relationship('Sessao', backref='ingressos', lazy=True) # faz relacionamento com a sessão EU ACHO
    # TODO ALUNO: relationship sessao
