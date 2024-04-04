from models import Base
from connect import engine

if not engine.dialect.has_table(engine.connect(), "skins"):
    Base.metadata.create_all(bind=engine)
else:
    print('Tables exists..')