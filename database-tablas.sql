-- 1. Habilitar la extensión para vectores (indispensable para el RAG)
CREATE EXTENSION IF NOT EXISTS vector;

-- 2. Tablas de Seguridad y Usuarios
CREATE TABLE Roles (
    id_role SERIAL PRIMARY KEY,
    nombre_rol VARCHAR(50) NOT NULL
);

CREATE TABLE Users (
    id_user SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    id_role INT REFERENCES Roles(id_role)
);

CREATE TABLE Sessions (
    id_session SERIAL PRIMARY KEY,
    id_user INT REFERENCES Users(id_user),
    fecha_inicio TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Tablas de Taxonomía (Jerarquía)
CREATE TABLE Families (
    id_family SERIAL PRIMARY KEY,
    nombre_familia VARCHAR(100) NOT NULL
);

CREATE TABLE Genera (
    id_genera SERIAL PRIMARY KEY,
    nombre_genero VARCHAR(100) NOT NULL,
    id_family INT REFERENCES Families(id_family)
);

CREATE TABLE Species (
    id_species SERIAL PRIMARY KEY,
    scientific_name VARCHAR(150) NOT NULL,
    id_genera INT REFERENCES Genera(id_genera)
);

-- 4. Atributos Botánicos y Relaciones Muchos a Muchos
CREATE TABLE Altitudinal_Ranges (
    id_alt SERIAL PRIMARY KEY,
    min_altitude INT,
    max_altitude INT,
    id_species INT REFERENCES Species(id_species)
);

CREATE TABLE Usages (
    id_usage SERIAL PRIMARY KEY,
    descripcion_uso TEXT NOT NULL
);

-- Tabla intermedia Especie-Uso
CREATE TABLE Species_Usages (
    id_species INT REFERENCES Species(id_species) ON DELETE CASCADE,
    id_usage INT REFERENCES Usages(id_usage) ON DELETE CASCADE,
    PRIMARY KEY (id_species, id_usage)
);

CREATE TABLE Ecosystems (
    id_eco SERIAL PRIMARY KEY,
    nombre_ecosistema VARCHAR(100) NOT NULL
);

-- Tabla intermedia Especie-Ecosistema
CREATE TABLE Species_Eco (
    id_species INT REFERENCES Species(id_species) ON DELETE CASCADE,
    id_eco INT REFERENCES Ecosystems(id_eco) ON DELETE CASCADE,
    PRIMARY KEY (id_species, id_eco)
);

-- 5. Documentación y Multimedia
CREATE TABLE Documents (
    id_doc SERIAL PRIMARY KEY,
    id_species INT REFERENCES Species(id_species),
    fuente_url TEXT,
    titulo VARCHAR(255)
);

CREATE TABLE Chunks (
    id_chunk SERIAL PRIMARY KEY,
    id_doc INT REFERENCES Documents(id_doc) ON DELETE CASCADE,
    contenido_texto TEXT NOT NULL,
    orden_segmento INT
);

CREATE TABLE Images (
    id_img SERIAL PRIMARY KEY,
    id_species INT REFERENCES Species(id_species),
    file_path TEXT NOT NULL,
    description TEXT
);

-- 6. Tablas Vectoriales (Almacenamiento de Embeddings)
CREATE TABLE Embeddings_Text (
    id_emb SERIAL PRIMARY KEY,
    id_chunk INT REFERENCES Chunks(id_chunk) ON DELETE CASCADE,
    embedding vector(1536), -- Dimensión estándar para OpenAI (text-embedding-3-small)
    modelo_version VARCHAR(100)
);

CREATE TABLE Embeddings_Image (
    id_emb_img SERIAL PRIMARY KEY,
    id_img INT REFERENCES Images(id_img) ON DELETE CASCADE,
    embedding vector(512), -- Dimensión para modelos tipo CLIP
    modelo_version VARCHAR(100)
);

-- 7. Consultas y Evaluación RAG
CREATE TABLE Queries (
    id_query SERIAL PRIMARY KEY,
    id_session INT REFERENCES Sessions(id_session),
    query_text TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Evaluations (
    id_eval SERIAL PRIMARY KEY,
    id_query INT REFERENCES Queries(id_query) ON DELETE CASCADE,
    faithfulness FLOAT,
    answer_relevancy FLOAT,
    context_recall FLOAT
);