import sqlalchemy as db
from persistence.model import Auth_User
from sqlalchemy.orm import Session

class AuthUserRepository():
    def __init__(self):
        self.engine = db.create_engine('sqlite:///db/login.sqlite', echo = False, future = True)

    def getUserByUserName(self, user_name: str):
        user: Auth_User = None
        with Session(self.engine) as session:
            user = session.query(Auth_User).filter_by(username = user_name).first()
            return 
        
    def insertUser(self, user: Auth_User):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()