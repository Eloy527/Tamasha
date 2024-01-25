from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin
from app.extensions import db






class Liked(db.Model, UserMixin):
   id: Mapped[int] = mapped_column(Integer, primary_key=True)
   title: Mapped[str] = mapped_column(String, unique=False, nullable=False)
   date: Mapped[str] = mapped_column(String, unique=False, nullable=False)
   rate: Mapped[float] = mapped_column(Float, unique=False, nullable=False)
   poster_path: Mapped[str] = mapped_column(String, unique=False, nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   def __str__(self):
      return f"Movie: {self.title}"
   def __repr__(self):
      return f"Movie: {self.title}"
