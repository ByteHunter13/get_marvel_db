from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .database import engine, SessionLocal
from .models import Base
from . import crud, schemas

# Crear las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Marvel Data API",
    description="API para consumir el catálogo de cómics extraídos desde la Wiki de Marvel",
    version="1.0.0"
)
# Dependencia para obtener la sesión de la DB local
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency = Depends(get_db)

@app.get("/", tags=["Health Check"])
def read_root():
    return {
        "status": "online",
        "description": "Marvel Data Ingestion & Querying API is running successfully."
    }

@app.get("/api/volumes", response_model=List[schemas.ProcessedVolumeOut], tags=["Volumes"])
def read_volumes(skip: int = 0, limit: int = 100, db: Session = db_dependency):
    volumes = crud.get_volumes(db, skip=skip, limit=limit)
    return volumes

@app.get("/api/volumes/{volume_id}", response_model=schemas.ProcessedVolumeDetailOut, tags=["Volumes"])
def read_volume_detail(volume_id: int, db: Session = db_dependency):
    db_volume = crud.get_volume_by_id(db, volume_id=volume_id)
    if db_volume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Volumen con ID {volume_id} no encontrado"
        )
    return db_volume

@app.get("/api/volumes/{volume_id}/comics", response_model=List[schemas.ComicOut], tags=["Comics"])
def read_volume_comics(volume_id: int, skip: int = 0, limit: int = 100, db: Session = db_dependency):
    # Validamos que el volumen exista
    db_volume = crud.get_volume_by_id(db, volume_id=volume_id)
    if db_volume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Volumen con ID {volume_id} no encontrado"
        )
    comics = crud.get_comics_by_volume(db, volume_id=volume_id, skip=skip, limit=limit)
    return comics