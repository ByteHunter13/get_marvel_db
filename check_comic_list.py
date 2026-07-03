import json

def check_if_exist(comic_name_string):
    # Función para checar si ya realicé la búsqueda y guardé el archivo csv
    # Abrimos el archivo json
    with open("db/comic_register.json", "r", encoding="utf-8") as comic_list_file:
        
        # Cargamos el json
        comic_list = json.load(comic_list_file)

        # Si no existe nada en el json, creámos el primer registro
        if not comic_list:
            # Hay que crear el registro para que se agregue a mi lista de json sin reemplazarla
            new_register = {"id": 1, "comic": comic_name_string}
            comic_list.append(new_register)
            # Escribir el primer registro
            with open("db/comic_register.json", "w") as comic_list_file:
                json.dump(
                    comic_list,
                    comic_list_file, 
                    indent=4
                )
            # Retorno False porque quiero que mi función main() siga
            return False
        
        
        # Si existe algo en el json, recorro la lista
        for comic in comic_list:
            if comic["comic"] == comic_name_string:
                # Retorno True para que pare mi función main()
                return True
        
        # Si no existe en la lista, creo un nuevo id para prepararlo y registrarlo
        new_id = comic_list[-1]["id"] + 1
        
        # Hay que crear el registro para que se agregue a mi lista de json sin reemplazarla
        new_register = {"id": new_id, "comic": comic_name_string}
        comic_list.append(new_register)

        # Abro de nuevo el json para el nuevo registro
        with open("db/comic_register.json", "w") as comic_list_file:
            json.dump(
                comic_list,
                comic_list_file, 
                indent=4
            )
        # De nuevo retorno False para que mi función main() continúe
        return False