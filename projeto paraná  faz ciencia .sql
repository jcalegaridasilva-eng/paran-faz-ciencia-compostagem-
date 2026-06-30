CREATE DATABASE parana_faz_ciencia;

USE parana_faz_ciencia;
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    perfil ENUM('admin', 'professor', 'aluno') DEFAULT 'aluno',
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE artigos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(120),
    resumo TEXT,
    arquivo_pdf VARCHAR(255),
    ano INT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE fotos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150),
    descricao TEXT,
    caminho_imagem VARCHAR(255),
    data_upload TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE compostagem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperatura DECIMAL(5,2),
    umidade DECIMAL(5,2),
    peso DECIMAL(6,2),
    observacao TEXT,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE compostagem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperatura DECIMAL(5,2),
    umidade DECIMAL(5,2),
    peso DECIMAL(6,2),
    observacao TEXT,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE noticias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200),
    conteudo TEXT,
    imagem VARCHAR(255),
    data_publicacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO usuarios (nome, email, senha, perfil)
VALUES (
    'Administrador',
    'admin@parana.com',
    '123456',
    'admin'
);