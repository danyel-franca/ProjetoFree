def add_setting(dictUsuario, tuplaUsuario):

    tuplaUsuarioMinuscula  = (tuplaUsuario[0].lower(), tuplaUsuario[1].lower())

    chave, valor = tuplaUsuarioMinuscula

    if dictUsuario == True:

        print(f"Setting {chave} already exists! Cannot add a new setting with this name.")
        
    else:

        dictUsuario[chave] = valor
        print(f"Setting {chave} added with value {valor} successfully!")
    
    print(dictUsuario)

def update_setting(dictUsuario, tuplaUsuario):
    
    tuplaUsuarioMinuscula  = (tuplaUsuario[0].lower(), tuplaUsuario[1].lower())

    chave, valor = tuplaUsuarioMinuscula

    if dictUsuario[chave] == True:

        dictUsuario.update({chave: valor})
        print(f"Setting {chave} updated to {valor} successfully!")

    else:
        print(f"Setting {chave} does not exist! Cannot update a non-existing setting.")
    
    print(dictUsuario)

def delete_setting(dicUsuario, chave):
    
    chave.lower()
    
    if chave in dicUsuario:
        dicUsuario.pop(chave, None)
        print(f"Setting {chave} deleted successfully!")
    
    else:
        print("Setting not found!")

def view_settings(dicUsuario):


    if dicUsuario == True:
        print("Current User Settings")
        for chave, valor in dicUsuario.items():
            print(f"{chave}: {valor}")
    else:
        print("No settings available.")

