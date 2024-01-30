import mysql.connector

class Salarie:

    def __init__(self, host, utilisateur, mot_de_passe, base_de_donnees):
        self.connexion = mysql.connector.connect(
            host=host,
            user=utilisateur,
            password=mot_de_passe,
            database=base_de_donnees
        )
        self.curseur = self.connexion.cursor()

    def recuperer_employes_et_services(self):
        requete_sql = """
            SELECT employe.nom AS nom_employe, employe.prenom, employe.salaire, service.nom AS nom_service
            FROM employe
            JOIN service ON employe.id_service = service.id;
        """
        self.curseur.execute(requete_sql)
        resultats = self.curseur.fetchall()
        return resultats

    def creer_table_salarie(self):
        requete_sql = """
            CREATE TABLE salarie (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255)
            );
        """
        self.curseur.execute(requete_sql)

    def inserer_noms_salarie(self, noms):
        for nom in noms:
            requete_sql = "INSERT INTO salarie (nom) VALUES (%s);"
            valeurs = (nom,)
            self.curseur.execute(requete_sql, valeurs)
        
        # Valider les modifications
        self.connexion.commit()

    def fermer_connexion(self):
        self.curseur.close()
        self.connexion.close()

# Exemple d'utilisation de la classe
if __name__ == "__main__":
    # Remplacez les valeurs par vos propres informations de connexion
    salarie_manager = Salarie(host="votre_host", utilisateur="votre_utilisateur", mot_de_passe="votre_mot_de_passe", base_de_donnees="VotreBaseDeDonnees")

    # Récupérer tous les employés et leur service respectif
    employes_et_services = salarie_manager.recuperer_employes_et_services()
    print("Employés et leur service respectif:")
    for employe in employes_et_services:
        print(employe)

    # Créer la table "salarie"
    salarie_manager.creer_table_salarie()

    # Insérer les noms dans la table "salarie"
    noms_a_inserer = ['Doumec', 'Belarbi', 'Zerouki']
    salarie_manager.inserer_noms_salarie(noms_a_inserer)

    # Fermer la connexion à la base de données
    salarie_manager.fermer_connexion()
