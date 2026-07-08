import argparse
import sys
from app.database import SessionLocal
from pipeline import extractor, transformer, loader

# Pedimos ayuda a la IA para utilizar mis funciones
def run(title: str):
    db = SessionLocal()
    try:
        # Paso 1: Verificar si el volumen ya fue cargado
        print(f"[*] Comprobando estado de '{title}'...")
        if loader.check_volume_processed(db, title):
            print(f"[!] El volumen '{title}' ya está registrado en la base de datos.")
            return

        # Paso 2: Extraer HTML del Wiki API
        print(f"[*] Extrayendo contenido web de Fandom...")
        html = extractor.get_html_content(title)
        if not html:
            print("[x] Error: No se pudo obtener el contenido HTML de la página.")
            sys.exit(1)

        # Paso 3: Obtener lista de cómics
        comics_list = extractor.get_comic_list(html)
        if not comics_list:
            print("[x] Error: No se encontraron cómics o galerías en la página.")
            sys.exit(1)
        print(f"[*] Se encontraron {len(comics_list)} cómics crudos.")

        # Paso 4: Limpiar y transformar
        print("[*] Limpiando y dando formato a las fechas...")
        df_cleaned = transformer.clean_data(comics_list)

        # Paso 5: Cargar en la base de datos
        print("[*] Guardando registros en la base de datos PostgreSQL...")
        loader.load_volume_to_db(db, title, df_cleaned)

    except Exception as e:
        print(f"[x] Error inesperado en el pipeline: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script para automatizar la ingesta de cómics a PostgreSQL")
    parser.add_argument("title", type=str, help="Título exacto de la página Wiki (ej: Incredible_Hulk_Vol_2)")
    args = parser.parse_args()
    
    run(args.title)
