import mysql.connector

host = "localhost"
utilisateur = "root"
mot_de_passe = "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"
base_de_données = "laplateforme"

#etablir la connexion 
connexion = mysql.connector.connect(
    host = host,
    user = utilisateur,
    password = mot_de_passe,
    database = base_de_données
)

curseur = connexion.cursor()

requete_sql = "SELECT SUM(capacite) AS capacite_totale FROM salle;"
curseur.execute(requete_sql)

resultat = curseur.fetchone()

capacite_totale = resultat[0]
print(f"La capacité de toutes les salles est de : {capacite_totale}")

curseur.close()
connexion.close()
