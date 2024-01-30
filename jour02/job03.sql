INSERT INTO etage (nom, numero, superficie)
    VALUES ('RDC', 0, 500), ('RDC+1', 1, 500);

INSERT INTO salle (nom, id_etage, capacite)
    VALUES  ('Lounge', 1, 100),
    ('Studio Son', 1, 5),
    ('Broadcasting', 2, 50),
    ('Bocal Peda', 2, 4),
    ('Coworking', 2, 80),
    ('Studio Video', 2, 5);

    "mysqldump -u root -p laplateforme > C:\Users\black\OneDrive\Documents\projets\runtrack-bdd-python\jour01\laplateforme.sql
Enter password: ****************************************"