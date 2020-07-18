import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine('mysql+mysqlconnector://Soty89:Bespredel0@localhost:3306/wine',echo=True)

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String(length=50))
  fullname = Column(String(length=50))
  nickname = Column(String(length=50))

  def __repr__(self):
    return "<User(name='{0}', fullname='{1}', nickname='{2}')>".format(self.name, self.fullname, self.nickname)

class ven_prod(Base):
    __tablename__ = 'vendor_products'

    id

Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

jwk_user = User(name='jesper', fullname='Jesper Wisborg Krogh', nickname='Toto')
session.add(jwk_user)
session.commit()
