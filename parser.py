def parser_mail(book):
    print("\n\n")
    print(f"Envois ce mail à l'adresse : {book['mail']}", end=" ")
    if book['formation'] == 'true':
        print(f"relance pour ma formation")
    else:
        print(f"travail alimentaire")
    print("Bonjour", end=" ")
    if not book.get('female'):
        print("Madame, Monsieur", end="")
    elif book['female'] == "true":
        print("Madame", end="")
    else:
        print("Monsieur", end="")
    if book.get('name'):
        print(f" {book['name']},")
    else:
        print(f",")

    if book.get('post'):
        print(f"Je me permets de revenir vers vous concernant ma candidature au poste : {book['post']}, envoyée le {book['first contact']}.")
    else:
        print(f"Je me permets de revenir vers vous concernant ma candidature spontannée, envoyée le {book['first contact']}.")

    print("Je reste très intéressée par ce poste et disponible pour toute information complémentaire ou un éventuel entretien.")
    print("Je vous remercie pour votre retour.\nCordialement De Oliveira Mathilde.")
    print("\n")
    return


def contact_phone(book):
    print("\n\n")
    print(f"Appelle : {book['contact']}, pour avoir : ", end="")
    if not book.get('female'):
        print(" ???? ")
    elif book['female'] == 'true':
        if book.get('name'):
            print(f"Madame {book['name']}", end="")
        else:
            print(f"Madame ", end="")
    else:
        if book.get('name'):
            print(f"Monsieur {book['name']}", end="")
        else:
            print(f"Monsieur ", end="")
    print(f" de l'entreprise : {book['entreprise']}")
    
    return