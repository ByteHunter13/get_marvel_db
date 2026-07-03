import get_data
import format_data
import check_comic_list
def main():
    # Título de la URL
    title = "Incredible_Hulk_Vol_2"

    if check_comic_list.check_if_exist(title):
        return "El comic ya fue registrado"
    
    html_content = get_data.get_html_content(title)

    # Obtener la lista de comics
    comic_list = get_data.get_comic_list(html_content)

    # Obtener el dataframe
    cleaned_dataframe = format_data.clean_data(comic_list)
    
    # TODO: Quitar este print, por ahora me sirve para saber que llega al final
    print(cleaned_dataframe.tail(10))
    
    # Convertimos el dataframe limpio a un archivo csv
    cleaned_dataframe.to_csv(f"result_files/{title}.csv", index=False)

if __name__=="__main__":
    main()