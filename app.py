import streamlit as st
from Tests import test1, test2, test3

# Título principal
st.title("Comandos básicos en Microsoft SQL Server")

st.sidebar.image("microsoft-sql_server.png")
st.sidebar.info("Dr. Jesus Alvarado-Huayhuaz")

# Menú lateral
menu = st.sidebar.radio("Selecciona una clase:", ["Ejercicio 1: Crear BD", 
                                                  "Ejercicio 2: Consultas SELECT", 
                                                  "Ejercicio 3: Joins y filtros",
                                                  "Prueba 1", 
                                                  "Prueba 2", 
                                                  "Prueba 3"])

# Contenido de cada clase
if menu == "Ejercicio 1: Crear BD":
    st.header("Ejercicio 1: Introducción")
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

###############################

elif menu == "Ejercicio 2: Consultas SELECT":
    st.header("Ejercicio 2: Consultas SELECT")
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

###############################

elif menu == "Ejercicio 3: Joins y filtros":
    st.header("Ejercicio 3: Joins y filtros")
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

# Contenido de quizz
elif menu == "Prueba 1":
    test1.mostrar()

elif opcion == "Prueba 2":
    test2.mostrar()

elif opcion == "Prueba 3":
    test3.mostrar()
