from __future__ import annotations
from typing import List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.schema import ForeignKey

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorites: Mapped[list['FavoritesCharacters']
                      ] = relationship(back_populates='user')
    favorites_planets: Mapped[list['FavoritesPlanets']
                              ] = relationship(back_populates='user')


class Characters(db.Model):
    _tablename__ = 'characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    height: Mapped[int] = mapped_column(Integer)
    weight: Mapped[int] = mapped_column(Integer)
    favorites_by: Mapped[list['FavoritesCharacters']
                         ] = relationship(back_populates='character')


class FavoritesCharacters(db.Model):
    __tablename__ = 'favorites_characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    users: Mapped['User'] = relationship(back_populates='favorites')
    character_id: Mapped[int] = mapped_column(ForeignKey('characters.id'))
    character: Mapped['Characters'] = relationship(
        back_populates='favorites_by')

    # entonces las siguientes tablas podrian ser: class FavoritosPlanets(db.Model)  y la siguientes class Planets y y claro ya con sus debidas relaciones


class Planets(db.Model):
    __tablename__ = 'planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    diameter: Mapped[int] = mapped_column(Integer)
    population: Mapped[int] = mapped_column(Integer)
    favorites_by: Mapped[list['FavoritesPlanets']
                         ] = relationship(back_populates='planet')


class FavoritesPlanets(db.Model):
    __tablename__ = 'favorites_planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    users: Mapped['User'] = relationship(back_populates='favorites')
    planet_id: Mapped[int] = mapped_column(ForeignKey('planets.id'))
    planet: Mapped['Planets'] = relationship(
        back_populates='favorites_by')
