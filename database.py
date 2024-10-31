from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

#לעדכן את הכתובת
URI =  "postgresql://admin:1234@localhost:5437/missions_db"
#יצירת החיבור והרצת הדאטאבייס
#convert_unicode: עוזר להבין את השם של הURI גם אם יש שם סימנים בעייתים
engine = create_engine(URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def init_db():
    import models
    Base.metadata.create_all(bind=engine)