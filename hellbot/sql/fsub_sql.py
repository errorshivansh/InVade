import threading
from sqlalchemy import Column, String, UnicodeText, distinct, func
from . import BASE, SESSION

class Fsub(BASE):
    __tablename__ = "fsub"
    chat_id = Column(String(14), primary_key=True)
    hunter = Column(String(14), primary_key=True, nullable=False)

    def __init__(self, chat_id, hunter):
        self.chat_id = str(chat_id)
        self.hunter = str(hunter)
  
    def __eq__(self, other):
        return bool(
            isinstance(other, Fsub)
            and self.chat_id == other.chat_id
            and self.hunter == other.hunter
        )


Fsub.__table__.create(checkfirst=True)


def is_fsub(chat_id):
    try:
        return SESSION.query(Fsub).filter(Fsub.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def add_fsub(chat_id, hunter):
    adder = Fsub(str(chat_id), str(hunter))
    SESSION.add(adder)
    SESSION.commit()


def rem_fsub(chat_id):
    rem = SESSION.query(Fsub).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def all_fsub():
    rem = SESSION.query(Fsub).all()
    SESSION.close()
    return rem
