# Extracción de base de datos para análisis

## 1. Obtener los datos crudos y devolverlos en un formato usable
- Con la API base de la wiki de MarvelDB obtenemos el HTML sin requests tan invasivos
- Con BeautifulSoup obtenemos los datos crudos
- Con la función get_comic_list obtenemos los datos en formato de lista

## 2. Limpieza inicial de dataframe
- Con pandas y funciones lambda quitamos el texto innecesario de las columnas
- Convertimos las columnas de fecha al formato correcto