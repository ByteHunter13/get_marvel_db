from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import ProcessedVolume, Comic
import pandas as pd

# Checo que no esté el volumen en la base de datos
def check_volume_processed(db: Session, title: str) -> bool:
    # Verifica si un volumen de cómic ya ha sido ingresado en la base
    return db.query(ProcessedVolume).filter(ProcessedVolume.title == title).first() is not None

# Carga el volumen y los cómics en la base de datos por medio del dataframe
def load_volume_to_db(db: Session, title: str, df:pd.DataFrame):
    # Carga los datos del volumen y sus respectivos números
    db_volume = ProcessedVolume(title=title)
    db.add(db_volume)
    db.flush() # flush para obtener el ID asignado por la DB (db_volume.id) sin hacer commit aún

    # Itera las filas del DataFrame cargando los cómics
    comics_to_add = []
    for _, row in df.iterrows():
        # Validamos fechas
        release_date = row["Release Date"].date() if pd.notnull(row["Release Date"]) else None
        cover_date = row["Cover Date"].date() if pd.notnull(row["Cover Date"]) else None

        # Creamos el objeto del Comic que se subirá
        comic = Comic(
            volume_id = db_volume.id,
            title = row["Title"],
            link = row["Link"],
            release_date = release_date,
            cover_date = cover_date
        )
        comics_to_add.append(comic)

    # Guardamos en bloque todos los cómics
    db.bulk_save_objects(comics_to_add)
    db.commit()

    print(f"Se registraron {len(comics_to_add)} cómics del volumen {title}")