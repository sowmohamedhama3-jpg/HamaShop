def process_payment(nom, numero, montant):
    """
    Ici on simule un paiement mobile money
    Dans un vrai projet on connecterait Wave / Orange API
    """

    print("Paiement en cours...")
    print("Client:", nom)
    print("Numéro:", numero)
    print("Montant:", montant)

    return {
        "status": "success",
        "message": "Paiement simulé avec succès"
    }