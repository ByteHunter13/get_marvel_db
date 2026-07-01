import get_data

def main():
    # Título de la URL
    title = "Incredible_Hulk_Vol_5"
    html_content = get_data.get_html_content(title)

    # Obtener la lista de comics
    comic_list = get_data.get_comic_list(html_content)
    print(comic_list)

if __name__=="__main__":
    main()