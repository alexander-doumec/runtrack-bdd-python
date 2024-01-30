 "création de la table étudiant "
 
 SHOW databases;
  USE laplateforme;
   create table etudiant (id INT AUTO_INCREMENT PRIMARY KEY,nom VARCHAR(255) NOT NULL,prenom VARCHAR(255) NOT NULL,age INT NOT NULL,email VARCHAR(255) NOT NULL);

