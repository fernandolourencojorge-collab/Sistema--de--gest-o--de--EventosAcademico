CREATE DATABASE EventosAcademico;
USE EventosAcademico;

CREATE TABLE Eventos (
    EventoID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100),
    DataInicio DATE,
    DataFim DATE,
    Local VARCHAR(100),
    Capacidade INT CHECK (Capacidade > 0),
    PrecoInscricao DECIMAL(10,2) CHECK (PrecoInscricao >= 0)
);

CREATE TABLE Participantes (
    ParticipanteID INT PRIMARY KEY AUTO_INCREMENT,
    NomeParticipante VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    Telefone VARCHAR(20)
);

CREATE TABLE Oradores (
    OradorID INT PRIMARY KEY AUTO_INCREMENT,
    NomeOrador VARCHAR(100),
    Especialidade VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE Sessoes (
    SessaoID INT PRIMARY KEY AUTO_INCREMENT,
    Titulo VARCHAR(100),
    DataHora DATETIME,
    EventoID INT,
    OradorID INT,
    FOREIGN KEY (EventoID) REFERENCES Eventos(EventoID),
    FOREIGN KEY (OradorID) REFERENCES Oradores(OradorID)
);

CREATE TABLE Inscricoes (
    InscricaoID INT PRIMARY KEY AUTO_INCREMENT,
    ParticipanteID INT,
    EventoID INT,
    DataInscricao DATE,
    FOREIGN KEY (ParticipanteID) REFERENCES Participantes(ParticipanteID),
    FOREIGN KEY (EventoID) REFERENCES Eventos(EventoID)
);
select *from Eventos;
select *from Oradores;
select *from participantes;
select *from Sessoes;
select *from inscricoes;
-- 5 eventos
INSERT INTO Eventos (EventoID, Nome, DataInicio,DataFim, local,capacidade,PrecoInscricao) VALUES
(1,'Conferência de Tecnologia','2025-06-10','2025-06-10','Luanda','200','2000'),
(2,'Workshop de Bases de Dados','2025-06-15','2025-06-15','Benguela','100','5000'),
(3,'Seminário de Inteligência Artificial','2025-06-20','2025-06-20','Huambo','50','15000'),
(4,'Fórum de Empreendedorismo','2025-06-25','2025-06-25','Lubango','80','7000'),
(5,'Congresso de Engenharia','2025-06-30','2025-06-30','Malanje','250','10000');
-- 10 Oradores
INSERT INTO Oradores (OradorID, NomeOrador,Especialidade, email) VALUES
(1,'Dr. João Manuel','Docente','joaogmail.com'),
(2,'Eng. Maria Silva','Palestrate','mariagmail.com'),
(3,'Prof. Pedro Costa','Docente','pedrogmail.com'),
(4,'Dra. Ana Paula','Orador','anagmail.com'),
(5,'Eng. Carlos Mendes','Mestre','carlosgmail.com'),
(6,'Prof. Helena Dias','Coordenador','helenagmail.com'),
(7,'Dr. Bruno Fernandes','Docente','brunogmail.com'),
(8,'Eng. Sofia Lopes','Doctor','sofiagmail.com'),
(9,'Prof. Ricardo Alves','Docente','ricardogmail.com'),
(10,'Dra. Joana Pinto','Palestrante','joanagmail.com');

-- 20 participantes 
INSERT INTO Participantes (ParticipanteID, NomeParticipante,Email,Telefone) VALUES
(1,'Ana','anagmail.com','932457598'),(2,'Bruno','brunogmail.com','933555500'),(3,'Carlos','carlosgmail.com','948523016'),(4,'Dina','dinagmail.com','925281101'),(5,'Eduardo','eduardogmail.com','933555200'),
(6,'Fátima','fatimagmail.com','933999196'),(7,'Gil','gilgmail.com','924212191'),(8,'Helena','helenagmail.com','933052056'),(9,'Igor','igorgmail.com','942562443'),(10,'Joana','joanagmail.com','933052066'),
(11,'Katia','katiagmail.com','924562443'),(12,'Luis','luisgmail.com','9327773'),(13,'Marta','martagmail.com','932457598'),(14,'Nelson','nelsongmail.com','936270119'),(15,'Olga','olgagmail.com','973197663'),
(16,'Paulo','paulogmail.com','932457598'),(17,'Rita','ritagmail.com','932457598'),(18,'Sérgio','sergiogmail.com','932457598'),(19,'Teresa','teresagmail.com','932457598'),(20,'Valter','valtergmail.com','932457598');

INSERT INTO Sessoes (SessaoID,Titulo,DataHora,EventoID, OradorID) VALUES
(1,'SQL Avançado','2025-09-01 20:00',1,1),(2,'python','2025-04-01 11:00',1,2),
(3,'Algóritmo','2025-05-28 10:00',2,3),(4,'karate do','2025-05-22 12:00',2,4),
(5,'Pai Rico Pai Pobre','2025-04-06 21:00',3,5),(6,'saúde da Mulher','2025-07-24 13:00',3,6),
(7,'c##','2025-05-05 14:00',4,7),(8,'o filho Prodigo','2025-02-21 14:00',4,8),
(9,'javaScript','2025-06-03 8:00',2,1),(10,' Ditongos Nazais','2025-08-11 15:00',3,1);


-- 30 inscrições
INSERT INTO Inscricoes (ParticipanteID, EventoID, DataInscricao) VALUES

-- Evento 1 (8 participantes)
(1,1,'2025-05-01'),(2,1,'2025-05-01'),(3,1,'2025-05-01'),
(4,1,'2025-05-01'),(5,1,'2025-05-01'),(6,1,'2025-05-01'),
(7,1,'2025-05-01'),(8,1,'2025-05-01'),

-- Evento 2 (6 participantes)
(2,2,'2025-05-02'),(3,2,'2025-05-02'),(4,2,'2025-05-02'),
(5,2,'2025-05-02'),(6,2,'2025-05-02'),(7,2,'2025-05-02'),

-- Evento 3 (7 participantes)
(8,3,'2025-05-03'),(9,3,'2025-05-03'),(10,3,'2025-05-03'),
(11,3,'2025-05-03'),(12,3,'2025-05-03'),
(13,3,'2025-05-03'),(14,3,'2025-05-03'),

-- Evento 4 (5 participantes)
(15,4,'2025-05-04'),(16,4,'2025-05-04'),
(17,4,'2025-05-04'),(18,4,'2025-05-04'),
(19,4,'2025-05-04'),

-- Evento 5 (6 participantes)
(10,5,'2025-05-05'),(11,5,'2025-05-05'),
(12,5,'2025-05-05'),(13,5,'2025-05-05'),
(14,5,'2025-05-05'),(20,5,'2025-05-05'); 
-- i. Listar todos os eventos com os seus oradores e o número total de participantes inscritos.
 SELECT 
    E.Nome AS Evento,
    O.NomeOrador,
    COUNT(DISTINCT I.ParticipanteID) AS TotalParticipantes
FROM Eventos E
LEFT JOIN Sessoes S ON E.EventoID = S.EventoID
LEFT JOIN Oradores O ON S.OradorID = O.OradorID
LEFT JOIN Inscricoes I ON E.EventoID = I.EventoID
GROUP BY E.EventoID, E.Nome, O.NomeOrador;
-- ii. Encontrar os participantes que se inscreveram em mais de um evento. 
SELECT 
    P.ParticipanteID,
    P.NomeParticipante,
    COUNT(I.EventoID) AS TotalEventos
FROM Participantes P
JOIN Inscricoes I ON P.ParticipanteID = I.ParticipanteID
GROUP BY P.ParticipanteID, P.NomeParticipante
HAVING COUNT(I.EventoID) > 1;
-- iii. Obter a lista de sessões de um evento específico, ordenadas por data e hora.
SELECT 
    S.SessaoID,
    S.Titulo,
    S.DataHora,
    O.NomeOrador,
    E.Nome AS Evento
FROM Sessoes S
JOIN Eventos E ON S.EventoID = E.EventoID
JOIN Oradores O ON S.OradorID = O.OradorID
WHERE S.EventoID = 1
ORDER BY S.DataHora ASC;
-- iv. Calcular a receita total gerada por cada evento.
SELECT 
    E.EventoID,
    E.Nome AS Evento,
    COUNT(I.InscricaoID) AS TotalInscricoes,
    E.PrecoInscricao,
    COUNT(I.InscricaoID) * E.PrecoInscricao AS ReceitaTotal
FROM Eventos E
LEFT JOIN Inscricoes I ON E.EventoID = I.EventoID
GROUP BY E.EventoID, E.Nome, E.PrecoInscricao;
-- v. Identificar oradores que participam em eventos em mais de uma cidade. 
SELECT 
    O.OradorID,
    O.NomeOrador,
    COUNT(DISTINCT E.Local) AS TotalCidades
FROM Oradores O
JOIN Sessoes S ON O.OradorID = S.OradorID
JOIN Eventos E ON S.EventoID = E.EventoID
GROUP BY O.OradorID, O.NomeOrador
HAVING COUNT(DISTINCT E.Local) > 1;
