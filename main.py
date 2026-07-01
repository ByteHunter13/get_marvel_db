import get_data
import format_data

def main():
    # Título de la URL
    title = "Incredible_Hulk_Vol_5"
    html_content = get_data.get_html_content(title)

    # Obtener la lista de comics
    comic_list = get_data.get_comic_list(html_content)
    print(comic_list)

    # Obtener el dataframe
    cleaned_dataframe = format_data.clean_data(comic_list)
    print(cleaned_dataframe.head(10))

if __name__=="__main__":
    main()