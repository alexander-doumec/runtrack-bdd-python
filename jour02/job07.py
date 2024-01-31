import mysql.connector

class Employe:
    def __init__(self):
        self.conn = mysql.connector.connect (
            host = "localhost",
            utilisateur = "root",
            mot_de_passe = "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",
            base_de_données = "employe"
            )
        
        self.cursor = self.conn.cursor()

    def read_all_employes_with_service(self):
        sql = """
            SELECT employe.id, employe.nom, employe.prenom, employe.salaire, service.nom AS service_nom
            FROM employe
            JOIN service ON employe.id_service = service.id  """
        
        self.cursor.execute(sql)
        result = self.cursor.fetchall
        return result
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()
    

    
employe_manager = Employe()


all_employes_with_service = employe_manager.read_all_employes_with_service()

# Parcours des résultats et affichage en console
for employe in all_employes_with_service:
    print("ID:", employe[0])
    print("Nom:", employe[1])
    print("Prenom:", employe[2])
    print("Salaire:", employe[3])
    print("Service:", employe[4])
    print("---------------------------")

# Suppression de l'objet Employe à la fin pour libérer les ressources
del employe_manager