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

#création d'un objet curseur pour exécuter des requêtes sql
curseur = connexion.cursor()

# Exécuter la requête pour récupérer les noms et capacités de la table "salle"
requete_sql = "SELECT nom, capacite FROM salle;"
curseur.execute(requete_sql)

#Recupérer les résultat 
resultats = curseur.fetchall()

#afficher les resultats en console 
for resultat in resultats:
    print(f"Nom : {resultat[0]}, Capacite: {resultat[1]}")

#fermer le curseur
curseur.close()
connexion.close()