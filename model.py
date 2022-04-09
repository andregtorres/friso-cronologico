from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from sqlalchemy import *
 
Base = declarative_base()

evento_tag = Table(
    "evento_tag",
    Base.metadata,
    Column("fk_evento", Integer, ForeignKey("evento.id")),
    Column("fk_tag", Integer, ForeignKey("tag.id")),
)

evento_ponto = Table(
    "evento_ponto",
    Base.metadata,
    Column("fk_evento", Integer, ForeignKey("evento.id")),
    Column("fk_ponto", Integer, ForeignKey("ponto.id")),
)

 
class Evento(Base):
    __tablename__ = 'evento'

    id = Column(Integer, primary_key=True)
    nome = Column(String(250), nullable=False)
    n= Column(Integer,nullable=False)
    m= Column(Integer,nullable=False)
    split=Column(Integer,nullable=True)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    categoria = relationship("Categoria",backref="eventos")
    nacionalidade_id = Column(Integer, ForeignKey('nacionalidade.id'))
    nacionalidade = relationship("Nacionalidade", backref="eventos")
    #tag_id = Column(Integer, ForeignKey('tag.id'))
    #tags = relationship("Tag")
    #ponto_id = Column(Integer, ForeignKey('ponto.id'))
    #pontos = relationship("Ponto")

    tags = relationship(
        "Tag", backref="evento",secondary=evento_tag)
    pontos = relationship(
        "Ponto", backref="evento",secondary=evento_ponto)


    def mostrar(self):
        print ("id: {}".format(self.id))
        print ("Nome: {}".format(self.nome))
        print ("n: {}".format(self.n))
        print ("m: {}".format(self.m))
        print ("Split: {}".format(self.split))
        print ("Nacionalidade: {}".format(self.nacionalidade))
        print ("Categoria: {}".format(self.categoria))
        print ("Tags: {}".format(self.tags))
        print ("Pontos: {}".format(self.pontos))

    def __repr__(self):
        return '<{}>' .format(self.nome)


class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    nome = Column(String(250))
    #eventos_id = Column(Integer, ForeignKey('evento.id'))

    def __repr__(self):
        return '<{}>' .format(self.nome)

class Nacionalidade(Base):
    __tablename__ = 'nacionalidade'

    id = Column(Integer, primary_key=True)
    nome = Column(String(250))
    sigla = Column(String(20))
    #eventos_id = Column(Integer, ForeignKey('evento.id'))

    def __repr__(self):
        return '<{} - {}>' .format(self.sigla, self.nome)

class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    nome = Column(String(250))
    #eventos_id = Column(Integer, ForeignKey('evento.id'))
    #eventos = relationship("Evento",
                    #primaryjoin="Tag.id == Evento.tag_id")

    def __repr__(self):
        return '<{}>' .format( self.nome)

class Ponto(Base):
    __tablename__ = 'ponto'

    id = Column(Integer, primary_key=True)
    nome = Column(String(250))
    ano= Column(Integer)
    #eventos_id = Column(Integer, ForeignKey('evento.id'))

    def __repr__(self):
        return '<{} ({})>' .format( self.nome, self.ano)

engine = create_engine('sqlite:///DB_Friso.db')

Base.metadata.create_all(engine)

