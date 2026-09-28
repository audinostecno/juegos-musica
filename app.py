import streamlit as st
import os
import random

# Configuración de la página
st.set_page_config(page_title="Juegos Musicales - LAC", page_icon="🎮", layout="centered")

# Inyectar CSS para poner fondo blanco a las imágenes transparentes
st.markdown("""
    <style>
    img {
        background-color: white;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Cabecera con tu avatar
col1, col2 = st.columns([1, 4])
with col1:
    if os.path.exists("juan_cartoon.png"):
        st.image("juan_cartoon.png", width=120)
with col2:
    st.title("🎮 Sala de Juegos - LAC Música")
    st.write("¡Poné a prueba lo que aprendimos en clase!")

# --- BANCOS DE PREGUNTAS ACTUALIZADO ---
banco_pentagrama = [
    {"img": "clave_de_sol_nota_do.png", "opciones": ["Do", "Re", "Mi"], "correcta": "Do"},
    {"img": "clave_de_sol_nota_re.png", "opciones": ["Re", "Fa", "Sol"], "correcta": "Re"},
    {"img": "clave_de_sol_nota_dosostenido.png", "opciones": ["Do", "Do sostenido", "Re bemol"], "correcta": "Do sostenido"},
    {"img": "clave_de_sol_nota_mib.png", "opciones": ["Mi", "Re sostenido", "Mi bemol"], "correcta": "Mi bemol"},
    {"img": "clave_de_sol_nota_fa.png", "opciones": ["Fa", "La", "Si"], "correcta": "Fa"},
    {"img": "clave_de_sol_nota_sol.png", "opciones": ["Fa", "Sol", "La"], "correcta": "Sol"},
    {"img": "clave_de_sol_nota_la.png", "opciones": ["Sol", "La", "Si"], "correcta": "La"},
    {"img": "clave_de_sol_nota_lasostenido.png", "opciones": ["La", "La sostenido", "Si bemol"], "correcta": "La sostenido"},
    {"img": "clave_de_sol_nota_sib.png", "opciones": ["Si", "Si bemol", "La sostenido"], "correcta": "Si bemol"},
    {"img": "clave_de_fa_nota_re.png", "opciones": ["Fa", "Re", "Si"], "correcta": "Re"},
    {"img": "clave_de_fa_nota_fa.png", "opciones": ["Re", "Fa", "La"], "correcta": "Fa"}
]

banco_intervalos = [
    {"pregunta": "¿Qué distancia hay entre Re y Sol?", "opciones": ["Tercera", "Cuarta", "Quinta"], "correcta": "Cuarta"},
    {"pregunta": "¿Qué distancia hay entre Do y Mi?", "opciones": ["Segunda", "Tercera", "Cuarta"], "correcta": "Tercera"},
    {"pregunta": "¿Qué distancia hay entre Mi y Si?", "opciones": ["Cuarta", "Quinta", "Sexta"], "correcta": "Quinta"},
    {"pregunta": "¿Qué distancia hay entre Fa y Sol?", "opciones": ["Primera", "Segunda", "Tercera"], "correcta": "Segunda"},
    {"pregunta": "¿Qué distancia hay entre Do y el siguiente Do?", "opciones": ["Sexta", "Séptima", "Octava"], "correcta": "Octava"},
    {"pregunta": "¿Qué distancia hay entre La y Do (agudo)?", "opciones": ["Segunda", "Tercera", "Cuarta"], "correcta": "Tercera"}
]

# --- INICIALIZAR MEMORIA Y PREGUNTAS ALEATORIAS ---
if 'puntaje' not in st.session_state:
    st.session_state.puntaje = 0
if 'juegos_completados' not in st.session_state:
    st.session_state.juegos_completados = []

if 'preguntas_n3' not in st.session_state:
    st.session_state.preguntas_n3 = random.sample(banco_pentagrama, 3)
if 'preguntas_n5' not in st.session_state:
    st.session_state.preguntas_n5 = random.sample(banco_intervalos, 3)

# Menú lateral
st.sidebar.title("📌 Menú de Desafíos")
juego_actual = st.sidebar.radio("Elegí un nivel:", 
    ["1. Historia y Orígenes", 
     "2. La Escalera de Notas", 
     "3. El Pentagrama Visual", 
     "4. Sonido, Eco y Figuras", 
     "5. Calculadora de Intervalos"])

st.sidebar.markdown("---")
st.sidebar.title(f"🏆 Puntaje total: {st.session_state.puntaje}")
if st.sidebar.button("Jugar de nuevo (Mezclar preguntas)"):
    st.session_state.puntaje = 0
    st.session_state.juegos_completados = []
    st.session_state.preguntas_n3 = random.sample(banco_pentagrama, 3)
    st.session_state.preguntas_n5 = random.sample(banco_intervalos, 3)
    st.rerun()

# --- NIVEL 1: HISTORIA ---
if juego_actual == "1. Historia y Orígenes":
    st.header("📜 Nivel 1: Historia de las Notas")
    q1 = st.radio("1. ¿Dónde se encontró la partitura musical más antigua hace 3400 años?", ["Egipto", "Roma", "Siria", "Grecia"], index=None)
    q2 = st.radio("2. ¿Qué monje italiano ideó los nombres de las notas en el siglo XI?", ["San Juan", "Guido D'Arezzo", "Papa Gregorio"], index=None)
    q3 = st.radio("3. ¿Por qué se reemplazó la sílaba 'Ut' por la nota 'Do'?", ["Porque sobraba una letra", "Porque era el nombre de una diosa", "Porque Do era más fácil de pronunciar"], index=None)
    
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
            st.warning("Ya completaste este nivel.")

# --- NIVEL 2: NOTAS VECINAS ---
elif juego_actual == "2. La Escalera de Notas":
    st.header("🪜 Nivel 2: Grados Conjuntos")
    q1 = st.radio("1. ¿Cuáles son las notas vecinas de SOL?", ["Do y Mi", "Fa y La", "La y Si"], index=None)
    q2 = st.radio("2. ¿Cuáles son las notas vecinas de RE?", ["Do y Mi", "Fa y Sol", "Si y Do"], index=None)
    q3 = st.radio("3. ¿Cuáles son las notas vecinas de DO?", ["Mi y Fa", "Sol y La", "Si y Re"], index=None)

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
            st.warning("Ya completaste este nivel.")

# --- NIVEL 3: PENTAGRAMA VISUAL (ALEATORIO) ---
elif juego_actual == "3. El Pentagrama Visual":
    st.header("🎼 Nivel 3: El Pentagrama (Aleatorio)")
    st.write("Mirá la imagen, prestá atención a la clave y a las alteraciones, y descubrí qué nota es. ¡Cada vez que jugás son distintas!")
    
    respuestas_n3 = []
    for i, q in enumerate(st.session_state.preguntas_n3):
        st.markdown(f"**Pregunta {i+1}:**")
        if os.path.exists(q['img']):
            st.image(q['img'], width=200)
        else:
            st.info(f"*(Acá iría la imagen {q['img']}. Profe Juan: ¡acordate de subirla a GitHub!)*")
        
        resp = st.radio("¿Qué nota ves arriba?", q['opciones'], key=f"n3_{i}", index=None)
        respuestas_n3.append((resp, q['correcta']))
        st.write("---")

    if st.button("Corregir Nivel 3"):
        if "nivel3" not in st.session_state.juegos_completados:
            puntos = 0
            for seleccion, correcta in respuestas_n3:
                if seleccion == correcta:
                    puntos += 10
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel3")
            st.success(f"¡Genial! Sumaste {puntos} puntos.")
        else:
            st.warning("Ya completaste este nivel.")

# --- NIVEL 4: SONIDO Y FIGURAS ---
elif juego_actual == "4. Sonido, Eco y Figuras":
    st.header("🔊 Nivel 4: Cualidades y Figuras")
    q1 = st.radio("1. ¿Qué diferencia hay entre el Eco y la Reverberación?", ["El eco repite la palabra clara, la reverberación alarga el sonido", "Son exactamente lo mismo", "La reverberación solo ocurre al aire libre"], index=None)
    q2 = st.radio("2. ¿Qué cualidad del sonido nos permite distinguir si es Fuerte o Suave?", ["Altura", "Intensidad", "Timbre"], index=None)
    q3 = st.radio("3. ¿Cuál de estas figuras musicales dura más tiempo?", ["Negra", "Corchea", "Redonda", "Blanca"], index=None)

    if st.button("Corregir Nivel 4"):
        if "nivel4" not in st.session_state.juegos_completados:
            puntos = 0
            if q1 == "El eco repite la palabra clara, la reverberación alarga el sonido": puntos += 10
            if q2 == "Intensidad": puntos += 10
            if q3 == "Redonda": puntos += 10
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel4")
            st.success(f"¡Súper! Sumaste {puntos} puntos.")
        else:
            st.warning("Ya completaste este nivel.")

# --- NIVEL 5: INTERVALOS (ALEATORIO) ---
elif juego_actual == "5. Calculadora de Intervalos":
    st.header("🥁 Nivel 5: Compases e Intervalos (Aleatorio)")
    
    q_compas = st.radio("1. ¿Un compás de 6/8 es simple o compuesto?", ["Simple", "Compuesto"], index=None)
    
    st.write("Calculá la distancia contando los grados (¡acordate de contar la primera y la última nota!)")
    respuestas_n5 = []
    for i, q in enumerate(st.session_state.preguntas_n5[:2]):
        resp = st.radio(f"{i+2}. {q['pregunta']}", q['opciones'], key=f"n5_{i}", index=None)
        respuestas_n5.append((resp, q['correcta']))

    if st.button("Corregir Nivel 5"):
        if "nivel5" not in st.session_state.juegos_completados:
            puntos = 0
            if q_compas == "Compuesto": puntos += 10
            for seleccion, correcta in respuestas_n5:
                if seleccion == correcta:
                    puntos += 10
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel5")
            st.success(f"¡Perfecto! Sumaste {puntos} puntos.")
            st.balloons()
        else:
            st.warning("Ya completaste este nivel.")
