CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    adresse VARCHAR(100),
    telephone VARCHAR(15),
    email VARCHAR(50)
);

INSERT INTO contacts (nom, prenom, adresse, telephone, email)
VALUES ('Dupont', 'Jean', '123 Rue de la Paix', '0601010101', 'jean.dupont@example.com'),
       ('Blanc', 'Clara', '2223 Rue des Étoiles', '0610101010', 'clara.blanc@example.com');
