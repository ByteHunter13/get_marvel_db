# Extracción de base de datos para análisis

## 1. Obtener los datos crudos y devolverlos en un formato usable
- Con la API base de la wiki de MarvelDB obtenemos el HTML sin requests tan invasivos
- Con BeautifulSoup obtenemos los datos crudos
- Con la función get_comic_list obtenemos los datos en formato de lista

## 2. Limpieza inicial de dataframe
- Con pandas y funciones lambda quitamos el texto innecesario de las columnas
- Convertimos las columnas de fecha al formato correcto

## 3. Chequeo de comics registrados
- Con la función check_if_exist verificamos si el comic ya fue registrado
- Si no fue registrado, lo agregamos a la lista de comics registrados

# 4. Reorganización del código
- Separación de los scripts en sus carpetas correspondientes
- Creación de un pipeline para automatizar el proceso
- Creación de los modelos y esquemas para subir y consultar de la base de datos
- Creación de una API para consultar los datos