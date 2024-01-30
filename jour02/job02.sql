CREATE TABLE etage (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255) NOT NULL,
    ->     numero INT NOT NULL,
    ->     superficie INT NOT NULL
    -> );

CREATE TABLE salle (
    -> id int auto_increment primary key, 
    -> nom varchar(255) not null,
    -> id_etage int not null,
    -> capacite int not null );