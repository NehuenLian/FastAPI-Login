from sqlalchemy.orm import Session

from app.data_access import models
from app.security.password_utils import hash_password
from app.security.password_utils import \
    verify_password as verify_hashed_password


def get_user_by_username(db: Session, username: str):
    return db.query(models.Users).filter(models.Users.username == username).first()

def verify_password(user: models.Users, input_password: str) -> bool:
    return verify_hashed_password(input_password, user.password)

def create_user(db: Session, username: str, password: str):
    hashed_pw = hash_password(password)
    db_user = models.Users(username=username, password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user