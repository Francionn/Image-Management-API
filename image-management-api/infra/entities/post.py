from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, LargeBinary, text
import base64


class Db_post(Base):
    __tablename__ = "db_post"

    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(LargeBinary, nullable=False)
    descrip = Column(String(50))
    action_time = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

    def __repr__(self):
        return f'{self.image}\n{self.descrip}\n{self.action_time}\nid={self.id}\n'
    
    def __init__(self, image, descrip):
        self.image = image
        self.descrip = descrip
    
    def to_dict(self):
        image_base64 = base64.b64encode(self.image).decode('utf-8') if self.image else None
        return {
            'id': self.id,
            'image': image_base64,
            'descrip': self.descrip,
            'action_time': self.action_time.isoformat()
        }