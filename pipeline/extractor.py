from bs4 import BeautifulSoup
import requests

def get_html_content(page_title):
    # Endpoint principal de la API de Marvel
    url = "https://marvel.fandom.com/api.php"

    # Parámetros de la solicitud
    params = {
        "action": "parse",
        "page": page_title,
        "format": "json",
        "prop": "text" # Texto crudo para procesar los datos
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Verificación de conexión
        data = response.json()
        
        # Validar si la página no existe o hay un error en la consulta
        if "error" in data:
            print(f"Error de la API: {data['error']['info']}")
            return None
        # Extraer el contenido del wikitext
        html_content = data['parse']['text']['*']

        return html_content
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None

def get_comic_list(html):
    # Convertir a un formato de soup
    soup = BeautifulSoup(html, 'html.parser')

    # Inicio la lista de comics vacía
    comic_list = []

    # El formato de la página inicia en 0 sus galerías
    num_gallery = 0
    galleries = []

    # Recibiré un None, cuando deje de encontrar galerías
    while True:
        # Siempre recibiré "algo" por la galería cero
        actual_gallery = soup.find('div', {'id': f"gallery-{num_gallery}"})

        # Relleno la lista de galerías
        if actual_gallery:
            galleries.append(f"gallery-{num_gallery}")
            num_gallery += 1
        else:
            break
    
    # Recorro cada galería
    for gallery in galleries:
        # Obtengo el soup de cada galería
        gallery_div = soup.find('div', {'id': gallery})

        # Obtengo cada item que hay en cada galería
        for gallery_item in gallery_div.find_all('div', {
            'class': 'wikia-gallery-item'}):
            
            # Recibo el soup de cada item
            info_box = gallery_item.find('div', {
                'class': 'md-volume__issue__info--unlimited'})
            
            # Inicio la lista de información del comic
            comic_info = []

            # Obtenemos los datos en orden: Link, Title, Release Date, Cover Date
            for div in info_box.find_all('div'):
                # El dato del link se encuentra en esta clase
                # TODO: hacer varias pruebas para confirmar la clase
                if div.get('class')[0] == "md-volume__issue__info__link":
                    link = div.find('a')['href']
                    comic_info.append(link)
                else:
                    comic_info.append(div.text.strip())
            comic_list.append(comic_info)
    return comic_list