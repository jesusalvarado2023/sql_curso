import streamlit as st

# Título principal
st.title("Tutorial de comandos básicos en Microsoft SQL Server")

# Menú lateral
menu = st.sidebar.radio("Selecciona una clase:", ["Clase 1: Comandos básicos", "Clase 2: Consultas SELECT", "Clase 3: Joins y filtros"])

# Contenido de cada clase
if menu == "Clase 1: Comandos básicos":
    st.header("Clase 1: Comandos básicos")
    st.code("""
-- Crear una base de datos
CREATE DATABASE MiPrimeraBD;

-- Usar la base de datos
USE MiPrimeraBD;

-- Crear una tabla
CREATE TABLE Estudiantes (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Edad INT
);

-- Insertar datos
INSERT INTO Estudiantes (ID, Nombre, Edad) VALUES (1, 'Ana', 21);
INSERT INTO Estudiantes (ID, Nombre, Edad) VALUES (2, 'Luis', 22);

-- Mostrar todos los datos
SELECT * FROM Estudiantes;
""", language='sql')

elif menu == "Clase 2: Consultas SELECT":
    st.header("Clase 2: Consultas SELECT")
    st.code("""
-- Seleccionar columnas específicas
SELECT Nombre, Edad FROM Estudiantes;

-- Filtros con WHERE
SELECT * FROM Estudiantes WHERE Edad > 21;

-- Ordenar resultados
SELECT * FROM Estudiantes ORDER BY Edad DESC;

-- Contar registros
SELECT COUNT(*) AS TotalEstudiantes FROM Estudiantes;
""", language='sql')

elif menu == "Clase 3: Joins y filtros":
    st.header("Clase 3: Joins y filtros")
    st.code("""
-- Crear una segunda tabla
CREATE TABLE Cursos (
    CursoID INT PRIMARY KEY,
    NombreCurso VARCHAR(50)
);

CREATE TABLE Inscripciones (
    ID INT,
    CursoID INT,
    FOREIGN KEY (ID) REFERENCES Estudiantes(ID),
    FOREIGN KEY (CursoID) REFERENCES Cursos(CursoID)
);

-- Insertar datos
INSERT INTO Cursos (CursoID, NombreCurso) VALUES (101, 'Matemáticas');
INSERT INTO Cursos (CursoID, NombreCurso) VALUES (102, 'Biología');

INSERT INTO Inscripciones (ID, CursoID) VALUES (1, 101);
INSERT INTO Inscripciones (ID, CursoID) VALUES (2, 102);

-- INNER JOIN entre Estudiantes y Inscripciones
SELECT e.Nombre, c.NombreCurso
FROM Estudiantes e
JOIN Inscripciones i ON e.ID = i.ID
JOIN Cursos c ON i.CursoID = c.CursoID;

-- Filtros combinados
SELECT e.Nombre, c.NombreCurso
FROM Estudiantes e
JOIN Inscripciones i ON e.ID = i.ID
JOIN Cursos c ON i.CursoID = c.CursoID
WHERE c.NombreCurso = 'Biología';
""", language='sql')
