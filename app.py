import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Juegos Musicales - LAC", page_icon="🎮", layout="centered")

# Cabecera con tu avatar
col1, col2 = st.columns([1, 4])
with col1:
    if os.path.exists("juan_cartoon.png"):
        st.image("juan_cartoon.png", width=120)
with col2:
    st.title("🎮 Sala de Juegos - LAC Música")
    st.write("¡Poné a prueba lo que aprendimos con el profe Juan!")

# Inicializar puntaje en la memoria temporal
if 'puntaje' not in st.session_state:
    st.session_state.puntaje = 0
if 'juegos_completados' not in st.session_state:
    st.session_state.juegos_completados = []

# Menú lateral
st.sidebar.title("📌 Menú de Desafíos")
juego_actual = st.sidebar.radio("Elegí un nivel:", 
    ["1. Historia y Orígenes", 
     "2. La Escalera de Notas", 
     "3. El Pentagrama", 
     "4. Sonido, Eco y Figuras", 
     "5. Compases e Intervalos"])

st.sidebar.markdown("---")
st.sidebar.title(f"🏆 Puntaje total: {st.session_state.puntaje}")
if st.sidebar.button("Reiniciar Puntaje"):
    st.session_state.puntaje = 0
    st.session_state.juegos_completados = []
    st.rerun()

# --- NIVEL 1: HISTORIA ---
if juego_actual == "1. Historia y Orígenes":
    st.header("📜 Nivel 1: Historia de las Notas")
    st.write("Demostrá qué tanto leíste el cuadernillo.")
    
    q1 = st.radio("1. ¿Dónde se encontró la partitura musical más antigua hace 3400 años?", 
                  ["Egipto", "Roma", "Siria", "Grecia"], index=None)
    q2 = st.radio("2. ¿Qué monje italiano ideó los nombres de las notas en el siglo XI?", 
                  ["San Juan", "Guido D'Arezzo", "Papa Gregorio"], index=None)
    q3 = st.radio("3. ¿Por qué se reemplazó la sílaba 'Ut' por la nota 'Do'?", 
                  ["Porque sobraba una letra", "Porque era el nombre de una diosa", "Porque Do era más fácil de pronunciar"], index=None)
    
    if st.button("Corregir Nivel 1"):
        if "nivel1" not in st.session_state.juegos_completados:
            puntos = 0
            if q1 == "Siria": puntos += 10
            if q2 == "Guido D'Arezzo": puntos += 10
            if q3 == "Porque Do era más fácil de pronunciar": puntos += 10
            
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel1")
            st.success(f"¡Excelente! Sumaste {puntos} puntos.")
        else:
            st.warning("Ya completaste este nivel. ¡Pasá al siguiente!")

# --- NIVEL 2: NOTAS VECINAS ---
elif juego_actual == "2. La Escalera de Notas":
    st.header("🪜 Nivel 2: Grados Conjuntos")
    st.write("Imaginá que las notas son una escalera. ¿Cuáles son las notas vecinas?")
    
    q1 = st.radio("1. ¿Cuáles son las notas vecinas de SOL?", 
                  ["Do y Mi", "Fa y La", "La y Si"], index=None)
    q2 = st.radio("2. ¿Cuáles son las notas vecinas de RE?", 
                  ["Do y Mi", "Fa y Sol", "Si y Do"], index=None)
    q3 = st.radio("3. ¿Cuáles son las notas vecinas de DO?", 
                  ["Mi y Fa", "Sol y La", "Si y Re"], index=None)

    if st.button("Corregir Nivel 2"):
        if "nivel2" not in st.session_state.juegos_completados:
            puntos = 0
            if q1 == "Fa y La": puntos += 10
            if q2 == "Do y Mi": puntos += 10
            if q3 == "Si y Re": puntos += 10
            
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel2")
            st.success(f"¡Bien ahí! Sumaste {puntos} puntos.")
        else:
            st.warning("Ya completaste este nivel. ¡Pasá al siguiente!")

