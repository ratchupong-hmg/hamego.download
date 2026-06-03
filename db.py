# db.py

from sqlalchemy.exc import SQLAlchemyError
from connect import SessionLocal

class DB:

    @staticmethod
    def insert(obj):
        db = SessionLocal()
        try:
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return obj
        except SQLAlchemyError:
            db.rollback()
            raise
        finally:
            db.close()

    @staticmethod
    def update():
        db = SessionLocal()
        try:
            db.commit()
        except SQLAlchemyError:
            db.rollback()
            raise
        finally:
            db.close()

    @staticmethod
    def delete(obj):
        db = SessionLocal()
        try:
            db.delete(obj)
            db.commit()
        except SQLAlchemyError:
            db.rollback()
            raise
        finally:
            db.close()

    @staticmethod
    def session():
        return SessionLocal()