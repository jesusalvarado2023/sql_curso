import streamlit as st

#st.set_page_config(page_title="Quiz SQL Server 2022", layout="centered")
#st.title("🧠 Quiz Interactivo: SQL Server 2022")

def mostrar():
    st.write("Responde las siguientes preguntas y haz clic en **Verificar respuestas** para ver si acertaste. Al final de cada pregunta se mostrará la explicación.")

# Diccionario de preguntas, opciones, respuestas correctas y explicaciones
    quiz_data = [
        {
            "pregunta": "1. ¿Puede SQL Server ser instalado en un idioma diferente al idioma de visualización de Windows en ediciones de Windows que no son 'Single Language'?",
            "opciones": [
                "a. Únicamente si se instala a través de la línea de comandos.",
                "b. Sí, en ediciones de Windows que permiten múltiples idiomas, el instalador de SQL Server a menudo ofrece la opción de seleccionar el idioma de instalación independientemente del idioma de visualización actual del sistema.",
                "c. Solo si se utiliza una versión de SQL Server anterior a 2012.",
                "d. No, el instalador de SQL Server siempre fuerza el idioma del sistema operativo.",
                "e. No, en ediciones de Windows que permiten múltiples idiomas, el instalador de SQL Server solo permite instalar en el idioma ingles."
            ],
            "respuesta_correcta": "b",
            "explicacion": "SQL Server puede instalarse en un idioma distinto al del sistema, si la edición de Windows lo permite. El idioma del instalador determina el idioma de instalación."
        },
        {
            "pregunta": "2. ¿Qué tipo de sistema de gestión de bases de datos es SQL Server 2022?",
            "opciones": [
                "a. Relacional",
                "b. Orientado a grafos",
                "c. Orientado a documentos",
                "d. Desnormalizado",
                "e. NoSQL"
            ],
            "respuesta_correcta": "a",
            "explicacion": "SQL Server es un sistema de bases de datos relacional (RDBMS), aunque soporta datos semiestructurados y grafos, su núcleo sigue siendo relacional."
        },
        {
            "pregunta": "3. Si un desarrollador necesita añadir una nueva columna llamada 'email' a una tabla existente llamada 'Usuarios', ¿qué tipo de comando SQL utilizaría?",
            "opciones": [
                "a. TCC (Transaction Control Commands)",
                "b. DDL (Data Definition Language)",
                "c. DCL (Data Control Language)",
                "d. DQL (Data Query Language)",
                "e. DML (Data Manipulation Language)"
            ],
            "respuesta_correcta": "b",
            "explicacion": "Agregar columnas modifica la estructura de la tabla, por lo tanto se usa un comando DDL como ALTER TABLE."
        },
        {
            "pregunta": "4. ¿Qué edición de SQL Server 2022 ofrece la funcionalidad completa de la edición Enterprise, pero está licenciada únicamente para desarrollo y pruebas, no para uso en producción?",
            "opciones": [
                "a. SQL Server 2022 Developer Edition",
                "b. SQL Server 2022 Enterprise Edition",
                "c. SQL Server 2022 Express Edition",
                "d. SQL Server 2022 Web Edition",
                "e. SQL Server 2022 Standard Edition"
            ],
            "respuesta_correcta": "a",
            "explicacion": "La Developer Edition ofrece todas las funciones de Enterprise, pero solo se puede usar para desarrollo y pruebas, no en producción."
        },
        {
            "pregunta": "5. ¿Qué tecnología en SQL Server 2022 permite consultar datos de fuentes externas como Oracle, Teradata o almacenamiento compatible con S3 sin moverlos?",
            "opciones": [
                "a. Always Encrypted",
                "b. En SQL Server no es posible.",
                "c. PolyBase",
                "d. Change Data Capture",
                "e. In-Memory OLTP"
            ],
            "respuesta_correcta": "c",
            "explicacion": "PolyBase permite consultar datos externos como si fueran locales, incluyendo Oracle, Teradata y S3, sin mover los datos."
        }
    ]
    
    # Para almacenar respuestas del usuario
    respuestas_usuario = []
    
    with st.form(key="quiz_form"):
        for idx, item in enumerate(quiz_data):
            st.write(f"### {item['pregunta']}")
            respuesta = st.radio(
                label="Selecciona una respuesta:",
                options=item["opciones"],
                key=f"pregunta_{idx}"
            )
            respuestas_usuario.append(respuesta)
    
        submit = st.form_submit_button("✅ Verificar respuestas")
    
    # Mostrar resultados y explicaciones
    if submit:
        st.markdown("---")
        st.subheader("📊 Resultados")
        puntaje = 0
    
        for idx, item in enumerate(quiz_data):
            seleccion = respuestas_usuario[idx]
            letra_seleccionada = seleccion.split(".")[0]
            correcta = item["respuesta_correcta"]
    
            if letra_seleccionada == correcta:
                st.success(f"✔ Pregunta {idx+1}: ¡Correcto!")
                puntaje += 1
            else:
                st.error(f"✘ Pregunta {idx+1}: Incorrecto. Tu respuesta: {seleccion}")
    
            st.info(f"**Explicación:** {item['explicacion']}")
            st.markdown("---")
    
        st.subheader(f"🎯 Puntuación final: {puntaje} / {len(quiz_data)}")
    
