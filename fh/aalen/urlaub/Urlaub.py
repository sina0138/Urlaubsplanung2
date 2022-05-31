import sqlalchemy as sa
from fh.aalen.data.modelbase import ModelBase
from fh.aalen.relations.besitzt import Besitzt

class Urlaub(ModelBase):
    __tablename__ = 'Urlaub'

    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    zeitraum = sa.Column('zeitraum', sa.String, nullable=False)
    titel = sa.Column('titel', sa.String, nullable=False)
    urlaubswuensche = sa.orm.relationship("Besitzt", back_populates="Urlaubswunsch")

    #Helpermethod to create a dictionary representation from video attributes
    def to_dict(self):
        return dict(id=self.id,
                zeitraum=self.zeitraum,
                titel=self.titel,
                urlaubswuensche=self.urlaubswuensche,.
                )
