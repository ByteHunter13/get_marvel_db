import pandas as pd
import re

from datetime import datetime

def clean_data(comic_list):
    # Orden del header que marqué que llegaría en la lista
    header = ["Link", "Title", "Release Date", "Cover Date"]

    # Lo convierto en un dataframe para utilizarlo fácilmente
    df_base = pd.DataFrame(comic_list, columns=header)

    # ------ Fechas ------
    # Elimino de manera básica el texto que no necesito para formatear mis fechas
    df_base["Release Date"] = df_base["Release Date"].str.replace('Release date: ', '')
    df_base["Cover Date"] = df_base["Cover Date"].str.replace('Cover date: ', '')
    df_base["Cover Date"] = df_base["Cover Date"].str.replace(',', '')
    df_base["Cover Date"] = df_base["Cover Date"].str.replace('Mid ', '')
    
    # Copio el dataframe para modificarlo con funciones
    df_formatted = df_base.copy()
    
    # Pido un expresión regular a la IA para manejar mi función
    # resultado = re.sub(r'\b\d{1,2}\b', '', texto)
    df_formatted["Release Date"] = df_formatted["Release Date"].apply(lambda x: re.sub(r'\b\d{1,2}\b,?', '', x))
    
    # Convierto a un formato de fecha
    # fecha_objeto = datetime.strptime(fecha_texto, "%B %Y")
    df_formatted["Release Date"] = df_formatted["Release Date"].apply(lambda x: datetime.strptime(x, "%B %Y"))
    df_formatted["Cover Date"] = df_formatted["Cover Date"].apply(lambda x: datetime.strptime(x, "%B %Y"))

    df_cleaned = df_formatted.copy()

    return df_cleaned