# --- NIVEL 3: PENTAGRAMA ---
elif juego_actual == "3. El Pentagrama":
    st.header("🎼 Nivel 3: El Pentagrama")
    st.write("¡A contar líneas y espacios de abajo hacia arriba!")
    
    q1 = st.radio("1. ¿Cuántas líneas y espacios tiene el pentagrama?", 
                  ["5 líneas y 5 espacios", "4 líneas y 5 espacios", "5 líneas y 4 espacios"], index=None)
    q2 = st.radio("2. Si una nota es muy alta o muy baja y no entra, ¿qué usamos?", 
                  ["Líneas y espacios adicionales", "Otra hoja", "Clave de Fa"], index=None)
    q3 = st.radio("3. ¿Dónde se ubica la Clave de Sol que usamos habitualmente?", 
                  ["En la primera línea", "En la segunda línea", "En el tercer espacio"], index=None)

    if st.button("Corregir Nivel 3"):
        if "nivel3" not in st.session_state.juegos_completados:
            puntos = 0
            if q1 == "5 líneas y 4 espacios": puntos += 10
            if q2 == "Líneas y espacios adicionales": puntos += 10
            if q3 == "En la segunda línea": puntos += 10
            
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel3")
            st.success(f"¡Genial! Sumaste {puntos} puntos.")
        else:
            st.warning("Ya completaste este nivel. ¡Pasá al siguiente!")

# --- NIVEL 4: SONIDO Y FIGURAS ---
elif juego_actual == "4. Sonido, Eco y Figuras":
    st.header("🔊 Nivel 4: Cualidades y Figuras")
    
    q1 = st.radio("1. ¿Qué diferencia principal hay entre el Eco y la Reverberación?", 
                  ["El eco repite la palabra clara, la reverberación alarga el sonido confundiéndolo", "Son exactamente lo mismo", "La reverberación solo ocurre al aire libre"], index=None)
    q2 = st.radio("2. ¿Qué cualidad del sonido nos permite distinguir si es Fuerte o Suave?", 
                  ["Altura", "Intensidad", "Timbre"], index=None)
    q3 = st.radio("3. ¿Cuál de estas figuras musicales dura más tiempo?", 
                  ["Negra", "Corchea", "Redonda", "Blanca"], index=None)

    if st.button("Corregir Nivel 4"):
        if "nivel4" not in st.session_state.juegos_completados:
            puntos = 0
            if q1 == "El eco repite la palabra clara, la reverberación alarga el sonido confundiéndolo": puntos += 10
            if q2 == "Intensidad": puntos += 10
            if q3 == "Redonda": puntos += 10
            
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel4")
            st.success(f"¡Súper! Sumaste {puntos} puntos.")
        else:
            st.warning("Ya completaste este nivel. ¡Pasá al siguiente!")

# --- NIVEL 5: COMPASES E INTERVALOS ---
elif juego_actual == "5. Compases e Intervalos":
    st.header("🥁 Nivel 5: Compases y Distancias")
    
    q1 = st.radio("1. ¿Un compás de 4/4 es simple o compuesto?", 
                  ["Simple", "Compuesto"], index=None)
    q2 = st.radio("2. ¿Un compás de 6/8 es simple o compuesto?", 
                  ["Simple", "Compuesto"], index=None)
    q3 = st.radio("3. ¿Cuál es la distancia mínima (el escalón más chico) entre dos notas?", 
                  ["Un Tono", "Un Semitono", "Una Octava"], index=None)

    if st.button("Corregir Nivel 5"):
        if "nivel5" not in st.session_state.juegos_completados:
            puntos = 0
            if q1 == "Simple": puntos += 10
            if q2 == "Compuesto": puntos += 10
            if q3 == "Un Semitono": puntos += 10
            
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel5")
            st.success(f"¡Perfecto! Sumaste {puntos} puntos.")
            st.balloons() # Lluvia de globos al terminar
        else:
            st.warning("Ya completaste este nivel. ¡Pasá al siguiente!")