import sqlalchemy as sa
from fh.aalen.data.modelbase import ModelBase
from sqlalchemy.orm import relationship

class Besitzt(ModelBase):
    __tablename__ = 'Besitzt'
    urlaub_id = sa.Column(sa.ForeignKey('Urlaub.id'), primary_key=True)
    urlaubswunsch_id = sa.Column(sa.ForeignKey('Urlaubswunsch.id'), primary_key=True)