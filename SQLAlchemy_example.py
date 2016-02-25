import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pet(Base):
	__tablename__ = "pet"
	id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True) 
	type = sqla.Column(sqla.String(16))
	breed = sqla.Column(sqla.String(32)) 
	gender = sqla.Column(sqla.Enum("Male", "Female")) 
	name = sqla.Column(sqla.String(64))

sqlite3_engine = sqla.create_engine('sqlite:///pet.db')
Base.metadata.create_all(sqlite3_engine)

pet = Pet()
pet.type = 'cat'
pet.breed = 'syberian'
pet.gender = 'Female'
pet.name = 'Zuza'

Session = sqla.orm.sessionmaker(bind=sqlite3_engine)
session = Session()
session.add(pet)
try:
	session.commit()
except sqla.exc.IntegrityError as e:
	session.rollback()
	print(pet.name, "is already in DB")

result = session.query(Pet).filter_by(name="Zuza").one()
print(result.id, result.type, result.breed, result.gender, result.name)
