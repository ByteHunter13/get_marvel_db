from sqlalchemy.orm import Session
from . import models, schemas

def get_volumes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProcessedVolume).offset(skip).limit(limit).all()

def get_volume_by_id(db: Session, volume_id: int):
    return db.query(models.ProcessedVolume).filter(models.ProcessedVolume.id == volume_id).first()

def get_volume_by_title(db: Session, title: str):
    return db.query(models.ProcessedVolume).filter(models.ProcessedVolume.title == title).first()

def get_comics_by_volume(db: Session, volume_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Comic).filter(models.Comic.volume_id == volume_id).offset(skip).limit(limit).all()
