#!/usr/bin/python3
""" drugs model """
from healthapp.models.base import BaseModel
from healthapp import db


users_drugs = db.Table('users_drugs',
                       db.Column('user_id', db.Integer,
                                 db.ForeignKey('user.id')),
                       db.Column('drug_id', db.Integer,
                                 db.ForeignKey('drug.id')))


class Drug(BaseModel, db.Model):
    """ class meds models """
    __tablename__ = 'drug'
    name = db.Column(db.String(255), nullable=False)
    user = db.relationship('User', secondary=users_drugs, back_populates="drug")

    def __init__(self, name, user):
        """ init class """
        self.name = name
        self.user = user
