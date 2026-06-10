from datetime import datetime

from . import db


class Operacao(db.Model):
    """Model — dados e acesso ao banco (tabela operacoes)."""

    __tablename__ = "operacoes"
    # insira as operações
    """model dados e bancio de dados """

    __tablename__ = "operacoes"


    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Float, nullable=False)
    num2 = db.Column(db.Float, nullable=False)
    Operacao = db.Column(db.String(100), nullable=False )
    Resultado = db.Column(db.String(100), nullable=False )
    criado_em = db.Column(db.DateTime, nullable=False, default=0)


    @classmethod
    def salvar(cls, num1, num2, operacao, etapas, resultado):
        registro = cls(
            num1=num1,
            num2=num2,
            operacao=operacao,
            etapas=etapas,
            resultado=str(resultado),
        )
        #insira os comandos par salvar
        db.session.add(registro)
        db.session.commit()
        return registro


    @classmethod
    def listar_recentes(cls, limite=10):
        return (
            cls.query.order_by(cls.criado_em.desc()).limit(limite).all()
        )

    def __repr__(self):
        return f"<Operacao {self.id}: {self.etapas}>"