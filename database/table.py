import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database.config import engine


Base = declarative_base()
Session = sessionmaker(bind=engine)


class Products(Base):
    __tablename__ = "products"

    id = sq.Column(sq.Integer, primary_key=True)
    category = sq.Column(sq.String(50), nullable=False)
    img = sq.Column(sq.String(50), nullable=False)
    model = sq.Column(sq.String(50), nullable=False)
    name = sq.Column(sq.String(50), nullable=False)
    price = sq.Column(sq.String(50), nullable=False)


if __name__ == "__main__":
    session = Session()
    Base.metadata.create_all(engine)
    print('finish')