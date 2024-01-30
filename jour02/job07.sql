Create database employe;
create table employe (
     id int auto_increment primary key,
     nom varchar(255) not null,
     prenom varchar(255) not null,
     salaire decimal not null,
     id_service int not null);

     INSERT TO employe (nom, prenom, salaire,id_service)
     VALUES ('Doumec','Alexander', 8000.00, 1),
     ('Belarbi','Walid', 4000.00, 1),
     ('Benmamas','Youssef',10000.00, 2),
     ('Vincent','Francky',2000.00, 2),
     ('Zerouki','Renand',1000.00,1);

     CREATE TABLE service (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(255));
    
