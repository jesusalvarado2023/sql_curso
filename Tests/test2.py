import streamlit as st

def mostrar():
    preguntas = [
        {
            "texto": "¿Qué extensión de archivo se utiliza típicamente para el archivo de registro de transacciones de una base de datos de SQL Server?",
            "alternativas": ["a. .ldf", "b. .sql", "c. .mdf", "d. .log", "e. .ndf"],
            "respuesta_correcta": "a. .ldf",
            "explicacion": "✅ **.ldf** es el archivo de registro de transacciones. `.mdf` es el archivo de datos principal, `.ndf` secundarios, `.sql` son scripts y `.log` no es válido en SQL Server."
        },
        {
            "texto": "Un Tipo de Datos Definido por el Usuario (UDT) de alias en SQL Server debe basarse en qué?",
            "alternativas": ["a. Un tipo de dato del CLR", "b. Un tipo de datos definido por el sistema de SQL Server.", "c. Otro tipo de datos definido por el usuario.", "d. Un procedimiento almacenado.", "e. Un ensamblado CLR."],
            "respuesta_correcta": "b. Un tipo de datos definido por el sistema de SQL Server.",
            "explicacion": "✅ Un UDT alias debe basarse en un tipo de datos **del sistema** (ej. `CHAR(10)`), no en CLR ni en otros UDTs."
        },
        {
            "texto": "¿Cuál es el comando principal para crear una nueva base de datos en SQL Server?",
            "alternativas": ["a. NEW DATABASE", "b. ALTER DATABASE", "c. BUILD DATABASE", "d. CREATE DATABASE", "e. ADD DATABASE"],
            "respuesta_correcta": "d. CREATE DATABASE",
            "explicacion": "✅ `CREATE DATABASE` es el comando correcto. Las otras opciones no son comandos válidos en SQL Server para este propósito."
        },
        {
            "texto": "¿Qué comando se utiliza para crear un Tipo de Datos Definido por el Usuario (UDT) de alias basado en un tipo de datos de sistema existente?",
            "alternativas": ["a. ALTER TYPE", "b. CREATE TYPE", "c. DEFINE TYPE", "d. CREATE ALIAS", "e. NEW TYPE"],
            "respuesta_correcta": "b. CREATE TYPE",
            "explicacion": "✅ `CREATE TYPE` se utiliza para crear un UDT alias. Las otras opciones no aplican o no existen en SQL Server."
        },
        {
            "texto": "Por defecto, ¿Qué tipo de índice crea SQL Server cuando se define una restricción UNIQUE en una columna?",
            "alternativas": ["a. Índice XML", "b. No crea ningún índice", "c. Índice agrupado (Clustered index)", "d. Índice espacial (Spatial index)", "e. Índice no agrupado (Non-clustered index)"],
            "respuesta_correcta": "e. Índice no agrupado (Non-clustered index)",
            "explicacion": "✅ Por defecto, SQL Server crea un **índice no agrupado** para restricciones `UNIQUE`, a menos que se especifique lo contrario."
        },
    ]
    
    respuestas_usuario = []
    
    st.markdown("### Prueba 2:")
    st.write("Responde las siguientes preguntas y haz clic en **Verificar respuestas** para ver si acertaste. Al final de cada pregunta se mostrará la explicación.")
    
    for i, p in enumerate(preguntas):
        st.markdown(f"**Pregunta {i+1}:** {p['texto']}")
        respuesta = st.radio(
            f"Selecciona tu respuesta para la pregunta {i+1}:",
            options=p["alternativas"],
            key=f"pregunta_{i}"
        )
        respuestas_usuario.append(respuesta)
        st.markdown("---")
    
    if st.button("✅ Verificar respuestas"):
        for i, p in enumerate(preguntas):
            st.markdown(f"**Pregunta {i+1}:** {p['texto']}")
            if respuestas_usuario[i] == p["respuesta_correcta"]:
                st.success(f"✔️ Correcto: {respuestas_usuario[i]}")
            else:
                st.error(f"❌ Incorrecto: {respuestas_usuario[i]}. La respuesta correcta es: {p['respuesta_correcta']}")
            st.info(p["explicacion"])
            st.markdown("---")


