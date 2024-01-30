import mysql.connector

#parametres de connexion à la base de donnees 
host = "localhost"
utilisateur = "root"
mot_de_passe = "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"
base_de_données = "laplateforme"

#etablir connexion

connexion = mysql.connector.connect(host = host,
    user = utilisateur,
    password = mot_de_passe,
    database = base_de_données)

#creer un objet curseur pour executer des requetes sql

curseur = connexion.cursor()

#executer la requete pour recuperer tous les etudiants
requete_sql = "SELECT * FROM etudiant;"
curseur.execute(requete_sql)

#recuperer resultats
resultats = curseur.fetchall()

#afficher resultats 
for resultat in resultats:
    print(resultat)

# Fermer le curseur et la connexion
curseur.close()
connexion.close()