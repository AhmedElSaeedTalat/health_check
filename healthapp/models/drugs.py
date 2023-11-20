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
    users = db.relationship('User', secondary=users_drugs, lazy='subquery',
                            backref=db.backref('drug', lazy=True))
