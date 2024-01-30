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

requete_sql = "SELECT SUM(superficie) AS superficie_totale FROM etage;"
curseur.execute(requete_sql)

resultat = curseur.fetchone()

superficie_totale = resultat[0]
print(f"La superficie de la Plateforme est de {superficie_totale} m2")

curseur.close()
connexion.close()
