import sqlalchemy as sa
from fh.aalen.data.modelbase import ModelBase
from sqlalchemy.orm import relationship

class Priorisiert(ModelBase):
    __tablename__ = 'Priorisiert'
    familienmitglied_id = sa.Column(sa.ForeignKey('Familienmitglied.id'), primary_key=True)
    urlaubswunsch_id = sa.Column(sa.ForeignKey('Urlaubswunsch.id'), primary_key=True)