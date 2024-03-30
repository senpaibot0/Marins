IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'GeoBD')
BEGIN
  CREATE DATABASE GeoBD;
END;

GO

USE GeoBD;
GO

DROP TABLE IF EXISTS AnimalLocation;
DROP TABLE IF EXISTS Locations;	
DROP TABLE IF EXISTS Climat;
DROP TABLE IF EXISTS Adoption;
DROP TABLE IF EXISTS Particulier;
DROP TABLE IF EXISTS Sante;	
DROP TABLE IF EXISTS Animal;


GO


CREATE TABLE Animal (
	IDAnimal INT PRIMARY KEY IDENTITY,
	Espece VARCHAR(50) NOT NULL,
	Nom VARCHAR(50),
    StatutAdoption BIT
);

GO

CREATE TABLE Sante (
    IDSante INT PRIMARY KEY IDENTITY, 
    IDAnimal INT,
    Taille FLOAT,
    Age INT, 
    Conditions VARCHAR(255), 
    DateCheckup DATE,
    CONSTRAINT FK_Sante_Animal FOREIGN KEY (IDAnimal) REFERENCES Animal(IDAnimal)
)

GO

CREATE TABLE Particulier (
    IDParticulier INT PRIMARY KEY IDENTITY,
    TypeParticulier VARCHAR(50), 
    Nom VARCHAR(50) NOT NULL,
    Contact VARCHAR(50)
);

GO

CREATE TABLE Adoption (
    IDAdoption INT PRIMARY KEY IDENTITY, 
    DateAdoption DATE,
    Interet VARCHAR(50),
    IDAnimal INT, 
    IDParticulier INT, 
    CONSTRAINT FK_Adoption_Animal FOREIGN KEY (IDAnimal) REFERENCES Animal(IDAnimal),
    CONSTRAINT FK_Adoption_Particulier FOREIGN KEY (IDParticulier) REFERENCES Particulier(IDParticulier)
);

GO

CREATE TABLE Climat(
    IDClimat INT PRIMARY KEY IDENTITY, 
    Temperature FLOAT, 
    Vent FLOAT, 
    Courant FLOAT
);

GO

CREATE TABLE Locations(
    IDLocation INT PRIMARY KEY IDENTITY,
    IDClimat INT,
    Habitat VARCHAR(30),
	Latitude FLOAT NOT NULL,
    Longitude FLOAT NOT NULL 
    CONSTRAINT FK_Locations_Climat FOREIGN KEY (IDClimat) REFERENCES Climat(IDClimat)

);

GO



CREATE TABLE AnimalLocation(
    IDAnimal INT,
    IDLocation INT,
    DateEnregistrement DATE,
    TempsEnregistrement TIME,
    Latitude FLOAT,
    Longitude FLOAT,
    CONSTRAINT PK_AnimalLocation PRIMARY KEY (IDAnimal, IDLocation, DateEnregistrement, TempsEnregistrement),
    CONSTRAINT FK_AnimalLoc_Animal FOREIGN KEY (IDAnimal) REFERENCES Animal(IDAnimal),
    CONSTRAINT FK_AnimalLoc_Location FOREIGN KEY (IDLocation) REFERENCES Locations(IDLocation)
);

Go

USE GeoBD;
GO


INSERT INTO Animal (Espece, Nom, StatutAdoption) VALUES
('Dauphin', 'Flipper', 0),
('Requin blanc', 'Bruce', 0),
('Tortue marine', 'Leonardo', 0),
('Raie manta', 'Manta', 0),
('Phoque', 'Seal', 0),
('Baleine bleue', 'Moby Dick', 0),
('Orque', 'Willy', 0),
('Pieuvre', 'Octo', 0),
('Morse', 'Morsey', 0),
('Manchot empereur', 'Pingu', 0);

INSERT INTO Sante (IDAnimal, Taille, Age, Conditions, DateCheckup) VALUES
(1, 2.5, 5, 'En bonne sante', '2024-01-01'),
(2, 3.8, 7, 'Petites egratignures', '2024-01-02'),
(3, 1.2, 15, 'En bonne sante', '2024-01-03'),
(4, 5.5, 9, 'Recuperation apres blessure', '2024-01-04'),
(5, 1.5, 4, 'En bonne sante', '2024-01-05'),
(6, 24.0, 30, 'En bonne sante', '2024-01-06'),
(7, 6.0, 12, 'En bonne sante', '2024-01-07'),
(8, 2.0, 8, 'Legere deshydratation', '2024-01-08'),
(9, 2.2, 10, 'En bonne sante', '2024-01-09'),
(10, 1.1, 6, 'Besoin de vitamines', '2024-01-10');

INSERT INTO Particulier (TypeParticulier, Nom, Contact) VALUES
('Centre de recherche', 'Oceanix', 'contact@oceanix.ca'),
('Aquarium', 'AquaMonde', 'info@aquamonde.ca'),
('Reserve marine', 'MarinProtect', 'sauvegarde@marinprotect.ca'),
('Centre de soin', 'SoinsMarins', 'soins@soinsmarins.ca'),
('Organisation de conservation', 'ConservOceans', 'contact@conseroceans.ca'),
('Centre de recherche', 'DeepSeaExplore', 'explore@deepsea.ca'),
('Aquarium', 'AquaVie', 'info@aquavie.ca'),
('Reserve marine', 'EcoMarine', 'protection@ecomarine.ca'),
('Centre de soin', 'VetoOceans', 'urgence@vetooceans.ca'),
('Organisation de conservation', 'OceanSave', 'save@oceansave.ca');

INSERT INTO Adoption (DateAdoption, Interet, IDAnimal, IDParticulier) VALUES
('2024-01-01', 'Recherche', 1, 1),
('2024-02-01', 'Conservation', 2, 2),
('2024-03-01', 'Education', 3, 3),
('2024-04-01', 'Recherche', 4, 4),
('2024-05-01', 'Conservation', 5, 5),
('2024-06-01', 'Education', 6, 6),
('2024-07-01', 'Recherche', 7, 7),
('2024-08-01', 'Conservation', 8, 8),
('2024-09-01', 'Education', 9, 9),
('2024-10-01', 'Recherche', 10, 10);

INSERT INTO Climat (Temperature, Vent, Courant) VALUES
(25.0, 5, 1.5),
(22.0, 10, 1.2),
(28.0, 3, 2.0),
(15.0, 20, 0.5),
(30.0, 2, 2.5),
(18.0, 15, 1.0),
(20.0, 8, 1.8),
(24.0, 12, 1.4),
(27.0, 4, 2.2),
(16.0, 25, 0.8);

INSERT INTO Locations (IDClimat, Habitat, Latitude, Longitude) VALUES
(1, 'Recif corallien', -18.1710, 147.4250),
(2, 'Zone pelagique', -45.3312, 167.7154),
(3, 'Mangrove', 25.2866, 51.5340),
(4, 'Fond marin', -58.3838, -62.5836),
(5, 'Estuaire', 38.9765, -76.4895),
(6, 'Banquise', -75.2500, -0.0714),
(7, 'Recif corallien', -8.3405, 115.0920),
(8, 'Zone pelagique', 28.2916, -16.6291),
(9, 'Mangrove', -2.2170, 38.9736),
(10, 'Fond marin', 36.8508, -75.9779);




SELECT spid, status, loginame, hostname ,blocked, db_name(dbid) as DBName, cmd
FROM sys.sysprocesses
WHERE dbid = DB_ID('GeoBD');


select * from AnimalLocation
select * from Animal
select * from Adoption 
select * from Particulier