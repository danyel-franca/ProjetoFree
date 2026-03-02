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


    if dicUsuario:
        print("Current User Settings:")
        for chave, valor in dicUsuario.items():
            print(f"{chave}: {valor}")
    else:
        print("No settings available.")

def main():

    dictUsuario = {}

    while True:
        print("\nUser Settings Management")
        print("1. Add Setting")
        print("2. Update Setting")
        print("3. Delete Setting")
        print("4. View Settings")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            chave = input("Enter setting name: ")
            valor = input("Enter setting value: ")
            add_setting(dictUsuario, (chave, valor))

        elif choice == '2':
            chave = input("Enter setting name to update: ")
            valor = input("Enter new setting value: ")
            update_setting(dictUsuario, (chave, valor))

        elif choice == '3':
            chave = input("Enter setting name to delete: ")
            delete_setting(dictUsuario, chave)

        elif choice == '4':
            view_settings(dictUsuario)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

