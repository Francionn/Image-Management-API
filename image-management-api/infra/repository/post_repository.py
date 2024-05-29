from infra.configs.connection import DBConnectionHandler
from infra.entities.post import Db_post

class PostRepository:
    
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Db_post).all()
            return data
    
    def insert(self, image, descrip):
        with open(image, 'rb') as file:
            binary_data = file.read()
            data_insert = Db_post(binary_data, descrip)
        
        with DBConnectionHandler() as db:
            db.session.add(data_insert)
            db.session.commit()
            self.reorganize_ids()
    
    def delete(self, id: int):
        with DBConnectionHandler() as db:
            db.session.query(Db_post).filter(Db_post.id == id).delete()
            db.session.commit()
            self.reorganize_ids()
    
    def update(self, id: int, descrip: str):
        with DBConnectionHandler() as db:
            db.session.query(Db_post).filter(Db_post.id == id).update({'descrip': descrip})
            db.session.commit()

    def count(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Db_post).count()
            return data
    
    def reorganize_ids(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Db_post).order_by(Db_post.id).all()
            for index, post in enumerate(data):
                post.id = index + 1
            db.session.commit()